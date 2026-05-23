import random

class Lane():
    def __init__(self):
        self.queuelen = 0
        self.waittime = 0
        self.carspassed = 0

lanes = {
    "North" : Lane(),
    "South" : Lane(),
    "West" : Lane(),
    "East" : Lane()
}

history = {
    "North" : [],
    "South" : [],
    "West" : [],
    "East" : []
}

arrivalprob = {
    "North" : 0.7,
    "South" : 0.7,
    "West" : 0.5,
    "East" : 0.5,
}

simtime = 500
roadcap = 3
current = "North"

for second in range (simtime):
    
    cycle = second % 120

    if cycle > 89:
        current = "East"
    elif cycle > 59:
        current = "West"
    elif cycle > 29:
        current = "South"
    else:
        current = "North"

    print("Second: ",second)
        
    for lanename, lane in lanes.items():

        if random.random() < arrivalprob[lanename]:
            lane.queuelen += 1
        
    currlane = lanes [current]

    carsleav = min(currlane.queuelen, roadcap)
    currlane.queuelen -= carsleav
    currlane.carspassed += carsleav

    print("Current Green Light:", current)
    print("Cars passed:", carsleav)

    for name in lanes:
        history[name].append(lanes[name].queuelen)

    for lanename, lane in lanes.items():
        print(lanename,"queue:", lane.queuelen)
        
    print()


totalpassed = 0

for name, lane in lanes.items():
    print(name, "Cars passed:", lane.carspassed)
    totalpassed += lane.carspassed

print("Total cars passed:", totalpassed)



from graphing import plot
plot(history)