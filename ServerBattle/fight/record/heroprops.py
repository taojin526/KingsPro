from fight.corehero.heroprop import HeroProp
from fight.data.battletrigger import BattleTriggerData
from fight.data.const import ENBASE
from fight.enum.hero import EHeroProp
from fight.utils.singleton import Singleton


@Singleton
class HeroPropsRec:
    """记录英雄属性"""
    def __init__(self):
        """"""
        self.baseprops = {}  # 属性基本值
        self.curprops = {}  # 属性当前总值

    def setallprops(self, uuids: list):
        """设置所有英雄的属性"""
        for uuid in uuids:
            self.setbaseprops(uuid)
            self.setcurprops(uuid)

    def setbaseprops(self, uuid: int):
        """设置基础属性"""
        self.baseprops.setdefault(uuid, HeroProp())

    def setcurprops(self, uuid: int):
        """设置当前属性"""
        self.fixedprops.setdefault(uuid, HeroProp())

    def changebaseprops(self, uuid: int, prop: EHeroProp, val: int):
        """对基本属性做加减法"""
        baseprop: HeroProp = self.baseprops[uuid]
        baseprop.pchange(prop, val)

    def changecurprops(self, uuid: int, prop: EHeroProp, val: int):
        """对当前属性做加减法"""
        fixedprop: HeroProp = self.fixedprops[uuid]
        fixedprop.pchange(prop, val)

    def getbaseprops(self, uuid: int):
        """获取基本属性"""
        baseprops: HeroProp = self.baseprops[uuid]
        return baseprops

    def getcurprops(self, uuid: int):
        """获取当前属性"""
        curprops: HeroProp = self.curprops[uuid]
        return curprops

    def refreshcurprops(self, uuid):
        """刷新动态记录属性"""
        maxhp = self.getcurprops(uuid).pget(EHeroProp.Hp)
        curhp = self.getcurprops(uuid).pget(EHeroProp.CurHp)
        curhprate = curhp / maxhp * ENBASE
        losehp = maxhp - curhp
        losehprate = losehp / maxhp * ENBASE
        self.getcurprops(uuid).pset(EHeroProp.CurHpRate, curhprate)
        self.getcurprops(uuid).pset(EHeroProp.LostHp, losehp)
        self.getcurprops(uuid).pset(EHeroProp.LostHpRate, losehprate)

    def judgeprop(self, uuid: int, cond: int):
        """判断指定英雄的属性是否满足某个条件"""
        propinfo = BattleTriggerData().argprop(cond)
        pk = propinfo[0]
        op = propinfo[1]
        val = propinfo[2]
        return self.getcurprops(uuid).ckpropstate(pk, op, val)
