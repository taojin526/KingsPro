from enum import IntEnum, unique


@unique
class ETeamCamp(IntEnum):
    """
    队伍阵营枚举：
     * 1、我方 2、敌方
    """
    Own = 1
    Foe = 2
