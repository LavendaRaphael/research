#!/bin/sh
set -eo pipefail
source ~/tianff/codes/common/environment.sh

if [ ! -f "make.sys" ]; then
  ./configure
fi

make clean
make veryclean

export FC=ifort
export CC=icc
export F77=ifort
export MPIF90=mpiifort
export FCFLAGS=-O2
export CFLAGS=-O2
export FFLAGS=-O2
./configure \
BLAS_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_intel_lp64.a $MKL_LIB_PATH/libmkl_sequential.a $MKL_LIB_PATH/libmkl_core.a -Wl,--end-group" \
LAPACK_LIBS="-Wl,--start-group $MKL_LIB_PATH/libmkl_lapack95_lp64.a -Wl,--end-group" \
FFT_LIBS="$FFT_LIB_PATH/libfftw3.a"

#icc -c CPV/src/sockets.c
#if [ -f "sockets.o" ]; then
#  cp sockets.o CPV/src/
#  cp sockets.o PW/src/
#fi

#make all
make cp
make pw
make links 

#reference
#http://blog.sciencenet.cn/blog-2909108-1152511.html
#https://blog.csdn.net/odin_linux/article/details/81130075
#http://bbs.keinsci.com/thread-1324-1-1.html
#http://muchong.com/html/201409/7951501.html

