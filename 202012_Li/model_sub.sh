#!/bin/bash
source ~/tianff/codes/common/environment.sh
set -euo pipefail

jobname=Li
ncore=1
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >> ${jobname}.sh<<eof
 ~/tianff/codes/202012_Li/e0_a.sh

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
