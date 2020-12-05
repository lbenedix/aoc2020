import json
from pathlib import Path

lines = Path('input').open().readlines()

required_fields = {
    'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',
}

passport_str = ''
passport = {}
part_1_count = 0
part_2_count = 0
passports = []
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

        passports.append(passport)
        passport = {}
        passport_str = ''

for passport in passports:
    diff = required_fields - passport.keys()
    if len(diff) == 0:
        part_1_count += 1

        if not (1920 <= int(passport['byr']) <= 2002):
            print(json.dumps(passport, sort_keys=True))
            print('🐣', passport['byr'])
            continue

        if not (2010 <= int(passport['iyr']) <= 2020):
            print(json.dumps(passport, sort_keys=True))
            print('💌', passport['iyr'])
            continue

        if not (2020 <= int(passport['eyr']) <= 2030):
            print(json.dumps(passport, sort_keys=True))
            print('🛑', passport['eyr'])
            continue

        if 'cm' in passport['hgt'] or 'in' in passport['hgt']:
            if 'cm' in passport['hgt']:
                if not (150 <= int(passport['hgt'].split('cm')[0]) <= 193):
                    print(json.dumps(passport, sort_keys=True))
                    print('📏', passport['hgt'])
                    continue

            if 'in' in passport['hgt']:
                if not (59 <= int(passport['hgt'].split('in')[0]) <= 76):
                    print(json.dumps(passport, sort_keys=True))
                    print('📏', passport['hgt'])
                    continue
        else:
            print('📏', passport['hgt'])
            continue

        if passport['hcl'][0] != '#':
            print(json.dumps(passport, sort_keys=True))
            print('💇', passport['hcl'])
            continue

        try:
            int(passport['hcl'][1:], 16)
        except ValueError as e:
            print(json.dumps(passport, sort_keys=True))
            print('💇', passport['hcl'])
            continue

        if passport['ecl'] not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            print(json.dumps(passport, sort_keys=True))
            print('👁', passport['ecl'])
            continue

        if len(passport['pid']) == 9:
            try:
                int(passport['pid'])
            except ValueError as e:
                print(json.dumps(passport, sort_keys=True))
                print('🛂', passport['pid'])
                continue
        else:
            print(json.dumps(passport, sort_keys=True))
            print('🛂', passport['pid'])
            continue

        part_2_count += 1
        # print('👍', json.dumps(passport, sort_keys=True))

print('part1', part_1_count)
print('part2', part_2_count)
