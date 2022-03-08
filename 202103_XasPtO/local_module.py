#!/user/bin/env python

import xas_module
import os
import json
from ase.io import read,write
import math

def def_list1d_key():
    list1d_key=[]
   
    #---------------------------------- 
    #list1d_key.append('exp.20210926.pto111')
    #list1d_key.append('exp.20210924.pto110_a20')
    #list1d_key.append('exp.20210924.pto110_a41')
    #----------------------------------
    #list1d_key.append('111.a2b2_O1_feffk')
    #list1d_key.append('111.x4y4_O4')
    #list1d_key.append('111.x4y4_O4_hch')
    
    #----------------------------------
    #list1d_key.append('110.x1y1.a2b2_O2_a1b2')
    list1d_key.append('110.x2y12_O22')
    #list1d_key.append('110.x2y12_O22_aimd')
    #list1d_key.append('110.x2y1_O1_a1b3')
    #list1d_key.append('110.x2y1_O2_feffk')
    #list1d_key.append('110.x2y1_O2_a1b3')
    #list1d_key.append('110.x2y2_O1_a1b2')
    #list1d_key.append('110.x2y2_O2.14_a1b2')
    #list1d_key.append('110.x2y2_O3_a1b2')
    #list1d_key.append('110.x2y3_O1')
    #list1d_key.append('110.x2y3_O1_a1b2')
    #list1d_key.append('110.x2y3_O2.12')
    #list1d_key.append('110.x2y3_O2.13')
    #list1d_key.append('110.x2y3_O2.14')
    #list1d_key.append('110.x2y3_O3.123')
    #list1d_key.append('110.x2y3_O3.136')
    #list1d_key.append('110.x2y3_O4.v56')
    #list1d_key.append('110.x2y3_O5')
    #list1d_key.append('110.x2y4_O2.16')
    #list1d_key.append('110.x2y4_O3.137')
    #list1d_key.append('110.x2y4_O3.148')
    #list1d_key.append('110.x2y4_O4.1237')
    #list1d_key.append('110.x2y4_O6.v56')
    #list1d_key.append('110.x2y6_O2.18')
    #list1d_key.append('110.x4y3_O2.12')
    #list1d_key.append('110.x4y3_O6')

    return list1d_key

def def_class_paras():

    class_paras = xas_module.class_paras()

    #class_paras.str_scalingmethod = 'float_mainscaling'
    class_paras.str_scalingmethod = 'float_postscaling'
    
    #class_paras.log_tm2xas = False
    class_paras.log_tm2xas = True
    class_paras.str_broadmethod = 'gaussian'
    #class_paras.str_broadmethod = 'lorentzian'
    #class_paras.float_hwhm = 0.45*math.sqrt( math.log(2) )
    #class_paras.float_hwhm = 0.225
    class_paras.float_hwhm = 0.4*math.sqrt( 2*math.log(2) )
    class_paras.int_broadnbin = 3000
 
    str_temp = ''
    class_paras.str_xasfile = 'xas'+str_temp+'.csv'
    class_paras.str_avefile = 'xas'+str_temp+'.ave.csv'
    class_paras.str_alphafile = 'xas'+str_temp+'.alpha.csv'

    list2d_angle = []
    list2d_angle.append( [ 20, 90, 'trigonal' ] )
    list2d_angle.append( [ 90, 45, 'trigonal' ] )
    list2d_angle.append( [  0, 90, 'trigonal' ] )
    list2d_angle.append( [ 41, 90, 'trigonal' ] )
    list2d_angle.append( [ 90,  0, 'orthorhombic' ] )
    list2d_angle.append( [ 90, 90, 'orthorhombic' ] )
    class_paras.list2d_angle = list2d_angle
    
    list1d_alignangle = [ 20, 90, 'trigonal']
    class_paras.list1d_alignangle = list1d_alignangle

    str_abname = xas_module.def_abname( alpha=list1d_alignangle[0], beta=list1d_alignangle[1])
    class_paras.str_alignfile = 'xas.'+str_abname+'.align.json'

    class_paras.int_atomkey = 11
    class_paras.float_tm_scaling = 5.0

    return class_paras

