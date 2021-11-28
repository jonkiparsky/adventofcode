
sample_data = '''ba dec 37 if znx != 0
zrn inc -344 if znx > -9
ffz inc -928 if kjt > 3
al inc -562 if py == 0
odo dec 294 if odo >= 0
o inc -232 if bef <= 2
al inc 536 if bef >= -7
o dec 688 if iz <= 2
sms dec 407 if kjt == 0
vg inc 245 if ije < 8
ba inc 483 if app >= -7
tsh dec -557 if vg > 242
p inc 901 if o >= -929
ga dec -352 if ffz < 8
ffz inc -525 if vg < 248
j inc -992 if app != -816
tsh inc 853 if ije == 0'''



sign = {"inc": +1, "dec": -1}
comparison = {"<": lambda a, b: a < b,
              ">": lambda a, b: a > b,
              "<=": lambda a, b: a <= b,
              ">=": lambda a, b: a >= b,
              "==": lambda a, b: a == b,
              "!=": lambda a, b: a != b,
              }

def parse_input(registers, input_file=None):
    if input_file:
        with open(input_file) as f:
            lines = f.readlines()
    else:
        lines = sample_data.split("\n")
    return [Line(line, registers) for line in lines]

class Line:
    def __init__(self, line, registers):
        (self.target_addr,
         i_d,
         val,
         _,
         self.cmp_addr,
         self.comparison,
         cmp_val) = line.split(" ")
        self.val = int(val) * sign[i_d]
        self.cmp_val = int(cmp_val)
        registers[self.target_addr] = 0
        registers[self.cmp_addr] = 0
        
    def execute(self, registers, max_val):
        comparison_op = comparison[self.comparison]        
        if comparison_op(registers[self.cmp_addr], self.cmp_val):
            registers[self.target_addr] += self.val
            max_val = max(registers[self.target_addr], max_val)
        return max_val
    
    def __repr__(self):
        return "<Line: {} + {} if {} {} {}>".format(
            self.target_addr, self.val, self.cmp_addr,
            self.comparison, self.cmp_val)


sample_data = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
    
registers = {}
max_val = 0
instructions = parse_input(registers, input_file="day_8.txt")
for instruction in instructions:
    max_val = instruction.execute(registers, max_val)
solution = max(registers.values())
