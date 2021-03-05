from fight.enum.arena import EArenaState
from fight.utils.singleton import Singleton


@Singleton
class ArenaStateRec:
    """记录战场状态"""
    def __init__(self):
        """初始化"""
        self.estate: EArenaState = None

    def setstate(self, state: EArenaState):
        """打点战场状态"""
        self.estate = state

    def isstate(self, state: int):
        """判断当前战场状态"""
        return self.estate == EArenaState(state)
