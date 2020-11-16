#! /bin/bash
#SBATCH -J outgwxNUMx
#SBATCH -p ssct
#SBATCH -N 16
#SBATCH --ntasks-per-node=32

set -eo pipefail
source ~/tianff/environment.sh

SECONDS=0
NP=512
CP=~/tianff/201903/tianff/GW-lf-fq-cori-ice/bin/cp.x

echo $CP
echo $NP

mpirun -np $NP $CP < gw.in > gw.out

echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s; CoreNum ${NP}."
