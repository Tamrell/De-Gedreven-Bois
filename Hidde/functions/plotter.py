'''import pandas

from bokeh.io import gridplot, output_file, show
from bokeh.plotting import figure

SD = pandas.read_excel('Sensor Data.xlsx')
MD = pandas.read_excel('Meteorological Data.xlsx')

#return a set of the chemicals
def getChemicals(SD):
    return list(set(pandas.Series(SD['Chemical']).values))

#return a set of the sensors
def getSensors(SD):
    return list(set(pandas.Series(SD['Monitor']).values))

chemicals = getChemicals(SD)
sensors = getSensors(SD)'''

from bokeh.io import gridplot, output_file, show
from bokeh.plotting import figure

output_file("layout.html")

x = list(range(11))
y0 = x
y1 = [10-i for i in x]
y2 = [abs(i-5) for i in x]

# create a new plot
s1 = figure(width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create another one
s2 = figure(width=250, height=250, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create and another
s3 = figure(width=250, height=250, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# put all the plots in a grid layout
p = gridplot([[s1, s2], [None, s3]])

# show the results
show(p)