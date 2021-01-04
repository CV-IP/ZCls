# -*- coding: utf-8 -*-

"""
@date: 2020/11/21 下午3:15
@file: bottleneck.py
@author: zj
@description: 
"""
from abc import ABC

import torch.nn as nn

from zcls.model.attention_helper import make_attention_block
from zcls.model.layers.split_attention_conv2d import SplitAttentionConv2d

"""
from 《ResNeSt: Split-Attention Networks》 Appendix
1. depth-wise convolution is not optimal for training and inference efficiency on GPU;
2. model accuracy get saturated on ImageNet with a fixed input image size;
3. increasing input image size can get better accuracy and FLOPS trade-off;
4. bicubic upsampling strategy is needed for large crop-size (≥ 320).
"""


class ResNetStBlock(nn.Module, ABC):
    """
    依次执行大小为1x1、3x3、1x1的卷积操作，如果进行下采样，那么使用第二个卷积层对输入空间尺寸进行减半操作
    参考Torchvision实现
    对于注意力模块，有两种嵌入方式：
    1. 对于Squeeze-And-Excitation或者Global Context操作，在残差连接中（after 1x1）嵌入；
    2. 对于NonLocal或者SimplifiedNonLoal，在Block完成计算后（after add）嵌入。
    对于Selective Kernel Conv2d，替换3x3卷积层；
    对于下采样操作，参考
    ResNeSt-fast setting, the effective average downsampling is applied prior to the
    3 × 3 convolution to avoid introducing extra computational costs in the model.
    With the downsampling operation moved after the convolutional layer, ResNeSt-
    50 achieves 81.13% accuracy
    在3x3卷积层之前（fast设置）或者之后执行AvgPool2d操作
    """
    expansion = 4

    def __init__(self,
                 # 输入通道数
                 in_planes,
                 # 输出通道数
                 out_planes,
                 # 步长
                 stride=1,
                 # 下采样
                 down_sample=None,
                 # cardinality
                 groups=1,
                 # 基础宽度
                 base_width=64,
                 # 是否使用注意力模块
                 with_attention=False,
                 # 衰减率
                 reduction=4,
                 # 注意力模块类型
                 attention_type='SqueezeAndExcitationBlock2D',
                 # 卷积层类型
                 conv_layer=None,
                 # 归一化层类型
                 norm_layer=None,
                 # 激活层类型
                 act_layer=None,
                 # 每个group中的分离数
                 radix=1,
                 # 在3x3之前执行下采样操作
                 fast_avg=False,
                 # 其他参数
                 **kwargs
                 ):
        super(ResNetStBlock, self).__init__()
        assert with_attention in (0, 1)
        assert attention_type in ['GlobalContextBlock2D',
                                  'SimplifiedNonLocal2DEmbeddedGaussian',
                                  'NonLocal2DEmbeddedGaussian',
                                  'SqueezeAndExcitationBlock2D']

        if conv_layer is None:
            conv_layer = nn.Conv2d
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if act_layer is None:
            act_layer = nn.ReLU

        self.down_sample = down_sample

        width = int(out_planes * (base_width / 64.)) * groups
        self.conv1 = conv_layer(in_planes, width, kernel_size=1, stride=1, bias=False)
        self.bn1 = norm_layer(width)

        self.conv2 = SplitAttentionConv2d(width, width, groups, radix, reduction_rate=reduction)
        self.bn2 = norm_layer(width)

        self.conv3 = conv_layer(width, out_planes * self.expansion, kernel_size=1, stride=1, bias=False)
        self.bn3 = norm_layer(out_planes * self.expansion)

        self.relu = act_layer(inplace=True)

        self.attention_after_1x1 = None
        self.attention_after_add = None
        if with_attention and attention_type in ['SqueezeAndExcitationBlock2D', 'GlobalContextBlock2D']:
            self.attention_after_1x1 = make_attention_block(out_planes * self.expansion, reduction, attention_type)
            self.attention_after_add = None
        if with_attention and attention_type in ['NonLocal2DEmbeddedGaussian', 'SimplifiedNonLocal2DEmbeddedGaussian']:
            self.attention_after_1x1 = None
            self.attention_after_add = make_attention_block(out_planes * self.expansion, reduction, attention_type)

        self.fast_avg = fast_avg
        self.avg = None
        if stride > 1:
            self.avg = nn.AvgPool2d(kernel_size=3, stride=stride, padding=1)

    def forward(self, x):
        identity = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        if self.fast_avg and self.avg is not None:
            out = self.avg(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)

        if not self.fast_avg and self.avg is not None:
            out = self.avg(out)

        out = self.conv3(out)
        out = self.bn3(out)

        if self.attention_after_1x1 is not None:
            out = self.attention_after_1x1(out)

        if self.down_sample is not None:
            identity = self.down_sample(x)

        out += identity
        out = self.relu(out)

        if self.attention_after_add is not None:
            out = self.attention_after_add(out)

        return out
