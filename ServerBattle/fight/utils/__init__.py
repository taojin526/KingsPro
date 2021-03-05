import random

from fight.data.const import ENBASE


def judgeprob(prob: int):
    """判断概率"""
    rnd = random.randint(1, ENBASE)
    return rnd <= prob
