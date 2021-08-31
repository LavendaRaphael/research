#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/group/common/groupenv.sh
set -euo pipefail

jobname=test
ncore=$[${maxppn}*2]
source ${homedir}codes/group/common/sub_head.sh

#==========================================================[main script]
cat >> ${jobname}.sh<<eof
mpirun ${software_bin}intelmpi_test.x > nodetest.log

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

#==========================================================[vasp]
if [ -f "INCAR" ]; then
    sed -i "/NCORE/c\  NCORE = $[($maxppn/2)]" INCAR
    source ${software_bin}vasp_pot.sh
fi

if true;then
    jobsub ${jobname}.sh
fi
