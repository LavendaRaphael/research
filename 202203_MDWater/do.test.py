from matplotlib import pyplot as plt
import numpy as np
import os

# setup

fig, ax = plt.subplots()

str_npy_0 = 'rdf.1_1.1600000_2000000.npy'
str_npy_1 = 'rdf.O_O.1600000_2000000.npy'

array_rdf = np.load(str_npy_0)
ax.plot(
    array_rdf[0], 
    array_rdf[1],
    marker='o',
    mfc = 'none',
    linestyle = '',
    markersize=3,
    label = '0',
    )

array_rdf = np.load(str_npy_1)
print(array_rdf)
ax.plot(
    array_rdf[0], 
    array_rdf[1], 
    label = '1',
    )

ax.legend()
ax.set_xlabel('r (Å)')
ax.set_ylabel('RDF')
ax.set_xlim(None)
ax.set_ylim(None)
fig.set_size_inches(8, 4)
plt.show()

