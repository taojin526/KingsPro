import random

from fight.corehero.heroprop import HeroProp
from fight.data import jsondt
from fight.data.const import ENBASE
from fight.data.jsonconf import JsonSkill
from fight.dataenum.common import EGetRelation
from fight.dataenum.hero import EHeroArg, EHeroProp
from fight.utils.singleton import Singleton


@Singleton
class SkillData:
    """
    @获取技能数据
    """
    def stype(self, skill):
        """获取技能类型"""
        st: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.stype)
        return st

    def triconds(self, skill):
        """触发条件列表"""
        conds: list = jsondt.get(JsonSkill.filename, skill, JsonSkill.triconds)
        return conds

    def triconn(self, skill):
        """触发条件关系"""
        conn: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.triconn)
        return conn

    def triprob(self, skill):
        """判断技能触发概率"""
        prob: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.triprob)
        return prob

    def arg(self, skill):
        """获取技能对象"""
        arg: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.arg)
        return arg

    def effect(self, skill):
        """获取技能效果"""
        ef: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.effect)
        return ef

    def epara(self, skill):
        """获取技能效果参数"""
        efp: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.epara)
        return efp

    def dtype(self, skill):
        """获取技能伤害类型"""
        dt: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.dtype)
        return dt

    def effectdymval(self, skill: int, props: HeroProp):
        """获取技能效果值"""
        dymdam = jsondt.get(JsonSkill.filename, skill, JsonSkill.dymdam)
        if dymdam is not None:
            dymdam = dict(dymdam)
            dymval = 0
            for k, v in dymdam.items():
                prop = props.pget(EHeroProp(k), 0)
                rate = v
                dymval += prop * rate / ENBASE
            return dymval
        return 0

    def effectfixedval(self, skill: int):
        """获取效果固定值"""
        fixedval: int = jsondt.get(JsonSkill.filename, skill,
                                   JsonSkill.fixeddam)
        return fixedval or 0

    def takebuff(self, skill):
        """获取技能携带buff"""
        fbuff: list = jsondt.get(JsonSkill.filename, skill, JsonSkill.takebuff)
        return fbuff

    def emitbuff(self, skill):
        """获取技能发射buff"""
        ebuff: list = jsondt.get(JsonSkill.filename, skill, JsonSkill.emitbuff)
        econn: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.emitconn)
        if ebuff is not None:
            if EGetRelation(econn) == EGetRelation.All:
                return ebuff
            elif EGetRelation(econn) == EGetRelation.AnyOne:
                return [random.choice(ebuff)]
        else:
            return None

    def emitarg(self, skill):
        """获取技能发射对象"""
        earg: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.emitarg)
        return EHeroArg(earg)

    def emitprob(self, skill):
        """获取技能发射buff成功概率"""
        eprob: int = jsondt.get(JsonSkill.filename, skill, JsonSkill.emitprob)
        return eprob