def def_dict_structure():
    
    dict_structure = {}
    #===================================================================================
    str_key='exp.20210926.pto111'
    dict_structure[ str_key ] = def_pto_class(
        marker = ['exp','111'],
        str_datfile = '20210926.Pt111-XAS.CSV',
        list1d_column = [0,2]
        )
    str_key='exp.20210924.pto110_a20'
    dict_structure[ str_key ] = def_pto_class(
        marker = ['exp','110'],
        str_datfile = '20210924.Pt110-XAS.CSV',
        list1d_column = [6,8]
        )
    str_key='exp.20210924.pto110_a41'
    dict_structure[ str_key ] = def_pto_class(
        marker = ['exp','110'],
        str_datfile = '20210924.Pt110-XAS.CSV',
        list1d_column = [10,12]
        )
    #===================================================================================
    str_key='111.a2b2_O1_feff'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.111.a2b2_O1_vac/feff/',
        list1d_bbox = [ 0.5/4,1.5/4,1,1 ],
        )
    #------------------------------------------
    str_key='111.a2b2_O1_feffk'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.111.a2b2_O1_vac/feff_kspace/',
        list1d_bbox = [ 0.5/4,1.5/4,1,1 ],
        float_onset_sft = 0.3
        )
    #------------------------------------------
    str_key='111.x4y4_O4'
    dict_structure[ str_key ] = def_pto_class(
        marker = ['theory','vasp','111'],
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.25,-0.25,1.5,1.5 ],
        )
    #------------------------------------------
    str_key='111.x4y4_O4_hch'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.111.x4y4_O4_vac/vasp_sch.hch/'
        )
    #===================================================================================
    str_key='110.x1y1.a2b2_O2_a1b2'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y12_O22'
    dict_atom = {}
    dict_atom[1] = [ 4.0]
    dict_atom[3] = [ 4.0]
    dict_atom[5] = [4.0]
    dict_atom[7] = [4.0]
    dict_atom[9] = [4.0]
    dict_atom[11] = [2.0]
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        dict_atom = dict_atom,
        list1d_bbox = [ -0.5,-0.5/12,2,13/12 ]
        )
    #------------------------------------------
    str_key='110.x2y12_O22_aimd'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [1.0]
    dict_atom[3] = [1.0]
    dict_atom[4] = [1.0]
    dict_atom[5] = [1.0]
    dict_atom[6] = [1.0]
    dict_atom[7] = [1.0]
    dict_atom[8] = [1.0]
    dict_atom[9] = [1.0]
    dict_atom[10] = [1.0]
    dict_atom[11] = [1.0]
    dict_atom[12] = [1.0]
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.110.x2y12_O22_vac/vasp_sch.aimd2_932/', 
        list1d_bbox = [ 0.5, 0.5/12, 1, 1 ],
        dict_atom = dict_atom
        )
    #------------------------------------------
    str_key='110.x2y1_O1_a1b3'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y1_O2_feffk'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.110.x2y1_O2_vac/feff_k/',
        list1d_bbox = [ -0.5,-0.5,2,2 ],
        )
    #------------------------------------------
    str_key='110.x2y1_O2_a1b3'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y1_O2_a1b3'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
   #------------------------------------------
    str_key='110.x2y2_O1_a1b2'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y2_O2.14_a1b2'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y2_O3_a1b2'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [1.0]
    dict_atom[3] = [1.0]
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        dict_atom = dict_atom, 
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O1'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/', 
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O1_a1b2'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+ str_key +'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O2.12'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/', 
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O2.13'
    dict_structure[ str_key ] = def_pto_class( 
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/', 
        list1d_bbox = [ -0.5,-0.5,2,2 ], 
        )
    #------------------------------------------
    str_key='110.x2y3_O2.14'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O3.123'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [1.0]
    dict_atom[3] = [1.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        dict_atom = dict_atom,
        list1d_bbox = [ -0.5,-0.5,2,2 ]
        )
    #------------------------------------------
    str_key='110.x2y3_O3.136'
    dict_atom = {}
    dict_atom[1] = [2.0]
    dict_atom[3] = [1.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y3_O4.v56'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ],
        )
    #------------------------------------------
    str_key='110.x2y3_O5'
    dict_atom = {}
    dict_atom[1] = [2.0]
    dict_atom[2] = [2.0]
    dict_atom[5] = [1.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.5,2,2 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y4_O2.16'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ]
        )
    #------------------------------------------
    str_key='110.x2y4_O3.137'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [2.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y4_O3.148'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [2.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y4_O4.1237'
    dict_atom = {}
    dict_atom[1] = [1.0]
    dict_atom[2] = [1.0]
    dict_atom[3] = [2.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y4_O6.v56'
    dict_atom = {}
    dict_atom[1] = [2.0]
    dict_atom[3] = [4.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ -0.5,-0.25,2,1.5 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    str_key='110.x2y6_O2.18'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+ str_key +'_vac/vasp_sch/',
        list1d_bbox = [ 1/2,5/6,1,1 ]
        )
    #------------------------------------------
    str_key='110.x4y3_O2.12'
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ 3/4,2/3,1,1 ]
        )
    #------------------------------------------
    str_key='110.x4y3_O6'
    dict_atom = {}
    dict_atom[1] = [2.0]
    dict_structure[ str_key ] = def_pto_class(
        str_workdir = 'Pt.'+str_key+'_vac/vasp_sch/',
        list1d_bbox = [ 1/4,0.5/3,1,1 ],
        dict_atom = dict_atom,
        )
    #------------------------------------------
    return dict_structure

