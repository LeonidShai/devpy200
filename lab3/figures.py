class Figure:
    def __init__(self, x=0, y=0, w=0, h=0):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError
        self._y = y


class Rectangle(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y, w, h)

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def square(self):
        return self.width * self.height


class Ellipse(Figure):
    def __init__(self, x=0, y=0, w=0, h=0):
        super().__init__(x, y, w, h)

    def perimeter(self):
        return 2 * (4 * self.square() + (self.height - self.width) * (self.height - self.width)) / (self.width + self.height)

    def square(self):
        return 3.14 * self.width * self.height / 4


class CloseFigure(Figure):
    def __init__(self, *args):
        super().__init__(args[0]['x'], args[0]['y'])
        self._args = args

    def __iter__(self):
        return iter(self._args)

if __name__ == "__main__":
    rect = Rectangle(100, 100, 5, 10)
    print(rect.perimeter())
