#!/user/bin/env python
import os
import json
from tf_xas_kit import class_structure
from XasPtO import local_class_paras_pp

def def_class_structure_alphabeta(
        dict_input,
        ):
    instance_structure = def_class_structure_basic(dict_input)

    instance_structure.float_onset = def_class_structure_scaling_json(dict_input).float_onset

    str_scalingmethod = local_class_paras_pp.def_instance_paras_alphabeta().str_scalingmethod
    str_code = instance_structure.str_code
    str_surface = instance_structure.dict_input['str_surface']
    str_dir_pto_shtu = os.environ['dir_pto_shtu']
    if (str_code == 'vasp'):
        if ( str_surface == '111'):
            str_scalingfile = os.path.join( str_dir_pto_shtu, 'Pt.111_O_vac', 'Pt.111.x4y4_O4_vac/vasp_sch/xas.a20_b90.scaling.json')
        elif ( str_surface == '110' ):
            str_scalingfile = os.path.join( str_dir_pto_shtu, 'Pt.110_O_vac', 'Pt.110.x2y12_O22_vac/vasp_sch/xas.a20_b90.scaling.json')
        else:
            raise
    elif (str_code == 'feff'):
        if ( str_surface == '111'):
            str_scalingfile = os.path.join( str_dir_pto_shtu, 'Pt.111_O_vac', 'Pt.111.a2b2_O1_vac/feff_kspace/xas.a20_b90.scaling.json')
        elif (str_surface == '110'):
            str_scalingfile = os.path.join( str_dir_pto_shtu, 'Pt.110_O_vac', 'Pt.110.x2y1_O2_vac/feff_k/xas.a20_b90.scaling.json')
        else:
            raise
    else:
        raise
    with open( str_scalingfile, 'r') as open_json:
        dict_scaling = json.load( open_json )
        instance_structure.float_scaling = dict_scaling[ str_scalingmethod ]

    return instance_structure

def def_class_structure_scaling_json(
        dict_input,
        ):
    instance_structure = def_class_structure_basic(dict_input)

    str_exp = os.environ['dir_pto_exp']
    str_surface = instance_structure.dict_input['str_surface']

    if (str_surface == '110'):
        tuple_mainxrange = (527.0, 540.0)
        tuple_postxrange = (539, 544)
    elif ( str_surface == '111'):
        tuple_mainxrange = (527.0, 540.0)
        tuple_postxrange = (534, 544)
    else:
        raise
    instance_structure.tuple_mainxrange = tuple_mainxrange
    instance_structure.tuple_postxrange = tuple_postxrange
    
    if (str_surface == '110'):
        str_onsetfile = os.path.join( str_exp, '20210924.pto110_a20_info.json')
    elif ( str_surface == '111'):
        str_onsetfile = os.path.join( str_exp, '20210926.pto111_a20_info.json')
    else:
        raise
    with open( str_onsetfile, 'r' ) as open_json:
        dict_onset = json.load( open_json )
        instance_structure.float_onset = dict_onset[ 'float_onset' ]

    return instance_structure

def def_class_structure_basic( 
        dict_input,
        ):

    instance_structure = class_structure.class_structure()
    
    instance_structure.dict_input = dict_input
    
    if ('dict_atom' not in dict_input):
        dict_input['dict_atom'] = {1: 1.0}
    instance_structure.dict_atom = dict_input['dict_atom']

    if ( dict_input['str_surface'] == '110' ):
        str_dir = 'Pt.110_O_vac'
    elif ( dict_input['str_surface'] == '111'):
        str_dir = 'Pt.111_O_vac'
    else:
        raise
    instance_structure.str_chdir = os.path.join( os.environ['dir_pto_shtu'], str_dir, dict_input['str_workdir'] ) 

    instance_structure.str_code = dict_input['str_code']

    return instance_structure
