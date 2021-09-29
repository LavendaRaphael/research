#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

dict_structures={}
str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
list_atoms = [[1,1.0],[3,1.0],[5,1.0],[7,1.0],[9,1.0],[11,0.5]]
dict_structures[ str_workdir ] = { 'list_atoms': list_atoms }

list_workdirs=[]
#----------------------------------[Pt.110]
list_workdirs.append('Pt.110.x12y2z4.5_O22_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O1_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.13_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.137_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.135_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.12_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O2.14_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O3.148_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1458_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O3.123_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O4.1237_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O4.v56_vac15/')
#list_workdirs.append('Pt.110.x2y4z4.5_O6.v56_vac15/')
#list_workdirs.append('Pt.110.x2y3z4.5_O6_vac15/')
str_headdir=str_110

#----------------------------------[Pt.111]

#----------------------------------[loop]
str_datfile = 'xas_ave.dat'

#str_outfile = 'xas.a'+str(list_normangle[0])+'_b'+str(list_normangle[1])+'.csv'
str_outfile = 'test.csv'

for str_workdir in list_workdirs:
    str_cddir = str_headdir+str_workdir+'vasp_sch/'
    os.chdir(str_cddir)
    os.chdir('atom_1/')    
    #_, _, array_xdata_origin, array_ydatas_origin = def_vasp_outcar2xas()
    float_finalenergy_1 = def_vasp_finalenergy() 
    os.chdir('..')
    for list_atom in dict_structures[ str_workdir ][ 'list_atoms' ]:
        print(list_atom)
        int_atom = list_atom[0]
        float_scaling = list_atom[1]
        os.chdir('atom_'+str(int_atom))
        float_finalenergy = def_vasp_finalenergy()
        float_sft = float_finalenergy-float_finalenergy_1
        print( json.dumps({ 'float_sft': float_sft }) )
        os.chdir('..')
