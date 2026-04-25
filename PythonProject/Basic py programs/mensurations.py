from MyPackage.basic_shapes import areaofsquare, perimeterofsquare, area_of_rect
from MyPackage.circle import areaofcircle, perimeter

radius = int(input('enter a radius: '))

print('area :', areaofcircle(rad=radius))
print('peri :', perimeter(rad=radius))

si = int(input('Enter side of sq: '))
print('Area : ', areaofsquare(side=si))
print('peri :', perimeterofsquare(side=si))

l = int(input('Enter length: '))
b = int(input('enter breadth: '))
print('area : ', area_of_rect(l, b))
