#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh

source ~/codes/202011_XasWater32Qe/local_env.sh
subfile=xas.sh

for ((N = 1; N <= ${O_num}; N++))
do
	echo $N
    cd Oxygen_${N}/
	cp ${script_dir}/${subfile} ./
    sed -i "s/xNUMx/$N/g"  $subfile
    ./$subfile
    cd ../
done
