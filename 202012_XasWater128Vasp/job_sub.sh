#!/bin/bash
source ~/tianff/codes/202012_XasWater128Vasp/local_env.sh
set -euo pipefail

jobname=xasxNUMx
ncore=36
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >>${jobname}.sh<<eof
mpirun ${vasp_bin}vasp_gam

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
