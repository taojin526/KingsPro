from enum import IntEnum, unique


@unique
class EBattleTriggerType(IntEnum):
    """
    触发条件类型枚举：
     * 1、战场状态
     * 2、英雄行为状态
     * 3、英雄属性状态
     * 4、英雄Buff状态
     * 5、英雄出战状态
     * 6、英雄携带状态
    """
    ArenaState = 1
    HeroAct = 2
    HeroProp = 3
    HeroBuff = 4
    HeroFight = 5
    HeroState = 6
