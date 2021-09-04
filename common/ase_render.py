#!/user/bin/env python
from ase.visualize import view
from ase.io import read,write
import sys
sys.path.append(r'./')
from render_in import render_in
import os
import shutil

cont=read(str(sys.argv[1]))
cont=cont*(3,3,1)

r = [{'O': 0.74, 'Pt': 1.39}[at.symbol] for at in cont]

generic_projection_settings = {
    'bbox':(render_in.x1, render_in.y1, render_in.x2, render_in.y2),
    'show_unit_cell': 2,
    'radii': r,
}

povray_settings={
    'camera_dist': 50.,
}
renderer=write('render.pov',cont,
    **generic_projection_settings,
    povray_settings=povray_settings)
renderer.render()

os.remove('render.ini')
os.remove('render.pov')
shutil.rmtree('__pycache__')
