from typing import Union

from fight.dataenum.hero import EHeroArg


class HeroArg:
    """英雄目标类"""
    def __init__(self):
        self.dictargs = {}  # 目标记录

    def setarg(self, earg: EHeroArg, uuid: Union[int, list]):
        """设置目标"""
        self.dictargs[earg] = uuid

    def getarg(self, earg: EHeroArg):
        """获取指定目标"""
        args: Union[int, list] = self.dictargs.setdefault(earg, None)
        return args

    def reset(self, earg: EHeroArg):
        """重置指定目标数据"""
        self.dictargs[earg] = None

    def resetatkarg(self):
        """重置自身攻击的目标和攻击自身的目标"""
        self.reset(EHeroArg.ItSelfAtkArg)
        self.reset(EHeroArg.AtkItSelfArg)
