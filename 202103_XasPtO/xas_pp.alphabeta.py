import xas_module
import os
import local_module

list1d_key=[]
#----------------------------------
#list1d_key.append('111.a2b2c4_O1_feff_kspace')
#list1d_key.append('111.x4y4z4_O4')
#list1d_key.append('111.x4y4z4_O4_hch')

#----------------------------------
#list1d_key.append('110.x1y1z4.5.a2b4_O4')
#list1d_key.append('110.x2y12z4.5_O22')
#list1d_key.append('110.x2y12z4.5_O22_aimd')
list1d_key.append('110.x2y1z4.5.a1b2_O3_a1b2')
#list1d_key.append('110.x2y3z4.5_O1')
#list1d_key.append('110.x2y3z4.5_O2.12')
#list1d_key.append('110.x2y3z4.5_O2.13')
#list1d_key.append('110.x2y3z4.5_O2.14')
#list1d_key.append('110.x2y3z4.5_O3.123')
#list1d_key.append('110.x2y3z4.5_O3.135')
#list1d_key.append('110.x2y3z4.5_O3.136')
#list1d_key.append('110.x2y3z4.5_O4.v56')
#list1d_key.append('110.x2y3z4.5_O5')
#list1d_key.append('110.x2y3z4.5_O6')
#list1d_key.append('110.x2y4z4.5_O2.15')
#list1d_key.append('110.x2y4z4.5_O2.16')
#list1d_key.append('110.x2y4z4.5_O3.137')
#list1d_key.append('110.x2y4z4.5_O3.148')
#list1d_key.append('110.x2y4z4.5_O4.1237')
#list1d_key.append('110.x2y4z4.5_O4.1458')
#list1d_key.append('110.x2y4z4.5_O6.v56')
#list1d_key.append('110.x2y6z4.5_O2.17')
#list1d_key.append('110.x2y6z4.5_O2.18')
#list1d_key.append('110.x4y3z4.5_O2.12')
#list1d_key.append('110.x4y3z4.5_O6')

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
        str_outfile = str_outfile
        ) 
    
