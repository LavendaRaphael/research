# MD

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MD](#md)
  - [DPMD](#dpmd)
    - [Install from src](#install-from-src)
    - [Install from conda](#install-from-conda)
  - [KIM](#kim)
  - [PLUMED2](#plumed2)
  - [LAMMPS](#lammps)

<!-- /code_chunk_output -->

## DPMD

### Install from src

<https://github.com/deepmodeling/deepmd-kit/blob/master/doc/install/install-from-source.md>

TensorFlow

<https://www.tensorflow.org/install/gpu>

GPU Driver

CUDA

```sh
export PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/bin:$PATH"
export LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/lib64:$LIBRARY_PATH"
export LD_LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cuda-11.6/lib64:$LD_LIBRARY_PATH"
```

```sh
export CUDA_VISIBLE_DEVICES=0
```

cuDNN

```sh
export LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cudnn-linux-x86_64-8.3.2.44_cuda11.5/lib:$LIBRARY_PATH"
export LD_LIBRARY_PATH="/public/spst/home/tianff/tianff/software/src/cudnn-linux-x86_64-8.3.2.44_cuda11.5/lib:$LD_LIBRARY_PATH"
```

### Install from conda

和原本安装 tensorflow 冲突

## KIM

<https://openkim.org/doc/usage/obtaining-models/>

```sh
git clone https://github.com/openkim/kim-api.git
cd kim-api
mkdir build
cd build
CC=icx CXX=icpx FC=ifx cmake .. -DCMAKE_INSTALL_PREFIX="$software" -DCMAKE_BUILD_TYPE=Release
make
make install
```

```sh
source $software/bin/kim-api-activate
```

## PLUMED2

<https://github.com/CSIprinceton/CSI-hacks-and-tricks/tree/master/Compilation/Plumed>

```sh
git clone -b v2.7 https://github.com/plumed/plumed2.git plumed2.7
```

```sh
./configure CC=icx FC=ifx CXX=mpiicpc --prefix=$software
make -j 4
make install
```

```sh
export PKG_CONFIG_PATH="${software}/lib/pkgconfig:$PKG_CONFIG_PATH"
```

if not `make install`

```sh
source sourceme.sh
```

## LAMMPS

```sh
git clone -b release --depth=1000 https://github.com/lammps/lammps.git lammps
```

```sh
cd lammps                # change to the LAMMPS distribution directory
mkdir build; cd build    # create and use a build directory
cmake ../cmake           # configuration reading CMake scripts from ../cmake
cmake --build .          # compilation (or type "make")
```

GSL

```sh
sudo apt install libgsl-dev
```

```sh
module add mathlib/gsl/intel
```

Building

```sh
# Building with GNU Compilers:
cmake ../cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DCMAKE_Fortran_COMPILER=gfortran
# Building with Intel Compilers:
cmake ../cmake -DCMAKE_C_COMPILER=icc -DCMAKE_CXX_COMPILER=icpc -DCMAKE_Fortran_COMPILER=ifort
# Building with Intel oneAPI Compilers:
cmake ../cmake -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx -DCMAKE_Fortran_COMPILER=ifx
```

```sh
cmake -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=mpiicpc -DCMAKE_Fortran_COMPILER=ifx -C ../cmake/presets/basic.cmake -D PKG_PLUMED=yes -D DOWNLOAD_PLUMED=no -D PKG_KIM=yes -D BUILD_MPI=yes ../cmake
```