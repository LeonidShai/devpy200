import os
import sys

from figures import Figure
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint
from figures import Rectangle
from figures import Ellipse
from figures import CloseFigure


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # чтобы помнить что там в QWidget
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):

        painter = QPainter(self)
        reset_brush = painter.brush()

        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.x, figure.y, figure.width, figure.height)
                continue

            if isinstance(figure, Ellipse):  # ждёт прямоугольник
                 painter.setBrush(QBrush(Qt.green))
                 painter.drawEllipse(figure.x, figure.y, figure.width, figure.height)
                 continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))

                points = []
                for point in figure:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue



if __name__ == '__main__':
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = './platforms'
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    rect_1 = Rectangle(20, 30, 400, 200)
    rect_2 = Rectangle(100, 300, 300, 50)
    ell = Ellipse(200, 400, 150, 100)
    zamk = CloseFigure({'x': 200, 'y': 500},
                       {'x': 300, 'y': 600},
                       {'x': 250, 'y': 650},
                       {'x': 100, 'y': 700},
                       {'x': 100, 'y': 600})
    figures = [rect_1, rect_2, ell, zamk]
    print(f"Периметр прямоугольника 1: {rect_1.perimeter()}, Площадь: {rect_1.square()}")
    print(f"Периметр прямоугольника 2: {rect_2.perimeter()}, Площадь: {rect_2.square()}")
    print(f"Периметр эллипса: {ell.perimeter()}, Площадь: {ell.square()}")

    # figures = []
    figure_widget.set_figures(figures)

    figure_widget.show()  # Paint Event
    sys.exit(app.exec_())