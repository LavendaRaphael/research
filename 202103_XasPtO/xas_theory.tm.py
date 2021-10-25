#!/bin/env python
import xas_module
import os
import local_module

list1d_workdir=[]
#----------------------------------[Pt.110]
list1d_workdir.append('Pt.110.x12y2z4.5_O22_vac15/')

#----------------------------------[loop]
str_jsonfile='xas.a20_b90.json'
list2d_angle = []
list2d_angle.append( [ 90, 45 ] )
list2d_angle.append( [  0, 90 ] )
list2d_angle.append( [  0, 90 ] )
list2d_angle.append( [  0, 90 ] )


dict_structures = local_module.def_dict_structures()
for str_workdir in list1d_workdir:
    str_chdir = dict_structures[ str_workdir ].str_chdir
    str_chdir = str_chdir+'vasp_sch/'
    os.chdir(str_chdir)
    print(os.getcwd())

    list2d_atom = dict_structures[ str_workdir ].list2d_atom
    xas_module.def_xas_atom_abworkflow(
        str_jsonfile=str_jsonfile, 
        list2d_angle=list2d_angle, 
        list2d_atom=list2d_atom
        )