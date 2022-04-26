from matplotlib import pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots()
str_homedir = os.environ['homedir']

list2d_filerdf = []
list2d_filerdf.append(['rdf.8_8.0_200000.npy',     '0-100ps'])
list2d_filerdf.append(['rdf.8_8.200000_400000.npy','100-200ps'])
list2d_filerdf.append(['rdf.8_8.400000_600000.npy','200-300ps'])
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)
'''
str_filerdf = 'rdf.8_1.npy'
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)
'''
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
#plt.savefig('rdf.pdf', bbox_inches='tight')
plt.show()

