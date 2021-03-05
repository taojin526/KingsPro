from fight.utils.singleton import Singleton


class MakeUUID:
    """uuid制造类"""
    def __init__(self, seed: int):
        """初始化"""
        self.idx = seed

    def getuuid(self):
        """获取uuid"""
        self.idx += 1
        return self.idx


@Singleton
class UUIDSeed:
    """种子类"""
    def __init__(self):
        """初始化"""
        self.seed = 0

    def getseed(self):
        """获取新种子"""
        self.seed += 0x10000
        return self.seed
