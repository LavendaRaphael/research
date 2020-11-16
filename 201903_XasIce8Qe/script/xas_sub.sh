#!/bin/bash
set -eo pipefail
source ~/tianff/environment.sh

subfile="xas.$mycluster"
dir=~/tianff/201903/tianff/script
for N in {1,}
do
	echo $N
        cd Oxygen_${N}/
	rm -f node $subfile fort.8* fort.90 eig.dat diag_lambda* eigc.dat fort.20 tm* xas.out outxas*
	cp $dir/$subfile ./
	sed -i "s/xNUMx/$N/g"  $subfile
        
	if [ "$mycluster" = "slurm" ]; then
        sbatch < $subfile
    elif [ "$mycluster" = "pbs" ]; then
        qsub $subfile
    elif [ "$mycluster" = "lsf" ]; then
        bsub < $subfile
	fi

	cd ../
done
