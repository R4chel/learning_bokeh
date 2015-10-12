import random
from bokeh.plotting import figure, output_file, show

x = range(20)
y = [random.randint((-1)*i,i) for i in x]

output_file("randomish_line.html", title="line plot example")

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

p.line(x,y, line_width=2)

show(p)
