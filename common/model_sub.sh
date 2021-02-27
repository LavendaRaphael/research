#!/bin/bash
source ~/tianff/codes/common/environment.sh
set -euo pipefail

jobname=test
ncore=$[${maxppn}*3]
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >> ${jobname}.sh<<eof
mpirun ${software_bin}intelmpi_test.x > nodetest.log

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
