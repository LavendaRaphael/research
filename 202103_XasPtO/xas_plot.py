#!/bin/env python
from from_xas_modules import *
import os
import numpy
import json
import matplotlib.pyplot as plt
import matplotlib

print(matplotlib.matplotlib_fname())

matplotlib.rcParams['font.size']=25
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
matplotlib.rcParams["figure.figsize"] = (10,8)

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='20210924.Pt.110.a20.csv', int_xcolumn=0, list1d_ycolumn=[1] )
plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 20$\degree$' )

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='20210924.Pt.110.a41.csv', int_xcolumn=0, list1d_ycolumn=[1] )
plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 41$\degree$' )

str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile='xas_exp.xyfit.csv', int_xcolumn=0, list1d_ycolumn=[1] )
#array2d_ydata.reshape( (len(array1d_xdata)) )
plt.plot( array1d_xdata, array2d_ydata,label=r'Exp. 90$\degree$ fit' )

plt.legend()

plt.xlim( 527,540 )
plt.ylim( bottom=0 )
plt.xlabel( 'Energy (eV)' )
plt.ylabel( "Intensity (Arb. Units)" )
plt.savefig( 'xas_exp.xyfit.pdf',bbox_inches='tight' )
plt.show()
