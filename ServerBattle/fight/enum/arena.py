from enum import IntEnum, unique


@unique
class EArenaState(IntEnum):
    """
    战场状态枚举：
     * 1、对战开始时
     * 2、回合开始时
     * 3、回合结束时
     * 4、对战结束时
    """
    FightStart = 1
    RoundStart = 2
    RoundEnd = 3
    FightEnd = 4
