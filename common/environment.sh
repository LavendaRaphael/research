#!/bin/bash
#set -eo pipefail

source ~/tianff/codes/common/server.sh

export VIMINIT='source ~/tianff/codes/common/vimrc.me'
cdl() {
    cd "${1}";
    ll -a;
}
alias cpi="cp -i"

#======================================[MYUBUNTU]
if [ "$myserver" = "MYUBUNTU" ]; then
echo "MYUBUNTU"
source /opt/intel/parallel_studio_xe_2020.2.108/psxevars.sh
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0
echo "DISPLAY="$DISPLAY
export PATH=/home/tianff/.local/bin:$PATH
export PATH=/home/tianff/tianff/software/vasp/vtstscripts-966:$PATH
export vaspkit=~/tianff/software/vasp/vaspkit.1.2.1/bin
echo "vaspkit="$vaspkit

#======================================[KUNLUN]
elif [ "$myserver" = "KUNLUN" ]; then
echo "KUNLUN"
module purge
#source ~/tianff/myscript/compiler_intel-compiler-2017.5.239.sh
#source ~/tianff/myscript/mpi_intelmpi-2017.4.239.sh
export MKL_LIB_PATH=/opt/hpc/software/compiler/intel/intel-compiler-2017.5.239/mkl/lib/intel64
export FFT_LIB_PATH=/public/software/mathlib/fftw/3.3.8/double/intel/lib
mycluster=sbatch
module load compiler/intel/2017.5.239
module load mpi/intelmpi/2017.4.239

#======================================[SPST]
elif [ "$myserver" = "SPST" ]; then
#echo 'spst'
source /opt/intel/bin/compilervars.sh intel64
source /opt/intel/impi/2017.2.174/bin64/mpivars.sh intel64 

#======================================[SHTU]
elif [ "$myserver" = "SHTU" ]; then
echo "SHTU"
module purge
module add compiler/intel/composer_xe_2019.1.053
module add mpi/intelmpi/2019.7
module add apps/gnuplot/5.0.6
mycluster=pbs
PATH=$PATH:~/tianff/software/vasp/vasp.6.1.0/bin/

#======================================[MAGIC3]
elif [ "$myserver" = "MAGIC3" ]; then
module add intel/2019 
workhome=/public/home/users/shtu011/tianff/201903/tianff
export MKL_LIB_PATH=/public/home/users/app/compiler/intel-2019.4/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64
export FFT_LIB_PATH=/public/home/users/app/lib/fftw/intel/double/lib
fi
