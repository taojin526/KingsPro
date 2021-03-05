from enum import Enum


class ArenaState(Enum):
    """战场状态枚举"""
    Init = 0
    CreateTeam = 1
    ShowFight = 2
    ShowRound = 3
    Finish = 4


# 战场转换关系
TRANSARENA = [
    {
        "trigger": "createteam",
        "source": ArenaState.Init,
        "dest": ArenaState.CreateTeam,
        "before": "createteambefore",
        "after": "createteamafter"
    },
    {
        "trigger": "showfight",
        "source": [ArenaState.CreateTeam, ArenaState.ShowRound],
        "dest": ArenaState.ShowFight,
        "before": "showfightbefore",
        "after": "showfightafter"
    },
    {
        "trigger": "showround",
        "source": [ArenaState.ShowRound, ArenaState.ShowFight],
        "dest": ArenaState.ShowRound,
        "before": "showroundbefore",
        "after": "showroundafter"
    },
    {
        "trigger": "showfinish",
        "source": ArenaState.ShowFight,
        "dest": ArenaState.Finish,
        "before": "showfinishbefore",
        "after": "showfinishafter"
    },
]
