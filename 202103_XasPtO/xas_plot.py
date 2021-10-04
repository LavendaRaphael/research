#!/bin/env python
from from_xas_modules import *
import os
import numpy
import json
import matplotlib.pyplot as plt

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='20210924.Pt.110.a20.csv', int_xcolumn=0, list1d_ycolumn=[1] )
plt.plot( array1d_xdata, array2d_ydata,label='20' )

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='20210924.Pt.110.a41.csv', int_xcolumn=0, list1d_ycolumn=[1] )
plt.plot( array1d_xdata, array2d_ydata,label='41' )

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='xas_exp.xyfit.csv', int_xcolumn=0, list1d_ycolumn=[1] )
#array2d_ydata.reshape( (len(array1d_xdata)) )
plt.plot( array1d_xdata, array2d_ydata,label='xyfit' )

plt.legend()

plt.xlim( 527,540 )
plt.ylim( bottom=0 )
plt.xlabel( 'Energy (eV)' )
plt.ylabel( "Intensity (Arb. Units)" )

plt.show()
plt.savefig( 'xas_exp.xyfit.pdf' )
