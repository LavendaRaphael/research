import os
import local_module

list1d_workdir=[]
list1d_workdir.append('Pt.110.x2y3z4.5_O6_vac15/')
#list1d_workdir.append('Pt.110.x4y3z4.5_O6_vac15/')

dict_structure = local_module.def_dict_structure()

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir + 'vasp_sch/template/'
    os.chdir( str_chdir )
    print( os.getcwd() )

    local_module.def_render(
        #list1d_bbox = class_structure.list1d_bbox,
        list1d_bbox = [ 0.5, 0.5/3, 2, 1 ],
        str_savefig = 'render0',
    )

