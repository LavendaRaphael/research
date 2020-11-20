#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

jobname=gwxNUMx
ncore=$nbands
source ~/tianff/codes/common/model_sub.sh
#========================================[main script]
cat >>${jobname}_sub.sh<<eof
CP=${qe_cohsex_water_bin}cp.x
echo \$CP

mpirun \$CP < gw.in > gw.out

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}_sub.sh
fi
