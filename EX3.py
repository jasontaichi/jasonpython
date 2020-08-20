import math

string1 = input('Please input the first coordinate:')
string2 = input('Please input the second coordinate:')

x1 = int(string1.split(",")[0])
y1 = int(string1.split(",")[1])
x2 = int(string2.split(",")[0])
y2 = int(string2.split(",")[1])

distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 )

print("{:d},{:d}到{:d},{:d}的距離為{:.2f}".format(x1, y1, x2, y2, distance))


