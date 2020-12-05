import json
from pathlib import Path

lines = Path('input').open().readlines()

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

        diff = required_fields - passport.keys()
        if len(diff) == 0:
            count += 1
            print('👍', json.dumps(passport, sort_keys=True))
        else:
            print('🛑', json.dumps(passport, sort_keys=True))
            print('🧐', diff)


        passport = {}
        passport_str = ''

print(count)
