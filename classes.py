"""Modulo de ejemplo para clase de FP2"""

import math


class Punto:
    """Clase que representa un punto en un plano."""

    # method - self는 필수  / 좌표 만드는 클래스
    def __init__(self, x=0, y=0):
        """Constructor de clase punto.

        Descripción más larga, pueden ser varias lineas.

        x: Numero => valor del eje x
        y: Numero => valor del eje y
        No devuelve nada
        """
        self.x = x  # self == this is in C++, Java, PHP, etc.
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, nuevo_x):
        if type(nuevo_x) is not int:
            raise TypeError("new x must be int")
        self.__x = nuevo_x
        if self.__x < 0:
            self.__x = 0

    def __repr__(self):
        return f"Punto({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    # changed x and y to __x and __y
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, nuevo_x):
        if type(nuevo_x) is not int:
            raise TypeError("new x must be int")
        self.__x = nuevo_x
        if self.__x < 0:
            self.__x = 0

    def set_y(self, nuevo_y):
        if type(nuevo_y) is not int:
            raise TypeError("new y must be int")
        self.__y = nuevo_y
        if self.__y < 0:
            self.__y = 0


"""     def __algo(self):
        print("Getter algo")

    def __algo1(self, s):
        print("setter algo")

    propiedad = property(__algo, __algo1)

    x = property(get_x, set_x)
    y = property(get_y, set_y) """


class Linea:
    def __init__(self, p1, p2):
        self.ini = p1
        self.fin = p2

    def __str__(self):
        return f"({self.ini}, {self.fin})"

    """
    def get_str(self):
        return f"({self.ini.get_str()}, {self.fin.get_str()})"
    """

    def __repr__(self):
        return f"Linea({repr(self.ini)}, {repr(self.fin)})"

    def dibuja(self, canvas):
        canvas.create_line(
            self.ini.x, self.ini.y, self.fin.x, self.fin.y, fill="blue", width=2
        )

    def __size(self):
        difx = self.ini.get_x() - self.fin.get_x()
        dify = self.ini.get_y() - self.fin.get_y()
        return math.sqrt(difx * difx + dify * dify)

    size = property(__size)


"""
p1 = Punto(5, 5)
p2 = Punto(6, 6)
p3 = Punto(7, 10)
l1 = Linea(p1, p2)
l2 = Linea(p2, p3)
print(p1.get_str(), p2.get_str(), l1.get_str(), l1.size())
print(p2.get_str(), p3.get_str(), l2.get_str(), l2.size())

objecto = Punto()
print(objecto.x, objecto.y)  # 0, 0
objecto.x = 45
objecto.y = 35

ob2 = Punto(5, 5)
print(ob2.x, ob2.y)  # 5, 5

print(type(objecto))
print(objecto.x, objecto.y)  # 45, 35

lista_puntos = [Punto(x, x + 5) for x in range(3)]

for punto in lista_puntos:
    print(punto.x, punto.y)
    # 0, 5
    # 1, 6
    # 2, 7
"""
