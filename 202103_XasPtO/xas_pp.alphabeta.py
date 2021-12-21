import xas_module
import os
import local_module

#----------------------------------
list2d_angle = []
list2d_angle.append( [ 20, 90, 'trigonal' ] )
list2d_angle.append( [ 90, 45, 'trigonal' ] )
list2d_angle.append( [  0, 90, 'trigonal' ] )

list1d_alignangle = [ 20, 90, 'trigonal']
#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()
list1d_key = local_module.def_list1d_key()

#str_abname = xas_module.def_abname( alpha=list1d_alignangle[0], beta=list1d_alignangle[1] )
#str_outfile = 'xas.'+str_abname+'.csv'
#str_outfile = 'test.csv'

for str_key in list1d_key:
    class_structure = dict_structure[ str_key ]
    str_chdir = class_structure.str_chdir
    str_chdir = str_chdir
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_alphabeta_workflow( 
        list1d_alignangle = list1d_alignangle, 
        list2d_angle = list2d_angle, 
        class_structure = class_structure, 
        ) 
    
