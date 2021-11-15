import numpy
import matplotlib.pyplot as plt

array1d_degree = numpy.linspace( 0,90,num=100 )
array1d_rad = numpy.radians( array1d_degree )
array1d_cos2 = numpy.cos( array1d_rad )**2

for int_i in range(0,45):
    array1d_degree_new = array1d_degree + int_i
    array1d_rad_new = numpy.radians( array1d_degree_new )
    array1d_cos2_new = numpy.cos( array1d_rad_new )**2
    plt.plot( array1d_cos2_new, array1d_cos2, label=int_i )
plt.legend()
plt.show()
