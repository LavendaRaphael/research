#!/bin/bash
set -eo pipefail
source ~/tianff/environment.sh

subfile=xas$suffix
dir=~/tianff/201903/tianff/ice_Ih/script
for N in {1,}
do
	echo $N
    cd Oxygen_${N}/
	rm -rf node $subfile fort.8* fort.90 eig.dat diag_lambda* eigc.dat fort.20 tm* xas.out outxas*
	cp $dir/$subfile ./
	sed -i "s/xNUMx/$N/g"  $subfile

	qsub $subfile #SPST #SHTU
	#bsub < $subfile #MAGIC3

	cd ../
done
