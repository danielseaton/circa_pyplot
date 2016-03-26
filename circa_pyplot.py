from matplotlib.patches import Rectangle
from matplotlib.pyplot import *

#TODO - allow input of linestyles
#TODO - create function to work on single instance of axes

fig = figure()
ax = fig.add_subplot(111)

#Required inputs
timepoints = range(0,25,4)
data = [[1.1,1.2,1.3,1.4,1.5,1.4,1.1],
        [3.1,0.2,0.15,1.1,1.1,1.5,3.1]]

colors = ['w','grey','k']
transition_times = [0,8,16,24]

#Default values
errors = None
linestyle = 's-'
xmin = timepoints[0]
xmax = timepoints[-1]

#Optional inputs
errors = [[0.1 for _ in y] for y in data]
#linestyle = 's-k'
ymin = 0
ymax = None
legend = None

#number of timeseries
nTS = len(data)


for timeseries,timeseries_errors in zip(data,errors):
    if errors:
        errorbar(timepoints,timeseries,yerr=timeseries_errors,fmt=linestyle)
    else:
        plot(timepoints,timeseries,linestyle)


if ymax:
    #ymax is specified by the user
    pass
else:
    #work out a good ymax value
    ymax_data = max([max(x) for x in [y.get_ydata() for y in ax.get_lines()]])
    ymax = ymax_data*1.1

thickness = 0.05 #as fraction of ymax
height = thickness*ymax

for time1,time2,color in zip(transition_times[:-1],transition_times[1:],colors):
    ax.add_patch(Rectangle((time1,ymin-height),time2-time1,height,angle=0.0,facecolor=color))


xlim([xmin,xmax])
ylim([ymin-height,ymax])