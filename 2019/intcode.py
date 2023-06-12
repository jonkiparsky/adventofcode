from collections import UserList

INDIRECT_MODE = 1


class EmptyQueue(Exception):
    """Raised when popping from an empty IOBuffer"""

class HaltException(Exception):
    """Raised by a Halt instruction"""

def parse_opcode(raw_value):
    "Return opcode plus modes for parameters"

    raw_modes, opcode = divmod(raw_value, 100)
    mode_set = []
    while raw_modes:
        raw_modes, mode = divmod(raw_modes, 10)
        mode_set.append(mode)
    return opcode, mode_set


class Intcode:
    '''Opcode 3 takes a single integer as input and saves it to the position
    given by its only parameter. For example, the instruction 3,50 would take
    an input value and store it at address 50.
    Opcode 4 outputs the value of its only
    parameter. For example, the instruction 4,50 would output the value at
    address 50.

    Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
    the instruction pointer to the value from the second parameter. Otherwise,
    it does nothing.
    Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
    instruction pointer to the value from the second parameter. Otherwise, it
    does nothing.
    Opcode 7 is less than: if the first parameter is less than the second
    parameter, it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0.
    Opcode 8 is equals: if the first parameter is equal to the second
    parameter, it stores 1 in the position given by the third parameter.
    Otherwise, it stores 0.

    '''
    instance_count = 0

    def __init__(self, data, input_source=None):
        self.data = data[:]
        self._original_data = self.data[:]
        self.program_counter = 0
        self.output_buffer = IOBuffer()
        self.input_source = IOBuffer()
        self.advance_counter = True
        self.halted = False
        self.index = Intcode.instance_count
        Intcode.instance_count += 1

    def get_parameter(self, offset=1):
        '''given the rather confusing terminology of the instructions,
        by "parameter" I mean the tuple (parameter, modes)
        '''
        location = self.program_counter + offset
        return self.data[location]

    def chain(self, follower):
        '''Connect this machine's output to _follower_'s input'''
        follower.follow(self)

    def follow(self, leader):
        '''Set up input function for chaining'''
        self.input_source = leader.output_buffer


    def current_parameters(self, parameter_count):
        return [self.get_parameter(offset) for offset in range(1, parameter_count + 1)]


    def resolve_parameter(self, parameter):
        param_val, mode = parameter
        if mode == INDIRECT_MODE:
            final_value = param_val
        else:
            final_value = self.data[param_val]
        return final_value

    def resolve_parameters(self, parameter_set):
        return [self.resolve_parameter(parameter) for parameter in parameter_set]

    def halt(self, *args):
        raise HaltException

    def add(self, params):
        x, y, destination = params
        self.write_to_addr(destination, (self.resolve_parameter(x) +
                                         self.resolve_parameter(y)))

    def multiply(self, params):
        x, y, destination = params
        self.write_to_addr(destination, (self.resolve_parameter(x) *
                                         self.resolve_parameter(y)))

    def write_to_addr(self, addr, value):
        if len(addr) > 1:
            addr = addr[0]  # allows us to pass full parameters
        try:
            self.data[addr] = value
        except IndexError:
            pad = addr - len(self.data) + 1
            self.data.extend( [0] * pad)
            self.data[addr] = value

    def advance_program_counter(self, advance):
        self.program_counter += advance

    def store(self, params):
        address = params[0][0]
        input_val = None
        # self.data[address] = int(self.input_func())
        if self.input_source is not None:
            try:
                input_val = next (self.input_source)
            except:
                self.advance_counter = False
        else:
            input_val = int(input("Enter some input: "))
        if input_val is not None:
            self.data[address] = input_val


    def output(self, params):
        '''Expects a single parameter, which is always read in position mode'''
        value = self.resolve_parameter(params[0])
        self.output_buffer.append(value)

    def jump_if_true(self, params):
        '''Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets
        the instruction pointer to the value from the second parameter. Otherwise,
        it does nothing.'''
        test,  pointer = [self.resolve_parameter(p) for p in params]
        if test:
            self.program_counter = pointer
            self.advance_counter = False

    def jump_if_false(self, params):

        '''Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise, it
        does nothing.'''
        test, pointer = [self.resolve_parameter(p) for p in params]
        if not test:
            self.program_counter = pointer
            self.advance_counter = False

    def less_than(self, params):

        '''Opcode 7 is less than: if the first parameter is less than the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.'''

        a, b, _ = [self.resolve_parameter(p) for p in params]
        destination = params[2][0]
        result = int(a<b)
        self.data[destination] = result

    def equals(self, params):

        '''Opcode 8 is equals: if the first parameter is equal to the second
        parameter, it stores 1 in the position given by the third parameter.
        Otherwise, it stores 0.'''

        a, b, _ = [self.resolve_parameter(p) for p in params]
        destination = params[2][0]
        result = int(a==b)
        self.data[destination] = result

    def next_instruction(self):
        raw_opcode = self.data[self.program_counter]
        instr_index, parameter_modes = parse_opcode(raw_opcode)
        instruction = self.intcode_func[instr_index]
        p_count = self.parameter_count[instr_index]
        missing_modes = p_count - len(parameter_modes)
        parameter_modes.extend(missing_modes * [0])
        return instruction, p_count, parameter_modes

    intcode_func = {
        99: halt,
        1: add,
        2: multiply,
        3: store,
        4: output,
        5: jump_if_true,
        6: jump_if_false,
        7: less_than,
        8: equals,
        }

    parameter_count = {
        99: 0,
        1: 3,
        2: 3,
        3: 1,
        4: 1,
        5: 2,
        6: 2,
        7: 3,
        8: 3,
    }

    def reset(self):
        self.data = self._original_data[:]
        self.output_buffer = []
        self.program_counter = 0


    def step(self, debug=False):
        instruction, param_count, parameter_modes = self.next_instruction()
        raw_parameters = self.current_parameters(param_count)
        parameters = list(zip(raw_parameters, parameter_modes))
        if debug:
            start, end = self.program_counter, self.program_counter + param_count + 1
            current_region = self.data[start:end]

            print(f"""instruction={instruction.__name__} | """
                  f"""{self.program_counter=} | {current_region=}""")
            inp = input()
            if inp == "b":
                breakpoint()

        instruction(self, parameters)
        if not self.advance_counter:
            self.advance_counter = True
        else:
            self.advance_program_counter(param_count + 1)

    def run(self, debug=False):
        self.reset()
        if debug:
            print(f"{self.data=}")

        while True:
            try:
                self.step(debug=debug)
            except HaltException:
                self.print_output_buffer()
                self.halted = True
                return

    def run_single_step(self):
        try:
            self.step()
        except HaltException:
            self.halted = True
            return

    def print_output_buffer(self):
        if self.output_buffer:
            print("Output: ")
            print("\n".join(map(str, self.output_buffer)))

    def display_data(self):
        pass # reconsider this
        # ix = 0;
        # while ix < len(self.data):
        #     pcount = self.parameter_count[self.data[ix]]
        #     print([self.data[ix: ix+pcount]])
        #     ix += pcount + 1

    def status(self):
        pc = self.program_counter
        print(f"{self=} {self.program_counter=} {self.halted=} {self.data[pc:pc+4]=}")

    def diff_memory(self):
        print("\n".join(map(str, [(ix, original, modified) for (ix, (original, modified)) in
                                 enumerate(zip(self._original_data, self.data))
                                 if original != modified])))

    def message(self, msg):
        self.input_source.message(msg)

    def __repr__(self):
        return f"IntCode instance {self.index}"

class IOBuffer(UserList):
    def __next__(self):
        if self:
            return self.pop(0)
        else:
            raise EmptyQueue

    def message(self, value):
        self.append(value)
