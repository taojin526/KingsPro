from fight.data.battletrigger import BattleTriggerData
from fight.utils.singleton import Singleton


@Singleton
class HeroBuffRec:
    """记录英雄携带的buff"""
    def __init__(self):
        """"""
        self.dictbuffs = {}

    def record(self, uuid: int, buffs: list = []):
        """记录英雄携带的buff"""
        if uuid in self.dictbuffs:
            self.dictbuffs[uuid] = buffs
        else:
            self.dictbuffs.setdefault(uuid, [])

    def hasbuff(self, uuid: int, cond: int):
        """判断英雄是否携带某个buff"""
        bf = BattleTriggerData().argbuff(cond)
        return bf in self.dictbuffs[uuid]
