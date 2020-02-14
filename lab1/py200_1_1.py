# -*- coding: utf-8

# 
# Курс DEV-PY200. Объектно-ориентированное программирование на языке Python
# Тема 1.1 Основы ООП. Понятие класса, объекта. Создание экземпляра класса

# Лабораторная работа № 1.1 (4 ак.ч.)

# Слушатель (ФИО): Шайтанов Л.Л.

# ---------------------------------------------------------------------------------------------
# Понятие класса, объекта (стр. 1-22)

# 1. Создайте класс Glass с атрибутами capacity_volume и occupied_volume
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class Glass():
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        elif capacity_volume <= 0:
            raise ValueError
        else:
            self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        elif occupied_volume < 0:
            raise ValueError
        elif occupied_volume > capacity_volume:
            raise ValueError
        else:
            self.occupied_volume = occupied_volume


# 2. Создайте два и более объектов типа Glass
#    Измените и добавьте в любой стакан любое кол-во воды (через атрибуты)
#    Убедитесь, что у других объектов Glass атрибуты экземпляра класса не изменились.
stakan_1 = Glass(200, 12)
print(f"Volume stakan 1: {stakan_1.capacity_volume}, Volume water in stakan 1: {stakan_1.occupied_volume}")

stakan_2 = Glass(100, 0)
print(f"Volume stakan 2: {stakan_2.capacity_volume}, Volume water in stakan 2: {stakan_2.occupied_volume}")


# 3. Создайте класс GlassDefaultArg (нужен только __init__) c аргументом occupied_volume
#    По умолчанию occupied_volume равен нулю. Создайте два объекта с 0 и 200
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
class GlassDefaultArg():
    def __init__(self, capacity_volume, occupied_volume=0):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        elif capacity_volume <= 0:
            raise ValueError
        else:
            self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        elif occupied_volume < 0:
            raise ValueError
        elif occupied_volume > capacity_volume:
            raise ValueError
        else:
            self.occupied_volume = occupied_volume

stakan_1 = GlassDefaultArg(200)
print(f"Volume stakan 1: {stakan_1.capacity_volume}, Volume coffe in stakan 1: {stakan_1.occupied_volume}")

stakan_2 = GlassDefaultArg(200, 200)
print(f"Volume stakan 2: {stakan_2.capacity_volume}, Volume coffe in stakan 2: {stakan_2.occupied_volume}")


# 4. Создайте класс GlassDefaultListArg (нужен только __init__) 
#    c аргументами capacity_volume, occupied_volume.
#    Пусть аргументом по умолчанию для __init__ occupied_volume = []. Будет список.
#    Попробуйте создать 3 объекта, которые изменяют occupied_volume.append(2) внутри __init__.
#    Создавайте объект GlassDefaultListArg только с одним аргументом capacity_volume.
#    Опишите результат.
#    Подсказка: можно ли использовать для аргументов по умолчанию изменяемые типы?

class GlassDefaultListArg:
    def __init__(self, capacity_volume, occupied_volume=[]):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume
        self.occupied_volume.append(2)

stakan_1 = GlassDefaultListArg(200)
print(f"Volume stakan 1: {stakan_1.capacity_volume}, Volume coffe in stakan 1: {stakan_1.occupied_volume}")
stakan_2 = GlassDefaultListArg(200, 50)
print(f"Volume stakan 2: {stakan_1.capacity_volume}, Volume coffe in stakan 2: {stakan_1.occupied_volume}")
stakan_3 = GlassDefaultListArg(200, 150)
print(f"Volume stakan 3: {stakan_1.capacity_volume}, Volume coffe in stakan 3: {stakan_1.occupied_volume}")

# нельзя использовать для аргументов по умолчанию изменяемые типы
# при запуске возникает ошибка AttributeError
 


# 5. Создайте класс GlassAddRemove, добавьте методы add_water, remove_water
#    Обязательно проверяйте типы (TypeError) и значения переменных (ValueError)
#    Вызовите методы add_water и remove.
#    Убедитесь, что методы правильно изменяют атрибут occupied_volume.
class GlassAddRemove:
    def __init__(self, capacity_volume, occupied_volume):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        elif capacity_volume <= 0:
            raise ValueError
        else:
            self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        elif occupied_volume < 0:
            raise ValueError
        elif occupied_volume > capacity_volume:
            raise ValueError
        else:
            self.occupied_volume = occupied_volume

        self.ostatok = None

    def add_water(self, adding_water):
        if not isinstance(adding_water, (int, float)):
            raise TypeError

        space = self.capacity_volume - self.occupied_volume
        if space < adding_water:
            self.occupied_volume += space
            self.ostatok = adding_water - space
            return self.ostatok
        else:
            self.occupied_volume += adding_water

    def remove_water(self, remove_water):
        if not isinstance(remove_water, (int, float)):
            raise TypeError

        if remove_water >= self.occupied_volume:
            self.occupied_volume = 0
        else:
            self.occupied_volume -= remove_water


