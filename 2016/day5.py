from itertools import count
import re
seed = "cxdnnyjw"

hashes = (md5("{}{}".format(seed, i).encode()).hexdigest() for i in count())

pat = re.compile(r"^00000([0-7])(.)")
def search():
    while True:
        hash = next(hashes)
#        if hash.startswith("00000"):
        m = pat.match(hash)
        if m:
            yield m.groups()

results = ["#"] * 8

s = search()


def do_it():
    counter = 0    
    while "#" in results:
        pos, val = next(s)
        if results[int(pos)] == "#":
            results[int(pos)] = val
        if counter % 10000 == 0:
            print (counter, results)
        counter += 1
