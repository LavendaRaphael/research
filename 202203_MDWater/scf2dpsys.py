import dpdata
import os

dp_multisys = dpdata.MultiSystems.from_dir(
    dir_name='../scf_puww_25ps/sub_00000/', 
    file_name='pwscf.log', 
    fmt='qe/pw/scf',
    )
print(dp_multisys)
#os.chdir('../dpsys_puww_25ps')
