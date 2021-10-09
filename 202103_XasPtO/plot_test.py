#!/bin/env python
import from_xas_modules
import matplotlib.pyplot as plt

_, _, array1d_xdata_1, array2d_ydata_1 = from_xas_modules.def_xas_extract( str_datfile='xas.a20_b90.csv', int_xcolumn=0, list1d_ycolumn=[1,2,3] )
_, _, array1d_xdata_2, array2d_ydata_2 = from_xas_modules.def_xas_extract( str_datfile='test.csv', int_xcolumn=0, list1d_ycolumn=[1,2,3] )

for int_i in range(3):
    plt.figure(int_i)
    plt.plot( array1d_xdata_1, array2d_ydata_1[:,int_i], label='orgin')
    plt.scatter( array1d_xdata_2, array2d_ydata_2[:,int_i], facecolors='none',edgecolors='r', label='test')
    plt.legend()
plt.show()