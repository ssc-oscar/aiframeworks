import sys
from datetime import datetime
from matplotlib.dates import (DateFormatter, epoch2num)
import matplotlib.pyplot as plt
import numpy as np

file1 = sys.argv[1]
file2 = sys.argv[2]
path1 = "/data/play/ipythruMaps/" + file1
path2 = "/data/play/ipythruMaps/" + file2
f1 = open(path1, 'r')
f2 = open(path2, 'r')
months1 = []
months2 = []
times1 = {}
times2 = {}
for line in f1.readlines():
	l = line.rstrip('\n').split(';')
	time = l[1]
	date = str(datetime.fromtimestamp(float(time)))
	year_month_day = date.split(" ")[0]
	year_month = "-".join(date.split("-")[:2])
	year_month = year_month.split("-")
	time = datetime(int(year_month[0]), int(year_month[1]),1).timestamp()
	if time not in times1.keys():
		times1[time] = 1
	else:
		times1[time] += 1

for line in f2.readlines():
	l = line.rstrip('\n').split(';')
	time = l[1]
	date = str(datetime.fromtimestamp(float(time)))
	year_month_day = date.split(" ")[0]
	year_month = "-".join(date.split("-")[:])
	year_month = year_month.split("-")
	time = datetime(int(year_month[0]), int(year_month[1]), 1).timestamp()
	if time not in times2.keys():
		times2[time] = 1
	else:
		times2[time] += 1

f1.close()
f2.close()

freq1 = []
freq2 = []

sorted1 = sorted(times1.items(), key = lambda kv: kv[0])
sorted2 = sorted(times2.items(), key = lambda kv: kv[0])

for key, val in sorted1:
	freq1.append(val)

for key, val in sorted2:
	freq2.append(val)

x_min = epoch2num(min(min(times1.keys()), min(times2.keys())))
y_min = min(min(times1.values()), min(times2.values()))
y_max = max(max(times1.values()), max(times2.values())) + 5000

raw1 = np.array([int(t) for t in sorted(times1.keys())])
raw2 = np.array([int(t) for t in sorted(times2.keys())])

dates1 = epoch2num(raw1)
dates2 = epoch2num(raw2)

mod_name1 = file1.replace('.first', '').capitalize()
mod_name2 = file2.replace('.first', '').capitalize()

# plot the data with a legend reference
fig, ax = plt.subplots()
line1, = ax.plot_date(dates1, freq1, ls = '-', color='r', markevery=[0,-1], label = mod_name1)
line2, = ax.plot_date(dates2, freq2, ls = '-', color='b', markevery=[0,-1], label = mod_name2)
ax.legend(loc='best')

# format x axis date ticks
date_fmt = '%m/%y'
date_formatter = DateFormatter(date_fmt)
ax.xaxis.set_major_formatter(date_formatter)
fig.autofmt_xdate()
ax.set_xlim([datetime(2014,1,1), datetime(2019,6,6)])
ax.set_ylim(y_min, y_max)
ax.grid(ls = 'dotted')

# set x,y labels and title
plt.xlabel('Dates', fontsize=16)
plt.ylabel('# of Repos', fontsize=16)
title = mod_name1 + " vs. " + mod_name2 + " 1st Time Imports"
fig.suptitle(title, fontsize=18)

# save the graph as a .png picture
save_file = mod_name1 + 'Vs' + mod_name2 + '.png'
plt.savefig(save_file, bbox_inches='tight')

