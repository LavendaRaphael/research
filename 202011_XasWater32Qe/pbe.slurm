#!/bin/bash
#SBATCH -J outpbexNUMx
#SBATCH -p ssct
#SBATCH -N 1
#SBATCH --ntasks-per-node=6

set -eo pipefail
source ~/tianff/myscript/environment.sh

SECONDS=0
CP=~/tianff/201903/tianff/GW-lf-fq-cori-ice/bin/cp.x
PW=~/tianff/201903/tianff/GW-lf-fq-cori-ice/bin/pw.x
NP=6

echo $PW
echo $CP
echo $NP

mpirun -np $NP $PW < scf.in > scf.out
sleep 10s 
cp -r temp/water.save temp/water_50.save
grep ! scf.out | tail -1 | awk '{printf "%15.8f\n", $5/2}' | tee fort.777
grep ! ../Oxygen_1/scf.out | tail -1 | awk '{printf "256, %15.8f\n", $5/2}' | tee fort.13

mpirun -np $NP $CP < cp-scf.in > cp-scf.out
sleep 10s
mv temp/water_50.save temp/water_36.save
tail -256 temp/water.wfc > fort.408

mpirun -np $NP $PW  < nscf.in > nscf.out
sleep 10s
cp -r temp/water.save temp/water_50.save

mpirun -np $NP $CP  < cp-nscf.in > cp-nscf.out
sleep 10s

mpirun -np $NP $CP  < cp-nscf-wf.in > cp-nscf-wf.out
sleep 10s
tail -512  temp/water.wfc > fort.407

echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s; CoreNum ${NP}."

#reference
#https://www.jianshu.com/p/2f6c799ca147
