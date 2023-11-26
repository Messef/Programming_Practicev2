import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data = pd.read_csv('data.csv')
print(data.head(5))

axisFont = {'family': 'serif',      # Define font family dictionary for axes labels and tick marks
        'color':  'black',
        'weight': 'normal',
        'size': 12,
        }

titleFont = {'family': 'serif',     # Define font family dictionary for plot titles
        'color':  'black',
        'weight': 'bold',
        'size': 16,
        }
# Set size for plot figure (make sure this is done before plotting the data)
plt.figure(figsize=(10, 6))         # (10, 6) -> width = 10", height = 6"

# Plot Data
# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, 
#                           alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, 
#                           data=None, **kwargs)

# More info on MatPlotLib scatter plots:  https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.scatter.html

# Color picker:  https://www.w3schools.com/colors/colors_picker.asp
plt.scatter(data['Times'], data['Positive Control Group'], s = 12, marker = 'o', c = '#0052cc', label = 'PC')  
plt.scatter(data['Times'], data['1 Microamp Group'], s = 12, marker = 'o', c = '#0052cc', label = '1M')  
plt.scatter(data['Times'], data['2 Microamp Group'], s = 12, marker = '^', c = '#29a329', label = '2M')
plt.scatter(data['Times'], data['4 Microamp Group'], s = 12, marker = 's', c = '#ff8000', label = '4M')

# Set Plot Title (pad = padding between title and graph)
plt.title('No Music, Music @ 80 BPM and Music @ 116 BPM vs. Particpant', fontdict = titleFont, pad = 20)

# Set labels for axes
plt.xlabel('Time(Days)', fontdict = axisFont)
plt.ylabel('S. Pombe left in the petri dish', fontdict = axisFont)

# Set tick marks and grid lines for axes
#arbitrary code based off of a template - Data was NOT collected
plt.xticks(np.arange(0, 42, step = 4)) 
plt.yticks(np.arange(0, 35, step = 5))
plt.grid(b = 'True', which = 'major', axis = 'both', linestyle = '-')


# Set legend location (0 = best location as determined by MatPlotLib)
plt.legend(loc = 0)

# Change background color of plot 
plt.axes().set_facecolor('whitesmoke')

plt.show()