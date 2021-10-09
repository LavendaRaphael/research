#!/bin/env python

import from_xas_modules
import os
import sys
sys.path.append(r'./')
from from_dict_structures import dict_structures 

list_workdirs=[]
#----------------------------------[Pt.110]
list_workdirs.append('Pt.110.x12y2z4.5_O22_vac15/')

#----------------------------------[loop]
str_jsonfile='xas.a20_b90.json'
list2d_angle = []
list2d_angle.append( [ 90, 45 ] )
list2d_angle.append( [  0, 90 ] )

for str_workdir in list_workdirs:
    str_chdir = dict_structures[ str_workdir ].str_chdir
    str_chdir = str_chdir+'vasp_sch/'

    os.chdir(str_chdir)
    print(os.getcwd())

    list2d_atom = dict_structures[ str_workdir ].list2d_atom
    from_xas_modules.def_xas_atom_abworkflow(  str_jsonfile=str_jsonfile, list2d_angle=list2d_angle, list2d_atom=list2d_atom, float_tm_scaling=1.0)