# проверка добавления/удаления воды
stakan = GlassAddRemove(200, 50)
print(f"Volume stakan: {stakan.capacity_volume}, Volume coffe in stakan: {stakan.occupied_volume}")

stakan.add_water(200)  # добавление воды в стакан
print(f"Volume coffe in stakan posle dobavlenia: {stakan.occupied_volume}")
print(f"Остаток воды на счёте: {stakan.ostatok}")

stakan.remove_water(50)  # удаление воды из стакана
print(f"Volume coffe in stakan posle udalenia: {stakan.occupied_volume}")
stakan.remove_water(200)
print(f"Volume coffe in stakan posle novogo udalenia: {stakan.occupied_volume}")



# 6. Создайте три объекта типа GlassAddRemove, 
#    вызовите функцию dir для трёх объектов и для класса GlassAddRemove.
#    а. Получите типы объектов и класса
#    б. Проверьте тип созданного объекта.
stakan_1 = GlassAddRemove(200, 100)
stakan_2 = GlassAddRemove(300, 150)
stakan_3 = GlassAddRemove(200, 200)

print(type(stakan_1))
print(type(stakan_2))
print(type(stakan_3))
print(type(GlassAddRemove))
print(GlassAddRemove.__dir__)
stakan_1.__dir__()



# ---------------------------------------------------------------------------------------------
# Внутренние объекты класса (стр. 25-33)

# 7. Получите список атрибутов экземпляра класса в начале метода __init__, 
#    в середине __init__ и в конце __init__, (стр. 28-30)
#    а также после создания объекта.
#    Опишите результат.
class A:
    def __init__(self, v, s):
        print(dir(self))
        print(self.__dict__)

        self.v = v
        #print(dir(self))
        print(self.__dict__)

        self.s = s
        #print(dir(self))
        print(self.__dict__)

a = A(1, 15)

# 8. Создайте три объекта Glass. (стр. 27)
#    Получите id для каждого объекта с соответсвующим id переменной self.

# используется class Glass из задания 1
glass1 = Glass(20, 5)
glass2 = Glass(30, 10)
glass3 = Glass(20, 8)

print(f"id glass 1: {hex(id(glass1))}")
print(f"id glass 2: {hex(id(glass2))}")
print(f"id glass 3: {hex(id(glass3))}")

# 9. Корректно ли следующее объявление класса с точки зрения:
#     - интерпретатора Python;
#     - соглашения о стиле кодирования
#    Запустите код.

class d:
    def __init__(f, a=2):
        f.a = a
		
    def print_me(p):
        print(p.a)
		
d.print_me(d())

# Ответ: с точки зрения интерпретатора - код корректен, работает
# с точки зрения кодирования - нет, не корректен
# название класса с большой буквы, вместо f и p требуется self


# 10. Исправьте
class A:
    def __init__(self, a):
        if 10 < a < 50:
            #return
            raise ValueError
        self.a = a

chislo_1 = A(5)
print(chislo_1.__dict__)
chislo_2 = A(20)
print(chislo_2.__dict__)

# Объясните так реализовывать __init__ нельзя?
# Так реализовывать init не стоит,
# поскольку пользователь не сможет проверить успешность создания объекта
        
        
        
# 11. Циклическая зависимость (стр. 39-44)
# двусвязный список (структура данных)

# ПРАВИЛЬНЫЙ ВАРИАНТ СМОТРЕТЬ В ФАЙЛЕ: my_double_list.py !!!!

"""
class Node:
    def __init__(self, prev=None, next_=None):
        self.__prev = prev
        self.__next = next_
    def set_next(self, next_):
        self.__next = next_

    def set_prev(self, prev):
        self.__prev = prev
        
    def __str__(self):
        ...
        
    def __repr__(self):
        ...

class LinkedList:
    def __init__(self, nodes=None):
        if nodes is None:
            self.head = None
            self.tail = None
        elif isinstance(nodes, Node):
            self.head = nodes
            self.tail = nodes
        elif isinstance(nodes, list):
            self.head = nodes[0]
            self.tail = nodes[-1]
            self.linked_nodes(nodes)

    def linked_nodes(self, nodes):
        nodes[0].set_prev(nodes[-1])
        nodes[0].set_next(nodes[1])

        for i in range(1, len(nodes)-1):
            nodes[i].set_prev(nodes[i-1])
            nodes[i].setr_next(nodes[i+1])

        nodes[-1].set_prev(nodes[-2])  # TODO Check when lenght of list == 1
        nodes[-1].set_next(nodes[0])

    def insert(self, node, index=0):
        '''
        Insert Node to any place of LinkedList
        node - Node
        index - position of node
        '''
        ...
        
       
    def append(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail.set_next(self.head)
        self.head.set_prev(self.tail)


    def append_left(self, node):
        '''
        Append Node to tail of LinkedList
        node - Node
        '''
        self.tail.set_next(node)
        self.tail = node
        self.tail.set_next(self.head)


    def clear(self):
        '''
        Clear LinkedList
        '''
        ...

    def find(self, node):
        ...


    def remove(self, node):
        ...
        
    def delete(self, index):
        ...
"""
