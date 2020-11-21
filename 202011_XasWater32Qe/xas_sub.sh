#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

jobname=xasxNUMx
ncore=6
source ~/tianff/codes/common/sub_head.sh
#========================================[main script]
cat >>${jobname}.sh<<eof
cp ${Oxygen1swf_dir}fort.* ./

${xascodes_bin}diag_lambda.x
tail -${cbands}  eig.dat > eigc.dat
mpirun ${xascodes_bin}xas.x > xas.out
${xascodes_bin}tmsft.x
${xascodes_bin}tmsftbroad.x

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof

if true;then
    jobsub ${jobname}.sh
fi
