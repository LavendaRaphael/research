#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Vasp/local_env.sh

cd $work_dir
for N in $loopfile
do
	echo $N
	cd O_${N}/
	${script_dir}plot_core_imdiel.sh
	cd ../
done
