from matplotlib import pyplot as plt
import numpy as np
import os

# env
str_homedir = os.environ['homedir']

# setup

array_id = np.array([1600000,2000040])

#'''
tuple_elements = ('O','O')
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_a.csv')
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)

'''
tuple_elements = (8,1)
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_b.csv')
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)
#'''

# common

def gen_filename(
        tuple_elements,
        array_id,
        ):
    return f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.npy'
def gen_filesave(
        tuple_elements,
        array_id,
        ):
    return f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.pdf'

fig, ax = plt.subplots()

str_filerdf = gen_filename(
    tuple_elements = tuple_elements,
    array_id = array_id,
    )
str_filesave = gen_filesave(
    tuple_elements = tuple_elements,
    array_id = array_id,
    )

array_rdf = np.load(str_filerdf)
ax.plot(
    array_rdf[0], 
    array_rdf[1], 
    label = 'Mine',
    )

array_ref = np.genfromtxt(
    fname = str_fileref,
    delimiter = ',',
    )
ax.plot(
    array_ref[:,0], 
    array_ref[:,1], 
    label = 'Ref',
    marker='o', 
    linestyle = '',
    markersize=2
    )

ax.legend()
ax.set_xlabel('r (Å)')
ax.set_ylabel(str_ylabel)
ax.set_xlim(tuple_xlim)
ax.set_ylim(tuple_ylim)
fig. set_size_inches(8, 4)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

