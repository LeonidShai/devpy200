# Наблюдатель со слабыми ссылками
from weakref import ref

class Observer:
    def update(self):
        pass


class Subject:
    def __init__(self):
        self._o = set()

    def add_observer(self, o):
        self._o.add(ref(o))

    def remove_observer(self, o):
        self._o.remove(ref(o))

    def notify(self):
        for o in self._o:
            o.update(self)
