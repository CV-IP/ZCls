# -*- coding: utf-8 -*-

"""
@date: 2020/11/21 下午2:38
@file: basicblock.py
@author: zj
@description: 
"""

import torch.nn as nn

from zcls.model.layers.squeeze_and_excitation_block import SqueezeAndExcitationBlock2D


class SEResNetBasicBlock(nn.Module):
    """
    使用两个3x3卷积，如果进行下采样，那么使用第一个卷积层对输入空间尺寸进行减半操作
    标准SE操作：在残差块操作后嵌入SE操作；
    SE-PRE操作：在残差连接之前嵌入SE操作
    参考：[嵌入策略](https://blog.zhujian.life/posts/79124905.html)
    使用SE-PRE操作
    """
    expansion = 1

    def __init__(self,
                 # 输入通道数
                 inplanes,
                 # 输出通道数
                 planes,
                 # 步长
                 stride=1,
                 # 下采样
                 downsample=None,
                 # 是否使用SE
                 with_se=True,
                 # 衰减率
                 reduction=16,
                 # 卷积层类型
                 conv_layer=None,
                 # 归一化层类型
                 norm_layer=None,
                 # 激活层类型
                 act_layer=None
                 ):
        super(SEResNetBasicBlock, self).__init__()
        if conv_layer is None:
            conv_layer = nn.Conv2d
        if norm_layer is None:
            norm_layer = nn.BatchNorm2d
        if act_layer is None:
            act_layer = nn.ReLU

        self.with_se = with_se
        self.se_layer = SqueezeAndExcitationBlock2D(in_channels=inplanes, reduction=reduction)

        self.downsample = downsample

        self.conv1 = conv_layer(inplanes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
        self.bn1 = norm_layer(planes)

        self.conv2 = conv_layer(planes, planes, kernel_size=3, stride=1, padding=1, bias=False)
        self.bn2 = norm_layer(planes)

        self.relu = act_layer(inplace=True)

    def forward(self, x):
        identity = x

        if self.with_se:
            out = self.se_layer(x)
        else:
            out = x

        out = self.conv1(out)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)

        if self.downsample is not None:
            identity = self.downsample(x)

        out += identity
        out = self.relu(out)

        return out
