from fight.corehero.heroact import HeroAct
from fight.data.battletrigger import BattleTriggerData
from fight.enum.hero import EHeroAct
from fight.utils.singleton import Singleton


@Singleton
class HeroActRec:
    """记录英雄行为"""
    def __init__(self):
        """初始化"""
        self.dictacts = {}

    def record(self, uuid: int, act: EHeroAct):
        """
        记录行为：
         * uuid：英雄唯一标识id
         * act：行为
        """
        acts: HeroAct = self.dictacts.setdefault(uuid, HeroAct())
        acts.setstate(act, True)
        acts.addcount(act)

    def allclear(self):
        """清除行为打点"""
        for uuid in self.dictacts:
            acts: HeroAct = self.dictacts[uuid]
            acts.resetstate()

    def getacts(self, uuid: int):
        """获取指定英雄的行为打点数据"""
        if uuid in self.dictacts:
            acts: HeroAct = self.dictacts[uuid]
            return acts
        else:
            return None

    def hasact(self, uuid: int, cond: int):
        """判断指定英雄的指定行为条件是否满足"""
        actinfo = BattleTriggerData().argact(cond)
        act = actinfo[0]  # 行为
        cycle = actinfo[1]  # 行为判断周期
        state = self.getacts(uuid).getstate(act)
        count = self.getacts(uuid).getcount(act)
        return (state is True and count % cycle == 0)
