PROBLEM_BASENAME = "day11"
default_data_filename = "{}.txt".format(PROBLEM_BASENAME)


FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"

def parse_input(filename=None):
    fname = filename or default_data_filename
    f = open(fname)
    data = f.read().split("\n")
    
    return [row for row in data if row]



class LobbyLife:
    def __init__(self, data):
        self.grid = data
        self.grid_width = len(self.grid[0])
        self.grid_height = len(self.grid)
        self.stable = False
        self.generations = 0
        if any([len(row) != self.grid_width for row in self.grid]):
            print("Bad row length")

            

    def transition_floor(self, i, j):
        return FLOOR

    
    def transition_empty(self, i, j):
        if self.count_adjacent(i, j, OCCUPIED) == 0:
            return OCCUPIED
        else:
            return EMPTY

    def transition_occupied(self, i, j):
        if self.count_adjacent(i, j, OCCUPIED) >= 4:
            return EMPTY
        else:
            return OCCUPIED
    
    def transition(self):
        new_grid = []
        self.stable = True
        for i in range(self.grid_height):
            new_row = self.transition_row(i)
            new_grid.append(new_row)
        if any([new != old for new, old in zip(new_grid, self.grid)]):
            self.stable = False
        self.generations += 1
        self.grid = new_grid

    def transition_row(self, i):
        new_row = "".join([self.transition_cell(i, j) for j in range(self.grid_width)])
        return new_row

    def transition_cell(self, i, j):
        initial_state = self.grid[i][j]
        if initial_state == EMPTY:
            return self.transition_empty(i, j)
        elif initial_state == OCCUPIED:
            return self.transition_occupied(i, j)
        elif initial_state == FLOOR:
            return self.transition_floor(i, j)
        else:
            raise Exception
            
    def count_adjacent(self, i, j, target):
        count = 0
        if i > 0:
            prev_row = self.grid[i-1]
            count += sum([prev_row[j+dx]==target for dx in self.adj_cols(j)])
        current_row = self.grid[i]
        if j > 0:
            count += current_row[j-1] == target
        if j < len(current_row)-1:
            count += current_row[j+1] == target
        if i < len(self.grid) - 1:
            next_row = self.grid[i+1]
            count += sum([next_row[j+dx]==target for dx in self.adj_cols(j)])
            
        return count

    def adj_cols(self, col):
        cols = [0]
        if col > 0:
            cols.insert(0, -1)
        if col < self.grid_width - 1:
            cols.append(1)
        return cols

    def count_occupied(self):
        return sum([row.count(OCCUPIED) for row in self.grid])

    def solve1(self):
        while not self.stable:
            self.transition()
        print(self.count_occupied())
        
    def __str__(self):
        return "\n".join(self.grid)

    def __repr__(self):
        return str(self)

sample_rows = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".split("\n")

sample_lobby = LobbyLife(sample_rows)

