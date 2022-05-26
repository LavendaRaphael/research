import MDAnalysis as mda
from MDAnalysis.analysis.rdf import InterRDF

mda_universe = mda.Universe('traj.pdb', format="PDB", dt=0.0005)
print(mda_universe.trajectory)
mda_atomgroup_1 = mda_universe.select_atoms("element O")
mda_atomgroup_2 = mda_universe.select_atoms("element O")
mda_rdf = InterRDF(
    mda_atomgroup_1,
    mda_atomgroup_2,
    nbins = 200,
    range=(0.5, 6.0),
    )
mda_rdf.run(
    start = 0,
    stop = 100,
    verbose = True,
    )
print(mda_rdf.results.bins)
print(mda_rdf.results.rdf)
