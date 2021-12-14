#!/bin/env python
import xas_module
import os
import local_module
import pandas as pd

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
int_ycolumn = 12


