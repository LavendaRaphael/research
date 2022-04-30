from matplotlib import pyplot as plt
import numpy as np
import os

# setup

#'''
tuple_elements = (8,8)
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)
'''
tuple_elements = (8,1)
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)
'''

list_array_id = []
list_array_id.append(np.arange( 000000, 400040,40))
list_array_id.append(np.arange( 400000, 800040,40))
list_array_id.append(np.arange( 800000,1200040,40))
list_array_id.append(np.arange(1200000,1600040,40))
list_array_id.append(np.arange(1600000,2000040,40))

# common
str_homedir = os.environ['homedir']
float_timestep = 0.0005

def gen_filesave(
        tuple_elements,
        ):
    return f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.converge.pdf'
def gen_filename(
        tuple_elements,
        array_id,
        ):
    return f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.npy'
def gen_label(
        float_timestep,
        array_id,
        ):
    int_start = int(array_id[0]*float_timestep)
    int_end = int(array_id[-1]*float_timestep)
    return f'{int_start}-{int_end}ps'

fig, ax = plt.subplots()
for array_id in list_array_id:
    str_filerdf = gen_filename(
        tuple_elements = tuple_elements,
        array_id = array_id,
        )
    array_rdf = np.load( str_filerdf )
    str_label = gen_label(
        float_timestep = float_timestep,
        array_id = array_id,
        )
    ax.plot(
        array_rdf[0], 
        array_rdf[1], 
        label = str_label,
        )

str_filesave = gen_filesave(
    tuple_elements = tuple_elements,
    )

ax.legend()
ax.set_xlabel('r (Å)')
ax.set_ylabel(str_ylabel)
ax.set_xlim(tuple_xlim)
ax.set_ylim(tuple_ylim)
fig. set_size_inches(8, 4)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

