from enum import IntEnum, unique


@unique
class ESkillType(IntEnum):
    """
    技能类型枚举：
     * 1、普攻技能
     * 2、援助技能
     * 3、主技能
     * 4、觉醒技能
    """
    NorAtk = 1
    Aid = 2
    Chief = 3
    Latent = 4


@unique
class ESkillEffect(IntEnum):
    """
    技能效果枚举：
     * 1、单次攻击
     * 2、多段攻击
     * 3、挡刀
     * 4、治疗
    """
    SingleAtk = 1
    MutiLAtk = 2
    SufferForMate = 3
    Cure = 4


@unique
class ESkillDamType(IntEnum):
    """
    技能伤害类型：
     * 1、物理伤害
     * 2、法术伤害
     * 3、真实伤害
    """
    PhyDam = 1
    MagDam = 2
    TruthDam = 3
