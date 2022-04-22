
import dpdata
import model_devi
import os

dp_sys = dpdata.System(file_name="traj/10000.lammpstrj", fmt='lammps/dump', type_map=["O","H"])

str_save = "devi_f_atom.10000.pdf"

str_dir_iter = "../../"
#str_dir_iter = "../../../iter.000006/"
#str_dir_iter = "../../../../dpgen_origin/iter.000005/"

list_model = [
    os.path.join(str_dir_iter, "00.train/000/frozen_model.pb"),
    os.path.join(str_dir_iter, "00.train/001/frozen_model.pb"),
    os.path.join(str_dir_iter, "00.train/002/frozen_model.pb"),
    os.path.join(str_dir_iter, "00.train/003/frozen_model.pb"),
    ]

model_devi.def_model_devi_atom(
    list_model = list_model,
    dp_sys = dp_sys,
    float_lowthred = 0.15,
    str_save = str_save,
    #float_ylim = 2.6,
    )
