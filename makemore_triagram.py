import torch
import torch.nn as nn
import torch.nn.functional as F
words = open("names.txt", "r").read().splitlines()
print(words[:10])
