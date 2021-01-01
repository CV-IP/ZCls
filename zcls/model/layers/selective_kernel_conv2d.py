# -*- coding: utf-8 -*-

"""
@date: 2021/1/1 下午8:16
@file: selective_kernel_conv2d.py
@author: zj
@description:
"""
from abc import ABC

import torch
import torch.nn as nn
from torch import Tensor
from torch.nn.common_types import _size_2_t


class SelectiveKernelConv2d(nn.Module, ABC):
    """
    参考论文[Selective Kernel Networks](https://arxiv.org/abs/1903.06586)实现
    """

    def __init__(self,
                 in_channels: int,
                 out_channels: int,
                 stride: int,
                 groups: int,
                 # 中间层衰减率
                 reduction_rate: int,
                 # 默认中间层最小通道数
                 default_channels: int = 32,
                 # 维度
                 dimension: int = 2
                 ):
        super().__init__()

        # 3x3 conv
        self.split1 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, bias=False,
                      padding=1, dilation=1, groups=groups),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
        # 5x5 conv
        self.split2 = nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=stride, bias=False,
                      padding=2, dilation=2, groups=groups),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        )
        # fuse
        self.pool = nn.AdaptiveAvgPool2d((1, 1))
        inner_channels = max(out_channels // reduction_rate, default_channels)
        self.compact = nn.Sequential(
            nn.Conv2d(out_channels, inner_channels, kernel_size=1, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(inner_channels),
            nn.ReLU(inplace=True)
        )
        # select
        self.select_a = nn.Linear(inner_channels, out_channels, bias=False)
        self.select_b = nn.Linear(inner_channels, out_channels, bias=False)
        self.softmax = nn.Softmax(dim=0)
        self.dimension = dimension
        self.out_channels = out_channels

        self._init_weights()

    def _init_weights(self):
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, (nn.BatchNorm2d, nn.GroupNorm)):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)
            elif isinstance(m, nn.Linear):
                nn.init.normal_(m.weight, 0, 0.01)
                if m.bias is not None:
                    nn.init.zeros_(m.bias)

    def forward(self, x: Tensor) -> Tensor:
        N, C = x.shape[:2]

        # split
        u1 = self.split1(x)
        u2 = self.split2(x)
        # fuse
        u = u1 + u2
        s = self.pool(u)
        z = self.compact(s).flatten(1)
        # select
        # ac = torch.matmul(z, self.select_a)
        # bc = torch.matmul(z, self.select_b)
        ac = self.select_a(z)
        bc = self.select_b(z)
        abc = torch.stack((ac, bc)).reshape(2, N, self.out_channels, *([1] * self.dimension))
        softmax_abc = self.softmax(abc)
        v = torch.sum(torch.stack((u1, u2)).mul(softmax_abc), dim=0)

        return v
