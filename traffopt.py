import random

class Lane():
    def __init__(self):
        self.queuelen = 0
        self.waittime = 0
        self.carspassed = 0
        self.carsarrived = 0
        self.timesgreen = 0

lanes = {
    "North" : Lane(),
    "South" : Lane(),
    "West" : Lane(),
    "East" : Lane()
}

arrivalprob = {
    "North" : 0.3,
    "South" : 0.3,
    "West" : 0.12,
    "East" : 0.12,
}

simtime = 500
roadcap = 3
current = "North"

bail = 120

greentime = 10
timer = 0

history = {
    "North" : [],
    "South" : [],
    "West" : [],
    "East" : []
}

def cho_lane(lanes):

    bailed_lanes = []

    for name, lane in lanes.items():
        if lane.queuelen > 0 and lane.timesgreen >= bail:
            bailed_lanes.append(name)

    def get_wait(name):
        return lanes[name].timesgreen

    def get_que(name):
        return lanes[name].queuelen

    if bailed_lanes:
        return max(bailed_lanes, key=get_wait)

    return max(lanes.keys(), key = get_que)
    
for second in range (simtime):
    
    if timer == 0:
        current = cho_lane(lanes)

    for name, lane in lanes.items():
        if random.random() < arrivalprob[name]:
            lane.queuelen += 1
            lane.carsarrived += 1

    currlane = lanes[current]

    carsleav = min(currlane.queuelen, roadcap)
    currlane.queuelen -= carsleav
    currlane.carspassed += carsleav

    for name, lane in lanes.items():
        lane.waittime += lane.queuelen

        if name == current:
            lane.timesgreen = 0
        elif lane.queuelen > 0:
            lane.timesgreen += 1
        else:
            lane.timesgreen = 0


    for name in lanes:
        history[name].append(lanes[name].queuelen)

    timer += 1
    if timer >= greentime:
        timer = 0

totalwait = 0
totalpassed = 0

for name, lane in lanes.items():
    avg_wait = lane.waittime / max(1, lane.carsarrived)

    print(name, "Cars passed:", lane.carspassed)
    print(name, "Total wait:", lane.waittime)
    print(name, "Avg wait per car:", avg_wait)

from graphing import plot
plot(history)