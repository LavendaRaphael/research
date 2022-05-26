from matplotlib import pyplot as plt
import numpy as np
import os

# env
str_homedir = os.environ['homedir']

# setup

array_id = np.array([1600000,2000000])

# data
list2d_dirdata = []
#'''
list2d_dirdata.append( [ '../../validation_test/struc49000_4md/iter.000000/01.model_devi/task.000.000000', 'Steps 1e6' ] )
list2d_dirdata.append( [ '', 'Steps 8e6' ] )
str_filesaveinsert = 'steps'
#'''
'''
list2d_dirdata.append( [ 'validation_49000_4pb/iter.000000/01.model_devi/task.000.000000', '49000' ] )
list2d_dirdata.append( [ 'validation_0/iter.000000/01.model_devi/task.000.000000', '0' ] )
str_filesaveinsert = 'init'
#'''
'''
list2d_dirdata.append( [ 'validation_49000_4pb/iter.000000/01.model_devi/task.000.000000', 'taut 0.05' ] )
list2d_dirdata.append( [ 'validation_49000_taut0.1/iter.000000/01.model_devi/task.000.000000', 'taut 0.1' ] )
str_filesaveinsert = 'taut'
#'''
'''
list2d_dirdata.append( [ 'task.000.000000', '0' ] )
list2d_dirdata.append( [ 'task.001.000000', '1' ] )
list2d_dirdata.append( [ 'task.002.000000', '3' ] )
list2d_dirdata.append( [ 'task.003.000000', '4' ] )
str_filesaveinsert = 'model'
#'''

# ref

'''
tuple_elements = ('O','O')
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_a.csv')
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)

'''
tuple_elements = ('O','H')
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
    return f'rdf.compare_{str_filesaveinsert}.{tuple_elements[0]}_{tuple_elements[1]}.{array_id[0]:07d}_{array_id[-1]:07d}.pdf'

fig, ax = plt.subplots()

str_filerdf = gen_filename(
    tuple_elements = tuple_elements,
    array_id = array_id,
    )
str_filesave = gen_filesave(
    tuple_elements = tuple_elements,
    array_id = array_id,
    )

for list_dirdata in list2d_dirdata:
    array_rdf = np.load( os.path.join(list_dirdata[0], str_filerdf) )
    ax.plot(
        array_rdf[0], 
        array_rdf[1], 
        label = list_dirdata[1],
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

