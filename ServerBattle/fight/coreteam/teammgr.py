from fight.dataenum.team import ETeamCamp
from fight.datanotes.notemgr import NoteMgr
from fight.utils import judgeprob
from fight.utils.singleton import Singleton

from .team import Team

notemgr = NoteMgr()


@Singleton
class TeamMgr:
    """队伍管理器"""
    def __init__(self):
        """初始化"""
        self.dictteam = {}
        self.ownfirst = False

    def setteam(self, camp: ETeamCamp, team: Team):
        """设置需要管理的队伍"""
        self.dictteam.setdefault(camp, team)

    def getteam(self, camp: ETeamCamp):
        """获取指定阵营的队伍"""
        team: Team = self.dictteam.get(camp, None)
        return team

    def judgefirst(self):
        """判断双方队伍谁先手"""
        if (self.ownteam.teamspeed < self.foeteam.teamspeed):
            self.ownfirst = False
        elif (self.ownteam.teamspeed > self.foeteam.teamspeed):
            self.ownfirst = True
        else:
            self.ownfirst = judgeprob(5000)

    @property
    def firstteam(self):
        """先手队伍"""
        return self.getteam(ETeamCamp.Own) if (
            self.ownfirst is True) else self.getteam(ETeamCamp.Foe)

    @property
    def secondteam(self):
        """后手队伍"""
        return self.getteam(ETeamCamp.Own) if (
            self.ownfirst is False) else self.getteam(ETeamCamp.Foe)

    @property
    def ownteam(self):
        """我方队伍"""
        return self.getteam(ETeamCamp.Own)

    @property
    def foeteam(self):
        """敌方队伍"""
        return self.getteam(ETeamCamp.Foe)

    @property
    def isfinish(self):
        """判断战斗是否结束"""
        return (self.ownteam.lose is True or self.foeteam.lose is True)

    def teamshowfight(self):
        """双方队伍出战英雄"""
        self.ownteam.showfight()
        self.foeteam.showfight()
        notemgr.heroargnotefight(ownfight=self.ownteam.fighter.uuid,
                                 foefight=self.foeteam.fighter.uuid)

    def teamshowroundact(self):
        """双方根据先手进行回合行动"""
        self.firstteam.showroundact()
        self.secondteam.showroundact()
        self.secondteam.fighter.dead = True

    @property
    def endfight(self):
        """判断当前战次是否结束"""
        return (self.ownteam.fighter.dead is True
                or self.foeteam.fighter.dead is True)

    def reownteam(self, camp: ETeamCamp):
        """相对而言的我方队伍"""
        return self.getteam(camp)

    def refoeteam(self, camp: ETeamCamp):
        """相对而言的敌方队伍"""
        return self.getteam(ETeamCamp.Own) if (
            camp == ETeamCamp.Own is True) else self.getteam(ETeamCamp.Foe)

    def notebasepropschange(self):
        """打点队伍所有英雄的基本属性"""
        self.ownteam.notebasepropschange()
        self.foeteam.notebasepropschange()

    def getherowithuuid(self, uuid: int):
        """获取指定uuid的英雄"""
        if uuid in self.ownteam.teamuuids:
            return self.ownteam.getherowithuuid(uuid)
        elif uuid in self.foeteam.teamuuids:
            return self.foeteam.getherowithuuid(uuid)
        else:
            return None
