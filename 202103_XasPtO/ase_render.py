import os
import local_module

list1d_key=[]

#list1d_key.append('111.a2b2c4_O1_feff_kspace')
#list1d_key.append('111.x4y4_O4')

#list1d_key.append('110.x1y1.a2b4_O4')
#list1d_key.append('110.x2y12_O22')
#list1d_key.append('110.x2y12_O22_aimd')
list1d_key.append('110.x2y1.a1b2_O3_a1b2')
#list1d_key.append('110.x2y3_O1')
#list1d_key.append('110.x2y3_O2.12')
#list1d_key.append('110.x2y3_O2.13')
#list1d_key.append('110.x2y3_O2.14')
#list1d_key.append('110.x2y3_O3.123')
#list1d_key.append('110.x2y3_O3.135')
#list1d_key.append('110.x2y3_O3.136')
#list1d_key.append('110.x2y3_O4.v56')
#list1d_key.append('110.x2y3_O5')
#list1d_key.append('110.x2y3_O6')
#list1d_key.append('110.x2y4_O2.15')
#list1d_key.append('110.x2y4_O2.16')
#list1d_key.append('110.x2y4_O4.1237')
#list1d_key.append('110.x2y6_O2.17')
#list1d_key.append('110.x2y6_O2.18')
#list1d_key.append('110.x4y3_O2.12')
#list1d_key.append('110.x4y3_O6')

dict_structure = local_module.def_dict_structure()

for str_key in list1d_key:
    class_structure = dict_structure[ str_key ]
    str_chdir = class_structure.str_chdir
    os.chdir( str_chdir )
    print( os.getcwd() )

    local_module.def_render(
        class_structure=class_structure
    )

