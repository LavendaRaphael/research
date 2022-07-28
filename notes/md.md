# MD

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MD](#md)
  - [CUDA](#cuda)
  - [cuDNN](#cudnn)
  - [DeePMD-kit (easy install)](#deepmd-kit-easy-install)
  - [Tensorflow (python)](#tensorflow-python)
  - [DeePMD-kit (python)](#deepmd-kit-python)
  - [Tensorflow (C++)](#tensorflow-c)
  - [KIM](#kim)
  - [PLUMED2](#plumed2)
  - [LAMMPS](#lammps)

<!-- /code_chunk_output -->

## CUDA

<https://stackoverflow.com/questions/39379792/install-cuda-without-root>  
<https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=CentOS&target_version=7&target_type=runfile_local>

```sh
Toolkit:  Installed in /public/spst/home/tianff/install/cuda-11.7/

Please make sure that
 -   PATH includes /public/spst/home/tianff/software/cuda-11.7/bin
 -   LD_LIBRARY_PATH includes /public/spst/home/tianff/software/cuda-11.7/lib64, or, add /public/spst/home/tianff/software/cuda-11.7/lib64 to /etc/ld.so.conf and run ldconfig as root

To uninstall the CUDA Toolkit, run cuda-uninstaller in /public/spst/home/tianff/software/cuda-11.7/bin
***WARNING: Incomplete installation! This installation did not install the CUDA Driver. A driver of version at least 515.00 is required for CUDA 11.7 functionality to work.
To install the driver using this installer, run the following command, replacing <CudaInstaller> with the name of this run file:
    sudo <CudaInstaller>.run --silent --driver
```

```sh
export CUDA_VISIBLE_DEVICES=0
```

## cuDNN

<https://developer.nvidia.com/rdp/cudnn-download>

## DeePMD-kit (easy install)

<https://docs.deepmodeling.com/projects/deepmd/en/master/install/easy-install.html>

```sh
conda create -n deepmd deepmd-kit=*=*gpu libdeepmd=*=*gpu lammps cudatoolkit=11.6 horovod -c https://conda.deepmodeling.com
```

## Tensorflow (python)

```sh
python -m pip install --user --upgrade tensorflow
```

## DeePMD-kit (python)

<https://docs.deepmodeling.com/projects/deepmd/en/master/install/install-from-source.html>

```sh
git clone --recursive https://github.com/deepmodeling/deepmd-kit.git deepmd-kit
cd deepmd-kit
export DP_VARIANT=cuda
export CC=`which gcc`
export CXX=`which g++`
python -m pip install --user .
```

## Tensorflow (C++)

<https://www.tensorflow.org/install/gpu>  
<https://www.intel.com/content/www/us/en/developer/articles/guide/optimization-for-tensorflow-installation-guide.html>  
<https://docs.deepmodeling.com/projects/deepmd/en/master/install/install-tf.2.8.html>  
<https://wiki.cheng-group.net/wiki/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85/deepmd-kit_installation_104>  
<https://wiki.cheng-group.net/wiki/%E8%BD%AF%E4%BB%B6%E5%AE%89%E8%A3%85/deepmd-kit_installation_51>  

```sh
wget https://github.com/bazelbuild/bazelisk/releases/download/v1.12.0/bazelisk-linux-amd64 -O ${homedir}/.local/bin/bazel
```

```sh
git clone https://github.com/tensorflow/tensorflow tensorflow-2.9.1 -b v2.9.1 --depth=1
cd tensorflow-2.9.1
./configure
export TEST_TMPDIR=/tmp/tianff/.bazel
bazel build -c opt --config=mkl --verbose_failures --local_resources 2048,4,1.0 //tensorflow:libtensorflow_cc.so
```

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
./configure CC=icx CXX=mpicxx --prefix=$homedir
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
cmake -C ../cmake/presets/oneapi.cmake -C ../cmake/presets/basic.cmake -D PKG_PLUMED=yes -D DOWNLOAD_PLUMED=no -D PLUMED_MODE=runtime -D BUILD_MPI=yes -D PKG_GPU=on -D GPU_API=cuda -D CUDA_NVCC_FLAGS=-allow-unsupported-compiler ../cmake
```
