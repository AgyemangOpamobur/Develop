import bokeh
from bokeh.plotting import figure, output_file, show


x = [-20,-15,-10,-3,-2,-1,0,1,2,15,19.8]
y = [9,-120,3,-47,5,7,68,190,-70,89,12]
output_file("test.html")
plot = figure(plot_width = 250, plot_height = 250,
           x_range=(0,32), y_range=(-20,20))
plot.circle(x, y,size=10,color='blue',legend="trainset2")
show(plot)



