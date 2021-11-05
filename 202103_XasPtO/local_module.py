#!/user/bin/env python

import xas_module
import os
import json
from ase.io import read,write

def def_dict_structures():
    goto_pto_exp=os.environ['goto_pto_exp']
    goto_pto_work_110=os.environ['goto_pto_work_110']
    goto_pto_work_111=os.environ['goto_pto_work_111']

    float_onset_110 = 529.6
    float_onset_111 = 530.1

    dict_structures = {}
    #------------------------------------------
    str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,2.0])
    list2d_atom.append([ 5,2.0])
    list2d_atom.append([ 7,2.0])
    list2d_atom.append([ 9,2.0])
    list2d_atom.append([11,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_110 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_110
    #------------------------------------------
    str_workdir='Pt.111.x4y4z4_O4_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_111 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_111
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O1_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_110 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_110
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O2.12_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_111 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_111
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O3.135_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_111 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_111
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O4.1458_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_111 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_111
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O6_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = xas_module.class_structure()
    dict_structures[ str_workdir ].list2d_atom = list2d_atom
    dict_structures[ str_workdir ].str_chdir = goto_pto_work_111 + str_workdir
    dict_structures[ str_workdir ].float_onset = float_onset_111

    return dict_structures

def def_pto110_class(  ):
    xas_module.class_structure()

def def_render(tup_bbox, str_poscar):
    dict_args = locals()

    print("#--------------------[xas_sft]\n")
    print(json.dumps( obj=dict_args, indent=4 ))

    filename = 'render'
    
    cont=read(str_poscar)
    cell=cont.cell
    cont=cont*(3,3,1)
    cont.cell=cell
 
    #r = [{'O': 0.74, 'Pt': 1.39}[at.symbol] for at in cont]
    
    generic_projection_settings = {
        'bbox': tup_bbox,
        #'rotation': '90y',
        #'radii': .85,  # float, or a list with one float per atom
        'colors': None,  # List: one (r, g, b) tuple per atom
        'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell
    }
    
    povray_settings={
    #   'display': False,  # Display while rendering
    #   'pause': True,  # Pause when done rendering (only if display)
    #   'transparent': False,  # Transparent background
        'canvas_width': 500,  # Width of canvas in pixels
    #   'canvas_height': 1000,  # Height of canvas in pixels
    #   'camera_dist': 50.,  # Distance from camera to front atom
    #   'image_plane': None,  # Distance from front atom to image plane
    #    'camera_type': 'perspective',  # orthographic, perspective, ultra_wide_angle
        'point_lights': [],             # [[loc1, color1], [loc2, color2],...]
        'area_light': [(2., 3., 40.),  # location
                       'White',       # color
                       .7, .7, 3, 3],  # width, height, Nlamps_x, Nlamps_y
    #   'background': 'White',        # color
        'textures': ['jmol',]*10000,  # ase2, ase3, glass, simple, pale, intermediate, vmd, jmol
    #   'celllinewidth': 0.1,  # Radius of the cylinders representing the cell
    }
    
    renderer=write(filename+'.pov',cont,
        **generic_projection_settings,
        povray_settings=povray_settings)
    renderer.render()
    
    os.remove(filename+'.ini')
    os.remove(filename+'.pov')
