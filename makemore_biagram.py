import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
words = open('names.txt', 'r').read().splitlines()
print(words[:10])