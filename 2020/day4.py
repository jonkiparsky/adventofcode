import re
PROBLEM_BASENAME = "day4"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)

REQUIRED_KEYS = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']

def valid_integer(candidate, required_length, min_val, max_val):
    if not candidate:
        return False
    if not candidate.isdigit() or len(candidate) != required_length:
        return False
    return min_val <= int(candidate) <= max_val

def valid_byr(byr):
    return valid_integer(byr, 4, 1920, 2002)

def valid_iyr(iyr):
    return valid_integer(iyr, 4, 2010, 2020)

def valid_eyr(eyr):
    return valid_integer(eyr, 4, 2020, 2030)

def valid_hgt(hgt):
    if not hgt:
        return False
    pat = re.compile("(\d+)(\w+)")
    m = pat.match(hgt)
    if not m:
        return False
    measure, units = m.groups()
    if units == "cm":
        return 150 <= int(measure) <= 193
    if units == "in":
        return 59 <=int(measure) <= 76
    return False

def valid_hcl(hcl):
    if not hcl:
        return False
    pat = re.compile("#[a-f0-9]{6}")
    return pat.match(hcl)

def valid_ecl(ecl):
    return ecl in "amb blu brn gry grn hzl oth".split(" ")
    
def valid_pid(pid):
    if not pid:
        return False
    return pid.isdigit() and len(pid) == 9


    
validation_rules = {"hcl": valid_hcl,
                    "iyr": valid_iyr,
                    'eyr': valid_eyr,
                    'ecl': valid_ecl,                
                    'pid': valid_pid,
                    'byr': valid_byr,
                    'hgt': valid_hgt}

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    rows = f.read().split("\n\n")
    passports = [row.strip() for row in rows if row]
    passports = [to_dict(passport) for passport in passports]
    return passports

def to_dict(passport):
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    passport = dict([item.split(":") for item in passport if item])
    return passport

def solve(passports, validation):
    valid = [passport for passport in passports if validation(passport)]
    return len(valid)

def valid_1(passport):
    return all([passport.get(key) for key in REQUIRED_KEYS])

def valid_2(passport):
    return all([rule(passport.get(key)) for key, rule in validation_rules.items()])

def validate2(passport):
    return [rule(passport.get(key)) for key, rule in validation_rules.items()]
