#!/bin/bash
source ~/tianff/codes/202012_XasWater128Vasp/local_env.sh
set -euo pipefail

cd $work_dir
for N in $loopfile
do
	echo $N
	cd O_${N}/
	cp ${script_dir}/${subfile} ./
	sed -i "s/xNUMx/$N/g"  $subfile
	./$subfile
    rm ${subfile}
	cd ../
done
