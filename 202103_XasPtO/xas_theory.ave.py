#!/bin/env python
import xas_module
import os
import local_module

list1d_workdir=[]
#----------------------------------
#list1d_workdir.append('Pt.110.x12y2z4.5_O22_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O1_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O3.136_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O5_vac15/')
#list1d_workdir.append('Pt.110.x2y3z4.5_O6_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O2.15_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O2.16_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list1d_workdir.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list1d_workdir.append('Pt.110.x4y3z4.5_O2.12_vac15/')
list1d_workdir.append('Pt.110.x4y3z4.5_O6_vac15/')

#list1d_workdir.append('Pt.111.x4y4z4_O4_vac15/')

#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir+'vasp_sch/'
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_ave( class_structure )
