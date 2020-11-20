#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh
cd $work_dir
oIFS="$IFS"
IFS=$'\n'
atom=($(<snap.pos))
#for ((i = 1; i <= 1; i++))
for ((i = 2; i <= ${O_num}; i++))
do
	rm -rf Oxygen_${i}
	mkdir Oxygen_${i}
	cp ${Templates_dir}/*.* Oxygen_${i}/
	cd Oxygen_${i}/
	mkdir temp
	echo 'OO  ' ${atom[${i}-1]} >> OO_pos_${i}.dat
	echo ${atom[${i}-1]} >> fort.10

	for ((k = 1; k <= ${O_num}; k++))   #copy the O atomic positions
	do
		if [ $k != ${i} ]
		then
			echo 'O   ' ${atom[$k-1]} >> OO_pos_${i}.dat
		fi
	done


	for ((k = $[$O_num+1]; k <= $natoms; k++)) #copy the H atomic positions
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
