from pathlib import Path

lines = Path('input').open().readlines()


def how_many_trees(right=3, down=1):
    result = 0
    x = 0
    y = 0
    for _ in lines:
        y += down
        if y > len(lines) - 1:
            return result
        line = lines[y].strip()
        x += right
        x %= len(line)
        if line[x] == '#':
            result += 1


def part_1():
    print(how_many_trees())


def part_2():
    r = how_many_trees(1)
    r *= how_many_trees(3)
    r *= how_many_trees(5)
    r *= how_many_trees(7)
    r *= how_many_trees(1, 2)
    print(r)


if __name__ == '__main__':
    part_1()
    part_2()
