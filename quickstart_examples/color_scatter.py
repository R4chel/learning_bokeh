import numpy as np
from bokeh.plotting import figure, output_file, show

# prep data
N = 10000
x = np.random.random(size=N) * 255
y = np.random.random(size=N) * 255
z = np.random.random(size=N) * 255
radii = np.random.random(size=N) * 2
colors = ["#%02x%02x%02x" % (r, g, b) for r, g, b in zip(np.floor(x), np.floor(y), np.floor(z))]

# output to HTML
output_file("color_scatter.html", title="Color Scatter Example", mode="cdn")

TOOLS = "resize,crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

# create new plot
p = figure(tools=TOOLS, x_range=(0,255), y_range=(0,255))

p.circle(x,y,radius=radii,fill_color=colors,fill_alpha=0.6,line_color=None)

show(p)
