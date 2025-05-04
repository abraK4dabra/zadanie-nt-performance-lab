import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Укажите путь к файлу с числами.")
        exit()

    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f if line.strip()]

    numbers.sort()
    median = numbers[len(numbers) // 2]
    total_moves = sum(abs(n - median) for n in numbers)

    print(total_moves)
