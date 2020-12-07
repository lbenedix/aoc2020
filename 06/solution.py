from pathlib import Path

lines = Path('input').open().readlines()

part_1 = 0
group = []
all_groups = []
for line in lines:
    line = line.strip()
    if len(line) > 0:
        group.append(line)
    else:
        all_groups.append(group)
        distinct_letters = set(''.join(group))
        part_1 += len(distinct_letters)
        group = []

print('part1', part_1)

total = 0
for group in all_groups:
    counts = dict()
    for person in group:
        for a in person:
            if a not in counts:
                counts[a] = 0
            counts[a] += 1

    for answer, count in counts.items():
        if count == len(group):
            total += 1
print('part2', total)
