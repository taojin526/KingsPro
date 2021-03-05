from fight.corehero.hero import Hero
from fight.corehero.heroconf import TRANSHERO, HeroState
from fight.dataenum.hero import EHeroProp
from fight.dataenum.skill import ESkillEffect
from fight.dataenum.team import ETeamCamp
from fight.datanotes.notemgr import NoteMgr
from transitions import Machine

notemgr = NoteMgr()


class Team:
    """战斗队伍"""
    def __init__(self, camp: ETeamCamp, heros: dict):
        """初始化"""
        self.camp = camp  # 我方队伍阵营
        self.member = len(heros)  # 队伍英雄数
        self.fighterpos = 1  # 出战者位置
        self.aiderpos = 0  # 助战者位置
        self.clsheros = {}  # 队伍所有位置的英雄
        self.lose = False  # 队伍是否战败
        self.__createheros(heros)

    def __createheros(self, heros: dict):
        """创建队伍英雄数据"""
        for pos, hero in heros.items():
            clshero = Hero(self.camp, hero)
            Machine(clshero,
                    HeroState,
                    initial=HeroState.Init,
                    transitions=TRANSHERO)
            clshero.showwatch()  # 进入待战状态
            # clshero.handleskilltakebuff()  # 处理被动技能携带的buff
            self.clsheros.setdefault(pos, clshero)

    @property
    def teamuuids(self):
        """队伍所有英雄的uuids"""
        return [self.gethero(pos).uuid for pos in self.clsheros]

    def notebasepropschange(self):
        """打点所有英雄的基本属性"""
        for pos in self.clsheros:
            self.gethero(pos).notebasepropschange()

    def gethero(self, pos: int):
        """获取指定pos的英雄"""
        hero: Hero = self.clsheros.setdefault(pos, None)
        return hero

    def getherowithuuid(self, uuid: int):
        """获取队伍的英雄根据英雄的uuid"""
        for clshero in self.clsheros.values():
            hero: Hero = clshero
            if hero.uuid == uuid:
                return hero

    def selectfight(self):
        """选择出战者位置"""
        if (self.fighter.dead is True):
            idx = self.fighterpos + 1
            if (idx <= self.member):
                while (self.fighterpos < idx):
                    selecthero = self.gethero(idx)
                    if (selecthero.dead is True):
                        idx += 1
                    self.fighterpos += 1
            else:
                self.setlose()

    def selectaid(self, etype: ESkillEffect = None):
        """选择援助者位置"""
        checkpos = self.fighterpos + 1
        while (checkpos <= self.member):
            hero = self.gethero(checkpos)
            ck = True if etype is None or etype == hero.aid.effect else False
            if ck and hero.aid.islaunch:
                self.aiderpos = hero.pos
                break
            else:
                checkpos += 1

    def setlose(self):
        """队伍战败"""
        self.lose = True

    @property
    def fighter(self):
        """战斗英雄"""
        return self.gethero(self.fighterpos)

    @property
    def aider(self):
        """援助英雄"""
        return self.gethero(self.aiderpos)

    def showroundact(self):
        """队伍进行回合行为"""
        self.fighter.shownormal()
        self.fighter.showchief()

    def showaid(self, etype: ESkillEffect):
        """援助判断"""
        self.selectaid(etype)
        if (self.aider):
            self.aider.showaid()
            self.aider.showwatch()
            self.aidpos = 0

    @property
    def teamspeed(self):
        """队伍速度"""
        fighterprops = notemgr.heroprops.getprops(self.fighter.uuid)
        return fighterprops.getp(EHeroProp.Speed)

    @property
    def endround(self):
        """结束回合"""
        return self.fighter.dead

    def showfight(self):
        """战斗英雄出战"""
        self.selectfight()
        self.fighter.showfight()
