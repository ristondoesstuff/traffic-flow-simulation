# traffic-flow-simulation
This is my Python-based traffic flow simulation that compares fixed-cycle and adaptive traffic light control using queue simulation modeling and performance metrics such as wait time and congestion.

Overview

This project simulates traffic across four directions (North, South, East, West). Each lane tracks:

  Number of cars in the queue
  Total waiting time
  Number of cars that have passed

The simulation uses basic logic to represent how traffic builds up and clears over time.

How it works:
Each lane is represented as an object that stores its state. Cars are added on a probability factor and removed to simulate traffic flow, and statistics are updated continuously.

Technology Used:
Python

Possible Future Improvements:
  Poisson distribution for Vehicle Arrival Rates
  Machine Learning Integration
  Animated Simulation (GUI)

Created by Riston Castelino
