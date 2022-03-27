# QuantumEspresso

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [QuantumEspresso](#quantumespresso)
  - [xspectra](#xspectra)
  - [evc.dat](#evcdat)
  - [新版本编译-cmake](#新版本编译-cmake)
  - [新版本编译-make](#新版本编译-make)
  - [老版本编译](#老版本编译)
  - [libxc](#libxc)
  - [收敛问题](#收敛问题)

<!-- /code_chunk_output -->

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

## 新版本编译-cmake

ref: lammps compile method

```sh
mkdir build; cd build
cmake -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx -DCMAKE_Fortran_COMPILER=ifx ..
make
```

## 新版本编译-make

```sh
make clean
make veryclean

export CC=icc
export F77=ifort
export MPIF90=mpiifort
export F90=ifort

./configure

make all
```

## 老版本编译

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

## libxc

```sh
export CC=icc
export F77=ifort
export MPIF90=mpiifort
export F90=ifort
export FC=ifort
#---------------------------------------------libxc

./autogen.sh
make clean
./configure --prefix=/public/spst/home/tianff/tianff/software/libxc_for_QE-master/libxc/
make 
make install

#----------------------------------------------qe
make clean
./configure

vim make.sys
#>>
 DFLAGS  = -D__LIBXC
 LD_LIBS = -L/public/spst/home/tianff/tianff/software/libxc_for_QE-master/libxc/lib/ -lxcf90 -lxc
 IFLAGS  = -I/public/spst/home/tianff/tianff/software/libxc_for_QE-master/libxc/include/
#<<

make pw
```

## 收敛问题

```in
&system
    nbnd=415
    occupations='smearing'
    degauss=0.003
/
&electrons
    mixing_mode='local-TF'  # surface
/
```

<https://suncat.stanford.edu/wiki/convergence-tips>
<https://www.quantum-espresso.org/Doc/pw_user_guide/node21.html>