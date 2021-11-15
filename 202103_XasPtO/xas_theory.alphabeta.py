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

#----------------------------------
list2d_angle = []
list2d_angle.append( [ 20, 90, 'trigonal' ] )
list2d_angle.append( [ 90, 45, 'trigonal' ] )
list2d_angle.append( [  0, 90, 'trigonal' ] )
list2d_angle.append( [ 41, 90, 'trigonal' ] )

#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()

list1d_alignangle = [ 20, 90, 'trigonal']

str_abname = xas_module.def_abname( alpha=list1d_alignangle[0], beta=list1d_alignangle[1] )
str_outfile = 'xas.'+str_abname+'.csv'
#str_outfile = 'test.csv'

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir
    str_chdir = str_chdir+'vasp_sch/'
    os.chdir(str_chdir)
    print(os.getcwd())

    xas_module.def_alphabeta_workflow( 
        list1d_alignangle = list1d_alignangle, 
        list2d_angle = list2d_angle, 
        class_structure = class_structure, 
        str_outfile = str_outfile
        ) 
    
