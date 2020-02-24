# реализация циклического двусвязного списка с использование слабых ссылок
import weakref
import drivers
from react import Observer, Subject

class DLL(Observer):
    class Node(Subject):
        """
        Создание узла
        """
        def __init__(self, data=None, pred=None, sled=None):
            """
            Конструктор узла, на вход принимает данные типа int или str
            В противном случае - исключение TypeError
            :param data: int or str
            :param pred: type(self)
            :param sled: type(self)
            """
            super().__init__()
            if data is not None and not isinstance(data, (int, str)):
                raise TypeError
            elif pred is not None and not isinstance(pred, type(self)):
                raise TypeError
            elif sled is not None and not isinstance(pred, type(self)):
                raise TypeError
            else:
                self.pred = weakref.ref(pred) if pred is not None else None
                self.data = data
                self.sled = sled

        def __str__(self):
            return self.data

    def __init__(self):
        """
        Конструктор циклического двунаправленного списка
        """
        self.head = None
        self.tail = None
        self.__lenght = 0

        self.__structure_driver = None

    def __str__(self):
        """
        Метод, доступный через print(), выводит в консоль получившийся список,
        от начала self.head к концу self.tail
        :return: str
        """
        if self.__lenght == 0:
            return f"[]"

        usel = self.head
        spisok = str()
        i = 0
        while i < self.__lenght:
            spisok += f"{usel.data}, "
            usel = usel.sled
            i += 1
        spisok = "Список:\t\t\t [" + spisok[:-2] + "]"
        return spisok

    @property
    def str_lenght(self):
        """
        Метод, позволяющий посмотреть длину списка
        :return: int
        """
        return f"{self.__lenght} элементов"

    def __ssilki(self):
        """
        Метод для проверки ссылок, печает адрес каждого узла,
        и адреса, на которые можно перейти с данного узла.
        :return: None
        """
        usel = self.head
        i = 0
        while i < self.__lenght:
            print(usel.data, hex(id(usel)), usel.pred, hex(id(usel.sled)))
            usel = usel.sled
            i += 1

    def str_back(self):
        """
        Метод, выводящий в консоль получившийся список в обратном порядке,
        с конца self.tail к началу self.head
        :return: str
        """
        usel = self.head.pred
        spisok = "Обратный список: ["
        i = 0
        while i < self.__lenght:
            spisok += f"{usel().data}, "
            usel = usel().pred
            i += 1
        spisok = spisok[:-2] + "]"
        return spisok

    def add_node(self, node):
        """
        Добавление в нового узла в конец списка
        :param node: int, str
        :return:
        """
        if not self.head:
            self.head = self.Node(node, None, None)
        elif not self.tail:
            self.tail = self.Node(node, self.head, self.head)
            self.head.sled = self.tail
            self.head.pred = weakref.ref(self.tail)
        else:
            current_node = self.tail
            self.tail = self.Node(node, current_node, self.head)
            current_node.sled = self.tail
            self.head.pred = weakref.ref(self.tail)
        self.__lenght += 1
        t = self.Node()
        t.add_observer(self)
        t.notify()

    def remove_node(self, indx):
        """
        Удаление узла по индексу
        :param indx: int
        """
        if not isinstance(indx, int):
            raise TypeError

        print(f"Удаляю элемент с индексом {indx} из списка")
        if indx == 0:
            if self.__lenght > 1:
                current_node = self.head
                self.head = current_node.sled
                current_node.sled = None
                current_node.pred = None
                self.head.pred = weakref.ref(self.tail)
                self.tail.sled = self.head
            else:
                self.clear()

        elif indx == self.__lenght-1:
            current_node = self.tail
            self.tail = current_node.pred()
            current_node.pred = None
            current_node.sled = None
            self.tail.sled = self.head
            self.head.pred = weakref.ref(self.tail)

        elif 1 <= indx <= self.__lenght-1:
            current_node = self.head.sled
            pred_node = self.head
            sled_node = current_node.sled
            sch = 1
            while sch < self.__lenght-1:
                if sch == indx:
                    pred_node.sled = sled_node
                    sled_node.pred = weakref.ref(pred_node)
                    current_node.pred = None
                    current_node.sled = None
                    current_node = sled_node
                else:
                    current_node = current_node.sled
                    pred_node = pred_node.sled
                    sled_node = sled_node.sled
                sch += 1
        else:
            print("Нет такого индекса")
            self.__lenght += 1
        self.__lenght -= 1
        t = self.Node()
        t.notify()

    def delete_node(self, node):
        """
        Удаление узла по значению,
        если значение есть в списке, то оно будет удалено,
        если значение повторяется несколько раз, то и удалится оно несколько раз.
        :param node: int, str
        """
        print(f"Удаление узла со значением {node} из списка")
        index = self.search_node(node)
        if isinstance(index, list):
            self.remove_node(index[0])
            for i in range(1, len(index)):
                poz = index[i] - 1
                self.remove_node(poz)
        elif isinstance(index, str):
            print(index)
        else:
            self.remove_node(index)

    def insert_node(self, node, indx=0):
        """
        Вставка узла по индексу в список.
        По умолчанию значение вставляется первым элементом,
        если индекс больше длины списка, вставка в конец.
        :param node: int, str
        :param indx: int
        """
        if not isinstance(indx, int):
            raise TypeError
        if not isinstance(node, (int, str)):
            raise TypeError

        print(f"Вставка элемента {node} с индексом {indx}.")
        print("Индексация начинается с нуля!")
        if indx == 0:
            print("1")
            self.left_add_node(node)
        elif indx > self.__lenght-1:
            print("2")
            self.add_node(node)
        else:
            current_node = self.head
            sled_node = current_node.sled
            sch = 0
            while sch < self.__lenght-1:
                if sch+1 == indx:
                    current_node.sled = None
                    sled_node.pred = None
                    new_node = self.Node(node, current_node, sled_node)
                    current_node.sled = new_node
                    sled_node.pred = weakref.ref(new_node)

                current_node = current_node.sled
                sled_node = current_node.sled
                sch += 1
            self.__lenght += 1
        t = self.Node()
        t.notify()

    def left_add_node(self, node):
        """
        Добавление занчение в список слева.
        :param node: int, str
        """
        head = self.head
        self.head = self.Node(node, self.tail, head)
        head.pred = weakref.ref(self.head)
        self.tail.sled = self.head
        self.__lenght += 1
        t = self.Node()
        t.notify()

    def search_node(self, node):
        """
        Поиск по значению в списке,
        если значение есть, то выводится его индекс (индексация с нуля),
        если значение повторяется, выводятся все индексы
        :param node: int, str
        :return: str, list
        """
        if not isinstance(node, (int, str)):
            raise TypeError

        print(f"Провожу поиск узла {node} в списке")
        current_node = self.head
        spisok_index = []
        index = 0
        while index < self.__lenght:
            if current_node.data == node:
                spisok_index.append(index)
            index += 1
            current_node = current_node.sled

        if len(spisok_index) == 0:
            return "Такого узла в списке нет!"
        elif len(spisok_index) == 1:
            return spisok_index[0]
        else:
            return spisok_index

    def clear(self):
        """
        Очистка списка.
        """
        usel = self.head.pred
        i = 0
        while i < self.__lenght:
            del usel().sled
            usel = usel().pred
            i += 1
        self.__lenght = 0
        t = self.Node()
        t.notify()

    def to_dict(self):
        current_node = self.head
        d = {}
        i = 0
        while i < self.__lenght:
            d[i] = current_node.data
            i += 1
            current_node = current_node.sled
        return d

    def from_dict(self, d={0: "Python", 1: "good"}):
        for index, value in d.items():
            self.insert_node(value, index)
        print(self.to_dict())

    def set_structure_driver(self, driver):
        self.__structure_driver = driver

    def load(self):
        self.from_dict(self.__structure_driver.read())

    def save(self):
        self.__structure_driver.write(self.to_dict())

    def update(self, node):
        print("Value changed")
        self.save()


if __name__ == "__main__":
    dlist = DLL()
    dlist.add_node("hello")
    dlist.add_node("hey")
    dlist.add_node("hi")
    dlist.add_node("ciao")
    dlist.add_node("buonjiorno")
    dlist.add_node("salut")
    # print(dlist, dlist.str_lenght)
    # print(dlist.search_node(9))
    dlist.left_add_node("bounjour")
    dlist.left_add_node("gutentag")
    # print(dlist, dlist.str_lenght)
    # print(dlist.str_back())
    # dlist.remove_node(5)
    # print(dlist, dlist.str_lenght)
    # dlist.delete_node(1)
    # print(dlist, dlist.str_lenght)
    # dlist.insert_node(3, 4)
    print(dlist, dlist.str_lenght)
    # print(dlist.to_dict())
    # dlist.from_dict()
    # dlist.set_structure_driver(drivers.JSONFileDriver("test.json"))
    # dlist.save()
    dlist.clear()
    print(dlist, dlist.str_lenght)
