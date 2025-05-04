import sys


def circular_array(a, m):
    n = len(a)
    path = []
    current = 0
    while len(path) < n:
        path.append(a[current])
        current = (current + m - 1) % n
    print(path)


n_0 = int(sys.argv[1])
n_1 = int(sys.argv[2])
m = int(sys.argv[3])

n = [i for i in range(n_0, n_1 + 1)]
circular_array(n, m)
