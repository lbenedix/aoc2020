import json
from pathlib import Path

lines = Path('example').open().readlines()

required_fields = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
}

passport_str = ''
passport = {}
count = 0
for line in lines:
    line = line.strip()
    passport_str += line + ' '

    if len(line) == 0:
        for part in passport_str.split(' '):
            if len(part) == 0: continue
            # print(f'👉{part}👈')
            k = part.split(':')[0].strip()
            v = part.split(':')[1].strip()
            passport[k] = v

        if len(passport.keys() - required_fields) == 0:
            count += 1
            print('👍', end=' ')
        else:
            print('🛑', end=' ')

        print(json.dumps(passport, sort_keys=True))
        passport = {}
        passport_str = ''

print(count)
