#!/bin/bash
if [ $environmennt ]; then
    return
else
    environmennt=true
fi
echo "-----------------------------------------------------[~/tianff/codes/common/environment.sh]"
shopt -s expand_aliases
source ~/tianff/server/server.sh
#======================================[vim]
export VIMINIT='source ~/tianff/codes/common/vimrc.me'
#======================================[alias]
cdl() {
    cd "${1}";
    ll -a;
}
alias cpi="cp -i"
#==============================================================[myserver]
#======================================[MYUBUNTU]
if [ "$myserver" = "MYUBUNTU" ]; then
mycluster=none
maxppn=2
source /opt/intel/parallel_studio_xe_2020.2.108/psxevars.sh
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0
echo "DISPLAY="$DISPLAY
export PATH=/home/tianff/.local/bin:$PATH
export PATH=/home/tianff/tianff/software/vasp/vtstscripts-966:$PATH
export vaspkit=~/tianff/software/vasp/vaspkit.1.2.1/bin
echo "vaspkit="$vaspkit

#======================================[KUNLUN]
elif [ "$myserver" = "KUNLUN" ]; then
mycluster=sbatch
jobqueue=ssct
maxppn=32
module purge
MKL_LIB_PATH=/opt/hpc/software/compiler/intel/intel-compiler-2017.5.239/mkl/lib/intel64
FFT_LIB_PATH=/public/software/mathlib/fftw/3.3.8/double/intel/lib
echo "MKL_LIB_PATH=$MKL_LIB_PATH"
echo "FFT_LIB_PATH=$FFT_LIB_PATH"
#source ~/tianff/myscript/compiler_intel-compiler-2017.5.239.sh
#source ~/tianff/myscript/mpi_intelmpi-2017.4.239.sh
module load compiler/intel/2017.5.239
module load mpi/intelmpi/2017.4.239
module load mathlib/lapack/intel/3.8.0
module add apps/gnuplot/5.0.5/gcc-7.3.1
module list

#======================================[SPST]
elif [ "$myserver" = "SPST" ]; then
source /opt/intel/bin/compilervars.sh intel64
source /opt/intel/impi/2017.2.174/bin64/mpivars.sh intel64 

#======================================[SHTU]
elif [ "$myserver" = "SHTU" ]; then
mycluster=pbs
jobqueue=sbp_1
module purge
#module add compiler/intel/intel-compiler-2017.5.239
#module add mpi/intelmpi/2017.4.239
#source /public/spst/software/profile.d/compiler_intel-compiler-2017.5.239.sh
#source /public/spst/software/profile.d/mpi_intelmpi-2017.4.239.sh
#module add mpi/intelmpi/2019.1.144
module add compiler/intel/composer_xe_2019.1.053
module add mpi/intelmpi/2019.7
module add apps/gnuplot/5.0.6
module add apps/git/2.9.4
module list
lmp_bin=~/0example/software/lammps-3Mar20/build/lmp
echo "lmp_bin=${lmp_bin}"
vasp_bin=~/tianff/software/vasp/vasp.6.1.0/bin/
echo "vasp_bin=${vasp_bin}"

#======================================[MAGIC3]
elif [ "$myserver" = "MAGIC3" ]; then
module add intel/2019 
workhome=/public/home/users/shtu011/tianff/201903/tianff
export MKL_LIB_PATH=/public/home/users/app/compiler/intel-2019.4/compilers_and_libraries_2019.4.243/linux/mkl/lib/intel64
export FFT_LIB_PATH=/public/home/users/app/lib/fftw/intel/double/lib
#======================================[DEBUG]
else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi
#==========================================================[mycluster]
if [ "$mycluster" = "pbs" ]; then
    alias jobsub="qsub"
elif [ "$mycluster" = "sbatch" ]; then
    alias jobsub="sbatch <"
elif [ "$mycluster" = "none" ]; then
    echo ""
else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi
echo "myserver=$myserver"
echo "mycluster=$mycluster"
echo "maxppn=$maxppn"
echo "========================================================================="
