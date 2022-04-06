import traj_scf
import numpy
import group_module

instance_paras = traj_scf.class_paras()

# Weiyu Li
'''
instance_paras.list1d_filename = [ '0-1ps_XDATCAR', '1-5ps_XDATCAR' ]
instance_paras.str_format = 'vasp-xdatcar'
instance_paras.str_workdir = '../scf_liweiyu_5ps'
instance_paras.array_id = numpy.linspace(
    0,
    10000,
    num = 10,
    dtype = int,
    endpoint = False )
'''

# Weiwen Pu
instance_paras.list2d_files = [ 
    ['puww_0-5ps_cp',   'qe/cp/traj', 'dpdata' ],
    ['puww_5-15ps_cp',  'qe/cp/traj', 'dpdata' ],
    ['puww_15-25ps_cp', 'qe/cp/traj', 'dpdata' ],
    ]
instance_paras.str_workdir = '../scf_puww_25ps/'
instance_paras.array_id = numpy.linspace(
    0,
    50000,
    num = 50,
    dtype = int,
    endpoint = False )

#traj_scf.def_traj2poscar(instance_paras)

#traj_scf.def_inputinit_pwscf( instance_paras )

#instance_paras.array_id = instance_paras.array_id[0:1]
#group_module.def_subloop( instance_paras )

#traj_scf.def_scf2dpraw( instance_paras, int_copy = 100 )

