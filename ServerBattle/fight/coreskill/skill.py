from fight.calculation.fightcal import FightCal
from fight.data.const import ENBASE
from fight.data.skill import SkillData
from fight.enum.common import ERelation
from fight.enum.hero import EHeroArg, EHeroProp
from fight.enum.skill import ESkillDamType, ESkillEffect, ESkillType
from fight.record.recorder import Recorder
from fight.utils import judgeprob

recorder = Recorder()


class Skill:
    """技能类"""
    def __init__(self, uuid: int, sid: int):
        """初始化"""
        self.uuid = uuid  # 技能携带者uuid
        self.sid = sid  # 技能id

    @property
    def atkerprops(self):
        """技能发动者属性"""
        return recorder.heroprops.getprops(self.uuid)

    @property
    def deferprops(self):
        """技能目标属性"""
        return recorder.heroprops.getprops(self.deferuuid)

    def setdefer(self):
        """设置攻击者和被攻击者的目标数据"""
        deferuuid = recorder.heroarg.getarg(self.uuid, self.effectarg)
        recorder.heroarg.notesselfatk(self.uuid, deferuuid)
        recorder.heroarg.notesatkself(deferuuid, self.uuid)

    @property
    def effectarg(self):
        """技能效果的目标"""
        sarg = SkillData().arg(self.sid)
        return EHeroArg(sarg)

    @property
    def deferuuid(self):
        """被技能攻击者的uuid"""
        return recorder.heroarg.getarg(self.uuid, EHeroArg.ItSelfAtkArg)

    @property
    def emitbuffs(self):
        """获取需要发射的buff列表"""
        return SkillData().emitbuff(self.sid)

    @property
    def iscondreached(self):
        """判断触发条件是否达成"""
        conds = SkillData().triconds(self.sid)
        conn = SkillData().triconn(self.sid)
        if (ERelation(conn) == ERelation.AllAccord):
            for cond in conds:
                if recorder.triggerjudge(self.uuid, cond) is False:
                    return False
            return True
        elif (ERelation(conn) == ERelation.AnyOneAccord):
            for cond in conds:
                if recorder.triggerjudge(self.uuid, cond) is True:
                    return True
            return False

    @property
    def istrigger(self):
        """是否触发"""
        baseprob = SkillData().emitprob(self.sid)
        extraprob = 0  # 具体根据buff数据
        totalprob = baseprob + extraprob
        return judgeprob(totalprob)

    @property
    def islaunch(self):
        """是否发动"""
        return self.iscondreached and self.istrigger

    @property
    def effectval(self):
        """获取技能效果值"""
        dymval = SkillData().effectdymval(self.sid, self.atkerprops)
        fixedval = SkillData().effectfixedval(self.sid)
        return dymval + fixedval

    @property
    def isemit(self):
        """是否发射buff成功"""
        baseprob = SkillData().emitprob(self.sid)
        return judgeprob(baseprob)

    def ishit(self):
        """判断当前英雄是否命中"""
        hit = self.atkerprops.getp(EHeroProp.Hit)
        dod = self.deferprops.getp(EHeroProp.Dod)
        prob = int(hit - dod)
        return judgeprob(prob)

    @property
    def iscrit(self):
        """技能是否暴击"""
        crit = self.atkerprops.getp(EHeroProp.Crit)
        decrit = self.deferprops.getp(EHeroProp.DeCrit)
        prob = crit - decrit if crit - decrit > 0 else 0
        return judgeprob(prob)

    @property
    def damtype(self):
        """技能伤害类型"""
        dtype = SkillData().dtype(self.sid)
        return ESkillDamType(dtype)

    def singledam(self, crit: bool):
        """单次攻击伤害计算"""
        dams = [-1, -1, -1]
        if self.damtype == ESkillDamType.PhyDam:
            dams[0] = FightCal().phydamage(self.effectval, crit,
                                           self.atkerprops, self.deferprops)
        elif self.damtype == ESkillDamType.MagDam:
            dams[1] = FightCal().magdamage(self.effectval, crit,
                                           self.atkerprops, self.deferprops)
        elif self.damtype == ESkillDamType.TruthDam:
            dams[2] = FightCal().truthdamage(self.effectval, crit,
                                             self.atkerprops, self.deferprops)
        totaldam = sum([dam for dam in dams if dam != -1])
        recorder.heroprops.getdymprops(self.uuid).pset(EHeroProp.DamPerAtk,
                                                       totaldam)
        return dams

    @property
    def cureval(self):
        """治疗值"""
        effectrate = self.atkerprops.pget(EHeroProp.ReStoreHp)
        extra = int(self.effectval * effectrate / ENBASE)
        return self.effectval + extra

    @property
    def skilltype(self):
        """获取技能类型"""
        stype = SkillData().stype(self.sid)
        return ESkillType(stype)

    @property
    def effect(self):
        ef = SkillData().effect(self.sid)
        return ESkillEffect(ef)

    @property
    def takebuffs(self):
        """携带的buff"""
        return SkillData().takebuff(self.sid)

    def takebuffhandle(self):
        """处理携带的buff"""
        takebuffs = self.takebuffs
        recorder.herobuff.addbuffs(self.uuid, takebuffs)

    def emitbuffhandle(self):
        """处理发射的buff"""
        emitbuffs = self.emitbuffs
        # 发送事件让战场处理

    def singleatk(self, crit: bool):
        """"""
        dams = self.singledam(crit)
        totaldam = sum([dam for dam in dams if dam != -1])
        # 用buff修正伤害
        recorder.heroprops.changecurprops(self.deferuuid, EHeroProp.CurHp,
                                          -totaldam)
        recorder.heroprops.refreshcurprops(self.deferuuid)

    def mutiatk(self, crit: bool):
        """"""
        muti = SkillData().epara(self.sid)
        for i in range(muti):
            self.singleatk(crit)

    def exchangedefer(self):
        """把目标的攻击者换成自己"""
        # 找到要为其挡刀英雄的uuid
        arguuid = recorder.heroarg.getarg(self.uuid, self.effectarg)
        # 找到要为其挡刀英雄的攻击者的uuid
        argatkeruuid = recorder.heroarg.getarg(arguuid, EHeroArg.AtkItSelfArg)
        recorder.heroarg.notesatkself(self.uuid, argatkeruuid)
        recorder.heroarg.notesatkself(arguuid, None)
        recorder.heroarg.notesselfatk(argatkeruuid, self.uuid)

    def cure(self):
        """治疗英雄"""
        recorder.heroprops.changedymprops(self.deferuuid, EHeroProp.CurHp,
                                          self.cureval)
        recorder.heroprops.refreshdymprops(self.deferuuid)

    def handle(self):
        """处理技能"""
        islaunch = self.islaunch
        if islaunch is True:
            self.setdefer()
            ishit = self.ishit()
            if ishit is True:
                self.emitbuffhandle()
                iscrit = self.iscrit
                if self.effect == ESkillEffect.SingleAtk:
                    self.singleatk(iscrit)
                elif self.effect == ESkillEffect.MutiLAtk:
                    self.mutiatk(iscrit)
                elif self.effect == ESkillEffect.SufferForMate:
                    self.exchangedefer()
                elif self.effect == ESkillEffect.Cure:
                    self.cure()
