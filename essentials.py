import pandas as pd 
import numpy as np

import torch
import torchvision
import torchtext

import sklearn

import random

import re
import os 
import logging
import itertools
import datetime as dt 
from datetime import datetime



def set_seed(seed=1312):
	random.seed(1312)
	return random