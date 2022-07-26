from matplotlib import pyplot
import matplotlib
import numpy

matplotlib.rcParams['font.size']=15
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]

fig, ax = pyplot.subplots()

def coordination(x: float, n: int, m: int) -> float:
    return (1-numpy.power(x,n))/(1-numpy.power(x,m))

x = numpy.linspace( start=0, stop=2 )
ax.plot( x, coordination(x,6,12), label="6,12", linewidth=2)
ax.plot( x, coordination(x,8,16), label="8,16", linewidth=2)
ax.plot( x, coordination(x,12,24), label="12,24", linewidth=2)

ax.legend()
ax.set_xlim((0,2))
ax.set_ylim((0,1.1))
#fig.savefig('reaction_1.pdf', bbox_inches='tight')
pyplot.show()

