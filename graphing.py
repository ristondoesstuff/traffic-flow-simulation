import matplotlib.pyplot as graph

def plot(history):

    graph.title  ("Traffic Queues over time")
    graph.xlabel ("Time(seconds)")
    graph.ylabel ("Traffic Queue")
    
    for name, data in history.items():
        graph.plot (data, label = name)
    
    graph.legend()
    graph.grid(True)
    graph.show()