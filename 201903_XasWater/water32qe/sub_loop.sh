#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $work_dir
for N in $loopfile
do
	echo $N
	cd Oxygen_${N}/
	cp ${script_dir}/${subfile} ./
	sed -i "s/xNUMx/$N/g"  $subfile
	./$subfile
	cd ../
    rm $subfile
done
