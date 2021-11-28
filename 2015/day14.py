'''
--- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

Part 2
------
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old
scoring system.

Instead, at the end of each second, he awards one point to the reindeer
currently in the lead. (If there are multiple reindeer tied for the lead, they
each get one point.) He keeps the traditional 2503 second time limit, of course,
as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the
lead and gets one point. He stays in the lead until several seconds into Comet's
second burst: after the 140th second, Comet pulls into the lead and gets his
first point. Of course, since Dancer had been in the lead for the 139 seconds
before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet,
our old champion, only has 312. So, with the new scoring system, Dancer would
win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after
exactly 2503 seconds, how many points does the winning reindeer have?
'''
import re
pat = re.compile("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.")

RACE_TIME = 2503

def read_input():
    f = open("day14.txt")
    return r.readlines()



class Reindeer:
    def __init__(self, *args):
        self.name = args[0]
        self.rate, self.travel, self.rest = map(int, args[1:])
        self.score = 0
        self.dist = 0
        self.cycle_time = self.travel + self.rest

    def numbers(self):
        return self.rate, self.travel, self.rest

    def advance(self, t):
        q, r = divmod(t, self.cycle_time)
        self.dist = (q * self.travel * self.rate +
                     self.rate * min(r, self.travel))

    def __repr__(self):
        return "<Reindeer> {} score: {} dist: {} ({}, {}, {})".format(self.name,
                                                                      self.score,
                                                                      self.dist,
                                                                      self.rate,
                                                                      self.travel,
                                                                      self.rest)

def part_2(lines, race_time=RACE_TIME):
    herd = []

    for line in lines:
        data = pat.match(line).groups()
        herd.append (Reindeer(*data))

    for t in range(1, race_time):
        for deer in herd:
            deer.advance(t)
        herd = sorted(herd, key=lambda d:d.dist, reverse=True)
        
        for deer in herd:
            if deer.dist == herd[0].dist:
                deer.score += 1
    return herd
#    return max([d for d in herd], key=lambda d: d.score), herd

def part_1(lines, race_time=RACE_TIME):
    best = 0
    best_name = ""
    for line in lines:
        data =  pat.match(line).groups()
        numbers = map(int, data[1:])
        this_dist = dist(*numbers)
        if this_dist > best:
            best = this_dist
            best_name = data[0]
    print "{}: {}".format(best_name, best)

def dist(rate, travel_time, rest_time):
    cycle_time = travel_time + rest_time
    cycle_distance = travel_time * rate
    num_cycles, remainder = divmod(race_time, cycle_time)
    return cycle_distance * num_cycles + min(remainder, travel_time) * rate
    
