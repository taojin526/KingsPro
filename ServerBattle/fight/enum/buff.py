from enum import IntEnum, unique


@unique
class EBuffEffect(IntEnum):
    """
    效果枚举：
     * 1、提升目标指定属性值（增幅）
     * 2、降低目标指定属性值（降低）
     * 3、附加指定类型的伤害（伤害计算到自身行为中）
     * 4、造成指定类型的伤害（伤害单独表现）
     * 5、恢复指定数值的血量
     * 6、套一个指定类型的护盾（吸收盾、免伤盾、反射盾）
     * 7、标记目标
     * 8、无法行动（全部、普攻、主技能、援助）
     * 9、普攻伤害类型转变（法术、真伤）
     * 10、暴击无法产生暴伤
     * 11、无视减伤（物理减伤、法术减伤、减伤）
     * 12、复活并恢复一定血量
     * 13、提升技能发动概率（全部、普攻、主技能、援助）
     * 14、降低技能发动概率（全部、普攻、主技能、援助）
     * 15、提升技能伤害（全部、普攻、主技能、援助）
     * 16、降低技能伤害（全部、普攻、主技能、援助）
     * 17、给自身攻击的目标挂上某个buff
     * 18、增加多段技能的段数
     * 19、打断敌人技能（全部、普攻、主技能、援助）
     * 20、减少来自技能的伤害（全部、普攻、主技能、援助）
     * 21、增加额外施放技能次数（全部、普攻、主技能、援助）
    """
    PropsUpper = 1
    PropsLower = 2
    ExtraDam = 3
    MakeDam = 4
    Cure = 5
    Shield = 6
    Mark = 7
    UnableAct = 8
    TransNorDamType = 9
    UnableMakeCritDam = 10
    IgnoreDamLower = 11
    Revive = 12
    SkillProbUpper = 13
    SkillProbLower = 14
    SkillDamUpper = 15
    SkillDamLower = 16
    EmitBuff = 17
    SkillMutiUpper = 18
    SkillBreak = 19
    LowerDamFromSkill = 20
    ExtraSkillCast = 21


class EBuffArg(IntEnum):
    """
    Buff目标枚举：
     * 101、Buff发射者 102、Buff发射者攻击的目标
     * 201、Buff携带者 202、Buff携带者攻击的目标
     * 203、Buff携带者的敌方出战英雄(暂未实现)
    """
    BuffEmiter = 101
    BuffEmiterAtkArg = 102
    BuffTaker = 201
    BuffTakerAtkArg = 202
    BuffTakerTeamFighter = 203
