from classes import Punto
from classes import Linea

print(Punto.__doc__)
p1 = Punto(5, 5)
p2 = Punto(y=170)
p3 = Punto(400, 10)
l1 = Linea(p1, p2)
l2 = Linea(p2, p3)

""" print(p1.propiedad)
p1.propiedad = [] """

# print(p1)
# print(repr(p1))
# print(l1, l1.__size()) <- an error
print(l1, l1.size())
print(l2, l2.size())

p1.x = -50
p1.y = -10
print(p1)
exit()


import math
import tk_inter as tk

root = rk.Tk()
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

lineas = []
nlineas = ancho // 8
desx = ancho // nlineas
rotation = 2 * math.pi / nlineas
largo_linea = alto // 3
for i in range(nlineas):
    yini = alto // 2
    xini = i * desx
