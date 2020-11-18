#!/bin/bash
set -eo pipefail
source ~/tianff/environment.sh

subfile="gw.$mycluster"

dir=~/tianff/201903/tianff/script
for ((N = 1; N <= 1; N++)); do
	echo $N
	cd Oxygen_${N}/
	rm -f gw.pbs gw.lsf node gw.out outgw*
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
