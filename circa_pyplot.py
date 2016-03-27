from matplotlib.patches import Rectangle
from matplotlib.pyplot import *

##TODO - allow input of linestyles
#
#fig = figure()
#ax = fig.add_subplot(111)
#
##Required inputs
#timepoints = range(0,25,4)
#data = [[1.1,1.2,1.3,1.4,1.5,1.4,1.1],
#        [3.1,0.2,0.15,1.1,1.1,1.5,3.1]]
#colors = ['w','grey','k']
#transition_times = [0,8,16,24]
#errors = [[0.1 for _ in y] for y in data]
#
#for x in data:
#    plot(timepoints,x)

def circa_pyplot(transition_times,colors,ax=None,timepoints=None,data=None,errors=None,
                 xtick_locations=None,xlabel_text='',ylabel_text='',
                 ymin=0,ymax=None,linestyle='s-',fontsize=14):
    
    if not ax:
        #plot a new figure
        fig = figure()
        ax = fig.add_subplot(111)

    xmin = transition_times[0]
    xmax = transition_times[-1]
    
    if data:
        if errors:
            for timeseries,timeseries_errors in zip(data,errors):
                errorbar(timepoints,timeseries,yerr=timeseries_errors,fmt=linestyle)
        else:
            for timeseries in data:
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
    xlabel(xlabel_text,fontsize=fontsize)
    ylabel(ylabel_text,fontsize=fontsize)
    if xtick_locations:
        xticks(xtick_locations)
    tight_layout()

#circa_pyplot(transition_times,colors,timepoints=timepoints,data=data,ax=ax,
#             xlabel_text='Time (ZT h)',ylabel_text='Relative Expression',
#             xtick_locations=range(0,25,4))
#circa_pyplot(transition_times,colors,ax)