from matplotlib import pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots()
str_homedir = os.environ['homedir']

#str_step = '1600000_2000000'
str_step = '0400000_0600000'

'''
str_el = '8_8'
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_a.csv')
str_ylabel = r'$g_{\mathrm{OO}}$ (r)'
tuple_xlim = (2,6)
tuple_ylim = (0,3)

'''
str_el = '8_1'
str_fileref = os.path.join(str_homedir,'research/202112_MDMisc/record/ref/2022_naturecom_xifanwu/sf3_b.csv')
str_ylabel = r'$g_{\mathrm{OH}}$ (r)'
tuple_xlim = (0.5,4.5)
tuple_ylim = (0,2)

str_filerdf = 'rdf.'+str_el+'.'+str_step+'.npy'
str_filesave = 'rdf.'+str_el+'.'+str_step+'.pdf'

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
fig. set_size_inches(8, 4)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

