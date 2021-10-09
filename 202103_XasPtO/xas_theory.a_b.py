#!/bin/env python
import from_xas_modules
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

list1d_workdir=[]

#----------------------------------[Pt.110]
list1d_workdir.append('Pt.110.x12y2z4.5_O22_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O1_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O6_vac15/')
str_headdir=str_110
float_onset = 529.6

#----------------------------------[Pt.111]
#float_onset = 530.1

#----------------------------------[20]
list1d_scalingangle = [20, 90]
list2d_angle = []
list2d_angle.append( list1d_scalingangle )
list2d_angle.append( [ 90, 45 ] )
list2d_angle.append( [  0, 90 ] )

#----------------------------------[41]
#list1d_scalingangle = [41, 90]
#list2d_angle = []
#list2d_angle.append( list1d_scalingangle )

#----------------------------------[loop]
list1d_alignangle = [20,90]

#str_outfile = 'xas.a'+str(list1d_scalingangle[0])+'_b'+str(list1d_scalingangle[1])+'.csv'
str_outfile = 'test.csv'

for str_workdir in list1d_workdir:
    str_workdir = str_headdir+str_workdir+'vasp_sch/'
    os.chdir(str_workdir)
    from_xas_modules.def_xas_abworkflow( list1d_alignangle=list1d_alignangle, list1d_scalingangle=list1d_scalingangle, list2d_angle=list2d_angle, float_onset=float_onset, str_outfile=str_outfile) 
    
