#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

#--------------------------------------------------[Pt.111]
str_datfile = '20210926.Pt111-XAS.CSV'

str_outfile = '20210926.Pt.111.a20.csv'
int_xcolumn = 0
list_ycolumns = [2]

'''
#--------------------------------------------------[Pt.110]
str_datfile = '20210924.Pt110-XAS.CSV'

str_outfile = '20210924.Pt.110.a20.csv'
int_xcolumn = 6
list_ycolumns = [8]

str_outfile = '20210924.Pt.110.a41.csv'
int_xcolumn = 10
list_ycolumns = [12]
'''

#--------------------------------------------------[extract]
str_xheader, list_yheaders, array_xdata, array_ydatas = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list_ycolumns=list_ycolumns )
#--------------------------------------------------[findpeaks]
float_relheight = 0.4
float_relprominence = 0.02
list_peaks = def_xas_findpeaks( array_xdata=array_xdata, array_ydatas=array_ydatas, float_relheight=float_relheight, float_relprominence=float_relprominence )
#--------------------------------------------------[findarea]
tuple_xrange = (527.0, 540.0)
float_area = def_xas_findarea( array_xdata=array_xdata, array_ydatas=array_ydatas, tuple_xrange=tuple_xrange)

#--------------------------------------------------[norm]
float_normarea = 20.0
float_scaling = float_normarea/float_area
list_datas=[]
list_datas.append( [array_xdata, array_ydatas, [0], float_scaling] )
array_xdata_mix, array_ydatas_mix = def_xas_mix( list_datas )
'''
#--------------------------------------------------[writedata]
list_xdata = list_xdata_mix
list_ydatas = list_ydatas_mix
str_xheader = 'E(eV)'
list_yheaders = ['Intensity']
str_outfile = str_outfile
def_xas_writedata( list_xdata=list_xdata, list_ydatas=list_ydatas, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)
'''
