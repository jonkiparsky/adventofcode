

PROBLEM_BASENAME = "day13"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    
    timestamp = int(data[0])
    departure_data = data[1].split(",")

    return timestamp, departure_data

def solve1(timestamp, departure_data):
    bus_ids = [int(id) for id in departure_data if id.isdigit()]
    departures = [(id, (timestamp - timestamp % id) + id - timestamp ) for id in bus_ids]
    best_id, best_wait_time = min(departures, key= lambda t:t[1])
    return best_id * best_wait_time
                    

def solve2(departure_data, debug=False):
    times_and_routes = [(int(id), ix) for (ix, id) in enumerate(departure_data) if id.isdigit()]
    generators = [departures_mod_offset(bus_id, offset) for bus_id, offset in times_and_routes]
    p_gens = [PeekableGenerator(gen) for gen in generators]
    while True:
        if len(set([p_gen.next_item for p_gen in p_gens])) == 0:
            return p_gens[0].peek()
        next_gen = min(p_gens, key=lambda p:p.next_item)
        next_gen.pop()
        
    


class PeekableGenerator:
    def __init__(self, generator):
        self.generator = generator
        self.next_item = next(generator)

    def __next__(self):
        self._next_item = self.next_item
        self.next_item = next(self.generator)
        return self._next_item

    def pop(self):
        self._next_item = self.next_item
        self.next_item = next(self.generator)
        return self._next_item

    def __repr__(self):
        return "<{}>".format(str(self.next_item))
    
def departures_mod_offset(bus_id, offset):
    
    n = bus_id - offset
    while True:
        n += bus_id
        yield n
