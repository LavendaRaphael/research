#!/bin/bash
set -eo pipefail
source ~/tianff/environment.sh

subfile=pbe$suffix

dir=~/tianff/201903/tianff/ice_Ih/script
for N in {1,}
#for N in {2..96}
do
	echo $N
	cd Oxygen_${N}/
	rm -rf temp/* ${subfile} node *.out fort.777 fort.13 fort.408 fort.407 g.dat cp_lambda.dat cp_wf.dat outpbe*
	cp ${dir}/${subfile} ./
	sed -i "s/xNUMx/$N/g"  $subfile
	
	qsub $subfile #SPST #SHTU
	#bsub < $subfile #MAGIC3

	cd ../
done
