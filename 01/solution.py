from pathlib import Path
import timeit

numbers = [int(x.strip()) for x in Path('part1').open().readlines()]


def part_1_for():
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if j < i:
                continue

            if x + y == 2020:
                return y * y


def part_2_for():
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            if j < i:
                continue
            for k, c in enumerate(numbers):
                if k < j:
                    continue
                if a + b + c == 2020:
                    return a * b * c


def part_2_random():
    import random
    while True:
        a, b, c = random.sample(numbers, 3)
        if a + b + c == 2020:
            return a * b * c


def part_2_permutation():
    from itertools import permutations
    for a, b, c in permutations(numbers, 3):
        if a + b + c == 2020:
            return a * b * c


def part2_oneline():
    return next(n * m * o for i, n in enumerate(numbers) for ii, m in enumerate(numbers[i:]) for o in numbers[i + ii:] if n + m + o == 2020)


if __name__ == '__main__':
    print(timeit.timeit(part_1_for, number=10)/10)

    print(timeit.timeit(part_2_for, number=10)/10)

    print(timeit.timeit(part_2_permutation, number=10)/10)

    print(timeit.timeit(part2_oneline, number=10)/10)

    # print(timeit.timeit(part_2_random, number=1))
