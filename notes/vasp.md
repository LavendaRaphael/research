
# INCAR


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [INCAR](#incar)
  - [usual](#usual)
  - [gas](#gas)
  - [parchg](#parchg)
  - [vdw](#vdw)
  - [AIMD](#aimd)
  - [spin](#spin)
  - [dipole](#dipole)
- [POSCAR](#poscar)
- [AIMD](#aimd-1)
  - [初始速度](#初始速度)
  - [SMASS](#smass)
- [POTCAR](#potcar)
- [KPOINTS](#kpoints)
  - [ka](#ka)
  - [KSPACING/(2$\pi$)](#kspacing2pi)
  - [KSPACING](#kspacing)
- [STOPCAR](#stopcar)
- [Compile](#compile)
  - [mpi+omp混编](#mpiomp混编)
- [vtst](#vtst)
  - [vasp6.1兼容性](#vasp61兼容性)
  - [安装](#安装)
- [ERROR](#error)
  - [wavefunction orthogonal band](#wavefunction-orthogonal-band)
  - [PMPI_Allreduce: Invalid communicator](#pmpi_allreduce-invalid-communicator)
  - [EDDDAV: Call to ZHEGV failed](#edddav-call-to-zhegv-failed)
  - [segmentation fault](#segmentation-fault)
  - [EDDRMM: call to ZHEGV failed](#eddrmm-call-to-zhegv-failed)
- [杂项](#杂项)
  - [CRLF&LF](#crlflf)

<!-- /code_chunk_output -->

## usual

```sh
#-------------------------[common]
# ISTART = 0
  NCORE = 16
# PREC = Normal # default
  PREC = Accurate
# LREAL = .FALSE. # default
  LREAL = Auto
  ENCUT = 500
# ENCUT = 800 # volume opt

#-------------------------[electron]
# ISMEAR = 1        # default, for metal, Methfessel-Paxton smearing order N
# SIGMA = 0.2       # default
  ISMEAR = 0        # Gaussian smearing
  SIGMA = 0.05
# ALGO = Normal     # default, DAV
  ALGO = Fast       # DAV + RMM
# ALGO = VeryFast   # RMM
# ALGO = Damped
# ALGO = All        # CG
# NELM = 60         # default
  NELM = 500
# EDIFF = 1.0E-4    # default
  EDIFF = 1.0E-5

#-------------------------[ionic]
# NSW = 0           # default
  NSW = 500
# IBRION = 0        # default, MD
# IBRION = 1        # quasi-Newton
  IBRION = 2        # CG
# EDIFFG = EDIFF×10 # default
# EDIFFG = -0.02
  EDIFFG = -0.01
# ISIF = 2          # default, atom position
# ISIF = 3          # volume
# IOPTCELL =  1 0 0 1 1 0 1 1 1   # 0=fix, 1=relax

#-------------------------[file]
# LWAVE = .TRUE.    # default
  LWAVE = .FALSE.   # WAVECAR not write
# LCHARG = .TRUE.   # default
  LCHARG = .FALSE.  # CHAGCAR not write

#-------------------------[kpoints]
# KSPACING = 0.5    # default
  KSPACING = 0.25   # ang^-1, KSPACING/2pi ~ 0.4 ang^-1, 2pi/KSPACING ~ 25 ang (25.1327412287)
# KGAMMA = .TRUE.   # default
```

## gas

```sh
#-------------------------[common]
# ISTART = 0
  NPAR = 2
# PREC = Normal # default
  PREC = Accurate
# LREAL = .FALSE. # default
  ENCUT = 1500

#-------------------------[electron]
# ISMEAR = 1        # default, for metal, Methfessel-Paxton smearing order N
# SIGMA = 0.2       # default
  ISMEAR = 0        # Gaussian smearing
  SIGMA = 0.01

# ALGO = Normal     # default, DAV
# ALGO = Fast       # DAV + RMM
# ALGO = VeryFast   # RMM
# ALGO = Damped
  ALGO = All        # CG

# NELM = 60         # default
  NELM = 500
# EDIFF = 1.0E-4    # default
  EDIFF = 1.0E-6

#-------------------------[spin]
# ISPIN = 1         # default
  ISPIN = 2
# MAGMOM = NIONS * 1.0 # default
  MAGMOM = 1000*0
# LORBIT = None     # default
  LORBIT = 11       # mag per atom output

#-------------------------[SCAN]
  METAGGA = SCAN
  LASPH =.TRUE.

#-------------------------[ionic]
# NSW = 0           # default
  NSW = 500
# IBRION = 0        # default, MD
# IBRION = 1        # quasi-Newton
  IBRION = 2        # CG

# EDIFFG = EDIFF×10 # default
  EDIFFG = -0.01
# ISIF = 2          # default, atom position

#-------------------------[file]
# LWAVE = .TRUE.    # default
  LWAVE = .FALSE.   # WAVECAR not write
# LCHARG = .TRUE.   # default
  LCHARG = .FALSE.  # CHAGCAR not write
```

POSCAR

```poscar
20 0 0
0 21 0
0 0 22
```

## parchg

```sh
  LPARD = .TRUE.
  NGXF = 240
  NGYF = 1000
  NGZF = 800
#  ENCUT = 2600  # ~ 0.03 ang
#----------------------------[KB]
  IBAND = 271
  KPUSE = 6
  LSEPB = .TRUE.
  LSEPK = .TRUE.
#-----------------------------[EINT]
  EINT = 3.1939 4.19390
  NBMOD = -2
```

<https://www.vasp.at/wiki/index.php/Band_decomposed_charge_densities>

## vdw

```sh
#-------------------------[DFT-D]
# IVDW=0            # default, no correction
# IVDW=11           # zero damping DFT-D3 method of Grimme (available as of VASP.5.3.4)
# IVDW=12           # DFT-D3 method with Becke-Jonson damping (available as of VASP.5.3.4)
# IVDW=13           # DFT-D4 method (available as of VASP.6.2 as external package).
#-------------------------[optB88-vdW]
 GGA = BO
 PARAM1 = 0.1833333333
 PARAM2 = 0.2200000000
 LUSE_VDW = .TRUE.
 AGGAC = 0.0000
 LASPH = .TRUE.
```

## AIMD

```sh
# IBRION = 0        # default, MD
# MDALGO = 0        # default, standard
  MDALGO = 2        # Nose-Hoover
# ISIF = 0          # default for IBRION=0, stress tensor not cal
  SMASS = 0         # temperature oscillation
  POTIM = 0.5       # fs
  NSW = 2000
  ISYM = 0
  TEBEG = 473
  IWAVPR = 11
```

## spin

```sh
# ISPIN = 1         # default
# ISPIN = 2
# MAGMOM = NIONS * 1.0 # default
# MAGMOM = 1000*0
# LORBIT = None     # default
# LORBIT = 11       # mag per atom output
```

## dipole

```sh
# LDIPOLE = .TRUE.  # slibe dipole correction
# IDIPOLE = 3       # z direction
```

# POSCAR

删除 POSCAR 中初始速度，预测坐标

# AIMD

## 初始速度

删除 POSCAR 中初始速度

## SMASS

<http://bbs.keinsci.com/thread-15872-1-1.html>

<https://www.vasp.at/forum/viewtopic.php?f=4&t=10860&p=13886&hilit=smass+value#p13886>

# POTCAR

<https://www.vasp.at/wiki/index.php/Available_PAW_potentials>

# KPOINTS

## ka

- k*a ~ 30 Å, for d band metals
- k*a ~ 25 Å, for simple metals
- k*a ~ 20 Å, for semiconductors
- k*a ~ 15 Å, for insulators

<https://www.bigbrosci.com/2017/12/10/ex18/>

<https://wiki.fysik.dtu.dk/gpaw/exercises/surface/surface.html>

## KSPACING/(2$\pi$)

- Low: 0.06~0.04;
- Medium: 0.04~0.03;
- Fine: 0.02-0.01.

<https://vaspkit.com/tutorials.html#generate-kpoints>

## KSPACING

```sh
KSPACING=0.25 # ang^-1
```

```math
KSPACING = \frac{2\pi}{ak}
```

- KSPACING = 0.25
- KSPACING/(2$\pi$) $\approx$ 0.04
- k\*a = 2$\pi$/KSPACING = 25.1327412287

<https://www.vasp.at/wiki/index.php/KSPACING>

# STOPCAR

```sh
LSTOP = .TRUE.
```

# Compile

## mpi+omp混编

<http://bbs.keinsci.com/thread-16191-1-1.html>

<https://www.vasp.at/wiki/index.php/Hybrid_MPI/OpenMP_parallelization>

# vtst

## vasp6.1兼容性

<http://henkelmanlab.org/forum/viewtopic.php?t=10916>

## 安装

<http://hmli.ustc.edu.cn/doc/app/vasp.5.4.1-vtst.htm>

# ERROR

## wavefunction orthogonal band

```
Information: wavefunction orthogonal band  107  0.8718
```

```sh
 IWAVPR = 11
```

<https://www.vasp.at/forum/viewtopic.php?f=3&t=3561>

## PMPI_Allreduce: Invalid communicator

```
Abort(537470981) on node 71 (rank 71 in comm 0): Fatal error in PMPI_Allreduce: Invalid communicator, error stack:
PMPI_Allreduce(454): MPI_Allreduce(sbuf=0x7fffe380a628, rbuf=0xc56a238, count=1, datatype=MPI_INT, op=op=0x98000001, comm=comm=0x3bffffec) failed
PMPI_Allreduce(375): Invalid communicator
```

```sh
  AMIX = 0.01
  ALGO = All 
  MAGMOM = 1000*0
```

<https://www.vasp.at/forum/viewtopic.php?f=4&t=18071>

## EDDDAV: Call to ZHEGV failed

```
Sub-Space-Matrix
Error EDDDAV: Call to ZHEGV failed. Returncode
```

```sh
module add mathlib/lapack/intel/3.8.0
```

<https://www.vasp.at/forum/viewtopic.php?f=2&t=10409&p=19151&hilit=Returncode+%3D+8+1+8#p19151>

## segmentation fault

```
forrtl: severe (174): SIGSEGV, segmentation fault occurred
```

```sh
ulimit -s unlimited
```

<https://www.vasp.at/forum/viewtopic.php?t=17257&p=18513>

## EDDRMM: call to ZHEGV failed

```
WARNING in EDDRMM: call to ZHEGV failed, returncode =   6  3     68
{    0,    0}:  On entry to
PDSTEIN parameter number    4 had an illegal value
```

编译问题，换用服务器提供vasp版本，换编译器
RMM 改成 DAV 算法
调整slab层间距
换不同ALGO
重试一次

# 杂项

## CRLF&LF

注意 POSCAR 格式转换 dos or unix
