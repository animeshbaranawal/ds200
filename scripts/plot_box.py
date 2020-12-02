import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

dataset = 'datasets/August_MySpeed-2020.csv'

speed_data_upload = dict()
speed_data_download = dict()

with open(dataset, newline='') as csvfile:
	data = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in data:
		if row[5].lower() == "karnataka":
			serviceProvider = row[0]
			speed = float(row[3])
			if row[1].lower() == "4g":
				if row[2].lower() == "upload":
					if serviceProvider not in speed_data_upload:
						speed_data_upload[serviceProvider] = []
					speed_data_upload[serviceProvider].append(speed)
				elif row[2].lower() == "download":
					if serviceProvider not in speed_data_download:
						speed_data_download[serviceProvider] = []
					speed_data_download[serviceProvider].append(speed)

### print data
# print(speed_data_download)
# print(speed_data_upload)

all_data_download = []
all_data_upload = []
labels = []
for s in sorted(speed_data_download):
	labels.append(s.lower())
	all_data_download.append(speed_data_download[s])
	all_data_upload.append(speed_data_upload[s])

# for i in range(len(all_data_upload)):
# 	print(labels[i], "Upload", max(all_data_upload[i]), min(all_data_upload[i]), sum(all_data_upload[i])/len(all_data_upload[i]), "Download", max(all_data_download[i]), min(all_data_download[i]), sum(all_data_download[i])/len(all_data_download[i]))

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16,9))

bplot1 = axes[0].boxplot(all_data_download,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color

bplot2 = axes[1].boxplot(all_data_upload,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color

# fill with colors
colors = ['pink', 'lightblue', 'lightgreen', 'yellow', 'orange']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

for ax in axes:
    ax.yaxis.grid(True)
    ax.set_xticks([y+1 for y in range(len(all_data_download))])
    ax.set_xlabel('Service Provider')

axes[0].set_ylabel('Download Speed (in Kbps)')
axes[1].set_ylabel('Upload Speed (in Kbps)')

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_data_download))],
         xticklabels=labels)
fig.suptitle('4G Mobile speeds in Karnataka (Aug 2020)')
fig.tight_layout()
# plt.show()
plt.savefig("box_plot.png")
plt.close()
