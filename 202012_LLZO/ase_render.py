#!/user/bin/env python
from ase.visualize import view
from ase.io import read,write
import sys
import os

cont=read(str(sys.argv[1]))

generic_projection_settings = {
    'show_unit_cell': 2,
    'rotation': '90y',
}

povray_settings={
    'textures': ['simple',]*1000,
}
renderer=write('render.pov',cont,
    **generic_projection_settings,
    povray_settings=povray_settings)
renderer.render()

os.remove('render.ini')
os.remove('render.pov')
