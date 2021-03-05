from enum import Enum


class HeroState(Enum):
    """英雄状态枚举"""
    Init = 0  # 无
    Fight = 1  # 出战
    Watch = 2  # 待战
    NorAtk = 3  # 普攻攻击
    ChiefAtk = 4  # 主技能攻击
    AidAtk = 5  # 援助攻击
    Dead = 6  # 死亡


TRANSHERO = [
    {
        "trigger":
        "showfight",
        "source": [
            HeroState.Watch, HeroState.Fight, HeroState.NorAtk,
            HeroState.ChiefAtk
        ],
        "dest":
        HeroState.Fight,
        "before":
        "showfightbefore",
        "after":
        "showfightafter"
    },
    {
        "trigger": "showwatch",
        "source": [HeroState.Init, HeroState.AidAtk],
        "dest": HeroState.Watch,
        "before": "showwatchbefore",
        "after": "showwatchafter"
    },
    {
        "trigger": "shownormal",
        "source": [HeroState.Fight, HeroState.NorAtk],
        "dest": HeroState.NorAtk,
        "before": "shownormalbefore",
        "after": "shownormalafter"
    },
    {
        "trigger": "showchief",
        "source": [HeroState.Fight, HeroState.NorAtk, HeroState.ChiefAtk],
        "dest": HeroState.ChiefAtk,
        "before": "showchiefbefore",
        "after": "showchiefafter"
    },
    {
        "trigger": "showaid",
        "source": HeroState.Watch,
        "dest": HeroState.AidAtk,
        "before": "showaidbefore",
        "after": "showaidafter"
    },
    {
        "trigger":
        "showdead",
        "source": [
            HeroState.Fight, HeroState.NorAtk, HeroState.ChiefAtk,
            HeroState.AidAtk
        ],
        "dest":
        HeroState.Dead,
        "before":
        "showdeadbefore",
        "after":
        "showdeadafter"
    },
]
