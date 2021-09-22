#!/bin/env python
from from_xas_modules import *
import json

str_temp = '20210918.Pt.110.a20'
list_files = [ ('20210918.Pt110-XAS.CSV', 6, 7, 1.0) ]

str_temp = '20210918.Pt.110.a41'
list_files = [ ('20210918.Pt110-XAS.CSV', 9, 10, 1.0) ]

str_prefix = str_temp
def_xas_mix( list_files=list_files, str_prefix=str_prefix )

str_datfile = str_temp+'.csv'
float_relheight = 0.4
float_relprominence = 0.02
str_prefix = str_temp+'.findpeaks'
def_xas_findpeaks( str_datfile=str_datfile, float_relheight=float_relheight, float_relprominence=float_relprominence, str_prefix=str_prefix )

str_datfile = str_prefix+'.csv'
tuple_xrange = (527.0, 540.0)
str_prefix = str_temp+'.findarea'
def_xas_findarea( str_datfile=str_datfile, tuple_xrange=tuple_xrange, str_prefix=str_prefix )
str_outfile = str_prefix'.json'
with open( str_outfile, 'r' ) as ojb_outfile:
    dict_outfile = json.load( fp=str_outfile )
    float_area = dict_outfile['float_area']

str_datfile = str_temp+'.csv'
float_normarea = 20.0
float_scaling = float_area/float_normarea
str_prefix = str_temp+'.scale'
def_xas_scale( str_datfile=str_datfile, float_scaling=float_scaling, str_prefix=str_prefix )


