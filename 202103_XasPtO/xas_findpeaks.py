#!/bin/env python
from from_xas_modules import *

str_prefix = '20210918.Pt.110_a20'
list_files = []
list_files.append( ('20210918.Pt110-XAS.CSV', 6, 7, 1.0) )
def_xas_mix( list_files=list_files, str_prefix=str_prefix )

#def_xas_findpeaks( str_file=str_prefix+'.csv', float_relheight=0.3 ,str_prefix=str_prefix+'.findpeaks' )

