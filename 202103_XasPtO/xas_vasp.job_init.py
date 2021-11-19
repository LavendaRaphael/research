import local_module
import xml.etree.cElementTree as ET


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
    
    with open('POSCAR', r) as file_poscar:
        for int_i in range(7):
            file_poscar.next()
        int_numofatom0 = int(file_poscar.readline().split()[0])
        str_temp = file_poscar.readline()
        if ( str_temp[0] in 'CcKkDd' ):
            int_directline = 8
        else:
            str_temp = file_poscar.readline()
            if ( str_temp[0] in 'CcKkDd' ):
                int_directline = 9
            else:
                raise NameError ( 'POSCAR not format!' )
    
    tree_vasprun = ET.ElementTree(file='../../posopt/vasprun.xml')
    for elem in tree.iterfind( 'parameters/separator[@name="electronic"]/i[@name="NELECT"]' )
        print elem.tag, elem.attrib
    #with open( '../../posopt/OUTCAR',r ) as file_outcar:
    #    for str_line in file_outcar:
    #        int_nelect = 
