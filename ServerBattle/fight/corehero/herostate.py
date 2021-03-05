from fight.dataenum.hero import EHeroState


class HeroState:
    """英雄状态管理类"""
    def __init__(self):
        """初始化"""
        self.dictstate = {}

    def addstate(self, uuid: int, state: EHeroState):
        """添加状态"""
        self.dictstate[uuid] = state

    def delstate(self, uuid):
        """删除buff绑定的状态效果"""
        self.dictstate.pop(uuid, None)

    def resetstate(self):
        """重置所有状态"""
        self.dictstate.clear()

    def hasstate(self, state: int):
        """检查是否有某个状态"""
        has: bool = EHeroState(state) in self.dictstate.values()
        return has
