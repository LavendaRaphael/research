#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh
jobname=pbexNUMx
jobnodes=1
jobppn=6
#========================================[mycluster]
if [ "$mycluster" = "pbs" ]; then
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#PBS -l nodes=${jobnodes}:ppn=${jobppn}
#PBS -N ${jobname}
#PBS -q ${jobqueue}
cd \$PBS_O_WORKDIR
eof
elif [ "$mycluster" = "sbatch" ]; then
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#SBATCH -N ${jobnodes}
#SBATCH --ntasks-per-node=${jobppn}
#SBATCH -J ${jobname}
#SBATCH -p ${jobqueue}
eof
fi
#========================================[main script]
cat >> ${jobname}_sub.sh<<eof

set -euo pipefail
source ~/tianff/codes/common/environment.sh
SECONDS=0

CP=${qe_cohsex_water_bin}cp.x
PW=${qe_cohsex_water_bin}pw.x
echo \$PW
echo \$CP

mpirun \$PW < scf.in > scf.out
cp -r temp/water.save temp/water_50.save
grep ! scf.out | tail -1 | awk '{printf "%15.8f\n", \$5/2}' | tee fort.777
grep ! ../Oxygen_1/scf.out | tail -1 | awk '{printf "$vbands, %15.8f\n", \$5/2}' | tee fort.13

mpirun \$CP < cp-scf.in > cp-scf.out
mv temp/water_50.save temp/water_36.save
tail -$vbands temp/water.wfc > fort.408

mpirun \$PW  < nscf.in > nscf.out
cp -r temp/water.save temp/water_50.save

mpirun \$CP  < cp-nscf.in > cp-nscf.out

mpirun \$CP  < cp-nscf-wf.in > cp-nscf-wf.out
tail -$nbands  temp/water.wfc > fort.407

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}_sub.sh
fi
