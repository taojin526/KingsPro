from fight.events.events import BEvents

events = BEvents()


class Test:
    """"""
    def __init__(self, name):
        self.name = name
        self.bindevents()

    def bindevents(self):
        """"""
        events.register("test1", self.newtest)
        events.register("test1", self.mytest)

    def newtest(self, name, age):
        """"""
        print("{0}/{1}/{2}".format(self.name, name, age))

    def mytest(self, name, age):
        print("{0}-{1}-{2}".format(self.name, name, age))


test1 = Test("student")
test2 = Test("teacher")
# events.unregister("test1", test1.mytest)
events.emit("test1", name="lilei", age=18)
