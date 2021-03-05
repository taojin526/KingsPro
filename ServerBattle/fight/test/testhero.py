from .datanotes import TestDataNotes

NOTES = TestDataNotes()


class TestHero:
    """"""
    def __init__(self, hid):
        """"""
        self.hid = hid

    def atk(self):
        """"""
        NOTES.notecount(self.hid)

    def judge(self):
        """"""
        return NOTES.getcount(self.hid)
