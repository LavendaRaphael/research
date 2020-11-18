#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh

oIFS="$IFS"
IFS=$'\n'
atom=($(<snap.pos))
dir=~/tianff/201903/tianff/Templates

for i in {1,}
#for ((i = 1; i <= 2; i++))
do
	rm -rf Oxygen_${i}
	mkdir Oxygen_${i}
	cp ${dir}/*.* Oxygen_${i}/
	cd Oxygen_${i}/
	mkdir temp
	echo 'OO  ' ${atom[${i}-1]} >> OO_pos_${i}.dat
	echo ${atom[${i}-1]} >> fort.10

	for k in {1..64}   #copy the O atomic positions
	do
		if [ $k != ${i} ]
		then
			echo 'O   ' ${atom[$k-1]} >> OO_pos_${i}.dat
		fi
	done


	for k in {65..192}   #copy the H atomic positions
	do
		echo 'H   ' ${atom[$k-1]} >> OO_pos_${i}.dat
	done


	cat OO_pos_${i}.dat >> scf.in
    cat OO_pos_${i}.dat >> cp-scf.in
	cat OO_pos_${i}.dat >> nscf.in
    cat OO_pos_${i}.dat >> cp-nscf.in
    cat OO_pos_${i}.dat >> cp-nscf-wf.in
	cat OO_pos_${i}.dat >> gw.in

	cd ../

done
IFS=${oIFS}
