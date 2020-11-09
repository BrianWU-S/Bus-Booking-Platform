from galogic import *
import matplotlib.pyplot as plt
import progressbar
import numpy as np
pbar = progressbar.ProgressBar()

# Add Dustbins
dataSet = np.loadtxt("hk_50.txt",delimiter='\t')
for i in range(numNodes):
    RouteManager.addDustbin(Dustbin(dataSet[i][0],dataSet[i][1],i))
    
random.seed(seedValue)
yaxis = [] # Fittest value (distance)
xaxis = [] # Generation count

pop = Population(populationSize, True)
globalRoute = pop.getFittest()
print ('Initial minimum distance: ' + str(globalRoute.getDistance()))

# Start evolving
for i in pbar(range(numGenerations)):
    pop = GA.evolvePopulation(pop)
    localRoute = pop.getFittest()
    if globalRoute.getDistance() > localRoute.getDistance():
        globalRoute = localRoute
    yaxis.append(localRoute.getDistance())
    xaxis.append(i)

print ('Global minimum distance: ' + str(globalRoute.getDistance()))
print ('Final Route: \n' + globalRoute.toString())

fig = plt.figure()

plt.plot(xaxis, yaxis, 'r-')
plt.show()
