#!/user/bin/env python

def def_render(tup_bbox, str_poscar):
    dict_args = locals()
    import json
    from ase.io import read,write
    import sys
    import os

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
