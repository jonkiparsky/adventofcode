from md5 import md5

key = "iwrupvqb%d"

val = 0
while True:
    input = key % val
    hash = md5(input)
    if hash.hexdigest().startswith("000000"):
        print val
        break
    val += 1
    if val % 10000 == 0:
        print "trying %d" % val
