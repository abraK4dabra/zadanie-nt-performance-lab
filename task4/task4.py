if __name__ == '__main__':
    with open('numbers.txt', 'r') as f:
        nums = f.readlines()
        numbers = [int(num.strip()) for num in nums]

    numbers.sort()
    median = numbers[len(numbers) // 2]
    total_moves = sum(abs(n - median) for n in numbers)

    print(total_moves)
