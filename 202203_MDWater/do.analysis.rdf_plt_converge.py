from matplotlib import pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots()
str_homedir = os.environ['homedir']

#'''
str_el = '8_8'
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)
'''
str_el = '8_1'
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)
'''

list2d_filerdf = []
'''
list2d_filerdf.append(['rdf.'+str_el+'.0000000_0400000.npy','000-200ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0400000_0800000.npy','200-400ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0800000_1200000.npy','400-600ps'])
list2d_filerdf.append(['rdf.'+str_el+'.1200000_1600000.npy','600-800ps'])
list2d_filerdf.append(['rdf.'+str_el+'.1600000_2000000.npy','800-1000ps'])
'''
list2d_filerdf.append(['rdf.'+str_el+'.0000000_0200000.npy','000-100ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0200000_0400000.npy','100-200ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0400000_0600000.npy','200-300ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0600000_0800000.npy','300-400ps'])
list2d_filerdf.append(['rdf.'+str_el+'.0800000_1000000.npy','400-500ps'])

str_filesave = 'rdf.'+str_el+'.converge.pdf'

for list_filerdf in list2d_filerdf:
    array_rdf = np.load(list_filerdf[0])
    ax.plot(
        array_rdf[0], 
        array_rdf[1], 
        label = list_filerdf[1],
        )

ax.legend()
ax.set_xlabel('r (Å)')
ax.set_ylabel(str_ylabel)
ax.set_xlim(tuple_xlim)
ax.set_ylim(tuple_ylim)
fig. set_size_inches(8, 4)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

