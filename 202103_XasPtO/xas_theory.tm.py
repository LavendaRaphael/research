#!/bin/env python
import xas_module
import os
import local_module

dict_structures = local_module.def_dict_structures()
str_workdir='Pt.110.x12y2z4.5_O22_vac15/'

#----------------------------------[loop]
str_jsonfile='xas.a20_b90.json'
list2d_angle = []
list2d_angle.append( [ 90, 45, 'trigonal' ] )
list2d_angle.append( [  0, 90, 'trigonal' ] )
list2d_angle.append( [ 90,  0, 'orthorhombic' ] )
list2d_angle.append( [ 90, 90, 'orthorhombic' ] )

str_chdir = dict_structures[ str_workdir ].str_chdir
str_chdir = str_chdir+'vasp_sch/atom_11/'
os.chdir(str_chdir)
print(os.getcwd())

xas_module.def_xas_atom_abworkflow(
    str_jsonfile=str_jsonfile, 
    list2d_angle=list2d_angle, 
    str_workdir=str_workdir
    )