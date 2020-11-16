#!/bin/bash
set -eo pipefail

#物院
workhome=/home/tianff/201903/tianff
subfile=dos.pbs
#魔方三
#workhome=/public/home/users/shtu011/tianff/201903
#subfile=pbe.lsf

dir=$workhome/script
for ((N = 1 ;N <= 64; N++)); do
	echo $N
        cd Oxygen_${N}/
	rm -rf node ${subfile} dos.out outdos* water.dos
	cp $dir/$subfile ./
	sed -i "s/xNUMx/$N/g"  $subfile

	#物院
	qsub $subfile
	#魔方三
	#bsub < $subfile

	cd ../
done
