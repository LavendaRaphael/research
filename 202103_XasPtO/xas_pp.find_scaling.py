import xas_module
import os
import local_module

list1d_workdir=[]
#----------------------------------
list1d_workdir.append('Pt.110.x2y12z4.5_O22_vac15/')

#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir + 'vasp_sch/'
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_scaling_json( 
        list1d_alignangle = [20, 90, 'trigonal'],
        list1d_scalingangle = [20, 90, 'trigonal'], 
        class_structure = class_structure, 
        ) 
    