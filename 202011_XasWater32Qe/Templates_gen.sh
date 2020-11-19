#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh
source ~/codes/202011_XasWater32Qe/local_env.sh

cat > scf.in <<eof
#
&control
  calculation   = 'scf',
  restart_mode  = 'from_scratch',
  prefix        = "water",
  wf_collect    = .TRUE.,
  pseudo_dir    = "${pseudo_dir}"
  outdir        = "./temp"
  tprnfor       = .TRUE.
/
&system
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  ecutwfc       = 71.D0,
  nosym         = .true.,
  nbnd          = $vbands,
  tot_charge    = 1,
/
&electrons
  diagonalization  =  'david',
  mixing_mode      =  'plain',
  mixing_beta      =  0.7,
  mixing_ndim      =  8,
  conv_thr         =  1.0d-6,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

K_POINTS {Gamma}

ATOMIC_POSITIONS {bohr}
eof
cat > cp-scf.in <<eof
#
&CONTROL
  calculation   = "cp-wf",
  restart_mode  = 'restart',
  nstep         = 1,
  iprint        = 1,
  isave         = 1,
  dt            = 6.D0,
  etot_conv_thr = 1.D-6,
  ekin_conv_thr = 5.D-5,
  max_seconds   = 3000,
  prefix        = "water"
  pseudo_dir    = "${pseudo_dir}"
  outdir        = "./temp"
/
&SYSTEM
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  nbnd          = $vbands,
  ecutwfc       = 71.D0,
  tot_charge    = +1,
/
&ELECTRONS
  emass             = 400.D0,
  emass_cutoff      = 3.D0,
  ortho_eps         = 1.D-8,
  ortho_max         = 300,
  electron_dynamics = "damp",
  electron_damping  = 0.15,
/
&IONS
  ion_dynamics = "none",
/
&WANNIER
  nit    =  100,
  calwf  =  4,
  tolw   =  5.D-4,
  adapt  =  .false.,
  wfdt   =  2.D0,
  wf_q   =  500,
  wf_friction = 0.3d0,
  nsteps =  4000,
  poisson_eps = 1.D-5,
  dis_cutoff  = 7.0,
  exx_ps_rcut = 5.0,
  exx_me_rcut = 10.0,
  neigh = 50,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

ATOMIC_POSITIONS {bohr}
eof
cat > nscf.in <<eof
#
&control
  calculation   = 'nscf',
  restart_mode  = 'from_scratch',
  wf_collect    = .TRUE.
  prefix        = "water"
  pseudo_dir    = "${pseudo_dir}"
  outdir        = "./temp"
/
&system
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  ecutwfc       = 71.D0,
  nbnd          = $nbands,
  nosym         = .true.,
  tot_charge    = 1,
/
&electrons
  diagonalization  = 'david',
  mixing_mode      = 'plain',
  mixing_beta      = 0.7 ,
  mixing_ndim      = 8 ,
  conv_thr         = 1.0d-6,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

ATOMIC_POSITIONS {bohr}
eof
cat > cp-nscf.in <<eof
#
&CONTROL
  calculation   = "cp-wf-nscf",
  restart_mode  = 'restart',
  nstep         = 1,
  iprint        = 1,
  isave         = 1,
  dt            = 6.D0,
  etot_conv_thr = 1.D-6,
  ekin_conv_thr = 5.D-5,
  max_seconds   = 1700,
  prefix        = "water"
  pseudo_dir    = "${pseudo_dir}"
  outdir        = "./temp"
/
&SYSTEM
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  nbnd          = $nbands
  ecutwfc       = 71.D0
  tot_charge    = +1,
/
&ELECTRONS
  emass             = 400.D0,
  emass_cutoff      = 3.D0,
  ortho_eps         = 1.D-8,
  ortho_max         = 300,
  electron_dynamics = "verlet",
/
&IONS
  ion_dynamics = "none",
