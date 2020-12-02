import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

dataset = 'datasets/Religion_of_inmates.csv'

religion_data = dict()

with open(dataset, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in data:
		if row[0] == "KARNATAKA":
			year = row[1]
			
			if ' - ' in row[2]:
				religion = row[2].split()[2]
				count = int(row[17])
				if year not in religion_data:
					religion_data[year] = dict()
				if religion not in religion_data[year]:
					religion_data[year][religion] = count

### print data
# print(religion_data)

labels = []
r_data = dict()
for y in sorted(religion_data):
	labels.append(str(y))
	total = 0
	for r in religion_data[y]:
		total += religion_data[y][r]

	for r in religion_data[y]:
		if r not in r_data:
			r_data[r] = []
		r_data[r].append(religion_data[y][r]*100./total)

width = 0.35       # the width of the bars: can also be len(x) sequence

fig, ax = plt.subplots(figsize=(16,9))

b = [0]*len(labels)
for r in r_data:
	# print(r_data[r])
	ax.bar(labels, r_data[r], width, bottom=b, label=r)

	for i in range(len(r_data[r])):
		b[i] += r_data[r][i]

ax.yaxis.grid()
ax.set_yticks(np.arange(0,101,10))
ax.set_ylabel('Percentage')
ax.set_xlabel('Year')
ax.set_title('Convict Religion Profile in percentage across years : Karnaraka')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
fig.tight_layout()
# plt.show()
plt.savefig("bar_plot.png")
plt.close()
