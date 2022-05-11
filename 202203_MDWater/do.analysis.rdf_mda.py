import MDAnalysis as mda
from MDAnalysis.analysis.rdf import InterRDF
import numpy as np

# setup
int_nbins = 200
tuple_type = (1,1)
int_step = 40
npint_id = np.array([1600000, 2000000])
float_dt = 0.0005

# common
npint_index = np.array(npint_id/int_step, dtype=int)
mda_universe = mda.Universe('traj.dump', format="LAMMPSDUMP", dt=float_dt)
print(mda_universe.trajectory)
mda_atomgroup_1 = mda_universe.select_atoms("type 1")
mda_atomgroup_2 = mda_universe.select_atoms("type 1")
mda_rdf = InterRDF( 
    mda_atomgroup_1, 
    mda_atomgroup_2,
    nbins = int_nbins,
    range=(0.5, 6.0),
    )
mda_rdf.run(
    start = npint_index[0],
    stop = npint_index[1],
    verbose = True,
    )
array_final = np.empty( shape=(2,int_nbins) )
array_final[0] = mda_rdf.results.bins
array_final[1] = mda_rdf.results.rdf

def gen_filenpy(
        tuple_type,
        npint_id,
        ):
    return f'rdf.{tuple_type[0]}_{tuple_type[1]}.{npint_id[0]:07d}_{npint_id[-1]:07d}.npy'
str_filenpy = gen_filenpy(
    tuple_type = tuple_type,
    npint_id = npint_id,
    )

np.save(
    file = str_filenpy,
    arr = array_final,
    )

