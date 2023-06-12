from intcode import Intcode

class IntCodeCluster:
    """Manages a collection of IntCode instances to run
    concurrently,  together in sequence s/t the output from
    one is fed to the next
    """
    def __init__(self, programs, chained=True):
        self.machines = [Intcode(program) for program in programs]
        if chained:
            for (leader, follower) in zip(self.machines, self.machines[1:]):
                leader.chain(follower)
            self.machines[-1].chain(self.machines[0])

    def __getitem__(self, ix):
        return self.machines[ix]

    def run(self, verbose=0):
        while True:
            any_running = False
            for ic in self.machines:
                if verbose:
                    print (ic.status())
                if not ic.halted:
                    any_running = True
                    ic.run_single_step()
            if not any_running:
                break





sample_programs = [

    [1,0,0,0,99],          # becomes 2,0,0,0,99 (1 + 1 = 2).
    [2,3,0,3,99],          # becomes 2,3,0,6,99 (3 * 2 = 6).
    [2,4,4,5,99],          # 0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
    [1,1,1,4,99,5,6,0,99]  # becomes 30,1,1,4,2,5,6,0,99.
]

sample_add_1 = [3, 0, 1001, 1, 1, 0, 4, 0, 99]  # takes input and adds 1 to it
