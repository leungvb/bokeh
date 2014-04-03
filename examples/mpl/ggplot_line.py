from ggplot import *
from bokeh import pyplot
from bokeh import plotting

g = ggplot(aes(x='date', y='beef'), data=meat) + \
    geom_line()

g.draw()

plt.title("Line ggplot-based plot in Bokeh.")

pyplot.show_bokeh(plt.gcf(), filename="ggplot_line.html")

plotting.session().dumpjson(file="ggplot_line.json")
