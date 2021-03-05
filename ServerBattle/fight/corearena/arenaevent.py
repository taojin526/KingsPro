from enum import Enum, unique

from blinker import Namespace

eventArena = Namespace().signal("eventArena")


@unique
class EventArena(Enum):
    """战场类事件"""
    HeroAddBaseProps = "hero_addbaseprops"
    HeroAddFixedProps = "hero_addfixedprops"
    HeroAddTriProps = "hero_addtriprops"
    SkillFire = "skill_fire"
