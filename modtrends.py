import sys
from datetime import datetime
from matplotlib.dates import DateFormatter, epoch2num
import matplotlib.pyplot as plt
import numpy as np

mod_names = []
master_times = []

for i in range(1,len(sys.argv)):
	filename = sys.argv[i]
	f = open(filename, 'r')
	months = []
	times = {}
	for line in f.readlines():
		line_entries = line.rstrip('\n').split(';')
		time = line_entries[1]
		date = str(datetime.fromtimestamp(float(time)))
		year_month_day = date.split(" ")[0]
		year_month = "-".join(date.split("-")[:2])
		year_month = year_month.split("-")
		time = datetime(int(year_month[0]), int(year_month[1]),1).timestamp()
		if time not in times.keys():
			times[time] = 1
		else:
			times[time] += 1

	f.close()
	master_times.append(times)

	mod_name = filename.replace('.first', '')
	# combined py/ipynb file
	if "_combined" in mod_name:
		mod_name = mod_name.replace('_combined', '')

	# full file path
	if "/" in mod_name:
		mod_name = mod_name.split("/")[-1]

	# keras app module
	if "keras.applications" in mod_name:
		mod_name = mod_name.replace('keras.applications.', '').capitalize()

	mod_names.append(mod_name)
	

# set up the starting x date boundary for the graph
x_min_times = []

for i in range(len(master_times)):
	x_min_times.append(min(master_times[i].keys()))

x_min = epoch2num(max(x_min_times))

# plot each set of times on the line graph
fig, ax = plt.subplots()
for i in range(len(master_times)):
	freq = []
	sorted_times = sorted(master_times[i].items(), key = lambda kv: kv[0])

	for key, val in sorted_times:
		freq.append(val)
	
	raw = np.array([int(t) for t in sorted(master_times[i].keys())])
	dates = epoch2num(raw)

	line, = ax.plot_date(dates, freq, ls = '-', markevery=[0,-1], label = mod_names[i])


# format x axis date ticks
date_fmt = '%m/%y'
date_formatter = DateFormatter(date_fmt)
ax.xaxis.set_major_formatter(date_formatter)
fig.autofmt_xdate()

ax.legend(loc='best')
ax.set_xlim([x_min, datetime(2019,4,20)])
ax.grid(ls = 'dotted')

# set x,y labels
plt.xlabel('Dates (mm/yy)', fontsize=16)
plt.ylabel('Number of Repos', fontsize=16)

# save the graph as a .png picture
save_file = mod_names[0]
for i in range(1,len(mod_names)):
	save_file += "-vs-" + mod_names[i]
save_file += ".png"

plt.savefig(save_file, bbox_inches='tight')

