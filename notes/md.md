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

<https://github.com/plumed/plumed2.git>

```sh
./configure CC=icx FC=ifx CXX=mpicxx --prefix=$homedir
make -j 4
make install
```

```txt
Install prefix : /public/spst/home/tianff
Full name      : plumed

Setup your environment
- Ensure this is in your execution path         : /public/spst/home/tianff/bin
- Ensure this is in your include path           : /public/spst/home/tianff/include
- Ensure this is in your library path           : /public/spst/home/tianff/lib
- Ensure this is in your PKG_CONFIG_PATH path   : /public/spst/home/tianff/lib/pkgconfig
For runtime binding:
- Set this environment variable                 : PLUMED_KERNEL=/public/spst/home/tianff/lib/libplumedKernel.so

To create a tcl module that sets all the variables above, use this one as a starting point:
/public/spst/home/tianff/lib/plumed/modulefile

To uninstall, remove the following files and directories:
/public/spst/home/tianff/lib/plumed
/public/spst/home/tianff/share/doc/plumed
/public/spst/home/tianff/include/plumed
/public/spst/home/tianff/bin/plumed
/public/spst/home/tianff/bin/plumed-patch
/public/spst/home/tianff/bin/plumed-config
/public/spst/home/tianff/lib/pkgconfig/plumed.pc
/public/spst/home/tianff/lib/libplumed.so
/public/spst/home/tianff/lib/libplumedKernel.so
A vim plugin can be found here: /public/spst/home/tianff/lib/plumed/vim/
Copy it to /public/spst/home/tianff/.vim/ directory
Alternatively:
- Set this environment variable         : PLUMED_VIMPATH=/public/spst/home/tianff/lib/plumed/vim
- Add the command 'let &runtimepath.=','.$PLUMED_VIMPATH' to your .vimrc file
From vim, you can use :set syntax=plumed to enable it
A python plugin can be found here: /public/spst/home/tianff/lib/plumed/python/
To use PLUMED through python either : 
- Add /public/spst/home/tianff/lib/plumed/python/ to your PYTHONPATH
- Execute the command python buildPythonInterface.py install in the plumed2/python directory
Plumed can be loaded in a python script using the command import plumed
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
cmake -C ../cmake/presets/oneapi.cmake -C ../cmake/presets/basic.cmake -D PKG_PLUMED=yes -D DOWNLOAD_PLUMED=no -D PLUMED_MODE=runtime -D BUILD_MPI=yes -D PKG_GPU=on -D GPU_API=cuda ../cmake
```
