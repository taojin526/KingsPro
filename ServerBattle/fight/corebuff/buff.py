from fight.corehero.heroprop import EHeroProp, HeroProp
from fight.data.buff import BuffData
from fight.datanotes.notemgr import NoteMgr

notemgr = NoteMgr()


class Buff:
    """buff类"""
    def __init__(self, hid: int, bid: int):
        self.uuid = hid
        self.bid = bid
        self.duration = {}  # 每一层的持续时间
        self.fix = False  # 是否为固定Buff(不需要条件触发)
        self.effect = False  # buff效果是否生效
        self.props = HeroProp()  # 英雄属性
        self.phydam = 0  # 附加的物理伤害
        self.magdam = 0  # 附加法术伤害
        self.truthdam = 0  # 附加真实伤害

    def setduration(self, uuid: int):
        """设置持续回合"""
        dura: int = BuffData().duration(self.id)
        self.duration[uuid] = dura

    def updateduration(self):
        """叠加Buff时刷新持续时间"""
        duradt = BuffData().duraupdate(self.id)
        if (duradt is not None):
            for uuid in self.duration:
                self.setduration(uuid)

    def deduration(self):
        """回合开始持续回合减少1回合"""
        for uuid in self.duration:
            self.duration[uuid] -= 1

    @property
    def triggerconds(self):
        """获取触发条件"""
        return BuffData().triggerconds(self.bid)

    def checkfixed(self):
        """"""

    def handletrigger(self, uuid: int):
        """处理触发逻辑"""

    def addprops(self):
        """提升属性"""
        propkey = BuffData().epara(self.bid)
        total = self.effectfixed + self.effectdymcal
        self.props.pchange(EHeroProp(propkey), total)

    def subprops(self):
        """减少属性"""
        propkey = BuffData().epara(self.bid)
        total = self.effectfixed + self.effectdymcal
        self.props.pchange(EHeroProp(propkey), -total)

    @property
    def effectfixed(self):
        """效果固定值"""
        props = notemgr.heroprops.getbaseprops(self.uuid)
        fixedval = BuffData().effectfixed(self.bid, props)
        return fixedval

    @property
    def effectdymcal(self):
        """效果动态计算值"""
        dymarg = BuffData().calarg(self.bid)
        arguuid: int = notemgr.heroarg.getarg(self.uuid, dymarg)
        argprops = notemgr.heroprops.getbaseprops(arguuid)
        calval = BuffData().effectcalval(self.bid, argprops)
        return calval
