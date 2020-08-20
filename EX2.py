import math

x1 = int(input('Please input x1:'))
y1 = int(input('Please input y1:'))
x2 = int(input('Please input x2:'))
y2 = int(input('Please input y2:'))

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 )

print("{:d},{:d}到{:d},{:d}的距離為{:.2f}".format(x1, y1, x2, y2, distance))


