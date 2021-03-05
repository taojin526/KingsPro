from fight.data import jsondt
from fight.data.jsonconf import JsonBattleTrigger
from fight.utils.singleton import Singleton


@Singleton
class BattleTriggerData:
    """战斗触发"""
    def condtype(self, id: int):
        """触发条件类型"""
        ct: int = jsondt.get(JsonBattleTrigger.filename, id,
                             JsonBattleTrigger.condtype)
        return ct

    def arenastate(self, id: int):
        """战场行为"""
        s: int = jsondt.get(JsonBattleTrigger.filename, id,
                            JsonBattleTrigger.arenastate)
        return s

    def condarg(self, id: int):
        """条件对象"""
        arg: int = jsondt.get(JsonBattleTrigger.filename, id,
                              JsonBattleTrigger.arg)
        return arg

    def argact(self, id: int):
        """对象行为及周期"""
        act: int = jsondt.get(JsonBattleTrigger.filename, id,
                              JsonBattleTrigger.argact)
        cycle: int = jsondt.get(JsonBattleTrigger.filename, id,
                                JsonBattleTrigger.actcycle)
        return act, cycle

    def argstate(self, id: int):
        """对象状态"""
        state: int = jsondt.get(JsonBattleTrigger.filename, id,
                                JsonBattleTrigger.argstate)
        return state

    def argbuff(self, id: int):
        """对象携带buff"""
        buff: int = jsondt.get(JsonBattleTrigger.filename, id,
                               JsonBattleTrigger.argbuff)
        return buff

    def argprop(self, id: int):
        """用于判断的目标属性、运算符、值"""
        prop: int = jsondt.get(JsonBattleTrigger.filename, id,
                               JsonBattleTrigger.argprop)
        op: int = jsondt.get(JsonBattleTrigger.filename, id,
                             JsonBattleTrigger.op)
        val: int = jsondt.get(JsonBattleTrigger.filename, id,
                              JsonBattleTrigger.propfixed)
        return prop, op, val

    def isfight(self, id: int):
        """用于判断目标是否出战 """
        isf: int = jsondt.get(JsonBattleTrigger.filename, id,
                              JsonBattleTrigger.isfight)
        return bool(isf)