def def_pto_class( 
        marker = None,
        str_workdir='',
        dict_atom = None,
        list1d_bbox = None,
        str_cif = 'template/POSCAR',
        str_datfile = None,
        float_onset_sft = 0.0,
        list1d_column = None,
        log_test = False,
    ):
    if (dict_atom is None):
         dict_atom = {1:[1.0]}
    if list1d_bbox is None:
         list1d_bbox = [0,0,1,1]
    str_exp=os.environ['goto_pto_exp']
    goto_pto_work_110=os.environ['goto_pto_work_110']
    goto_pto_work_111=os.environ['goto_pto_work_111']
    class_structure = xas_module.class_structure()
    
    if ( marker == None ):
        marker = []
        str_surface = str_workdir[0:6] 
        if (str_surface == 'Pt.110'):
            marker.append( '110' )
        elif ( str_surface == 'Pt.111'):
            marker.append( '111' )
        else:
            raise
        if ('vasp' in str_workdir):
            marker.extend( ['vasp','theory'] )
        elif ('feff' in str_workdir):
            marker.extend( ['feff','theory'] )
        else:
            raise 

    if ('110' in marker):
        str_onsetfile = str_exp+'20210924.pto110_a20_info.json'
        goto_pto_work=goto_pto_work_110
        tuple_mainxrange = (527.0, 540.0)
        tuple_postxrange = (539, 544)
    elif ( '111' in marker):
        str_onsetfile = str_exp+'20210926.pto111_a20_info.json'
        goto_pto_work=goto_pto_work_111
        tuple_mainxrange = (527.0, 540.0)
        tuple_postxrange = (534, 544)
    else:
        raise

    if ('theory' in marker):
        class_paras = def_class_paras()
        if ('vasp' in marker):
            str_code = 'vasp'
            if ( '111' in marker):
                str_scalingfile = goto_pto_work_111+'Pt.111.x4y4_O4_vac/vasp_sch/xas.a20_b90.scaling.json'
            elif ( '110' in marker):
                str_scalingfile = goto_pto_work_110+'Pt.110.x2y12_O22_vac/vasp_sch/xas.a20_b90.scaling.json'
            str_cif = 'template/POSCAR'
        elif ('feff' in marker):
            str_code = 'feff'
            if ( '111' in marker):
                str_scalingfile = goto_pto_work_111+'Pt.111.a2b2_O1_vac/feff_kspace/xas.a20_b90.scaling.json'
            elif ( '110' in marker):
                str_scalingfile = goto_pto_work_110+'Pt.110.x2y1_O2_vac/feff_k/xas.a20_b90.scaling.json'
            str_cif = 'feff.cif'
        with open( str_onsetfile, 'r' ) as open_json:
            dict_onset = json.load( open_json )
        with open( str_scalingfile, 'r') as open_json:
            dict_scaling = json.load( open_json )
        class_structure.dict_atom = dict_atom
        class_structure.float_onset = dict_onset[ 'float_onset' ] + float_onset_sft
        class_structure.list1d_bbox = list1d_bbox
        class_structure.str_cif = str_cif
        class_structure.str_code = str_code
        class_structure.float_scaling = dict_scaling[ class_paras.str_scalingmethod ]
    elif ( 'exp' in marker ):
        goto_pto_work = str_exp
        class_structure.list1d_column = list1d_column
    else:
        raise
    class_structure.str_chdir = goto_pto_work + str_workdir
    class_structure.tuple_mainxrange = tuple_mainxrange
    class_structure.tuple_postxrange = tuple_postxrange
    class_structure.str_datfile = str_datfile

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
