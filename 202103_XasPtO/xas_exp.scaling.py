#!/bin/env python
import xas_module
import os
import local_module
import pandas

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

#--------------------------------------------------[Pt.111]
xas_module.def_exp_scaling( 
    str_datfile = '20210926.Pt111-XAS.CSV',
    int_xcolumn = 0,
    int_ycolumn = 2,
    str_outfile = '20210926.pto111_a20_postscaling.csv'
    )
'''
#--------------------------------------------------[Pt.110]
xas_module.def_exp_scaling( 
    str_datfile = '20210924.Pt110-XAS.CSV',
    int_xcolumn = 6,
    int_ycolumn = 8,
    str_outfile = '20210924.pto110_a20_postscaling.csv'
    )
xas_module.def_exp_scaling( 
    str_datfile = '20210924.Pt110-XAS.CSV',
    int_xcolumn = 10,
    int_ycolumn = 12,
    str_outfile = '20210924.pto110_a41_postscaling.csv'
    )
'''
