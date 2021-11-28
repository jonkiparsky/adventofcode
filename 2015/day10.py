input = "1113222113"
def see_and_say(input):
    acc = ""
    next_char = input[0]
    while input:
        next_char = input[0]
        next_group = re.match("({}*)".format(next_char), input).groups()[0]
        l = len(next_group)
        acc += str(l)+next_char        
        input = input[l:]
    return acc
    
    
def iterated_see_and_say(input, times=40):
    for _ in range(times):
        input = see_and_say(input)
    return input
        
