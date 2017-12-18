# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:19:14 2017

@author: Paul
"""

import random
import operator
import matplotlib.pyplot
import agentframework

def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 100
agents = []


#a = agentframework.Agent()

#print(a.x)
#print(a.y, a.x)
#a.move()
#print(a.y, a.x)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()


matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1) 