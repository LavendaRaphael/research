import model_devi
import ase.io

array_id = [10000]
str_save = '10000.pdb'

ase_atoms = model_devi.def_dump2ase(
    array_id = array_id,
    type_map = ["O", "H"]):
ase.io.write(format="proteindatabank", filename=str_save, images=ase_atoms)

