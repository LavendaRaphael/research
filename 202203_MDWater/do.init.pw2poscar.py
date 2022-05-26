import ase.io

ase_atoms = ase.io.read(
     filename = 'cp.in',
     format = 'espresso-in',
     )
ase.io.write(
    filename = 'POSCAR',
    images = ase_atoms,
    format = 'vasp',
    )
ase.io.write(
    filename = 'lammps.data',
    images = ase_atoms,
    specorder = ["O","H"],
    format = 'lammps-data', 
    )
