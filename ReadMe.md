## Introduction
The repository is a modification of [original repo](https://github.com/iMoonLab/MeshNet).
We make the project easier to use and less irritating to setup.

As authors mention, please cite them in your research:

```
@article{feng2018meshnet,
  title={MeshNet: Mesh Neural Network for 3D Shape Representation},
  author={Feng, Yutong and Feng, Yifan and You, Haoxuan and Zhao, Xibin and Gao, Yue},
  journal={AAAI 2019},
  year={2018}
}
```

## Quickstart

__scripts__ directory contains shell scripts for the main subroutines:
1. install_libs.sh downloads all required python libraries, listed in requirements.txt 
2. get_dataset.sh to download the dataset from Google.Drive
3. preprocess_data.sh does the data processing - unzips downloaded archive, re-encodes the mesh models, etc.
4. train_model.sh performs the model training
5. eval_model.sh checks model performance

To use the project as-is run all the .sh files sequentially

## Development

todo file description



### List of good deeds

- [x] make a plan
- [x] create script files
- [x] fill scripts
- [ ] docker file, docker image
- [ ] build system (do we need it?)
- [ ] tests
- [ ] github CI/CD


### Checking procedure
1. Clone repo, check dependencies are pulled
2. Read readme
3. Launch docker
    1. pull image from dockerhub
    2. build image locally
4. Run tests
5. Run entry-points