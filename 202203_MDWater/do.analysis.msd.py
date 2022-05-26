import MDAnalysis as mda
import MDAnalysis.analysis.msd as msd
import numpy as np

int_step = 40
npint_id = np.array([400000, 2000000])
float_dt = 0.0005

mda_universe = mda.Universe('traj.dump', format="LAMMPSDUMP", dt=float_dt)
mda_universe.select_atoms("type 1").types = 'O'
mda_universe.select_atoms("type 2").types = 'H'
print(mda_universe.trajectory)

mda_msd = msd.EinsteinMSD(
    u = mda_universe,
    select = 'type O'
    )
npint_index = np.array(npint_id/int_step, dtype=int)
print(npint_index)
mda_msd.run(
    start = npint_index[0],
    stop = npint_index[1],
    verbose = True,
    )

int_nframes = mda_msd.n_frames
npfloat_lagtimes = np.arange(int_nframes)*float_dt*int_step # make the lag-time axis

array_final = np.empty( shape=(2,int_nframes) )
array_final[0] = npfloat_lagtimes
array_final[1] = mda_msd.results.timeseries
def gen_filename(
        npint_id,
        ):
    return f'msd.{npint_id[0]:07d}_{npint_id[-1]:07d}.npy'
str_filenpy = gen_filename(
    npint_id = npint_id,
    )
np.save(
    file = str_filenpy,
    arr = array_final,
    )

