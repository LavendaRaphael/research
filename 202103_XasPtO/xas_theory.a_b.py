#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

list_workdirs=[]

#----------------------------------[Pt.110]
list_workdirs.append('Pt.110.x12y2z4.5_O22_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O1_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O6_vac15/')
str_headdir=str_110
float_onset = 529.6

#----------------------------------[Pt.111]
#float_onset = 530.1

#----------------------------------[20]
list_normangle = [20, 90]
list_resultangles = []
list_resultangles.append( list_normangle )
list_resultangles.append( [ 90, 45 ] )
list_resultangles.append( [  0, 90 ] )

#----------------------------------[41]
#list_normangle = [41, 90]
#list_resultangles = []
#list_resultangles.append( list_normangle )

#----------------------------------[loop]
list_alignangle = [20,90]

str_outfile = 'xas.a'+str(list_normangle[0])+'_b'+str(list_normangle[1])+'.csv'
#str_outfile = 'test.csv'

for str_workdir in list_workdirs:
    str_workdir = str_headdir+str_workdir+'vasp_sch/'
    os.chdir(str_workdir)
    def_xas_alignorm( list_alignangle=list_alignangle, list_normangle=list_normangle, list_resultangles=list_resultangles, float_onset=float_onset, str_outfile=str_outfile) 
    
