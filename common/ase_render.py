#!/user/bin/env python
from ase.visualize import view
from ase.io import read,write
import sys

cont=read(str(sys.argv[1]))
cont=cont*(3,3,1)

ax=7.934514/2.0
ay=2.80527433

r = [{'O': 0.74, 'Pt': 1.39}[at.symbol] for at in cont]

nx1=1
ny1=5
nx2=nx1+2
ny2=ny1+6

generic_projection_settings = {
    'bbox':(ax*nx1, ay*ny1, ax*nx2, ay*ny2),
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
