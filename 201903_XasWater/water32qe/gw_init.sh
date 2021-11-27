#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh

cd $cohsex_dir
for N in $loopfile
do
	echo $N
	rm -rf Oxygen_${N}/
	cp -r ${pbe_dir}Oxygen_${N} ./
done
