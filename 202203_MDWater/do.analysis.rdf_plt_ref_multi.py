from matplotlib import pyplot as plt
import numpy as np
import os
import matplotlib.colors as mcolors
import matplotlib

matplotlib.rcParams['font.size']=15
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]
list1d_color = list(mcolors.TABLEAU_COLORS)

# env
str_homedir = os.environ['homedir']

# setup

array_id = np.arange(1600000,2000040,40)

#'''
list2d_data = []
list2d_data.append([
    (8,8),
    'O-O',
    os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_a.csv'),
    list1d_color[0]
    ])
list2d_data.append([
    (8,1),
    'O-H',
    os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_b.csv'),
    list1d_color[1]
    ])

# common

def gen_filename(
        tuple_elements,
        array_id,
        ):
    return f'rdf.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.npy'
def gen_filesave(
        array_id,
        ):
    return f'rdf.{array_id[0]:07d}_{array_id[-1]:07d}.pdf'

fig, ax = plt.subplots()

for list_data in list2d_data:
    str_filerdf = gen_filename(
        tuple_elements = list_data[0],
        array_id = array_id,
        )
    array_rdf = np.load(str_filerdf)
    ax.plot(
        array_rdf[0], 
        array_rdf[1], 
        label = 'DPMD '+list_data[1],
        color = list_data[3]
        )
for list_data in list2d_data:
    array_ref = np.genfromtxt(
        fname = list_data[2],
        delimiter = ',',
        )
    ax.plot(
        array_ref[:,0], 
        array_ref[:,1], 
        label = 'Ref '+list_data[1],
        marker='o',
        mfc = 'none',
        linestyle = '',
        markersize=3,
        color = list_data[3]
        )
str_filesave = gen_filesave(
    array_id = array_id,
    )

ax.legend()
ax.set_xlabel('r [Å]')
ax.set_ylabel('RDF g(r)')
ax.set_xlim((0,6))
ax.set_ylim((0,3))
fig. set_size_inches(8, 4)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

