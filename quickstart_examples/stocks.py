import numpy as np

from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL

# prepare data
aapl = np.array(AAPL['adj_close'])
aapl_dates = np.array(AAPL['date'], dtype=np.datetime64)

window_size = 30
window = np.ones(window_size)/float(window_size)
aapl_avg = np.convolve(aapl, window, 'same')

# output to HTTP
output_file("stocks.html", title="stocks.py example")

# create plot
p = figure(width=800, height = 350, x_axis_type="datetime")

p.circle(aapl_dates, aapl, size=4, color='darkgery', alpha=0.2, legend='close')
p.line(aapl_dates, aapl_avg, color='navy', legend='avg')

show(p)
