#!/user/bin/env python

import xas_module
import os
import json
from ase.io import read,write

def def_class_paras():

    class_paras = xas_module.class_paras()

    class_paras.tuple_xrange = (527.0, 540.0)
    class_paras.float_scalingarea = 20.0

    goto_pto_work_110=os.environ['goto_pto_work_110']
    class_paras.scaling_json = goto_pto_work_110+'Pt.110.x12y2z4.5_O22_vac15/vasp_sch/xas.a20_b90.scaling.json'

    return class_paras

def def_dict_structures():
    
    dict_structures = {}
    #------------------------------------------
    str_workdir='Pt.111.x4y4z4_O4_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    dict_structures[ str_workdir ] = def_pto111_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x12y2z4.5_O22_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    list2d_atom.append([ 3,4.0])
    list2d_atom.append([ 5,4.0])
    list2d_atom.append([ 7,4.0])
    list2d_atom.append([ 9,4.0])
    list2d_atom.append([11,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O1_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O2.12_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O2.13_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O2.14_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O3.123_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,1.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O3.135_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,3.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O3.136_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,1.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O4.v56_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O5_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 2,2.0])
    list2d_atom.append([ 5,1.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y3z4.5_O6_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,6.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O2.15_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O2.16_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O3.137_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O3.148_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O4.1237_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O4.1458_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x2y4z4.5_O6.v56_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,4.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_workdir='Pt.110.x4y3z4.5_O2.12_vac15/'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    dict_structures[ str_workdir ] = def_pto110_class( list2d_atom, str_workdir )
    #------------------------------------------

    return dict_structures

def def_pto110_class( list2d_atom, str_workdir ):

    float_onset_110 = 529.6
    goto_pto_work_110=os.environ['goto_pto_work_110']

    class_structrue = xas_module.class_structure()
    class_structrue.list2d_atom = list2d_atom
    class_structrue.str_chdir = goto_pto_work_110 + str_workdir
    class_structrue.float_onset = float_onset_110

    return class_structrue

def def_pto111_class( list2d_atom, str_workdir ):

    goto_pto_work_111=os.environ['goto_pto_work_111']
    float_onset_111 = 530.1

    class_structrue = xas_module.class_structure()
    class_structrue.list2d_atom = list2d_atom
    class_structrue.str_chdir = goto_pto_work_111 + str_workdir
    class_structrue.float_onset = float_onset_111

    return class_structrue

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
