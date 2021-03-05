from collections.abc import Callable

from fight.utils.singleton import Singleton


class EventHandle:
    """事件处理"""
    def __init__(self, cb: Callable):
        # 回调处理函数
        self.cb = cb

    def __eq__(self, ehandle):
        if (isinstance(ehandle, EventHandle) is True
                and ehandle.cb == self.cb):
            return True
        else:
            return False

    def call(self, *args, **kwargs):
        """执行回调"""
        if self.cb is not None:
            self.cb(*args, **kwargs)


class EventHandles:
    """事件处理队列"""
    def __init__(self):
        self.handles = []

    def add(self, handle: EventHandle):
        """队列里添加事件处理"""
        self.handles.append(handle)

    def remove(self, handle: EventHandle):
        """队列里移除事件处理"""
        self.handles.remove(handle)


@Singleton
class BEvents:
    """事件管理类"""
    def __init__(self):
        """初始化"""
        self.events = {}

    def register(self, ename, ehandle: Callable):
        """注册事件"""
        eventhandles: EventHandles = self.events.setdefault(
            ename, EventHandles())
        eventhandle = EventHandle(ehandle)
        if eventhandle not in eventhandles.handles:
            eventhandles.add(eventhandle)

    def unregister(self, eventname, ehandle: Callable):
        """解绑事件"""
        eventhandles: EventHandles = self.events.setdefault(
            eventname, EventHandles())
        eventhandle = EventHandle(ehandle)
        if eventhandle in eventhandles.handles:
            eventhandles.remove(eventhandle)

    def emit(self, eventname, *args, **kwargs):
        """发射事件"""
        eventhandles: EventHandles = self.events.setdefault(
            eventname, EventHandles())
        for ehandle in eventhandles.handles:
            eventhandle: EventHandle = ehandle
            eventhandle.call(*args, **kwargs)
