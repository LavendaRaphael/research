from ase.geometry.analysis import Analysis
import model_devi
import numpy as np

# setup
array_id = np.arange(400000,600100,100)
tuple_elements = (8,8)
str_filerdf = f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]}_{array_id[-1]}.npy'

print(str_filerdf)
# common
float_rmax = 5.9
int_nbins = 160

# run
ase_atoms = model_devi.def_dump2ase(
    array_id = array_id,
    type_map = ["O", "H"])

int_nelement_1 = np.count_nonzero(ase_atoms[0].numbers == tuple_elements[1])
int_natoms = len(ase_atoms[0])

ase_analysis = Analysis(ase_atoms)
list_rdf = ase_analysis.get_rdf(
    rmax = float_rmax, 
    nbins = int_nbins, 
    elements= tuple_elements, 
    )

array_rdf = list_rdf[0]
array_rdf = 0
for array_tmp in list_rdf:
    array_rdf += array_tmp
int_frames = len(list_rdf)
array_rdf /= int_frames / int_natoms * int_nelement_1

array_r = ase_analysis.get_rdf(
    rmax = float_rmax, 
    nbins = int_nbins, 
    imageIdx=0, 
    elements= tuple_elements,
    return_dists=True,
    )[0][1]

array_final = np.empty( shape=(2,int_nbins) )
array_final[0] = array_r
array_final[1] = array_rdf

print(array_final)

np.save(
    file = str_filerdf,
    arr = array_final,
    )
