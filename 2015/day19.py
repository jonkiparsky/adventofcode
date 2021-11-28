from collections import defaultdict

def read_input(filename="day19.txt", part2=False):
    transformations = defaultdict(list)
    f = open (filename)
    for line in f:
        result = parse_line(line)
        if len(result) == 1:
            return (transformations, result[0])
        if len(result) == 0:
               continue
        else:
            input, output = result
            if part2:
                transformations[output].append(input)
            else:
                transformations[input].append(output)
    


def parse_line(line):
    match line.split():
        case [input, "=>", output]:
            return input, output
        case [molecule]:
            return molecule,
        case []:
            return []


transformations, molecule = read_input()
transformations2, molecule = read_input(part2=True)
transformations2 = [(key,  val[0]) for key, val in transformations2.items()]

def solution1(transformations, molecule):
    next_molecules = set()
    for element, replacements in transformations.items():
        next_molecules.update(transform_mol(molecule, element, replacements))

    return next_molecules

def transform_mol(molecule, element, replacements):
    match replacements:
        case []:
            return []
        case [first, *rest]:
            return transform_mol(molecule, element, first).union(
                transform_mol(molecule, element, rest))
        case replacement:
            return replace_each(molecule, element, replacement)

def replace_each(molecule, element, replacement):

    accumulator = set()
    ix = molecule.find(element)
    while ix > -1:
        prefix, tail = molecule[:ix], molecule[ix:]
        accumulator.add(prefix + tail.replace(element, replacement, 1))
        ix = tail[len(element):].find(element)
        if ix > -1:
            ix += ( len(prefix) + len(element))
    return accumulator

def partitions(molecule, transformations, accumulator=None):
    accumulator = accumulator or None

    if not molecule:
        return accumulator
    if not transformations:
        return accumulator


    
