#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh

jobname=pbexNUMx
jobnodes=1
jobppn=6
#========================================[myserver]
if [ "$myserver" = "SHTU" ]; then
    jobqueue=sbp_1
elif [ "$myserver" = "KUNLUN" ]; then
    jobqueue=ssct
else
    echo "ERROR: 'myserver' not exist!"
    exit
fi
#========================================[mycluster]
if [ "$mycluster" = "pbs" ]; then
    alias jobsub="qsub"
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#PBS -l nodes=${jobnodes}:ppn=${jobppn}
#PBS -N ${jobname}
#PBS -q ${jobqueue}
cd \$PBS_O_WORKDIR
eof
elif [ "$mycluster" = "sbatch" ]; then
    alias jobsub="sbatch <"
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#SBATCH -N ${jobnodes}
#SBATCH --ntasks-per-node=${jobppn}
#SBATCH -J ${jobname}
#SBATCH -p ${jobqueue}
eof
else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi
#========================================[main script]
cat >>pbe_sub.sh<<eof

set -eo pipefail
source ~/tianff/codes/common/environment.sh
SECONDS=0

CP=\${qe_cohsex_water_bin}cp.x
PW=\${qe_cohsex_water_bin}pw.x
echo \$PW
echo \$CP

mpirun \$PW < scf.in > scf.out
cp -r temp/water.save temp/water_50.save
grep ! scf.out | tail -1 | awk '{printf "%15.8f\n", \$5/2}' | tee fort.777
grep ! ../Oxygen_1/scf.out | tail -1 | awk '{printf "256, %15.8f\n", \$5/2}' | tee fort.13

mpirun \$CP < cp-scf.in > cp-scf.out
mv temp/water_50.save temp/water_36.save
tail -256 temp/water.wfc > fort.408

mpirun \$PW  < nscf.in > nscf.out
cp -r temp/water.save temp/water_50.save

mpirun \$CP  < cp-nscf.in > cp-nscf.out

mpirun \$CP  < cp-nscf-wf.in > cp-nscf-wf.out
tail -512  temp/water.wfc > fort.407

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof
