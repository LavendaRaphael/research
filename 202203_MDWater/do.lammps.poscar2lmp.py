import dpdata

dp_sys = dpdata.System(file_name='POSCAR', fmt='vasp/poscar')
print(dp_sys)
dp_sys.to('lammps/lmp', "poscar.lmp")
