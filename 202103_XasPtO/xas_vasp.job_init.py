import local_module
import os
from distutils.dir_util import copy_tree
import re

list1d_workdir=[]
#----------------------------------
list1d_workdir.append('110.x1y1z4.5.a2b4_O4')

#----------------------------------[loop]
dict_structure = local_module.def_dict_structure()

for str_workdir in list1d_workdir:
    class_structure = dict_structure[ str_workdir ]
    str_chdir = class_structure.str_chdir
    os.chdir(str_chdir)
    print(os.getcwd())

    os.chdir('template/')

    with open('POSCAR', 'r') as file_poscar:
        list1d_poscar = file_poscar.readlines()
        list1d_atomnum = [int(str_num) for str_num in list1d_poscar[6].split()]
        if (list1d_atomnum[0] != 1):
            list1d_poscar[5] = list1d_poscar[5].split()[0] +' '+ list1d_poscar[5]
            list1d_atomnum[0] -= 1
            list1d_poscar[6] = '1'
            for int_i in list1d_atomnum:
                list1d_poscar[6] += ' '+str(int_i)
            list1d_poscar[6] += '\n'

        if ( list1d_poscar[7].strip()[0] in 'CcKkDd' ):
            int_directline = 7
        elif ( list1d_poscar[8].strip()[0] in 'CcKkDd' ):
            int_directline = 8
        else:
            raise NameError ( 'POSCAR not format!' )
 
    int_nelect = 0
    list1d_atomname = list1d_poscar[5].split()
    list1d_atomnum = [int(str_num) for str_num in list1d_poscar[6].split()]
    dict_pot = groupmodule.def_dict_pot()
    for int_i in range(len(list1d_atomname)):
        int_val = dict_pot[ list1d_atomname[ int_i ] ][1]
        int_atomnum = list1d_atomnum[ int_i ]
        int_nelect += int_val * int_atomnum
    with open('INCAR','r+') as file_incar:
        list1d_incar = file_incar.readlines()
        for str_line in list1d_incar:
            if (str_line.strip()[0:6] == 'NBANDS'):
                str_line = 'NBANDS = '+str(int_nelect)
        file_incar.seek(0)
        file_incar.trunk()
        file_incar.writelines( list1d_incar )

    with open( 'vasp_sub.py','r' ) as file_sub:
        str_subfile = file_sub.read()

    os.chdir('..')

    for list1d_atomi in class_structure.list2d_atom:
        str_atomdir = list1d_atomi[2]
        int_atomi = list1d_atomi[0]
        copy_tree( 'template/', str_atomdir )
        os.chdir(str_atomdir)
        list1d_poscar_atomi = list1d_poscar
        list1d_poscar_atomi[ int_directline +1 ] = list1d_poscar[ int_directline +int_atomi ]
        list1d_poscar_atomi[ int_directline +int_atomi ] = list1d_poscar[ int_directline +1 ]
        with open('POSCAR', 'w') as file_poscar:
            file_poscar.writelines( list1d_poscar_atomi )

        with open( 'vasp_sub.py','w' ) as file_sub:
            str_subfile_new = re.sub( 'xNUMx',str(int_atomi),str_subfile )
            file_sub.write( str_subfile_new )

        os.chdir('..')
        
