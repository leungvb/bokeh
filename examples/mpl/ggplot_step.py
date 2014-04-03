from ggplot import *
from bokeh import pyplot
from bokeh import plotting

df = pd.DataFrame({
    "x": range(100),
    "y": np.random.choice([-1, 1], 100)
})

df.y = df.y.cumsum()

g = ggplot(aes(x='x', y='y'), data=df) + \
    geom_step()
g.draw()

plt.title("Step ggplot-based plot in Bokeh.")

pyplot.show_bokeh(plt.gcf(), filename="ggplot_step.html")

plotting.session().dumpjson(file="ggplot_step.json")
