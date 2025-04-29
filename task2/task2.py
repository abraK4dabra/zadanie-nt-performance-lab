from math import sqrt

circle_file = 'circle.txt'
dots_file = 'dot.txt'

with open(circle_file) as f:
    xc, yc = f.readline().split()
    xc, yc = float(xc), float(yc)
    r = float(f.readline())

with open(dots_file) as f:
    points = f.readlines()

for point in points:
    x_str, y_str = point.split()
    x = float(x_str)
    y = float(y_str)

    distance = sqrt((xc - x) ** 2 + (yc - y) ** 2)

    if distance == r:
        print(0)
    elif distance < r:
        print(1)
    else:
        print(2)
