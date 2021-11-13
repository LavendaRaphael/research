#!/bin/env python
import xas_module
import os

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)
#--------------------------------------------------[extract]
list2d_alpha = []
list2d_alpha.append( [20, '20210924.Pt.110.a20.csv',[0,1]] )
list2d_alpha.append( [41, '20210924.Pt.110.a41.csv',[0,2]] )

xas_module.exp_xyfit( list2d_alpha=list2d_alpha )
