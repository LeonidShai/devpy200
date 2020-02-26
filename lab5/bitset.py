import numpy as np

class BitSet:
    def __init__(self, value):
        self.__value = np.uint64(value)
        
    def __int__(self):
        return self.__value
    
    def __iand__(self, other): # &=
        if isinstance(other, int):
            self.__value &= np.uint64(other)
        # Добавьте для объекта BitSet
        return self
        
    def __ior__(self, other): # ^=
        self.__value ^= np.uint64(other)
        return self
        
    def __ixor__(self, other): # |=
        self.__value |= np.uint64(other)
        return self
        
    def __invert__(self): # инверсия всех битов (~)
        self.__value = ~self.__value
        return self
        
    def __str__(self):
        return f"{self.__value}"
        
    def __repr__(self):
        return f"({self.__value})"
    
    def __getitem__(self, items): # [] - чтение
        if isinstance(items, int):
            if items >= 0:
                return 0x1 & (self.__value >> items)
            raise ValueError()
        
    def __setitem__(self, items, value): # [] - запись 
        items.append(value)
        print(items)

if __name__ == "__main__":
    a = BitSet(1)
    print(a)
    print(a.__int__())

    b = BitSet(1)
    print(b.__iand__(3))
    print(b.__ior__(2))
    print(b.__ixor__(2))
    print(b.__invert__())
    c = BitSet([1, 2, 4, 5])
    print(c.__getitem__(2))
    c.__setitem__([1, 2, 4, 5], 9)
    print(c.__getitem__(0b001))
