import re


marker_re = re.compile(r"\((\d+)[Xx](\d+)")

def read_input(filename="day9.txt"):
    return open(filename).read().strip()

def process(data):
    output = []
    rest = data
    while rest:
        next_chunk, rest = consume(rest)
        output.append(next_chunk)
    return "".join(output)


def consume_text(data):
    return partition(data, "(")

def partition(original, substr):
    if substr not in original:
        return original, ""
    split_point = original.find(substr)
    return original[:split_point], original[split_point:]

def consume_marker(data):
    marker, rest = data.split(")", maxsplit=1)
    slice_width, multiplier = map(int, marker_re.match(marker).groups())
    return apply_marker(rest, slice_width, multiplier)

def apply_marker(data, slice_width, multiplier):
    slice, rest = data[:slice_width], data[slice_width:]
    return (multiplier * slice), rest

def consume(data, marker_fn=consume_marker):
    if data[0] == "(":
        return marker_fn(data)
    else:
        return consume_text(data)


def consume_marker2(data):
    marker, rest = data.split(")", maxsplit=1)
    slice_width, multiplier = map(int, marker_re.match(marker).groups())
    slice, rest = rest[:slice_width], rest[slice_width:]
    return "", "".join([slice * multiplier, rest])

def process2(data):
    ''' no good - passes the examples, but takes too long'''
    output_len = 0
    rest = data
    cycles = 0
    while rest:
        cycles += 1
        if cycles % 100000 == 0:
            print ("{}--{}--{}".format(cycles, output_len, len(rest)))
        next_chunk, rest = consume(rest, marker_fn = consume_marker2)
        output_len += len(next_chunk)
    return output_len



            
