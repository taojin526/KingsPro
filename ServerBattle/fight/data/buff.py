from fight.data import jsondt
from fight.data.const import ENBASE
from fight.data.jsonconf import JsonBuff
from fight.utils.singleton import Singleton


@Singleton
class BuffData:
    """Buff表数据"""
    def bpriority(self, bid: int):
        """buff优先级"""
        bp: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.priority)
        return bp

    def effect(self, bid: int):
        """buff效果"""
        bf: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.effect)
        return bf

    def epara(self, bid: int):
        """buff效果参数"""
        ep: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.epara)
        return ep

    def effectfixed(self, bid: int, eval: int, props: dict):
        """buff效果固定值"""
        fixed: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.fixed) or 0
        rate: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.rate) or 0
        exratedt: list = jsondt.get(JsonBuff.filename, bid, JsonBuff.extrarate)
        exratepk = 0  # 额外比率依据的属性
        exratepr = 0  # 额外比率依据的属性比率
        if (exratedt):
            exratepk = exratedt[0]
            exratepr = exratedt[1]
        exratepv = props.get(exratepk)
        fixedval = fixed + int(eval *
                               (rate +
                                (exratepv * exratepr) / ENBASE) / ENBASE)
        return fixedval

    def calarg(self, bid: int):
        """获取buff动态计算对象"""
        arg: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.dyncalarg)
        return arg

    def effectcalval(self, bid: int, props: dict):
        """buff效果值动态计算"""
        p: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.calprop)
        rate: int = jsondt.get(JsonBuff.filename, bid,
                               JsonBuff.calfixedrate) or 0
        exrate: list = jsondt.get(JsonBuff.filename, bid,
                                  JsonBuff.calextrarate)
        exratepk = 0  # 动态计算额外比率依据属性
        exratepr = 0  # 动态计算额外比率依据属性比率
        if (exrate):
            exratepk = exrate[0]
            exratepr = exrate[1]
        exratepv = props.get(exratepk) or 0
        calp = props.get(p) or 0
        calval = int(calp * (rate + (exratepv * exratepr) / ENBASE) / ENBASE)
        return calval

    def triggerconds(self, bid: int):
        """获取buff触发条件列表"""
        conds: list = jsondt.get(JsonBuff.filename, bid, JsonBuff.triggerconds)
        return conds

    def triggerprob(self, bid: int):
        """获取buff触发概率"""
        prob: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.triggerprob)
        return prob

    def triggercycle(self, bid: int):
        """获取buff触发周期"""
        cycle: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.triggercycle)
        return cycle

    def overlay(self, bid: int):
        """获取buff叠加上限"""
        stacklimit: int = jsondt.get(JsonBuff.filename, bid,
                                     JsonBuff.overlaymax)
        return stacklimit

    def duration(self, bid: int):
        """获取buff持续时间"""
        dura: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.dura)
        return dura

    def duraupdate(self, bid: int):
        """获取buff持续时间叠加时是否会刷新"""
        duradt: int = jsondt.get(JsonBuff.filename, bid, JsonBuff.duradt)
        return bool(duradt)

    def clearconds(self, bid: int):
        """获取buff主动清除条件"""
        clearc: list = jsondt.get(JsonBuff.filename, bid, JsonBuff.clearconds)
        return clearc

    def extraeffect(self, bid: int):
        """buff满层时额外的buff效果id"""
        exeffect: int = jsondt.get(JsonBuff.filename, bid,
                                   JsonBuff.extraeffect)
        return exeffect

    def extriggeredclear(self, bid: int):
        """额外效果触发后是否清除自身"""
        extriclear: int = jsondt.get(JsonBuff.filename, id,
                                     JsonBuff.extriclear)
        return bool(extriclear)
