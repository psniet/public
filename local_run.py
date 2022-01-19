from torchvision import datasets, transforms
from torch import nn, optim
import argparse
from model import MnistClassifier
from torch.utils.data import DataLoader
from dataset import MnistDataset

from cnvrg import Experiment, Dataset
# this will initialize the cnvrg experiment. Do not use Experiment.init() - it will generate another experiment from this one!
exp = Experiment(datasets = ['mnist-1'])
