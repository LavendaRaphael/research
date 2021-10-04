#!/bin/env python
from from_xas_modules import *
import os
import numpy
import json

str_exp=os.environ['goto_pto_exp']
os.chdir(str_exp)
#--------------------------------------------------[extract]
list2d_alpha = []
list2d_alpha.append( [20, '20210924.Pt.110.a20.csv'] )
list2d_alpha.append( [41, '20210924.Pt.110.a41.csv'] )

def_xas_exp_xyfit( list2d_alpha=list2d_alpha )