/
&WANNIER
  nit    =  100,
  calwf  =  4,
  tolw   =  5.D-4,
  adapt  =  .false.,
  wfdt   =  2.D0,
  wf_q   =  500,
  wf_friction = 0.3d0,
  nsteps =  2000,
  poisson_eps = 1.D-5,
  dis_cutoff  = 7.0,
  exx_ps_rcut = 5.0,
  exx_me_rcut = 10.0,
  neigh = 50,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

ATOMIC_POSITIONS {bohr}
eof
cat > cp-nscf-wf.in <<eof
#
&CONTROL
  calculation   = "cp-wf-nscf",
  restart_mode  = 'restart',
  nstep         = 1,
  iprint        = 1,
  isave         = 1,
  dt            = 6.D0,
  etot_conv_thr = 1.D-6,
  ekin_conv_thr = 5.D-5,
  max_seconds   = 1700,
  prefix        = "water"
  pseudo_dir    = "${pseudo_dir}" 
  outdir        = "./temp"
/
&SYSTEM
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  nbnd          = $nbands
  ecutwfc       = 71.D0
  tot_charge    = +1,
/
&ELECTRONS
  emass             = 400.D0,
  emass_cutoff      = 3.D0,
  ortho_eps         = 1.D-8,
  ortho_max         = 300,
  electron_dynamics = "verlet",
/
&IONS
  ion_dynamics = "none",
/
&WANNIER
  nit    =  100,
  calwf  =  4,
  tolw   =  5.D-4,
  adapt  =  .false.,
  wfdt   =  2.D0,
  wf_q   =  500,
  wf_friction = 0.3d0,
  nsteps =  1,
  poisson_eps = 1.D-5,
  dis_cutoff  = 7.0,
  exx_ps_rcut = 5.0,
  exx_me_rcut = 10.0,
  neigh = 50,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

ATOMIC_POSITIONS {bohr}
eof
cat > gw.in <<eof
#
&CONTROL
  calculation   = 'cohsex',
  restart_mode  = 'restart',
  nstep         = 1,
  iprint        = 1,
  isave         = 1,
  dt            = 0.1D0,
  etot_conv_thr = 1.D-6,
  ekin_conv_thr = 5.D-5,
  prefix        = "water",
  pseudo_dir    = "${pseudo_dir}" 
  outdir        = "./temp",
/
&SYSTEM
  ibrav          = 1,
  celldm(1)      = ${celldm1},
  nat           = $natoms,
  ntyp          = 3,
  nbnd          = $nbands, 
  ecutwfc       = 71.D0,
  tot_charge    = +1,
/
&ELECTRONS
  emass             = 400.D0,
  emass_cutoff      = 3.D0,
  ortho_eps         = 1.D-8,
  ortho_max         = 800,
  electron_dynamics = "damp",
  electron_damping  = 0.15,
/
&IONS
  ion_dynamics = "none",
/
&WANNIER
  nit         = 100,
  calwf       = 3,
  tolw        = 5.D-6,
  adapt       = .false.,
  wfdt        = 2.D0,
  wf_q        = 500,
  wf_friction = 0.3d0,
  nsteps      = 10,
  poisson_eps = 1.D-5,
  dis_cutoff  = 7.0,
  exx_ps_rcut = 5.0,
  exx_me_rcut = 9.0,
  neigh       = 60,
  vnbsp       = $vbands,
/
ATOMIC_SPECIES
OO 15.9994  o+.pbe.tm.ncpp.rcut1.1.upf
O  15.9994  O.pbe-mt.UPF
H  2.01355  H_MT_PBE.UPF 

ATOMIC_POSITIONS {bohr}
eof
cat > fort.10 <<eof
${volume}, ${celldm1}, 1.0, 1.0
${glines}, ${vbands}, ${cbands}
0.0, 0.0, 0.0
eof
cat > fort.11 <<eof
$nbands,  $vbands, ${glines} 
eof
cat > fort.12 <<eof
0.4, ${cbands}
eof
