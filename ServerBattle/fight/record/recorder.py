from fight.data.battletrigger import BattleTriggerData
from fight.dataenum.battletrigger import EBattleTriggerType
from fight.dataenum.hero import EHeroArg
from fight.utils.singleton import Singleton

from .arenastate import ArenaStateRec
from .heroact import HeroActRec
from .heroarg import HeroArgRec
from .herobuff import HeroBuffRec
from .heroprops import HeroPropsRec
from .herostate import HeroStateRec


@Singleton
class Recorder:
    """数据记录管理器"""
    def __init__(self):
        """初始化"""
        self.arenastate = ArenaStateRec()
        self.heroact = HeroActRec()
        self.heroarg = HeroArgRec()
        self.herobuff = HeroBuffRec()
        self.heroprops = HeroPropsRec()
        self.herostate = HeroStateRec()

    def notesuuids(self, own: list, foe: list):
        """记录所有英雄的uuid"""
        self.ownuuids = own
        self.foeuuids = foe
        self.alluuids = own + foe

    def heroargnotesbase(self):
        """每个英雄记录固定的目标数据"""
        for ownuuid in self.ownuuids:
            self.heroarg.notesall(ownuuid, self.alluuids)
            self.heroarg.notesownall(ownuuid, self.ownuuids)
            self.heroarg.notesfoeall(ownuuid, self.foeuuids)
        for foeuuid in self.foeuuids:
            self.heroarg.notesall(foeuuid, self.alluuids)
            self.heroarg.notesownall(foeuuid, self.foeuuids)
            self.heroarg.notesfoeall(foeuuid, self.ownuuids)

    def heroargnotefight(self, ownfight=None, foefight=None):
        """每个英雄记录我方出战英雄和对方出战英雄"""
        for ownuuid in self.ownuuids:
            self.heroarg.notesownfight(ownuuid, ownfight)
            self.heroarg.notesfoefight(ownuuid, foefight)
        for foeuuid in self.foeuuids:
            self.heroarg.notesownfight(foeuuid, foefight)
            self.heroarg.notesfoefight(foeuuid, ownfight)

    def triggerjudgearena(self, cond: int):
        """触发条件判断根据战场状态"""
        state = BattleTriggerData().arenastate(cond)
        return self.arenastate.isstate(state)

    def triggerjudgeheroact(self, uuid: int, cond: int):
        """触发条件判断根据英雄行为"""
        condarg = BattleTriggerData().condarg(cond)
        judgeuuids = self.heroarg.getarg(uuid, EHeroArg(condarg))
        if isinstance(judgeuuids, int):
            return self.heroact.hasact(judgeuuids, cond)
        elif isinstance(judgeuuids, list):
            for judgeuuid in judgeuuids:
                if self.heroact.hasact(judgeuuid, cond) is True:
                    return True
            return False

    def triggerjudgeherobuff(self, uuid: int, cond: int):
        """触发条件判断根据英雄buff"""
        condarg = BattleTriggerData().condarg(cond)
        judgeuuids = self.heroarg.getarg(uuid, EHeroArg(condarg))
        if isinstance(judgeuuids, int):
            return self.herobuff.hasbuff(judgeuuids, cond)
        elif isinstance(judgeuuids, list):
            for judgeuuid in judgeuuids:
                if self.herobuff.hasbuff(judgeuuid, cond) is True:
                    return True
            return False

    def triggerjudgeherostate(self, uuid: int, cond: int):
        """触发条件判断根据英雄状态"""
        condarg = BattleTriggerData().condarg(cond)
        judgeuuids = self.heroarg.getarg(uuid, EHeroArg(condarg))
        if isinstance(judgeuuids, int):
            return self.herostate.hasstate(judgeuuids, cond)
        elif isinstance(judgeuuids, list):
            for judgeuuid in judgeuuids:
                if self.herostate.hasstate(judgeuuid, cond) is True:
                    return True
            return False

    def triggerjudgeheroprop(self, uuid: int, cond: int):
        """触发条件判断根据英雄属性"""
        condarg = BattleTriggerData().condarg(cond)
        judgeuuids = self.heroarg.getarg(uuid, EHeroArg(condarg))
        if isinstance(judgeuuids, int):
            return self.heroprops.judgeprop(judgeuuids, cond)
        elif isinstance(judgeuuids, list):
            for judgeuuid in judgeuuids:
                if self.heroprops.judgeprop(judgeuuid, cond) is True:
                    return True
            return False

    def triggerjudgeherofight(self, uuid, cond: int):
        """触发条件判断根据英雄出战状态"""
        fight = BattleTriggerData().isfight(cond)
        fightuuid = self.heroarg.getarg(uuid, EHeroArg.OWNFIGHT)
        isfight = (fightuuid == uuid)
        return isfight == fight

    def triggerjudge(self, uuid: int, cond: int):
        """触发判断"""
        cdt = BattleTriggerData().condtype(cond)
        if (EBattleTriggerType(cdt) == EBattleTriggerType.ArenaState):
            return self.triggerjudgearena(uuid, cond)
        elif (EBattleTriggerType(cdt) == EBattleTriggerType.HeroAct):
            return self.triggerjudgeheroact(uuid, cond)
        elif (EBattleTriggerType(cdt) == EBattleTriggerType.HeroProp):
            return self.triggerjudgeheroprop(uuid, cond)
        elif (EBattleTriggerType(cdt) == EBattleTriggerType.HeroBuff):
            return self.triggerjudgeherobuff(uuid, cond)
        elif (EBattleTriggerType(cdt) == EBattleTriggerType.HeroFight):
            return self.triggerjudgeherofight(uuid, cond)
        elif (EBattleTriggerType(cdt) == EBattleTriggerType.HeroState):
            return self.triggerjudgeherostate(uuid, cond)
