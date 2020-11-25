#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $work_dir
rm -f tmsftbroad_tt.dat tmsftbroadave.dat
for N in $loopfile
do
	cat Oxygen_${N}/tmsftbroad.dat >> tmsftbroad_tt.dat
done

${xascodes_bin}tmsftbroadave.x

