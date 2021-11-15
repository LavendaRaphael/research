import os
import local_module

list1d_key=[]
list1d_key.append('110.x12y2z4.5_O22_aimd')
#list1d_key.append('110.x2y3z4.5_O6')
#list1d_key.append('110.x4y3z4.5_O6')

dict_structure = local_module.def_dict_structure()

for str_key in list1d_key:
    class_structure = dict_structure[ str_key ]
    str_chdir = class_structure.str_chdir + 'template/'
    os.chdir( str_chdir )
    print( os.getcwd() )

    local_module.def_render(
        list1d_bbox = class_structure.list1d_bbox,
    )

