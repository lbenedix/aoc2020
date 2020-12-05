import json
from pathlib import Path

lines = Path('input').open().readlines()

max_id = 0
seats = dict()

for line in lines:
    row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(line[7:].replace('R', '1').replace('L', '0'), 2)
    seat_id = row * 8 + col

    if row not in seats:
        seats[row] = '........'
    seats[row] = seats[row][:col] + 'X' + seats[row][col + 1:]

    max_id = max(max_id, seat_id)

part2 = ''
for row in sorted(seats):
    if '.' in seats[row]:
        free_col = seats[row].find('.')
        seat_id = row * 8 + free_col

        part2 += f'{row} {free_col} {seats[row]} {seat_id}' + '\n'

print('part 1', max_id)
print('part 2\n', part2)
