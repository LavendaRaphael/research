
import dpdata
import model_devi

dp_sys = dpdata.System(file_name="traj_bk/3800.lammpstrj", fmt='lammps/dump', type_map=["O","H"])

list_model = [
    "../../00.train/000/frozen_model.pb",
    "../../00.train/001/frozen_model.pb",
    "../../00.train/002/frozen_model.pb",
    "../../00.train/003/frozen_model.pb",
    ]
'''
list_model = [
    "../../../../dpgen_origin/iter.000006/00.train/000/frozen_model.pb",
    "../../../../dpgen_origin/iter.000006/00.train/001/frozen_model.pb",
    "../../../../dpgen_origin/iter.000006/00.train/002/frozen_model.pb",
    "../../../../dpgen_origin/iter.000006/00.train/003/frozen_model.pb",
    ]
'''
model_devi.def_model_devi_atom(
    list_model = list_model,
    dp_sys = dp_sys,
    float_lowthred = 0.25,
    str_save = "devi_f_atom.3800.pdf"
    )
