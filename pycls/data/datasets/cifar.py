# -*- coding: utf-8 -*-

"""
@date: 2020/11/10 下午5:02
@file: cifar.py
@author: zj
@description: 
"""

from torch.utils.data import Dataset
from torchvision.datasets import CIFAR100

from .evaluator.cifar import CIFAREvaluator


class CIFAR(Dataset):

    def __init__(self, root, train=True, transform=None, target_transform=None,
                 download=False):
        self.data_set = CIFAR100(root, train=train, transform=transform, target_transform=target_transform,
                                 download=download)
        self.classes = self.data_set.classes
        self._update_evaluator()

    def __getitem__(self, index: int):
        return self.data_set.__getitem__(index)

    def __len__(self) -> int:
        return self.data_set.__len__()

    def _update_evaluator(self):
        self.evaluator = CIFAREvaluator(self.classes, topk=(1, 5))
