#!/bin/bash
#SBATCH -J xNAMEx
#SBATCH -p ssct
#SBATCH -N 3
#SBATCH --tasks-per-node=32

set -eo pipefail
source ~/tianff/myscript/environment.sh
SECONDS=0

mpirun vasp_std

echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s."
