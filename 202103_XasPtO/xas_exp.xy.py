#!/bin/env python
from from_xas_modules import *
import os
import numpy

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)
#--------------------------------------------------[extract]
list_alpha = [20, 41]
int_lenalpha = len(list_alpha)

list_datas = []
for float_alpha in list_alpha:
    str_datfile = '20210924.Pt.110.a'+str(float_alpha)+'.csv'
    str_xheader, list_yheaders, array_xdata, array_ydatas = def_xas_extract( str_datfile=str_datfile, int_xcolumn=0, list_ycolumns=[1] )
    list_datas.append( [numpy.cos(float_alpha/180.0*numpy.pi), array_xdata, array_ydatas] )

array_fitx = numpy.empty( shape=(int_lendatas) )
for int_i in range(int_lendatas):
    array_fitx[int_i] = list_datas[ int_i ][0]

