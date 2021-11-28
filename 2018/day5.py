input = open("day5_input.txt").read()

class Reducer:
    def __init__(self, input):
        self.unconsumed = list(input)
        self.consumed = []
        

    def reduce(self):
        while self.unconsumed:
            self.react()
        return "".join(self.consumed)

    def react(self):
        next = self.unconsumed.pop(0)
        if not self.consumed:
            self.consumed.append(next)
            return
        if self.reacts(next):
            self.consumed.pop()
            return
        self.consumed.append(next)

    def reacts(self, char):
        prev = self.consumed[-1]
        if char == prev:
            return False
        if char.upper() == prev.upper():
            return True

