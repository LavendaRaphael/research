#!/bin/env python
from from_xas_modules import *
import os

str_exp=os.environ['goto_pto_exp']
str_110=os.environ['goto_pto_work_110']

dict_structures={}
str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
list_atoms = []
list_atoms.append([ 1,2.0])
list_atoms.append([ 3,2.0])
list_atoms.append([ 5,2.0])
list_atoms.append([ 7,2.0])
list_atoms.append([ 9,2.0])
list_atoms.append([11,1.0])
float_sum = 0
for list_i in list_atoms:
    float_sum += list_i[1]
for list_i in list_atoms:
    list_i[1] /= float_sum
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
    list_datas = []
    str_cddir = str_headdir+str_workdir+'vasp_sch/'
    os.chdir(str_cddir)
    os.chdir('atom_1/') 
    float_finalenergy_1 = def_vasp_finalenergy() 
    os.chdir('..')
    for list_atom in dict_structures[ str_workdir ][ 'list_atoms' ]:

        int_atom = list_atom[0]
        float_scaling = list_atom[1]
        os.chdir('atom_'+str(int_atom))

        float_finalenergy = def_vasp_finalenergy()
        float_sft = float_finalenergy-float_finalenergy_1 

        str_xheader, list_yheaders, array_xdata, array_ydatas = def_vasp_outcar2xas()

        array_xdata_sft = def_xas_sft( array_xdata=array_xdata, float_sft=float_sft)

        array_xdata = array_xdata_sft
        list_ycolums = list(range(len(array_ydatas[0])))
        list_datas.append( [ array_xdata, array_ydatas, list_ycolums, float_scaling ] )

        os.chdir('..')
    array_xdata_mix, array_ydatas_mix = def_xas_mix(list_datas=list_datas)
    def_xas_writedata( array_xdata=array_xdata_mix, array_ydatas=array_ydatas_mix, str_xheader=str_xheader, list_yheaders=list_yheaders, str_outfile=str_outfile)
