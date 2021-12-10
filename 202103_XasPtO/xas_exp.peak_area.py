#!/bin/env python
import xas_module
import os

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

xas_module.def_peak_area_json( 
    str_datfile = '20211113.Angel-Pt110-OXAS.csv',
    int_xcolumn = 0,
    int_ycolumn = 1,
    str_jsonfile = '20211113.peak_area_a25.json'
)
