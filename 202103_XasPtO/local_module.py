#!/user/bin/env python

import xas_module
import os
import json
from ase.io import read,write

def def_class_paras():

    class_paras = xas_module.class_paras()

    class_paras.tuple_xrange = (527.0, 540.0)
    class_paras.float_scalingarea = 20.0

    return class_paras

def def_dict_structure():
    
    dict_structure = {}
    #===================================================================================
    str_key='111.a2b2c4_O1_feff_kspace'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.111.a2b2c4_O1_vac15/feff_kspace/', 
        str_cif = 'template/polarization_z/feff.cif', 
        list1d_bbox = [ -0.25,-0.5,1.5,2 ]
        )
    #------------------------------------------
    str_key='111.x4y4z4_O4'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 0.5/4,1.5/4,1,1 ]
        )
    #------------------------------------------
    str_key='111.x4y4z4_O4_hch'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.111.x4y4z4_O4_vac15/vasp_sch.hch/'
        )
    #===================================================================================
    str_key='110.x1y1z4.5.a2b4_O4'
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/', 
        list1d_bbox = [ 0.5/2,0.5/4,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y1z4.5.a1b2_O3_a1b2'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,1.0])
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list2d_atom = list2d_atom, 
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y12z4.5_O22'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    list2d_atom.append([ 3,4.0])
    list2d_atom.append([ 5,4.0])
    list2d_atom.append([ 7,4.0])
    list2d_atom.append([ 9,4.0])
    list2d_atom.append([11,2.0])
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list2d_atom = list2d_atom,
        list1d_bbox = [ 1/2,0.5/12,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y12z4.5_O22_aimd'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,1.0])
    list2d_atom.append([ 4,1.0])
    list2d_atom.append([ 5,1.0])
    list2d_atom.append([ 6,1.0])
    list2d_atom.append([ 7,1.0])
    list2d_atom.append([ 8,1.0])
    list2d_atom.append([ 9,1.0])
    list2d_atom.append([10,1.0])
    list2d_atom.append([11,1.0])
    list2d_atom.append([12,1.0])
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.110.x2y12z4.5_O22_vac15/vasp_sch.aimd2_932/', 
        list1d_bbox = [ 0.5, 0.5/12, 1, 1 ],
        list2d_atom = list2d_atom
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O1'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/', 
        list1d_bbox = [ 1/2,2/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.12'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/', 
        list1d_bbox = [ 1/2,2/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.13'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/', 
        list1d_bbox = [ 1/2,2.5/3,1,1 ] 
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.14'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,2.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.123'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,2.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.135'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,0.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.136'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 0.5,0.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O4.v56'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,2.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O5'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 2,2.0])
    list2d_atom.append([ 5,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 0.5,0.5/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y3z4.5_O6'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 0.5, 0.5/3, 1, 1 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O2.15'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,1.5/4,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O2.16'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,3.5/4,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O3.137'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1,2.5,2,4 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O3.148'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1,2.5,2,4 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O4.1237'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,2.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,2.5/4,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O4.1458'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1,0.5,2,4 ]
        )
    #------------------------------------------
    str_key='110.x2y4z4.5_O6.v56'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,4.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1,2.5,2,4 ]
        )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+ str_key +'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,2/6,1,1 ]
        )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_ym'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.ym/' )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_xm'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.xm/' )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_xp'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.xp/' )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_zm'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.zm/' )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_zp'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.zp/' )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.18'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+ str_key +'_vac15/vasp_sch/',
        list1d_bbox = [ 1/2,5/6,1,1 ]
        )
    #------------------------------------------
    str_key='110.x4y3z4.5_O2.12'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 3/4,2/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x4y3z4.5_O6'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/',
        list1d_bbox = [ 1/4,0.5/3,1,1 ]
        )
    #------------------------------------------
    return dict_structure

def def_pto_class( 
        str_workdir,
        list2d_atom = [[1,1.0]],
        list1d_bbox = [0,0,1,1],
        str_cif = 'template/POSCAR'
    ):
 
    goto_pto_work_110=os.environ['goto_pto_work_110']
    goto_pto_work_111=os.environ['goto_pto_work_111']

    str_surface = str_workdir[0:6] 
    if (str_surface == 'Pt.110'):
        float_onset = 529.6
        goto_pto_work=goto_pto_work_110
    elif ( str_surface == 'Pt.111'):
        float_onset = 530.1
        goto_pto_work=goto_pto_work_111
    else:
        raise

    if ('vasp' in str_workdir):
        str_code = 'vasp'
        float_scaling = 0.15830009697342037
    elif ('feff' in str_workdir):
        str_code = 'feff'
        float_scaling = 228.0845335107418
    else:
        raise 

    class_structure = xas_module.class_structure()
    class_structure.list2d_atom = list2d_atom
    class_structure.str_chdir = goto_pto_work + str_workdir
    class_structure.float_onset = float_onset
    class_structure.list1d_bbox = list1d_bbox
    class_structure.str_cif = str_cif
    class_structure.str_code = str_code
    class_structure.float_scaling = float_scaling

    return class_structure

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
    
    renderer = write(str_savefig+'.pov', atom_poscar,
        **generic_projection_settings,
        povray_settings=povray_settings)
    renderer.render()
    
    os.remove(str_savefig+'.ini')
    os.remove(str_savefig+'.pov')
