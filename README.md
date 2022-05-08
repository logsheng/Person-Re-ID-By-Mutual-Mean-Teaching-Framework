# Reproducibility
Paper: [Mutual Mean-Teaching: Pseudo Label Refinery for Unsupervised Domain Adaptation on Person Re-identification](https://openreview.net/forum?id=rJlnOhVYPS)

## Install Packages

```shell
cd MMT
python setup.py install
```

## Datasets
```shell
cd examples && mkdir data
```

```
MMT/examples/data
├── dukemtmc
│   └── DukeMTMC-reID
└── market1501
    └── Market-1501-v15.09.15
```

### Generate Smaller Datasets
```shell
python split.py
```


## Experiments
### Duke-to-Market (ResNet-50)
#### 1. Pre-trained
```shell
sh scripts/pretrain.sh dukemtmc market1501 resnet50 1
sh scripts/pretrain.sh dukemtmc market1501 resnet50 2
```
#### 2. Baseline
```shell
sh scripts/train_baseline_kmeans.sh dukemtmc market1501 resnet50 500
```






## Reference
```
@inproceedings{
  ge2020mutual,
  title={Mutual Mean-Teaching: Pseudo Label Refinery for Unsupervised Domain Adaptation on Person Re-identification},
  author={Yixiao Ge and Dapeng Chen and Hongsheng Li},
  booktitle={International Conference on Learning Representations},
  year={2020},
  url={https://openreview.net/forum?id=rJlnOhVYPS}
}
```
