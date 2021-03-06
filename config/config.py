"""
functions to parse config
"""
import os
import os.path as osp
import yaml


def _check_dir(directory, make_dir=True):
    """
    checks the directory does not exist,
    otherwise creates it
    :exception if directory already exists
    """
    if not osp.exists(directory):
        if make_dir:
            print('Create directory {}'.format(directory))
            os.mkdir(directory)
        else:
            raise Exception('Directory not exist: {}'.format(directory))


def get_train_config(config_file='../config/train_config.yaml'):
    """
    parses training config
    :param config_file: path to train config .yaml file
    :return: parsed yaml file as a dict
    """
    with open(config_file, 'r') as f:
        cfg = yaml.load(f)

    _check_dir(cfg['dataset']['data_root'], make_dir=False)
    _check_dir(cfg['ckpt_root'])

    return cfg


def get_test_config(config_file='../config/test_config.yaml'):
    """
    parses test config
    :param config_file: path to test config .yaml file
    :return: parsed yaml file as a dict
    """
    with open(config_file, 'r') as f:
        cfg = yaml.load(f)

    _check_dir(cfg['dataset']['data_root'], make_dir=False)

    return cfg
