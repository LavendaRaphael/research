import os
import local_module

list1d_workdir=[]
list1d_workdir.append('Pt.110.x2y3z4.5_O6_vac15/')

dict_structure = local_module.def_dict_structure()

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir + 'vasp_sch/template/'
    os.chdir( str_chdir )
    print( os.getcwd() )

    def_render(
        tup_bbox = class_structure.tup_bbox
    )

