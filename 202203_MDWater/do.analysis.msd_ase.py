from ase.geometry.analysis import Analysis
from ase.md.analysis import DiffusionCoefficient
import model_devi
import numpy as np

# setup

tuple_elements = (8,8)
#tuple_elements = (8,1)

list_array_id = []
#'''
list_array_id.append(np.arange( 000000, 100040,40))
#list_array_id.append(np.arange( 000000, 400040,40))
#list_array_id.append(np.arange( 400000, 800040,40))
#list_array_id.append(np.arange( 800000,1200040,40))
#list_array_id.append(np.arange(1200000,1600040,40))
#list_array_id.append(np.arange(1600000,2000040,40))

# def

def gen_filename(
        tuple_elements,
        array_id,
        ):
    return f'msd.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.npy'

# common

# run
def msd(
        array_id,
        ):
    ase_atoms = model_devi.def_dump2ase(
        array_id = array_id,
        type_map = ["O", "H"])
    
    ase_analysis = DiffusionCoefficient(
        traj = ase_atoms,
        timestep = 0.02,
        atom_indices = [0,1,2]
        )
    ase_analysis.print_data()
    ase_analysis.plot(show=True)

for array_id in list_array_id:
    msd(
        array_id = array_id,
        )
