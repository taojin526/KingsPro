from fight.corebuff.buffmgr import BuffMgr
from fight.dataenum.hero import EHeroAct, EHeroProp
from fight.dataenum.team import ETeamCamp
from fight.datanotes.notemgr import NoteMgr
from fight.utils.makeuuid import UUIDSeed

uuidseed = UUIDSeed()  # BUFF唯一uuid的种子
notemgr = NoteMgr()


class Hero:
    """英雄类"""
    def __init__(self, camp: ETeamCamp, hero: dict):
        self.hid: int = hero.get("id", None)
        self.camp = camp
        self.pos: int = hero.get("pos", None)
        self.uuid = self.camp.value * 10 + self.pos

        self.props: dict = hero.get("props")

        self.buffs: list = hero.get("buffs")

        self.normal = hero.get("normal")
        self.chief = hero.get("chief")
        self.aid = hero.get("aid")
        self.latent = hero.get("latent")

        self.buffmgr = BuffMgr(self.uuid, uuidseed.getseed())
        self.buffmgr.addbuffs(self.buffs)

        self.fight = False  # 是否出战
        self.dead = False  # 是否死亡

    def notebasepropschange(self):
        for k, val in self.props.items():
            notemgr.heroprops.changebaseprops(self.uuid, EHeroProp(k), val)
            if EHeroProp(k) == EHeroProp.Hp:
                notemgr.heroprops.changecurprops(self.uuid, EHeroProp.CurHp,
                                                 val)
                notemgr.heroprops.refreshcurprops(self.uuid)

    def handlelatent(self):
        """处理被动技能携带的buff"""
        # 给战场发消息处理被动技能

    def showfightbefore(self):
        """进入出战状态前"""
        print("处理进入出战前逻辑")

    def showfightafter(self):
        """进入出战状态后"""
        self.fight = True
        print("处理进入出战后逻辑")

    def showwatchbefore(self):
        """进入待战状态前"""
        print("处理进入待战前逻辑")

    def showwatchafter(self):
        """进入待战状态后"""
        self.fight = False
        print("处理进入待战后逻辑")

    def shownormalbefore(self):
        """进入普攻状态前"""
        print("处理进入普攻前逻辑")

    def shownormalafter(self):
        """进入普攻状态后"""
        notemgr.heroact.actnotes(self.uuid, EHeroAct.NorHit)
        # 向战场发送普攻消息——战场处理逻辑如下
        # 选中目标
        # 判断技能是否命中    回血技能必然命中
        # 如果命中判断是否有BUFF要发射
        # 判断是否暴击          回血技能不能暴击
        # 向目标发送技能伤害消息
        print("处理进入普攻后逻辑")

    def showchiefbefore(self):
        """进入施放主技能状态前"""
        print("处理进入施放主技能前逻辑")

    def showchiefafter(self):
        """进入施放主技能状态后"""
        notemgr.heroact.actnotes(self.uuid, EHeroAct.ChiefHit)
        print("处理进入施放主技能后逻辑")

    def showaidbefore(self):
        """进入援助状态前"""
        print("处理进入援助前逻辑")

    def showaidafter(self):
        """进入援助状态后"""
        print("处理进入援助后逻辑")

    def showdeadbefore(self):
        """进入死亡状态前"""
        print("处理进入死亡前")

    def showdeadafter(self):
        """进入死亡状态后"""
        self.dead = True
        print("处理进入死亡后")
