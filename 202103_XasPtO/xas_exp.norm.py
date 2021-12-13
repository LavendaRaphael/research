#!/bin/env python
import xas_module
import os

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)
'''
#--------------------------------------------------[Pt.111]
str_datfile = '20210926.Pt111-XAS.CSV'

str_outfile = '20210926.Pt.111.a20.csv'
int_xcolumn = 0
list1d_ycolumn = [2]
'''
#--------------------------------------------------[Pt.110]
str_datfile = '20210924.Pt110-XAS.CSV'
'''
str_outfile = '20210924.Pt.110.a20.csv'
int_xcolumn = 6
list1d_ycolumn = [8]
'''
str_outfile = '20210924.Pt.110.a41.csv'
str_outfile='test.csv'
int_xcolumn = 10
list1d_ycolumn = [12]

#--------------------------------------------------[extract]
str_xheader, list_yheaders, array1d_xdata, array2d_ydata = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list1d_ycolumn=list1d_ycolumn )
#--------------------------------------------------[findpeaks]
float_relheight = 0.4
float_relprominence = 0.02
list_peaks = def_xas_findpeaks( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, float_relheight=float_relheight, float_relprominence=float_relprominence )
#--------------------------------------------------[findarea]
tuple_xrange = (527.0, 540.0)
float_area = def_xas_findarea( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, tuple_xrange=tuple_xrange)

#--------------------------------------------------[norm]
float_normarea = 20.0
float_scaling = float_normarea/float_area
list2d_data=[]
list2d_data.append( [array1d_xdata, array2d_ydata, [0], float_scaling] )
array1d_xdata_mix, array2d_ydata_mix = def_xas_mix( list2d_data )

#--------------------------------------------------[writedata]
array1d_xdata = array1d_xdata_mix
array2d_ydata = array2d_ydata_mix
str_xheader = 'E(eV)'
list_yheaders = ['Intensity']
str_outfile = str_outfile
def_xas_writedata( array1d_xdata=array1d_xdata, array2d_ydata=array2d_ydata, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)
