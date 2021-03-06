# -*- coding: utf-8 -*-

"""
@date: 2020/12/24 下午7:38
@file: shufflenetv1.py
@author: zj
@description: 
"""

from abc import ABC
import torch.nn as nn
from torch.nn.modules.module import T
from torchvision.models.utils import load_state_dict_from_url

from zcls.config.key_word import KEY_OUTPUT
from zcls.model import registry
from zcls.model.backbones.build import build_backbone
from zcls.model.heads.build import build_head
from zcls.model.norm_helper import freezing_bn


class MobileNetV3(nn.Module, ABC):

    def __init__(self, cfg):
        super(MobileNetV3, self).__init__()
        self.fix_bn = cfg.MODEL.NORM.FIX_BN
        self.partial_bn = cfg.MODEL.NORM.PARTIAL_BN

        self.backbone = build_backbone(cfg)
        self.head = build_head(cfg)

        zcls_pretrained = cfg.MODEL.RECOGNIZER.PRETRAINED
        pretrained_num_classes = cfg.MODEL.RECOGNIZER.PRETRAINED_NUM_CLASSES
        num_classes = cfg.MODEL.HEAD.NUM_CLASSES
        self.init_weights(zcls_pretrained,
                          pretrained_num_classes,
                          num_classes)

    def init_weights(self, pretrained, pretrained_num_classes, num_classes):
        if pretrained != "":
            state_dict = load_state_dict_from_url(pretrained, progress=True)
            self.load_state_dict(state_dict=state_dict, strict=False)
        if num_classes != pretrained_num_classes:
            in_channels = self.head.conv2.in_channels
            conv2 = nn.Conv2d(in_channels, num_classes, kernel_size=1, stride=1, padding=0, bias=True)

            nn.init.kaiming_normal_(conv2.weight, mode="fan_out", nonlinearity="relu")
            nn.init.zeros_(conv2.bias)

            self.head.conv2 = conv2

    def train(self, mode: bool = True) -> T:
        super(MobileNetV3, self).train(mode=mode)

        if mode and (self.partial_bn or self.fix_bn):
            freezing_bn(self, partial_bn=self.partial_bn)

        return self

    def forward(self, x):
        x = self.backbone(x)
        x = self.head(x)

        return {KEY_OUTPUT: x}


@registry.RECOGNIZER.register('MobileNetV3')
def build_mobilenet_v3(cfg):
    return MobileNetV3(cfg)
