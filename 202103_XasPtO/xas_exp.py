#!/bin/env python
from from_xas_modules import *

str_datfile = '20210926.Pt111-XAS.CSV'

str_outfile = '20210926.Pt.111.a20.csv'
int_xcolumn = 0
list_ycolumns = [2]

'''
str_datfile = '20210924.Pt110-XAS.CSV'

str_outfile = '20210924.Pt.110.a20.csv'
int_xcolumn = 6
list_ycolumns = [8]

str_outfile = '20210924.Pt.110.a41.csv'
int_xcolumn = 10
list_ycolumns = [12]
'''

str_xheader, list_yheaders, list_xdata, list_ydatas = def_xas_extract( str_datfile=str_datfile, int_xcolumn=int_xcolumn, list_ycolumns=list_ycolumns )

float_relheight = 0.4
float_relprominence = 0.02
list_peaks = def_xas_findpeaks( list_xdata=list_xdata, list_ydatas=list_ydatas, float_relheight=float_relheight, float_relprominence=float_relprominence )

tuple_xrange = (527.0, 540.0)
float_area = def_xas_findarea( list_xdata=list_xdata, list_ydatas=list_ydatas, tuple_xrange=tuple_xrange)

float_normarea = 20.0
float_scaling = float_normarea/float_area
list_datas=[]
list_datas.append( [list_xdata, list_ydatas, [0], float_scaling] )
list_xdata_mix, list_ydatas_mix = def_xas_mix( list_datas )

list_xdata = list_xdata_mix
list_ydatas = list_ydatas_mix
str_xheader = 'E(eV)'
list_yheaders = ['Intensity']
str_outfile = str_outfile
def_xas_writedata( list_xdata=list_xdata, list_ydatas=list_ydatas, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)

