#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

list_dirs=[]
list_dirs.append('Pt.110.x12y2z4.5_O22_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O1_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list_dirs.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list_dirs.append('Pt.110.x2y3z4.5_O6_vac15/')

for str_dir in list_dirs:

    #----------------------------------[Pt.111]
    #str_datfile = 'xas.dat'
    #float_onset = 530.1

    #----------------------------------[Pt.110]
    str_datfile = 'xas_ave.dat'
    float_onset = 529.6
    str_dir = str_110+str_dir+'vasp_sch/'

    #----------------------------------[
    #list_normangle = [20, 90]
    #list_resultangles = []
    #list_resultangles.append( list_normangle )
    #list_resultangles.append( [ 90, 45 ] )
    #list_resultangles.append( [  0, 90 ] )

    #----------------------------------[
    list_normangle = [41, 90]
    list_resultangles = []
    list_resultangles.append( list_normangle )

    #----------------------------------[
    os.chdir(str_dir)

    str_outfile = 'xas.a'+str(list_normangle[0])+'_b'+str(list_normangle[1])+'.csv'
    #str_outfile = 'test.csv'
    def_xas_alignorm( list_normangle=list_normangle, list_resultangles=list_resultangles, str_datfile=str_datfile, float_onset=float_onset, str_outfile=str_outfile) 
    
