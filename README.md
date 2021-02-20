<div align="right">
  Language:
    🇺🇸
  <a title="Chinese" href="./README.zh-CN.md">🇨🇳</a>
</div>

 <div align="center"><a title="" href="git@github.com:ZJCV/ZCls.git"><img align="center" src="./imgs/ZCls.png"></a></div>

<p align="center">
  «ZCls» is a classification model benchmark code base
<br>
<br>
  <a href="https://github.com/RichardLitt/standard-readme"><img src="https://img.shields.io/badge/standard--readme-OK-green.svg?style=flat-square"></a>
  <a href="https://conventionalcommits.org"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg"></a>
  <a href="http://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg"></a>
</p>

Supported Recognizers:

* [[2021]RepVGG](https://arxiv.org/abs/2101.03697)
* [[2020]ResNeSt](https://arxiv.org/abs/2004.08955)
* [[2019]ACNet](https://arxiv.org/abs/1908.03930)
* [[2019]MobileNetV3](https://arxiv.org/abs/1905.02244)
* [[2019]GCNet](https://arxiv.org/abs/1904.11492)
* [[2019]SKNet](https://arxiv.org/abs/1903.06586)
* [[2018]ResNetD](https://arxiv.org/abs/1812.01187)
* [[2018]MNasNet](https://arxiv.org/abs/1807.11626)
* [[2018]ShuffleNetV2](https://arxiv.org/abs/1807.11164)
* [[2018]MobileNetV2](https://arxiv.org/abs/1801.04381)
* [[2017]Non-local](https://arxiv.org/abs/1711.07971)
* [[2017]SENet](https://arxiv.org/abs/1709.01507)
* [[2017]ShuffleNetV1](https://arxiv.org/abs/1707.01083)
* [[2017]MobileNetV1](https://arxiv.org/abs/1704.04861)
* [[2016]ResNeXt](https://arxiv.org/abs/1611.05431)
* [[2015]ResNet](https://arxiv.org/abs/1512.03385)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Maintainers](#maintainers)
- [Thanks](#thanks)
- [Contributing](#contributing)
- [License](#license)

## Background

In order to further improve the algorithm performance, it is usually necessary to improve the existing model, which inevitably involves code refactoring. Creating this repo, on the one hand, serves as the CodeBase of the new model/optimization method, on the other hand, it also records the comparison between the custom model and the existing implementation (such as Torchvision Models)

## Maintainers

* zhujian - *Initial work* - [zjykzj](https://github.com/zjykzj)

## Thanks

```
@misc{ding2021repvgg,
      title={RepVGG: Making VGG-style ConvNets Great Again}, 
      author={Xiaohan Ding and Xiangyu Zhang and Ningning Ma and Jungong Han and Guiguang Ding and Jian Sun},
      year={2021},
      eprint={2101.03697},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{fan2020pyslowfast,
  author =       {Haoqi Fan and Yanghao Li and Bo Xiong and Wan-Yen Lo and
                  Christoph Feichtenhofer},
  title =        {PySlowFast},
  howpublished = {\url{https://github.com/facebookresearch/slowfast}},
  year =         {2020}
}

@misc{zhang2020resnest,
      title={ResNeSt: Split-Attention Networks}, 
      author={Hang Zhang and Chongruo Wu and Zhongyue Zhang and Yi Zhu and Haibin Lin and Zhi Zhang and Yue Sun and Tong He and Jonas Mueller and R. Manmatha and Mu Li and Alexander Smola},
      year={2020},
      eprint={2004.08955},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{ding2019acnet,
      title={ACNet: Strengthening the Kernel Skeletons for Powerful CNN via Asymmetric Convolution Blocks}, 
      author={Xiaohan Ding and Yuchen Guo and Guiguang Ding and Jungong Han},
      year={2019},
      eprint={1908.03930},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{howard2019searching,
      title={Searching for MobileNetV3}, 
      author={Andrew Howard and Mark Sandler and Grace Chu and Liang-Chieh Chen and Bo Chen and Mingxing Tan and Weijun Wang and Yukun Zhu and Ruoming Pang and Vijay Vasudevan and Quoc V. Le and Hartwig Adam},
      year={2019},
      eprint={1905.02244},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{cao2019gcnet,
      title={GCNet: Non-local Networks Meet Squeeze-Excitation Networks and Beyond}, 
      author={Yue Cao and Jiarui Xu and Stephen Lin and Fangyun Wei and Han Hu},
      year={2019},
      eprint={1904.11492},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{li2019selective,
      title={Selective Kernel Networks}, 
      author={Xiang Li and Wenhai Wang and Xiaolin Hu and Jian Yang},
      year={2019},
      eprint={1903.06586},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{tan2019mnasnet,
      title={MnasNet: Platform-Aware Neural Architecture Search for Mobile}, 
      author={Mingxing Tan and Bo Chen and Ruoming Pang and Vijay Vasudevan and Mark Sandler and Andrew Howard and Quoc V. Le},
      year={2019},
      eprint={1807.11626},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{sandler2019mobilenetv2,
      title={MobileNetV2: Inverted Residuals and Linear Bottlenecks}, 
      author={Mark Sandler and Andrew Howard and Menglong Zhu and Andrey Zhmoginov and Liang-Chieh Chen},
      year={2019},
      eprint={1801.04381},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{hu2019squeezeandexcitation,
      title={Squeeze-and-Excitation Networks}, 
      author={Jie Hu and Li Shen and Samuel Albanie and Gang Sun and Enhua Wu},
      year={2019},
      eprint={1709.01507},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{he2018bag,
      title={Bag of Tricks for Image Classification with Convolutional Neural Networks}, 
      author={Tong He and Zhi Zhang and Hang Zhang and Zhongyue Zhang and Junyuan Xie and Mu Li},
      year={2018},
      eprint={1812.01187},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{ma2018shufflenet,
      title={ShuffleNet V2: Practical Guidelines for Efficient CNN Architecture Design}, 
      author={Ningning Ma and Xiangyu Zhang and Hai-Tao Zheng and Jian Sun},
      year={2018},
      eprint={1807.11164},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{wu2018group,
      title={Group Normalization}, 
      author={Yuxin Wu and Kaiming He},
      year={2018},
      eprint={1803.08494},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{wang2018nonlocal,
      title={Non-local Neural Networks}, 
      author={Xiaolong Wang and Ross Girshick and Abhinav Gupta and Kaiming He},
      year={2018},
      eprint={1711.07971},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{micikevicius2018mixed,
      title={Mixed Precision Training}, 
      author={Paulius Micikevicius and Sharan Narang and Jonah Alben and Gregory Diamos and Erich Elsen and David Garcia and Boris Ginsburg and Michael Houston and Oleksii Kuchaiev and Ganesh Venkatesh and Hao Wu},
      year={2018},
      eprint={1710.03740},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}

@misc{zhang2017shufflenet,
      title={ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices}, 
      author={Xiangyu Zhang and Xinyu Zhou and Mengxiao Lin and Jian Sun},
      year={2017},
      eprint={1707.01083},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{goyal2018accurate,
      title={Accurate, Large Minibatch SGD: Training ImageNet in 1 Hour}, 
      author={Priya Goyal and Piotr Dollár and Ross Girshick and Pieter Noordhuis and Lukasz Wesolowski and Aapo Kyrola and Andrew Tulloch and Yangqing Jia and Kaiming He},
      year={2018},
      eprint={1706.02677},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{howard2017mobilenets,
      title={MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications}, 
      author={Andrew G. Howard and Menglong Zhu and Bo Chen and Dmitry Kalenichenko and Weijun Wang and Tobias Weyand and Marco Andreetto and Hartwig Adam},
      year={2017},
      eprint={1704.04861},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{xie2017aggregated,
      title={Aggregated Residual Transformations for Deep Neural Networks}, 
      author={Saining Xie and Ross Girshick and Piotr Dollár and Zhuowen Tu and Kaiming He},
      year={2017},
      eprint={1611.05431},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{he2015deep,
      title={Deep Residual Learning for Image Recognition}, 
      author={Kaiming He and Xiangyu Zhang and Shaoqing Ren and Jian Sun},
      year={2015},
      eprint={1512.03385},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}

@misc{szegedy2015rethinking,
      title={Rethinking the Inception Architecture for Computer Vision}, 
      author={Christian Szegedy and Vincent Vanhoucke and Sergey Ioffe and Jonathon Shlens and Zbigniew Wojna},
      year={2015},
      eprint={1512.00567},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Contributing

Anyone's participation is welcome! Open an [issue](https://github.com/zjykzj/ZCls/issues) or submit PRs.

Small note:

* Git submission specifications should be complied with [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/)
* If versioned, please conform to the [Semantic Versioning 2.0.0](https://semver.org) specification
* If editing the README, please conform to the [standard-readme](https://github.com/RichardLitt/standard-readme) specification.

## License

[Apache License 2.0](LICENSE) © 2020 zjykzj