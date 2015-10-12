import numpy as np
from bokeh.plotting import *

# prep data
N = 100
x = np.linspace(0, 4*np.pi, N)
y0 = np.sin(x)
y1 = np.cos(x)
y2 = np.sin(x) + np.cos(x)

# output file
output_file("linked_panning.html")

# create new plot
s0 = figure(width=250, plot_height=250)
s0.circle(x, y0, size=10, color="navy", alpha=0.5)

s1 = figure(width=250, height=250, x_range=s0.x_range, y_range=s0.y_range)
s1.circle(x, y1, size=10, color="firebrick", alpha=0.5)

s2 = figure(width=250, height=250, x_range=s0.x_range, y_range=s0.y_range)
s2.circle(x, y2, size=10, color="olive", alpha=0.5)

# put subplots on grid plot
p = gridplot([[s0,s1,s2]], toolbar_location=None)

show(p)
