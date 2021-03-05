from enum import IntEnum, unique


@unique
class ERelation(IntEnum):
    """
    条件关系枚举：
     * 1、所有条件都满足
     * 2、所有条件满足任意一个
    """
    AllAccord = 1
    AnyOneAccord = 2


class EGetRelation(IntEnum):
    """
    取值关系：
     * 1、全部值
     * 2、所有值的其中一个
    """
    All = 1
    AnyOne = 2


@unique
class ECalOp(IntEnum):
    """
    计算关系枚举：
     * 1、等于
     * 2、大于
     * 3、小于
     * 4、大于等于
     * 5、小于等于
    """
    Equal = 1
    More = 2
    Less = 3
    MoreAndEqual = 4
    LessAndEqual = 5
