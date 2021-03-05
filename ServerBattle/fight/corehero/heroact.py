from fight.dataenum.hero import EHeroAct


class HeroAct:
    """英雄行为类"""
    def __init__(self):
        """初始化"""
        self.state = {}  # 所有行为状态
        self.count = {}  # 所有行为计数

    def setstate(self, act: EHeroAct, state: bool):
        """设置状态"""
        self.state.update({act: state})

    def addcount(self, act: EHeroAct):
        """递增计数"""
        self.count.update({act: self.count.setdefault(act, 0) + 1})

    def getstate(self, act: int):
        """获取状态"""
        state: bool = self.state.setdefault(EHeroAct(act), False)
        return state

    def getcount(self, act: int):
        """获取计数"""
        count: int = self.count.setdefault(EHeroAct(act), 0)
        return count

    def resetstate(self):
        """重置行为状态打点"""
        self.state = {}

    def resetcount(self):
        """重置行为计数"""
        self.count = {}
