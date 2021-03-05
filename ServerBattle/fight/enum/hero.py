from enum import IntEnum, unique


@unique
class EHeroAct(IntEnum):
    """
    英雄行为枚举：
     * 1、攻击命中时 2、普攻命中时 3、主技能命中时
     * 4、造成伤害时 5、受到伤害时 6、死亡时
     * 7、暴击时
    """
    AtkHit = 1
    NorHit = 2
    ChiefHit = 3
    Hurt = 4
    Harm = 5
    Dead = 6
    CritHit = 7


@unique
class EHeroArg(IntEnum):
    """
    英雄目标枚举：
     * 101、我方战斗英雄 102、我方援助英雄 103、我方任意英雄
     * 201、敌方战斗英雄 202、敌方援助英雄 203、敌方任意英雄
     * 301、自身 302、自身攻击的目标 303、攻击自身的目标
     * 401、场上任意英雄
    """
    OwnFight = 101
    OwnAid = 102
    OwnAll = 103
    FoeFight = 201
    FoeAid = 202
    FoeAll = 203
    ItSelf = 301
    ItSelfAtkArg = 302
    AtkItSelfArg = 303
    All = 401


@unique
class EHeroProp(IntEnum):
    """
    英雄属性枚举：
     * 1、血量 2、攻击 3、法术 4、格挡 5、速度万分比
     * 6、暴击万分比 7、抗暴击万分比 8、爆伤万分比
     * 9、命中率万分比 10、闪避万分比
     * 11、减伤万分比 12、增伤万分比
     * 13、物理减伤万分比 14、物理增伤万分比
     * 15、法术减伤万分比 16、法术增伤万分比
     * 17、回血增幅效果万分比
     * 18、增益buff增幅万分比 19、减益buff增幅万分比
     * 101、当前血量值 102、当前血量万分比值
     * 103、已损失血量值 104、已损失血量万分比值
     * 105、单次攻击最终伤害
    """
    Hp = 1
    Atk = 2
    Mag = 3
    Def = 4
    Speed = 5
    Crit = 6
    DeCrit = 7
    CritDam = 8
    Hit = 9
    Dod = 10
    DamDown = 11
    DamUp = 12
    PhyDamDown = 13
    PhyDamUp = 14
    MagDamDown = 15
    MagDamUp = 16
    ReStoreHp = 17
    AddBuff = 18
    AddDeBuff = 19
    CurHp = 101
    CurHpRate = 102
    LostHp = 103
    LostHpRate = 104
    DamPerAtk = 105


@unique
class EHeroState(IntEnum):
    """
    英雄状态枚举：
     * 1、无法援助 2、无法主技能 3、无法普攻
    """
    BanAid = 1
    BanChief = 2
    BanNormal = 3
