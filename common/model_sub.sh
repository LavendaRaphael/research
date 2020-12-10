#!/bin/bash
set -euo pipefail
source ~/tianff/codes/common/environment.sh

jobname=test
ncore=36
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >> ${jobname}.sh<<eof
mpirun ${software_bin}intelmpi_test.x

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
