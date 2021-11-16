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
    class_paras.scaling_json = goto_pto_work_110+'Pt.110.x2y12z4.5_O22_vac15/vasp_sch/xas.a20_b90.scaling.json'

    return class_paras

def def_dict_structure():
    
    dict_structure = {}
    #------------------------------------------
    str_key='111.x4y4z4_O4'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto111_class( list2d_atom, str_workdir )
    #------------------------------------------
    str_key='110.x2y12z4.5_O22'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    list2d_atom.append([ 3,4.0])
    list2d_atom.append([ 5,4.0])
    list2d_atom.append([ 7,4.0])
    list2d_atom.append([ 9,4.0])
    list2d_atom.append([11,2.0])
    list1d_bbox = [ 1,11,4,15 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
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
    list1d_bbox = [ 0.5, 11/12, 2, 15/12 ]
    str_workdir = 'Pt.110.x2y12z4.5_O22_vac15/vasp_sch.aimd2_932/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O1'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.12'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.13'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O2.14'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.123'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,1.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.135'
    list2d_atom = []
    list2d_atom.append([ 1,3.0])
    list1d_bbox = [ 1,0.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O3.136'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,1.0])
    list1d_bbox = [ 1,1,2,3 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O4.v56'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    list1d_bbox = [ 1,1.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O5'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 2,2.0])
    list2d_atom.append([ 5,1.0])
    list1d_bbox = [ 1,1,2,3 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y3z4.5_O6'
    list2d_atom = []
    list2d_atom.append([ 1,6.0])
    list1d_bbox = [ 0.5, 0.5/3, 1, 4/3 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O2.15'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 1/2,1.5/4,1,1 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O2.16'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 1/2,3.5/4,1,1 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O3.137'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    list1d_bbox = [ 1,2.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O3.148'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,2.0])
    list1d_bbox = [ 1,2.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O4.1237'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 2,1.0])
    list2d_atom.append([ 3,2.0])
    list1d_bbox = [ 1,2.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O4.1458'
    list2d_atom = []
    list2d_atom.append([ 1,4.0])
    list1d_bbox = [ 1,0.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y4z4.5_O6.v56'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list2d_atom.append([ 3,4.0])
    list1d_bbox = [ 1,2.5,2,4 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_ym'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1/2,2/6,1,1 ]
    str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.ym/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_xm'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1/2,2/6,1,1 ]
    str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.xm/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_xp'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1/2,2/6,1,1 ]
    str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.xp/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_zm'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1/2,2/6,1,1 ]
    str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.zm/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x2y6z4.5_O2.17_zp'
    list2d_atom = []
    list2d_atom.append([ 1,1.0])
    list2d_atom.append([ 1,1.0])
    list1d_bbox = [ 1/2,2/6,1,1 ]
    str_workdir = 'Pt.110.x2y6z4.5_O2.17_vac15/vasp_sch.zp/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x4y3z4.5_O2.12'
    list2d_atom = []
    list2d_atom.append([ 1,2.0])
    list1d_bbox = [ 3/4,2/3,1,1 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------
    str_key='110.x4y3z4.5_O6'
    list2d_atom = []
    list2d_atom.append([ 1,6.0])
    list1d_bbox = [ 1/4,0.5/3,1,1 ]
    str_workdir = 'Pt.'+str_key+'_vac15/vasp_sch/'
    dict_structure[ str_key ] = def_pto110_class( list2d_atom, str_workdir, list1d_bbox )
    #------------------------------------------

    return dict_structure

def def_pto110_class( list2d_atom, str_workdir, list1d_bbox ):

    float_onset_110 = 529.6
    goto_pto_work_110=os.environ['goto_pto_work_110']

    class_structure = xas_module.class_structure()
    class_structure.list2d_atom = list2d_atom
    class_structure.str_chdir = goto_pto_work_110 + str_workdir
    class_structure.float_onset = float_onset_110
    class_structure.list1d_bbox = list1d_bbox

    return class_structure

def def_pto111_class( list2d_atom, str_workdir ):

    goto_pto_work_111=os.environ['goto_pto_work_111']
    float_onset_111 = 530.1

    class_structure = xas_module.class_structure()
    class_structure.list2d_atom = list2d_atom
    class_structure.str_chdir = goto_pto_work_111 + str_workdir
    class_structure.float_onset = float_onset_111

    return class_structure

def def_render(
        list1d_bbox, 
        str_poscar = 'POSCAR',
        str_savefig = 'render'
        ):

    atom_poscar = read(str_poscar)
    atom_cell = atom_poscar.cell
    atom_poscar = atom_poscar*(3,3,1)
    atom_poscar.cell = atom_cell

    array1d_cellpara = atom_cell.lengths()
    x1 = list1d_bbox[0] * array1d_cellpara[0]
    y1 = list1d_bbox[1] * array1d_cellpara[1]
    x2 = list1d_bbox[2] * array1d_cellpara[0] + x1
    y2 = list1d_bbox[3] * array1d_cellpara[1] + y1
    tup_bbox = ( x1,y1,x2,y2 )

    #r = [{'O': 0.74, 'Pt': 1.39}[at.symbol] for at in atom_poscar]
    
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
    
    renderer = write(str_savefig+'.pov', atom_poscar,
        **generic_projection_settings,
        povray_settings=povray_settings)
    renderer.render()
    
    os.remove(str_savefig+'.ini')
    os.remove(str_savefig+'.pov')
