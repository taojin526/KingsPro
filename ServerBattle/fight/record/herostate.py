from fight.corehero.herostate import HeroState
from fight.dataenum.hero import EHeroState
from fight.utils.singleton import Singleton


@Singleton
class HeroStateRec:
    """记录英雄状态"""
    def __init__(self):
        """初始化"""
        self.dictstate = {}

    def addstate(self, uuid: int, bfuuid: int, state: EHeroState):
        """添加某个状态"""
        herostate: HeroState = self.dictstate.setdefault(uuid, HeroState())
        herostate.addstate(bfuuid, state)

    def delstate(self, uuid: int, bfuuid):
        """删除某个状态"""
        herostate: HeroState = self.dictstate.setdefault(uuid, HeroState())
        herostate.delstate(bfuuid)

    def hasstate(self, uuid: int, state: int):
        """判断是否拥有某个状态"""
        herostate: HeroState = self.dictstate.setdefault(uuid, HeroState())
        herostate.hasstate(state)
