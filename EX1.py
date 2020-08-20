import math

diameter = int(input('Please input diameter: '))

area = math.pi * (diameter/2)**2
perimeter = 2 * math.pi * (diameter/2)

#print('%.2f, %.2f' % (area, perimeter))
print('{:.2f}, {:.2f}'.format(area,perimeter))
