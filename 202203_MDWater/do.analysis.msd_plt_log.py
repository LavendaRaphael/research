from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import linregress
from matplotlib import pyplot as plt
import matplotlib 

# setup

tup_id = (400000, 2000000)

# common
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['font.family']='sans-serif'
matplotlib.rcParams['font.sans-serif']=["Arial"]

fig, ax = plt.subplots()

def gen_filenpy(
        tup_id,
        ):
    return f'msd.{tup_id[0]:07d}_{tup_id[-1]:07d}.npy'
str_filenpy = gen_filenpy(
    tup_id = tup_id,
    )

def gen_filesave(
        tup_id,
        ):
    return f'msd.{tup_id[0]:07d}_{tup_id[-1]:07d}.pdf'
str_filesave = gen_filesave(
    tup_id = tup_id,
    )

array_data = np.load(str_filenpy)
ax.loglog( array_data[0], array_data[1], label = 'MSD')
#ax.loglog( array_rdf[0], array_rdf[1] )

np_time = np.array([200,600])
np_index = np.array( np_time / (array_data[0][1]-array_data[0][0]), dtype=int )
np_x = array_data[0][ np_index[0]: np_index[1] ]
np_y = array_data[1][ np_index[0]: np_index[1] ]
linear_model = linregress( np_x, np_y )
float_diffussioncoef = linear_model.slope / 6.0
ax.loglog( np_x, linear_model.intercept + linear_model.slope*np_x , '--', label = f'D = {float_diffussioncoef:.3f} Å$^2$/ps')

ax.legend()
ax.set_xlabel('t (ps)')
ax.set_ylabel('Mean Square Displacement (Å$^2$)')
ax.set_xlim(None)
ax.set_ylim(None)
fig.set_size_inches(8, 8)
plt.savefig(str_filesave, bbox_inches='tight')
plt.show()

