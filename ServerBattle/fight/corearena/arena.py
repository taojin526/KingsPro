from fight.coreteam.team import Team
from fight.coreteam.teammgr import TeamMgr
from fight.enum.arena import EArenaState
from fight.enum.team import ETeamCamp
from fight.record.recorder import Recorder
from fight.utils.singleton import Singleton

recorder = Recorder()


@Singleton
class Arena:
    """战场单例类"""
    def __init__(self):
        self.teammgr = TeamMgr()  # 队伍管理器
        self.first = None  # 先手队伍
        self.wave = 0  # 战次
        self.round = 0  # 回合

    def resetround(self):
        """重置回合数"""
        self.round = 0

    def addwave(self):
        """战数计数"""
        self.wave += 1
        print("{0}{1}".format("当前战次：", self.wave))

    def addround(self):
        """回合计数"""
        self.round += 1
        print("{0}{1}".format("当前回合：", self.round))

    def createteams(self, ownheros: dict, foeheros: dict):
        """创建敌我双方队伍"""
        # 创建双方队伍
        own = Team(ETeamCamp.Own, ownheros)
        foe = Team(ETeamCamp.Foe, foeheros)
        notemgr.notesuuids(own.teamuuids, foe.teamuuids)
        notemgr.heroargnotesbase()
        notemgr.heroprops.setallprops(notemgr.alluuids)  # 设置所有英雄属性管理类
        notemgr.herobuff.createbuffmgr(notemgr.alluuids)  # 设置所有英雄buff管理器
        # 双方队伍放入队伍管理器
        self.teammgr.setteam(ETeamCamp.Own, own)
        self.teammgr.setteam(ETeamCamp.Foe, foe)
        # 双方队伍英雄的基本属性打点处理
        self.teammgr.notebasepropschange()
        print("双方队伍创建完成")

    def createteambefore(self, own: dict, foe: dict):
        """展示队伍前处理"""
        self.createteams(own, foe)

    def createteamafter(self, own: dict, foe: dict):
        """展示队伍后处理"""
        self.showfight()

    def showfightbefore(self):
        """开始对战前"""
        self.resetround()

    def showfightafter(self):
        """开始对战后"""
        notemgr.arenastate.setstate(EArenaState.FightStart)
        self.teammgr.teamshowfight()
        if (self.teammgr.isfinish is True):
            self.showfinish()
        else:
            self.addwave()
            self.teammgr.judgefirst()  # 判断队伍先后手
            self.showround()

    def showroundbefore(self):
        """开始回合前"""
        self.addround()

    def showroundafter(self):
        """开始回合后"""
        notemgr.arenastate.setstate(EArenaState.RoundStart)
        self.teammgr.teamshowroundact()
        if (self.teammgr.endfight is True):
            notemgr.arenastate.setstate(EArenaState.FightEnd)
            self.showfight()
        else:
            notemgr.arenastate.setstate(EArenaState.RoundEnd)
            self.showround()

    def showfinishbefore(self):
        """战斗结束前"""
        print("战斗结束")

    def showfinishafter(self):
        """战斗结束后"""
        print("输出战报")
