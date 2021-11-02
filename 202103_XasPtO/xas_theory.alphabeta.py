import xas_module
import os
import local_module

list1d_workdir=[]
#----------------------------------
#list1d_workdir.append('Pt.110.x12y2z4.5_O22_vac15/')
list1d_workdir.append('Pt.111.x4y4z4_O4_vac15/')

#----------------------------------[20]
list1d_scalingangle = [20, 90, 'trigonal']
list2d_angle = []
list2d_angle.append( list1d_scalingangle )
list2d_angle.append( [ 90, 45, 'trigonal' ] )
list2d_angle.append( [  0, 90, 'trigonal' ] )

#----------------------------------[41]
#list1d_scalingangle = [41, 90]
#list2d_angle = []
#list2d_angle.append( list1d_scalingangle )

#----------------------------------[loop]
dict_structures = local_module.def_dict_structures()

list1d_alignangle = [ 20, 90, 'trigonal']

str_abname = xas_module.def_abname( alpha=list1d_scalingangle[0], beta=list1d_scalingangle[1] )
str_outfile = 'xas.'+str_abname+'.csv'
#str_outfile = 'test.csv'

for str_workdir in list1d_workdir:
    class_structure = dict_structures[ str_workdir ]
    str_chdir = class_structure.str_chdir
    str_chdir = str_chdir+'vasp_sch/'
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_abworkflow( 
        list1d_alignangle = list1d_alignangle, 
        list1d_scalingangle = list1d_scalingangle, 
        list2d_angle = list2d_angle, 
        class_structure = class_structure, 
        str_outfile = str_outfile
        ) 
    
