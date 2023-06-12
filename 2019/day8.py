def read_data(filename="day8.txt"):
    f = open(filename)
    return read_laters(f)

def read_chunks(f, chunk_size=25):
    next_chunk = f.read(chunk_size)
    while len(next_chunk) == chunk_size:
        yield next_chunk
        next_chunk = f.read(chunk_size)


def read_layers(f, row_count=6):
    chunks = list(read_chunks(f))
    return [chunks[i:i+row_count] for i in range(0, len(chunks), row_count)]

def count_chars(layer, chr):
    return sum([row.count(chr) for row in layer])

def check(layer):
    zeros, ones, twos = [count_chars(layer, chr) for chr in ("0", "1", "2")]
    return (zeros, ones*twos)

def validate_layers(layers):
    the_layer = min([check(layer) for layer in layers])
    return the_layer[1]

def render_cell(chars):
    return "".join(chars).replace("2", "")[0]

def render_row(row):
    stacked_chars = zip(*row)
    return "".join([render_cell(chars) for chars in stacked_chars])

def render_image(layers):
    # get the layers of row 0, row 1, row 2, etc
    stacked_rows = [[layer[i] for layer in layers] for i in range(6)]
    return "\n".join([render_row(row) for row in stacked_rows])
