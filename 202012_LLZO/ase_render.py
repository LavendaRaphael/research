#!/user/bin/env python
from ase.visualize import view
from ase.io import read,write
import sys
import os

cont=read(str(sys.argv[1]))
cell=cont.cell
cont=cont*(1,1,1)
cont.cell=cell

generic_projection_settings = {
    'show_unit_cell': 2,
    'rotation': '90y',
#    'rotation': '90x,90z'
#    'rotation': '10x,-10y'
#    'rotation': '-72x'
}

povray_settings={
    'textures': ['simple',]*1000,
#    'canvas_width': 500,
    'canvas_height': 500,
    'celllinewidth': 0.03
}
renderer=write('render.pov',cont,
    **generic_projection_settings,
    povray_settings=povray_settings)
renderer.render()

os.remove('render.ini')
os.remove('render.pov')
