#!/bin/env python
import xas_module
import os

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)

xas_module.def_exp_info_json( 
    str_datfile = '20210926.Pt111-XAS.CSV',
    int_xcolumn = 0,
    int_ycolumn = 2,
    str_jsonfile = '20210926.pto111_a20_info.json'
)
