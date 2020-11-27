#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

jobname=test_scf
ncore=6
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >> ${jobname}.sh<<eof
CP=${qe_cohsex_water_bin}cp.x
PW=${qe_cohsex_water_bin}pw.x
echo \$PW
echo \$CP

mpirun \$PW < scf.in > scf.out
cp -r temp/water.save temp/water_50.save
grep ! scf.out | tail -1 | awk '{printf "%15.8f\n", \$5/2}' | tee fort.777
grep ! ../Oxygen_1/scf.out | tail -1 | awk '{printf "$vbands, %15.8f\n", \$5/2}' | tee fort.13

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
