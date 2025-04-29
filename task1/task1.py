def circular_array(a, m):
    n = len(a)
    path = []
    current = 0
    while True:
        path.append(a[current])
        current = (current + (m - 1)) % n
        if current == 0:
            break
    print(path)


# Пример
n = [1, 2, 3, 4, 5]
m = 4
circular_array(n, m)
