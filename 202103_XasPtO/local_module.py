#!/user/bin/env python

import xas_module
import os
import json
from ase.io import read,write
import math


def def_class_paras():

    class_paras.int_atomkey = 11
    class_paras.float_tm_scaling = 5.0

    return class_paras

def def_render(
        class_structure, 
        str_savefig = 'render'
        ):

    list1d_bbox = class_structure.list1d_bbox
    str_cif = class_structure.str_cif

    atom_poscar = read( str_cif )
    atom_cell = atom_poscar.cell
    array2d_cell = atom_cell[:]

    atom_poscar = atom_poscar*(4,4,1)
    atom_poscar.translate( - array2d_cell[0] )
    atom_poscar.translate( - array2d_cell[1] )

    atom_poscar.cell = atom_cell

    array1d_bbox_1 = list1d_bbox[0] * array2d_cell[0] + list1d_bbox[1] * array2d_cell[1]
    array1d_bbox_2 = list1d_bbox[2] * array2d_cell[0] + list1d_bbox[3] * array2d_cell[1] + array1d_bbox_1

    tup_bbox = ( array1d_bbox_1[0], array1d_bbox_1[1], array1d_bbox_2[0], array1d_bbox_2[1] )

    #r = [{'O': 0.74, 'Pt': 1.39}[at.symbol] for at in atom_poscar]
    
    generic_projection_settings = {
        'bbox': tup_bbox,
        #'rotation': '90y',
        #'radii': .85,  # float, or a list with one float per atom
        'colors': None,  # List: one (r, g, b) tuple per atom
        'show_unit_cell': 1,   # 0, 1, or 2 to not show, show, and show all of cell
    }
    
    povray_settings={
        'display': True,  # Display while rendering
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
    
    renderer = write(str_savefig+'.pov', atom_poscar,
        **generic_projection_settings,
        povray_settings=povray_settings)
    renderer.render()
    
    os.remove(str_savefig+'.ini')
    os.remove(str_savefig+'.pov')
