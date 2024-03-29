# QuantumEspresso

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [QuantumEspresso](#quantumespresso)
  - [PW input](#pw-input)
  - [Xspectra](#xspectra)
  - [evc.dat](#evcdat)
  - [Compile](#compile)
    - [libxc](#libxc)
    - [qe](#qe)
  - [Qe-car_group_mirror](#qe-car_group_mirror)
  - [QE-dev.10.25-PI-copy-edison](#qe-dev1025-pi-copy-edison)
  - [Cohsex](#cohsex)
  - [收敛问题](#收敛问题)

<!-- /code_chunk_output -->

## PW input

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
    ntyp  = 2
    nat   = 192
    ibrav = 0
/
&ELECTRONS
    ! conv_thr Default: 1.D-6
    ! electron_maxstep Default: 100
/
 
ATOMIC_SPECIES 
  O  15.9994  O_HSCV_PBE-1.0.UPF 
  H  2.01588  H_HSCV_PBE-1.0.UPF 

K_POINTS gamma

CELL_PARAMETERS angstrom

ATOMIC_POSITIONS angstrom
```

## Xspectra

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

## Compile

### libxc

cmake

```sh
module load gcc

mkdir build; cd build
cmake -C ../../oneapi.cmake -DCMAKE_INSTALL_PREFIX=${homedir}/software/libxc.5.3.2_install -DENABLE_FORTRAN=ON  ..
make
make install
```

make

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

```sh
wget https://gitlab.com/QEF/q-e/-/archive/qe-7.1/q-e-qe-7.1.tar.gz
```

<https://www.quantum-espresso.org/Doc/user_guide/node13.html>

cmake

```sh
module load gcc
module load libxc

mkdir build; cd build
cmake -C ../../oneapi.cmake -DQE_ENABLE_LIBXC=ON -DCMAKE_INSTALL_PREFIX=${homedir}/software/q-e-qe-7.1_install ..
make -j 4
make install
```

make

```sh
export CC=icx
export F90=ifx

./configure --with-libxc
make
```

## Qe-car_group_mirror

```sh
cd libxc_for_QE-master

./autogen.sh

export CC=icc
export F77=ifort
export MPIF90=mpiifort
export F90=ifort
export FC=ifort

./configure --prefix=${homedir}/software/libxc-cpbo_install
make 
make install
```

```sh
cd qe-car_group_mirror

make clean
make veryclean

export CC=icx
export MPIF90=mpiifort

./configure --prefix=${homedir}/software/q-e-qe-cpbo_install

vim make.sys
```

- DFLAGS+=-D__LIBXC
- LD_LIBS+=-L/public/spst/home/tianff/software/libxc-cpbo_install/lib/ -lxcf90 -lxc
- IFLAGS+=-I/public/spst/home/tianff/software/libxc-cpbo_install/include/

```sh
make cp
```

## QE-dev.10.25-PI-copy-edison

```sh
make clean
make veryclean

export CC=icx
export MPIF90=mpiifort

./configure

icx -c CPV/src/sockets.c
if [ -f "sockets.o" ]; then
  cp sockets.o CPV/src/
  cp sockets.o PW/src/
fi

# make all
make cp
```

## Cohsex

```sh
# if [ ! -f "make.sys" ]; then
#  ./configure
# fi

make clean
make veryclean

export CC=icx
export F77=ifx
export MPIF90=mpiifort
export F90=ifx
export FC=ifx

./configure \
BLAS_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group" \
LAPACK_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_lapack95_lp64.a -Wl,--end-group" \
FFT_LIBS="$FFT_LIB_PATH/libfftw3.a"

# make all
make cp
make pw
make links
```

<http://blog.sciencenet.cn/blog-2909108-1152511.html>  
<https://blog.csdn.net/odin_linux/article/details/81130075>  
<http://bbs.keinsci.com/thread-1324-1-1.html>  
<http://muchong.com/html/201409/7951501.html>

## 收敛问题

```in
&system
    occupations='smearing'
    degauss=0.003
/
&electrons
    mixing_mode='local-TF'  ! surface
/
```

<https://suncat.stanford.edu/wiki/convergence-tips>  
<https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html>
