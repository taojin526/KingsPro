import math

from fight.corehero.heroprop import HeroProp
from fight.data.const import ENBASE
from fight.dataenum.hero import EHeroProp


class FightCal:
    """战斗计算"""
    @staticmethod
    def phydamage(self, initphy: int, crit: bool, atkerprops: HeroProp,
                  deferprops: HeroProp):
        """物理伤害公式"""
        phydamup = atkerprops.pget(EHeroProp.PhyDamUp)
        phydamdown = deferprops.pget(EHeroProp.PhyDamDown)
        damup = atkerprops.pget(EHeroProp.DamUp)
        damdown = deferprops.pget(EHeroProp.DamUp)
        defense = deferprops.pget(EHeroProp.Def)
        critrate = atkerprops.pget(EHeroProp.CritDam)
        totalrate = (ENBASE + phydamup + damup - phydamdown - damdown) / ENBASE
        totalrate = totalrate if totalrate >= 0 else 0
        basephy = initphy * totalrate - defense
        basephy = basephy if basephy >= 0 else 0
        damrate = critrate if (crit is True) else ENBASE
        finalphy = basephy * damrate / ENBASE
        return math.ceil(finalphy)

    @staticmethod
    def magdamage(self, initmag: int, crit: bool, atkerprops: HeroProp,
                  deferprops: HeroProp):
        """法术伤害公式"""
        magdamup = atkerprops.pget(EHeroProp.MagDamUp)
        magdamdown = deferprops.pget(EHeroProp.MagDamDown)
        damup = atkerprops.pget(EHeroProp.DamUp)
        damdown = deferprops.pget(EHeroProp.DamDown)
        defense = deferprops.pget(EHeroProp.Def)
        critrate = atkerprops.pget(EHeroProp.CritDam)
        totalrate = (ENBASE + magdamup + damup - magdamdown - damdown) / ENBASE
        totalrate = totalrate if totalrate >= 0 else 0
        basemag = initmag * totalrate - defense
        basemag = basemag if basemag >= 0 else 0
        damrate = critrate if (crit is True) else ENBASE
        finalmag = basemag * damrate / ENBASE
        return math.ceil(finalmag)

    @staticmethod
    def truthdamage(self, inittruth: int, crit: bool, atkerprops: HeroProp):
        """真实伤害计算公式"""
        basetruth = inittruth
        critrate = atkerprops.pget(EHeroProp.CritDam)
        damrate = critrate if (crit is True) else ENBASE
        finaltruth = basetruth * damrate / ENBASE
        return math.ceil(finaltruth)
