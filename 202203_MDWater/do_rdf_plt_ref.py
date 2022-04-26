from matplotlib import pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots()
str_homedir = os.environ['homedir']

str_filerdf = 'rdf.8_8.200000_400000.npy'
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_a.csv')
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)
'''
str_filerdf = 'rdf.8_1.npy'
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_b.csv')
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)
'''
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
print(array_ref)
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
#plt.savefig('rdf.pdf', bbox_inches='tight')
plt.show()

