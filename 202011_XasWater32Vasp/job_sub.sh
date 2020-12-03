#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Vasp/local_env.sh

jobname=xasxNUMx
ncore=4
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >>${jobname}.sh<<eof
mpirun ${vasp_bin}vasp_gam

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
