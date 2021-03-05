from fight.dataenum.common import ECalOp
from fight.dataenum.hero import EHeroProp


class HeroProp:
    """英雄属性管理类"""
    def __init__(self, props: dict = None):
        """初始化"""
        self.dictprops: dict = {EHeroProp(k): v
                                for k, v in props.items()} if (props) else {}

    def __add__(self, other):
        """加法运算"""
        result = HeroProp()
        result.dictprops = self.dictprops.copy()
        for k, v in other.dictprops.items():
            rv = result.dictprops.setdefault(k, 0)
            rv += v
            result.dictprops[k] = rv
        return result

    def __sub__(self, other):
        """减法运算"""
        result = HeroProp()
        result.dictprops = self.dictprops.copy()
        for k, v in other.dictprops.items():
            rv = result.dictprops.setdefault(k, 0)
            rv -= v
            result.dictprops[k] = rv
        return result

    def pset(self, k: EHeroProp, val: int):
        """设置指定属性的值"""
        self.dictprops.update({k: val})

    def pget(self, k: EHeroProp):
        """获取指定属性的值"""
        val: int = self.dictprops.get(k, 0)
        val = val if val > 0 else 0
        return val

    def pchange(self, k: EHeroProp, val: int):
        """修改属性减法传负值"""
        oldval = self.dictprops.setdefault(k, 0)
        newval = oldval + val
        self.dictprops[k] = newval

    def ckpropstate(self, k: int, op: int, val: int):
        """检查某个属性是否符合某个比对要求"""
        myval = self.pget(EHeroProp(k))
        if (ECalOp(op) == ECalOp.Equal):
            return myval == val
        elif (ECalOp(op) == ECalOp.More):
            return myval > val
        elif (ECalOp(op) == ECalOp.Less):
            return myval < val
        elif (ECalOp(op) == ECalOp.MoreAndEqual):
            return myval >= val
        elif (ECalOp(op) == ECalOp.LessAndEqual):
            return myval <= val

    def clear(self):
        """清除所有属性"""
        self.dictprops.clear()
