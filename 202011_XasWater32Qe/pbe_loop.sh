#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh
cd $work_dir
subfile=pbe.sh

#for ((N = 1; N <= 1; N++))
for ((N = 2; N <= ${O_num}; N++))
do
	echo $N
	cd Oxygen_${N}/
	cp ${script_dir}/${subfile} ./
	sed -i "s/xNUMx/$N/g"  $subfile
	./$subfile
	cd ../
done
