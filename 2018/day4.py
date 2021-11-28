import re
from collections import defaultdict
from datetime import datetime

def read_input(filename):
    with open(filename) as f:
        return f.readlines()

def parse_input(lines):
    lines = sorted(lines)
    lines = map(lambda l:l.strip(), lines)
    pat = re.compile("\[(\d+)-(\d+)-(\d+) (\d+):(\d+)] (.+)")
    guards = defaultdict(list)
    for line in lines:
        year, month, day, hour, minute, event = pat.match(line).groups()
        if "Guard" in event:
            guard_id = id_from_event(event)
            shift = Shift(guard_id)
        else:
            shift.add_event(year, month, day, hour, minute, event)


class Shift:
    shifts = defaultdict(list)
    
    def __init__(self, guard_id):
        self.guard_id = int(guard_id)
        self.events = []
        self.shifts[guard_id].append(self)

    def add_event(self, year, month, day, hour, minute, event):
        timestamp = datetime(int(year), int(month), int(day), int(hour), int(minute))
        self.events.append((timestamp, event))

def id_from_event(event):
    pat = re.compile("Guard #(\d+)")
    return pat.match(event).groups()[0]
                     
def solve(shifts):
    max_nap = 0
    for guard, guard_shifts in shifts.items():
        for (total_nap, nap_times) in tally_nap_times(guard_shifts).items():
            if total_nap > max_nap:
                max_nap = total_nap
                winning_nap_times = nap_times
                winning_guard = guard
    return winning_nap_times, winning_guard

def tally_nap_times(guard_shifts):
    nap_times = defaultdict(int)
    for shift in guard_shifts:
        for e1, e2 in paired_events(shift):
            for i in range(e1[0].minute,e2[0].minute):
                nap_times[i] += 1
    return nap_times

def paired_events(shift):
    return ((shift.events[2*i], shift.events[2*i+1]) for i in range(len(shift.events)/2))

        


lines = read_input("day4_input.txt")        
parse_input(lines)
