# -*- coding: utf-8 -*-

"""
@date: 2021/2/1 下午8:01
@file: test_asymmetric_convolution_block.py
@author: zj
@description: 
"""

import torch
import torch.nn as nn

from zcls.model.layers.asymmetric_convolution_block import AsymmetricConvolutionBlock
from zcls.model.acb_helper import insert_acblock, fuse_acblock


def test_asymmetric_convolution_block():
    in_channels = 32
    out_channels = 64
    dilation = 1
    groups = 1

    # inputs == outputs
    kernel_size = 3
    stride = 1
    padding = 1
    acblock = AsymmetricConvolutionBlock(in_channels,
                                         out_channels,
                                         kernel_size,
                                         stride=stride,
                                         padding=padding,
                                         dilation=dilation,
                                         groups=groups)

    data = torch.randn(1, in_channels, 56, 56)
    outputs = acblock.forward(data)

    _, _, h, w = data.shape[:4]
    _, _, h2, w2 = outputs.shape[:4]
    assert h == h2 and w == w2

    # 下采样
    kernel_size = 3
    stride = 2
    padding = 1
    acblock = AsymmetricConvolutionBlock(in_channels,
                                         out_channels,
                                         kernel_size,
                                         stride=stride,
                                         padding=padding,
                                         dilation=dilation,
                                         groups=groups)

    data = torch.randn(1, in_channels, 56, 56)
    outputs = acblock.forward(data)

    _, _, h, w = data.shape[:4]
    _, _, h2, w2 = outputs.shape[:4]
    assert h / 2 == h2 and w / 2 == w2

    # 下采样 + 分组卷积
    kernel_size = 3
    stride = 2
    padding = 1
    groups = 8
    acblock = AsymmetricConvolutionBlock(in_channels,
                                         out_channels,
                                         kernel_size,
                                         stride=stride,
                                         padding=padding,
                                         dilation=dilation,
                                         groups=groups)

    data = torch.randn(1, in_channels, 56, 56)
    outputs = acblock.forward(data)

    _, _, h, w = data.shape[:4]
    _, _, h2, w2 = outputs.shape[:4]
    assert h / 2 == h2 and w / 2 == w2


def test_acb_helper():
    in_channels = 32
    out_channels = 64
    dilation = 1

    # 下采样 + 分组卷积
    kernel_size = 3
    stride = 2
    padding = 1
    groups = 8

    model = nn.Sequential(
        nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size,
                      stride=stride, padding=padding, dilation=dilation, groups=groups),
            nn.BatchNorm2d(out_channels),
            nn.ReLU(inplace=True)
        ),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(inplace=True)
    )
    print(model)

    data = torch.randn(1, in_channels, 56, 56)
    insert_acblock(model)
    train_outputs = model(data)
    print(model)

    fuse_acblock(model, eps=1e-5)
    eval_outputs = model(data)
    print(model)

    print(torch.sum(train_outputs), torch.sum(eval_outputs))
    assert torch.allclose(train_outputs, eval_outputs)


if __name__ == '__main__':
    test_asymmetric_convolution_block()
    test_acb_helper()
