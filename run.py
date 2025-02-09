import math
import torch
import torch.nn as nn
# import torch.optim as optim
import torch.nn.functional as F


class GPTConfig:
    attn_dropout = 0.1
    embedded_dropout = 0.1
    ff_dropout = 0.1

    def __init__(self, vocab_size, max_len, **kwargs):
        self.vocab_size = vocab_size
        self.max_len = max_len

        for key, value in kwargs.items():
            setattr(self, key, value)
