from pathlib import Path

numbers = [int(x.strip()) for x in Path('part1').open().readlines()]


def part_1_for():
    print('part_1_for')
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if j < i:
                continue

            if x + y == 2020:
                print(x, y, x * y)
                return


def part_2_for():
    print('part_2_for')
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers):
            for k, c in enumerate(numbers):
                if j < i:
                    continue
                if k < j:
                    continue

                if a + b + c == 2020:
                    print(a, b, c, a * b * c)
                    return


def part_2_random():
    import random
    while True:
        a, b, c = random.sample(numbers, 3)
        if a + b + c == 2020:
            print(a, b, c, a * b * c)
            return


def part_2_permutation():
    from itertools import permutations
    for a, b, c in permutations(numbers, 3):
        if a + b + c == 2020:
            print(a, b, c, a * b * c)
            return


if __name__ == '__main__':
    part_1_for()
    part_2_for()
    part_2_permutation()
    part_2_random()
