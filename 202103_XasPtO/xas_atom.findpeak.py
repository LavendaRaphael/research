import xas_module
import os

str_110=os.environ['goto_pto_work_110']
str_chdir = str_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/atom_11'
os.chdir( str_chdir )

#list1d_angle = [00, 90]
list1d_angle = [90, 45]
xas_module.def_atom_findpeak( 
    list1d_angle = list1d_angle,
    str_workdir = 'Pt.110.x12y2z4.5_O22_vac15/',
    str_jsonfile = 'xas.a20_b90.json',
    )