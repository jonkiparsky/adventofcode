
class IntCode()
    def process_input(self, input, pos):
        if input[pos] == 99:
            return False
        if input[pos] == 1:
            op1, op2, dest = input[pos+1:pos+4]
            input[dest] = input[op1] + input[op2]
            return True
        if input[pos] == 2:
            op1, op2, dest = input[pos+1:pos+4]
            input[dest] = input[op1] * input[op2]
            return True
        if input[pos] == 3:

        raise Exception


    def run(self, input):
        cont = True
        pos = 0
        while cont:
            cont = self.process_input(input, pos)
            pos += 4
