class class_structures(object):
    def __init__(self, str_dir, list_atoms):
        self.str_dir = str_dir
        self.list_atoms = list_atoms

dict_structures = {}

str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
list_atoms = []
list_atoms.append([ 1,2.0])
list_atoms.append([ 3,2.0])
list_atoms.append([ 5,2.0])
list_atoms.append([ 7,2.0])
list_atoms.append([ 9,2.0])
list_atoms.append([11,1.0])

dict_structures[ str_workdir ] = class_structures( str_workdir,list_atoms )

print(dict_structures[ str_workdir ].list_atoms)
