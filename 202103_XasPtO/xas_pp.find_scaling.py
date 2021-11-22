import xas_module
import os
import local_module

list1d_key=[]

#----------------------------------
#list1d_key.append('111.a2b2c4_O1_feff_kspace')

list1d_key.append('110.x2y12z4.5_O22')

#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()

for str_key in list1d_key:
    class_structure = dict_structure[ str_key ]
    str_chdir = class_structure.str_chdir
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_scaling_json(
        list1d_alignangle = [20, 90, 'trigonal'],
        list1d_scalingangle = [20, 90, 'trigonal'],
        class_structure = class_structure,
        )

