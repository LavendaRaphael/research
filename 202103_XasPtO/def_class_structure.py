#!/user/bin/env python
import os
from tf_xas_kit import class_structure
from tf_xas_kit import def_class_paras

def def_dict_structure_alphabeta(
        dict_input,
        ):
    instance_structure = def_class_structure_basic(dict_input)

    instance_structure.float_onset = def_class_structure_scaling_json(dict_input).float_onset

    str_scalingmethod = def_class_paras.def_instance_paras_code2xas().str_broadmethod
    str_code = instance_structure.str_code
    str_surface = instance_structure.dict_input['surface']
    if (str_code == 'vasp'):
        if ( str_surface == '111'):
            str_scalingfile = goto_pto_work_111+'Pt.111.x4y4_O4_vac/vasp_sch/xas.a20_b90.scaling.json'
        elif ( str_surface == '110' ):
            str_scalingfile = goto_pto_work_110+'Pt.110.x2y12_O22_vac/vasp_sch/xas.a20_b90.scaling.json'
        else:
            raise
    elif (str_code == 'feff'):
        if ( str_surface == '111'):
            str_scalingfile = goto_pto_work_111+'Pt.111.a2b2_O1_vac/feff_kspace/xas.a20_b90.scaling.json'
        elif (str_surface == '110'):
            str_scalingfile = goto_pto_work_110+'Pt.110.x2y1_O2_vac/feff_k/xas.a20_b90.scaling.json'
        else:
            raise
    else:
        raise
    with open( str_scalingfile, 'r') as open_json:
        dict_scaling = json.load( open_json )
        instance_structure.float_scaling = dict_scaling[ str_scalingmethod ]

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
        str_onsetfile = str_exp+'20210924.pto110_a20_info.json'
    elif ( str_surface == '111'):
        str_onsetfile = str_exp+'20210926.pto111_a20_info.json'
    else:
        raise
    with open( str_onsetfile, 'r' ) as open_json:
        dict_onset = json.load( open_json )
        instance_structure.float_onset = dict_onset[ 'float_onset' ]

def def_class_structure_basic{ 
        dict_input,
        }:

    instance_structure = class_structure()
    
    instance_structure.dict_input = dict_input
    
    instance_structure.dict_atom = dict_structure_single['dict_atom']

    goto_pto_work_110 = os.environ['goto_pto_work_110']
    goto_pto_work_111 = os.environ['goto_pto_work_111']
    if ( dict_input['str_surface'] == '110' ):
        goto_pto_work = goto_pto_work_110
    elif ( dict_input['str_surface'] == '111'):
        goto_pto_work = goto_pto_work_111
    else:
        raise
    instance_structure.str_chdir = goto_pto_work

    instance_structure.str_code = dict_structure_single['str_code']

    return class_structure
