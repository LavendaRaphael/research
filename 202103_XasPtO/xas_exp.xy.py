#!/bin/env python
from from_xas_modules import *
import os
import numpy

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)
#--------------------------------------------------[extract]
array1d_alpha = [20, 41]
array1d_cosalpha2 = numpy.cos( numpy.radians( array1d_alpha ) ) **2
int_lenalpha = len(array1d_alpha)

array2d_data = []
for int_i in range(int_lenalpha):
    str_datfile = '20210924.Pt.110.a'+str(array1d_alpha[int_i])+'.csv'
    str_xheader, list1d_yheader, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list1d_ycolumn=[1] )
    list2d_data.append( [ array1d_cosalpha2[int_i], array1d_xdata, array2d_ydata] )

list2d_xydata = []
for list1d_data in list2d_data:
    list2d_xydata.append( [ list1d_data[1], list1d_data[2] ] )
array1d_xdata_interp, list1d_ydata_interp = def_xas_interp( list2d_xydata )

int_len1dxdata = len( array1d_xdata_interp )
array1d_ydata_xy = numpy.zeros( shape=(int_len1dxdata) )
array1d_temp = numpy.empty( shape=(int_lenalpha) )
for int_i in range( int_len1dxdata )
    
