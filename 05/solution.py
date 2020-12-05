from pathlib import Path

lines = Path('input').open().readlines()

max_id = 0
for line in lines:
    row = int(line[:7].replace('B', '1').replace('F', '0'), 2)
    col = int(line[7:].replace('R', '1').replace('L', '0'), 2)

    seat_id = row * 8 + col
    max_id = max(max_id, seat_id)

print(max_id)
