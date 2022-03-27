# MISC

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [MISC](#misc)
  - [KIM](#kim)
  - [PLUMED2](#plumed2)
  - [LAMMPS](#lammps)
  - [materials studio](#materials-studio)
    - [旋转分子](#旋转分子)
    - [内存占用高](#内存占用高)
    - [经验教程](#经验教程)
    - [图像重影问题](#图像重影问题)
    - [下载安装破解](#下载安装破解)
  - [cluster](#cluster)
    - [bug](#bug)
      - [error](#error)
      - [solution](#solution)
  - [VESTA](#vesta)

<!-- /code_chunk_output -->

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

## materials studio

### 旋转分子

SHIFT+右键  旋转
ALT+右键    平移

### 内存占用高

关闭结构窗口

### 经验教程
<http://muchong.com//t-11279111-1>

### 图像重影问题

MS界面→tools→options→Graphics ：
查看其中的选项是否勾选，如果没有勾选，全部勾选，重启MS；
如果已经勾选，现全部不勾选，重启MS。

### 下载安装破解
<https://www.zdfans.com/html/48131.html>

## cluster

### bug

#### error

提交的任务一直显示run，并行程序却没有真正执行，标准输出中相关的内容什么都没有

#### solution

mpi通信需要你的账号在计算节点之前可以ssh免密登录，但是你的.ssh目录不明原因被修改了导致节点互访出现问题

## VESTA

晶胞transform时先remove symmetry
