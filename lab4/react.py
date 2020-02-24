class Observer:
    def update(self):
        pass


class Subject:
    def __init__(self):
        self._o = set()

    def add_observer(self, o):
        self._o.add(o)

    def remove_observer(self, o):
        self._o.remove(o)

    def notify(self):
        for o in self._o:
            o.update(self)
