import sys
from math import sqrt

if len(sys.argv) != 3:
    print("Usage: python task2.py circle_file.txt dot_file.txt")
    sys.exit(1)

circle_file = sys.argv[1]
dots_file = sys.argv[2]

with open(circle_file) as f:
    xc, yc = map(float, f.readline().split())
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
