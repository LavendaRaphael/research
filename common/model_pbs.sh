#!/bin/bash
#PBS -l nodes=1:ppn=6
#PBS -N model.xNUMx
#PBS -q sbp_1
#PBS -j oe

set -eo pipefail
source ~/tianff/environment.sh
SECONDS=0 

cd $PBS_O_WORKDIR
NP=`wc -l < $PBS_NODEFILE`

mpirun -np $NP $bin < scf.in > scf.out

nodeinfo=($(sort -n $PBS_NODEFILE | uniq))
echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s; CoreNum ${NP}; CoreInfo ${nodeinfo[*]}."
#reference
#https://www.jianshu.com/p/2f6c799ca147
