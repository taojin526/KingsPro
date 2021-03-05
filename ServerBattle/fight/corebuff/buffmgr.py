from fight.datanotes.notemgr import NoteMgr
from fight.utils.makeuuid import MakeUUID

from .buff import Buff

notemgr = NoteMgr()


class BuffMgr:
    """Buff管理器"""
    def __init__(self, uuid: int, uuidseed: int):
        self.uuid = uuid  # 英雄的uuid
        self.uuidmake = MakeUUID(uuidseed)
        self.dictbuffs = {}  # buff字典

    def addbuff(self, bid: int):
        """添加buff"""
        if bid in self.buffs:
            buff: Buff = self.dictbuffs[bid]
            buff.updateduration()
            buff.setduration(self.uuidmake.getuuid())
        else:
            buff = Buff(self.uuid, bid)
            buff.setduration(self.uuidmake.getuuid())
            self.dictbuffs[bid] = buff

    def addbuffs(self, buffs: list):
        """批量添加buff"""
        [self.addbuff(bf) for bf in buffs]
        notemgr.herobuff.refreshtakebuffs(self.uuid, self.getbuffs())

    def deduration(self):
        """所有buff持续时间减1回合"""
        for bf in self.dictbuffs:
            buff: Buff = self.dictbuffs[bf]
            buff.deduration()

    def getbuffs(self):
        """获取buff列表"""
        return list(self.dictbuffs.keys())

    def triggercheck(self):
        """检测触发"""
        for bf in self.dictbuffs:
            ckbuff: Buff = bf
            ckbuff.handletrigger(self.uuid)
