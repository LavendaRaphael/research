from matplotlib import pyplot as plt
import numpy as np
import os

# setup

fig, ax = plt.subplots()

str_npy_0 = '../../../../validation_49000_4pb/iter.000000/01.model_devi/task.000.000000/rdf.8_8.1600000_2000000.npy'
str_npy_1 = 'rdf.1_1.1600000_2000000.npy'

array_rdf = np.load(str_npy_0)
ax.plot(
    array_rdf[0], 
    array_rdf[1], 
    label = 'RDF_ASE',
    )

array_rdf = np.load(str_npy_1)
ax.plot(
    array_rdf[0], 
    array_rdf[1], 
    label = 'RDF_MDA',
    )

ax.legend()
ax.set_xlabel('r (Å)')
ax.set_ylabel('RDF')
ax.set_xlim((0,6))
ax.set_ylim(None)
fig.set_size_inches(8, 4)
plt.show()

