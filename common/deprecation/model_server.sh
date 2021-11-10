#!/bin/bash

mycluster=sbatch
#mycluster=qsub
#mycluster=bsub
echo "mycluster=$mycluster"
jobqueue=ssct
echo "jobqueue=$jobqueue"
maxppn=32
echo "maxppn=$maxppn"

module purge
module load compiler/intel/2017.5.239
module load mpi/intelmpi/2017.4.239
module list

MKL_LIB_PATH=/opt/hpc/software/compiler/intel/intel-compiler-2017.5.239/mkl/lib/intel64/
FFT_LIB_PATH=/public/software/mathlib/fftw/3.3.8/double/intel/lib/
echo "MKL_LIB_PATH=$MKL_LIB_PATH"
echo "FFT_LIB_PATH=$FFT_LIB_PATH"

