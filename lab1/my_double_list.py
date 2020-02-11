# реализация циклического двусвязного списка
from weakref import ref

class DLL:
    class Node:
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
            if data is not None and not isinstance(data, (int, str)):
                raise TypeError
            elif pred is not None and not isinstance(pred, type(self)):
                raise TypeError
            elif sled is not None and not isinstance(pred, type(self)):
                raise TypeError
            else:
                self.pred = pred
                self.data = data
                self.sled = sled

    def __init__(self):
        """
        Конструктор циклического двунаправленного списка
        """
        self.head = None
        self.tail = None
        self.__lenght = 0

    def __str__(self):
        """
        Метод, доступный через print(), выводит в консоль получившийся список,
        от начала self.head к концу self.tail
        :return: str
        """
        usel = self.head
        spisok = str()
        i = 0
        while i < self.__lenght:
            spisok += f"{usel.data}, "
            usel = usel.sled
            i += 1
        spisok = "[" + spisok[:-2] + "]"
        return spisok

    @property
    def str_lenght(self):
        """
        Метод, позволяющий посмотреть длину списка
        :return: int
        """
        return self.__lenght

    def ssilki(self):
        """
        Метод для проверки ссылок, печает адрес каждого узла,
        и адреса, на которые можно перейти с данного узла.
        :return: None
        """
        usel = self.head
        i = 0
        while i < self.__lenght:
            print(usel.data, hex(id(usel)), hex(id(usel.pred)), hex(id(usel.sled)))
            usel = usel.sled
            i += 1

    def str_back(self):
        """
        Метод, выводящий в консоль получившийся список в обратном порядке,
        с конца self.tail к началу self.head
        :return: str
        """
        usel = self.tail
        spisok = "["
        i = 0
        while i < self.__lenght:
            spisok += f"{usel.data}, "
            usel = usel.pred
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
            self.tail = self.Node(node, self.head, None)
            self.head.sled = self.tail
        else:
            current_node = self.tail
            self.tail = self.Node(node, current_node, self.head)
            current_node.sled = self.tail
            self.head.pred = self.tail
        self.__lenght += 1

    def remove_node(self, indx):
        """
        Удаление узла по индексу
        :param indx: int
        """
        if not isinstance(indx, int):
            raise TypeError

        if indx == 0:
            if self.__lenght > 1:
                current_node = self.head
                self.head = current_node.sled
                current_node.sled = None
                current_node.pred = None
                self.head.pred = self.tail
                self.tail.sled = self.head
            else:
                self.clear()

        elif indx == self.__lenght-1:
            current_node = self.tail
            self.tail = current_node.pred
            current_node.pred = None
            current_node.sled = None
            self.tail.sled = self.head
            self.head.pred = self.tail

        elif 1 <= indx <= self.__lenght-1:
            current_node = self.head.sled
            pred_node = self.head
            sled_node = current_node.sled
            sch = 1
            while sch < self.__lenght-1:
                if sch == indx:
                    pred_node.sled = sled_node
                    sled_node.pred = pred_node
                    current_node.pred = None
                    current_node.sled = None
                    current_node = sled_node
                else:
                    current_node = current_node.sled
                    pred_node = current_node.pred
                    sled_node = current_node.sled
                sch += 1
        else:
            print("Нет такого индекса")
            self.__lenght += 1
        self.__lenght -= 1

    def delete_node(self, node):
        """
        Удаление узла по значению,
        если значение есть в списке, то оно будет удалено,
        если значение повторяется несколько раз, то и удалится оно несколько раз.
        :param node: int, str
        """
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
                    sled_node.pred = new_node

                current_node = current_node.sled
                sled_node = current_node.sled
                sch += 1
            self.__lenght += 1

    def left_add_node(self, node):
        """
        Добавление занчение в список слева.
        :param node: int, str
        """
        head = self.head
        self.head = self.Node(node, self.tail, head)
        head.pred = self.head
        self.tail.sled = self.head
        self.__lenght += 1

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
        self.head = None
        self.tail = None
        self.lenght = 0


if __name__ == "__main__":
    dlist = DLL()
    dlist.add_node(2)
    dlist.add_node(7)
    dlist.add_node(9)
    dlist.add_node(1)
    dlist.add_node(4)
    dlist.add_node(8)
    print(dlist, dlist.str_lenght)
    print(dlist.search_node(4))
    dlist.left_add_node(3)
    dlist.left_add_node(6)
    print(dlist, dlist.str_lenght)
    print(dlist.str_back())
    dlist.remove_node(7)
    print(dlist, dlist.str_lenght)
    dlist.delete_node(9)
    print(dlist, dlist.str_lenght)
    dlist.insert_node(3, 4)
    print(dlist, dlist.str_lenght)
    dlist.ssilki()
