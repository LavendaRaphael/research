# QuantumEspresso

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [QuantumEspresso](#quantumespresso)
  - [`pw.in`](#pwin)
  - [xspectra](#xspectra)
  - [evc.dat](#evcdat)
  - [编译](#编译)
    - [cmake](#cmake)
    - [make](#make)
    - [老版本](#老版本)
  - [Libxc](#libxc)
    - [cmake](#cmake-1)
    - [make](#make-1)
    - [qe](#qe)
  - [收敛问题](#收敛问题)

<!-- /code_chunk_output -->

## `pw.in`

```in
&CONTROL
    ! calculation Default: 'scf'
    ! tstress  Default:  .false.
    tstress = .true.   ! calcute stress
    ! tprnfor  Default:  .false.
    tprnfor = .true.   ! calcute force
    ! pseudo_dir  Default:  value of the $ESPRESSO_PSEUDO environment variable if set; '$HOME/espresso/pseudo/' otherwise
    ! outdir  Default:  value of the ESPRESSO_TMPDIR environment variable if set; current directory ('./') otherwise
    ! disk_io  Default is 'low' for the scf case, 'medium' otherwise.
    disk_io = 'none'
/
&SYSTEM
    input_dft = 'scan'
    ecutwfc = 150
    ! nosym  Default:  .FALSE.
    nosym = .TRUE.
    ntyp  = 2
    nat   = 192
    ibrav = 0
/
&ELECTRONS
    ! conv_thr Default: 1.D-6
    ! electron_maxstep Default: 100
    electron_maxstep = 500
/
 
ATOMIC_SPECIES 
  O  15.9994  O_HSCV_PBE-1.0.UPF 
  H  2.01588  H_HSCV_PBE-1.0.UPF 

K_POINTS gamma

CELL_PARAMETERS angstrom

ATOMIC_POSITIONS angstrom
```

## xspectra

```in
&input_xspectra
    calculation='xanes_dipole'
    edge='K'
    prefix='pwscf',
    outdir='../outdir/',
    xiabs=1,
    xcoordcrys = .false.
    xepsilon(1)=0.0,
    xepsilon(2)=1.0,
    xepsilon(3)=0.0,
    xniter=2000
    xcheck_conv=50,
    xerror=0.001,
    x_save_file="xanes.save"
/
&plot
    xnepoint=3000,
    xemin=-10.0,
    xemax=30.0,
    xgamma=0.225,
    cut_occ_states=.true.,
/
&pseudos
    filecore='O.core.wfc',
/
&cut_occ
    cut_desmooth=0.1,
/
3 3 1 0 0 0
```

## evc.dat

6.2 不支持 evc.dat, 变为 wfc*.dat  
6.0 支持 evc.dat  
<https://lists.quantum-espresso.org/pipermail/users/2019-June/042996.html>

## 编译

### cmake

ref: lammps compile method

```sh
mkdir build; cd build
cmake -DCMAKE_C_COMPILER=icx -DCMAKE_Fortran_COMPILER=ifx -DCMAKE_INSTALL_PREFIX=$homedir ..
make
```

### make

```sh
export CC=icx
export F90=ifx

./configure

make all
```

### 老版本

```sh
# if [ ! -f "make.sys" ]; then
#  ./configure
# fi

make clean
make veryclean

export CC=icc
export F77=ifort
export MPIF90=mpiifort
export F90=ifort
export FC=ifort

./configure \
BLAS_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group" \
LAPACK_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_lapack95_lp64.a -Wl,--end-group" \
FFT_LIBS="$FFT_LIB_PATH/libfftw3.a"

#icc -c CPV/src/sockets.c
#if [ -f "sockets.o" ]; then
#  cp sockets.o CPV/src/
#  cp sockets.o PW/src/
#fi

# make all
make cp
make pw
make links
```

<http://blog.sciencenet.cn/blog-2909108-1152511.html>  
<https://blog.csdn.net/odin_linux/article/details/81130075>  
<http://bbs.keinsci.com/thread-1324-1-1.html>  
<http://muchong.com/html/201409/7951501.html>

## Libxc

### cmake

```sh
mkdir build; cd build
cmake -DCMAKE_INSTALL_PREFIX=$homedir -DCMAKE_C_COMPILER=icx -DCMAKE_Fortran_COMPILER=ifx -DENABLE_FORTRAN=ON  ..
make
make test
make install
```

### make

```sh
export CC=icc
export F77=ifort
export MPIF90=mpiifort
export F90=ifort
export FC=ifort

./configure --prefix=$homedir
make 
make install
```

### qe

<https://www.quantum-espresso.org/Doc/user_guide/node13.html>

cmake

```sh
mkdir build; cd build
cmake -DCMAKE_C_COMPILER=icx -DCMAKE_Fortran_COMPILER=ifx -DQE_ENABLE_LIBXC=ON -DCMAKE_INSTALL_PREFIX=$homedir ..
make
```

make

```sh
export CC=icx
export F90=ifx

./configure --with-libxc

make
```

## 收敛问题

```in
&system
    nbnd=415
    occupations='smearing'
    degauss=0.003
/
&electrons
    mixing_mode='local-TF'  ! surface
/
```

<https://suncat.stanford.edu/wiki/convergence-tips>
<https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html>