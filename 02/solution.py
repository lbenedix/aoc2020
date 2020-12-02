from pathlib import Path
import timeit

passwords = [
    {
        'min': int(x.strip().split(':')[0].split(' ')[0].split('-')[0]),
        'max': int(x.strip().split(':')[0].split(' ')[0].split('-')[1]),
        'letter': x.strip().split(':')[0].split(' ')[1],
        'password': x.strip().split(':')[1],
    }
    for x in Path('part1').open().readlines()]


def part_1():
    result = 0
    for p in passwords:
        c = p['password'].count(p['letter'])
        if p['max'] >= c >= p['min']:
            result += 1

    return result


def part_2():
    result = 0
    for p in passwords:
        if bool(p['password'][p['min']] == p['letter']) ^ bool(p['password'][p['max']] == p['letter']):
            result += 1
    return result


if __name__ == '__main__':
    print(part_1())
    print(part_2())
    print(timeit.timeit(part_1, number=100) / 100)
    print(timeit.timeit(part_2, number=100) / 100)