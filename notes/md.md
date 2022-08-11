# MD

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MD](#md)
  - [CUDA](#cuda)
  - [cuDNN](#cudnn)
  - [DeePMD-kit (conda)](#deepmd-kit-conda)
  - [DeePMD-kit (offline)](#deepmd-kit-offline)
  - [Tensorflow (python)](#tensorflow-python)
  - [DeePMD-kit (python)](#deepmd-kit-python)
  - [Tensorflow (C++)](#tensorflow-c)
  - [DeePMD-kit (C++)](#deepmd-kit-c)
  - [Lapack](#lapack)
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

When run code on computing node, please remove libcuda.so

```sh
mkdir libcuda
mv lib64/stubs/licuda.so* libcuda/

export CUDA_VISIBLE_DEVICES=0
```

## cuDNN

<https://developer.nvidia.com/rdp/cudnn-download>

## DeePMD-kit (conda)

<https://docs.deepmodeling.com/projects/deepmd/en/master/install/easy-install.html>

```sh
conda create -n deepmd deepmd-kit=*=*gpu libdeepmd=*=*gpu lammps cudatoolkit=11.6 horovod -c https://conda.deepmodeling.com
```

## DeePMD-kit (offline)

```sh
Please activate the environment before using the packages:

/path/to/deepmd-kit/bin/conda activate /path/to/deepmd-kit

The following executable files have been installed:
1. DeePMD-kit CLi: dp -h
2. LAMMPS: lmp -h
3. DeePMD-kit i-Pi interface: dp_ipi
4. MPICH: mpirun -h
5. Horovod: horovod -h

The following Python libraries have been installed:
1. deepmd
2. dpdata
3. pylammps
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
wget https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.9.1.zip
cd tensorflow-2.9.1

./configure
#cuda: /public/spst/home/tianff/software/cuda-11.7,/public/spst/home/tianff/software/cudnn-linux-x86_64-8.4.1.50_cuda11.6-archive
#Compute capability: 7.0,7.5,8.0

export TEST_TMPDIR=/tmp/tianff/.bazel
bazel build -c opt --config=mkl --verbose_failures --local_cpu_resources=HOST_CPUS*.5 --local_ram_resources=2048 //tensorflow:libtensorflow_cc.so
```

```sh
tensorflow=${homedir}/software/tensorflow-2.9.1
tensorflow_root=${homedir}/software/tensorflow-2.9.1_install

mkdir -p ${tensorflow_root}/lib
cp -d ${tensorflow}/bazel-bin/tensorflow/libtensorflow_cc.so* $tensorflow_root/lib/
cp -d ${tensorflow}/bazel-bin/tensorflow/libtensorflow_framework.so* $tensorflow_root/lib/

mkdir -p $tensorflow_root/include/tensorflow
rsync -avzh --exclude '_virtual_includes/' --include '*/' --include '*.h' --include '*.inc' --exclude '*' ${tensorflow}/bazel-bin/ $tensorflow_root/include/

rsync -avzh --include '*/' --include '*.h' --include '*.inc' --exclude '*' ${tensorflow}/tensorflow/cc $tensorflow_root/include/tensorflow/
rsync -avzh --include '*/' --include '*.h' --include '*.inc' --exclude '*' ${tensorflow}/tensorflow/core $tensorflow_root/include/tensorflow/

rsync -avzh --include '*/' --include '*' --exclude '*.cc' ${tensorflow}/third_party/ $tensorflow_root/include/third_party/

rsync -avzh --include '*/' --include '*' --exclude '*.txt' ${tensorflow}/bazel-tensorflow-2.9.1/external/eigen_archive/Eigen/ $tensorflow_root/include/Eigen/
rsync -avzh --include '*/' --include '*' --exclude '*.txt' ${tensorflow}/bazel-tensorflow-2.9.1/external/eigen_archive/unsupported/ $tensorflow_root/include/unsupported/

rsync -avzh --include '*/' --include '*.h' --include '*.inc' --exclude '*' ${tensorflow}/bazel-tensorflow-2.9.1/external/com_google_protobuf/src/google/ $tensorflow_root/include/google/
rsync -avzh --include '*/' --include '*.h' --include '*.inc' --exclude '*' ${tensorflow}/bazel-tensorflow-2.9.1/external/com_google_absl/absl/ $tensorflow_root/include/absl/

cp -d ${tensorflow}/bazel-out/k8-opt/bin/external/llvm_openmp/libiomp5.so $tensorflow_root/lib/

find $tensorflow_root -type d -empty -delete
```

## DeePMD-kit (C++)

<https://docs.deepmodeling.com/projects/deepmd/en/master/install/install-from-source.html>

```sh
mkdir source/build 
cd source/build
export CC=`which gcc`
export CXX=`which g++`
cmake -DTENSORFLOW_ROOT=${homedir}/software/tensorflow-2.9.1_install -DCMAKE_INSTALL_PREFIX=${homedir}/software/deepmd-kit-2.1.3_install -DUSE_CUDA_TOOLKIT=TRUE -DLAMMPS_SOURCE_ROOT=${homedir}/software/lammps-stable_23Jun2022 ..
make -j4
make install
```

## Lapack

```sh
wget https://github.com/Reference-LAPACK/lapack/archive/refs/tags/v3.10.1.tar.gz
mkdir build
cd build
cmake -C ../../oneapi.cmake -D BUILD_SHARED_LIBS=ON -D CMAKE_INSTALL_PREFIX=${homedir}/software/lapack-3.10.1_install ..
```

## PLUMED2

<https://github.com/CSIprinceton/CSI-hacks-and-tricks/tree/master/Compilation/Plumed>  
<https://github.com/plumed/plumed2.git>  
<https://www.plumed.org/doc-v2.8/user-doc/html/_installation.html>

```sh
./configure CC=icx CXX=mpicxx --prefix=${homedir}/software/plumed-2.8.0_install
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

## LAMMPS

```sh
wget https://github.com/lammps/lammps/archive/stable_23Jun2022.tar.gz

mkdir build; cd build    # create and use a build directory

cmake -C ../cmake/presets/oneapi.cmake -C ../cmake/presets/most.cmake -D PKG_MACHDYN=no -D FFT=MKL -D PKG_PLUMED=yes -D DOWNLOAD_PLUMED=no -D PLUMED_MODE=runtime -D BUILD_MPI=yes -D PKG_GPU=on -D GPU_API=cuda -D LAMMPS_INSTALL_RPATH=ON -D BUILD_SHARED_LIBS=yes -D CUDA_NVCC_FLAGS=-allow-unsupported-compiler -D CMAKE_INSTALL_PREFIX=${homedir}/software/lammps-stable_23Jun2022_install ../cmake
make -j 4
make install
```
