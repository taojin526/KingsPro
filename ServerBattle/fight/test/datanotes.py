"""
xxxxxxxxxxxxxxxxx
"""
from fight.utils.singleton import Singleton


@Singleton
class TestDataNotes:
    """"""
    def __init__(self):
        self.dictnotes = {}

    def notecount(self, hid: int):
        """"""
        count = self.dictnotes.setdefault(hid, 0)
        count += 1
        self.dictnotes[hid] = count

    def getcount(self, hid: int):
        """"""
        return self.dictnotes.setdefault(hid, 0)
