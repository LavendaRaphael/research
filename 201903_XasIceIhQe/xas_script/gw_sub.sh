#!/bin/bash
set -eo pipefail
source ~/tianff/environment.sh

subfile=gw$suffix

dir=~/tianff/201903/tianff/ice_Ih/script
for ((N = 1; N <= 1; N++)); do
	echo $N
	cd Oxygen_${N}/
	rm -f gw.pbs gw.lsf node gw.out outgw*
	cp $dir/$subfile ./
	sed -i "s/xNUMx/$N/g"  $subfile
	
	qsub $subfile #SHTU #SPST
	#bsub < $subfile #MAGIC3
	
	cd ../
done
