from typing import Union

from fight.corehero.heroarg import HeroArg
from fight.enum.hero import EHeroArg
from fight.utils.singleton import Singleton


@Singleton
class HeroArgRec:
    """记录英雄的目标"""
    def __init__(self):
        """"""
        self.dictargs = {}

    def record(self, uuid, argname: EHeroArg, arguuid: Union[int, list]):
        """记录指定英雄"""
        heroargs: HeroArg = self.dictargs.setdefault(uuid, HeroArg())
        heroargs.setarg(argname, arguuid)

    def getarg(self, uuid: int, argname: EHeroArg):
        """获取指定英雄的指定目标uuid或者uuids"""
        heroargs: HeroArg = self.dictargs.setdefault(uuid, HeroArg())
        return heroargs.getarg(argname)
