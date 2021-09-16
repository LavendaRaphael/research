#!/user/bin/env python
from ase.visualize import view
from ase.io import read,write
from ase import Atoms
import sys
import os

filename='render'

fdist=7.0
posz=0.0
array_atom=['Li','C','O','La','Zr','Au','Zn','Al','Mo','S']
cont=Atoms()
for latom in array_atom:
    cont.extend(Atoms(latom, positions=[(0,0,posz)]))
    posz+=fdist

cont=read(str(sys.argv[1]))
cell=cont.cell
cont=cont*(1,1,1)
cont.cell=cell

generic_projection_settings = {
#    'rotation': '90y',
    'rotation': '90x,90z',
#   'rotation': '-90x,-90z',
#   'rotation': '-90y,180z',
#   'rotation': '10x,-10y',
#   'rotation': '-72x',
    'radii': .85,  # float, or a list with one float per atom
    'colors': None,  # List: one (r, g, b) tuple per atom
    'show_unit_cell': 0,   # 0, 1, or 2 to not show, show, and show all of cell
}

povray_settings={
#   'display': False,  # Display while rendering
#   'pause': True,  # Pause when done rendering (only if display)
#   'transparent': False,  # Transparent background
#   'canvas_width': None,  # Width of canvas in pixels
#    'canvas_height': 1000,  # Height of canvas in pixels
    'canvas_height': 500,  # Height of canvas in pixels
#   'camera_dist': 50.,  # Distance from camera to front atom
#   'image_plane': None,  # Distance from front atom to image plane
    'camera_type': 'perspective',  # orthographic, perspective, ultra_wide_angle
    'point_lights': [],             # [[loc1, color1], [loc2, color2],...]
    'area_light': [(2., 3., 40.),  # location
                   'White',       # color
                   .7, .7, 3, 3],  # width, height, Nlamps_x, Nlamps_y
#   'background': 'White',        # color
    'textures': ['jmol',]*1000,  # ase2, ase3, glass, simple, pale, intermediate, vmd, jmol
#   'celllinewidth': 0.1,  # Radius of the cylinders representing the cell
}
renderer=write(filename+'.pov',cont,
    **generic_projection_settings,
    povray_settings=povray_settings)
renderer.render()

os.remove(filename+'.ini')
os.remove(filename+'.pov')
