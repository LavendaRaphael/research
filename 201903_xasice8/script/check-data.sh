#!/bin/bash
#
cfile=xas
echo $cfile

for N in {1..12}
do
	echo ${N}
	cd Oxygen_$N/
	#cd Oxygen_$N
	tail -3  $cfile.out
        #tail -3 gw.out
	cd ..
done
