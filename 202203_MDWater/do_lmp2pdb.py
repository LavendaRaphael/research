import model_devi

array_id = [10000]

model_devi.def_lmp2pdb(
    array_id,
    type_map = ["O", "H"],
    str_save = "10000.pdb"
    )
