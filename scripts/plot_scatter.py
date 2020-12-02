import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

datasetX = 'datasets/State-wise-SR_2001_2011.csv'
datasetY = 'datasets/Literacy_Rate-Ministry_of_Finance.csv'

stateData = dict()

with open(datasetX, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in data:
		if row[0] == "State":
			stateData[row[1]] = [float(row[3]), 0.]

with open(datasetY, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in data:
		if row[0] in stateData:
			stateData[row[0]][1] = float(row[7])

xdata = [] ## sex ratio
ydata = [] ## literacy rate
fig, ax = plt.subplots(figsize=(16,9))
ax.yaxis.grid()
ax.xaxis.grid()

### print data
for state in stateData:
	# print(state, stateData[state][0], stateData[state][1])
	if state != "Jammu & Kashmir": # incorrect data for literacy rate
		xdata.append(stateData[state][0])
		ydata.append(stateData[state][1])


ax.scatter(xdata, ydata)
ax.set_yticks(np.arange(60,105,5))
ax.set_xticks(np.arange(850,1150,50))
ax.set_ylabel('Literacy Rate')
ax.set_xlabel('Sex Ratio')
ax.set_title("Literacy Rate vs Sex Ratio across states in India (2011)")

ax.annotate("Kerala", xy=(stateData["Kerala"][0], stateData["Kerala"][1]), xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
fig.tight_layout()
# plt.show()
plt.savefig("scatter_plot.png")
plt.close()
