import numpy as np
import random
import torch


def seed_all(seed_num):
    np.random.seed(seed_num)
    random.seed(seed_num)
    torch.manual_seed(seed_num)
    torch.cuda.manual_seed_all(seed_num)
