#!/bin/bash
set -eo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh
cd $pbe_dir
for i in $loopfile
do
    echo $i
	rm -rf Oxygen_${i}
	mkdir Oxygen_${i}
	cp ${Templates_dir}*.in Oxygen_${i}/
    cp ${Templates_dir}fort.* Oxygen_${i}/
	cd Oxygen_${i}/
	mkdir temp
    echo "OO  `head -n ${i} ${Templates_dir}snap.pos|tail -n 1`" >>  OO_pos_${i}.dat
	echo "`head -n ${i} ${Templates_dir}snap.pos|tail -n 1`" >> fort.10

	for ((k = 1; k <= ${O_num}; k++))   #copy the O atomic positions
	do
		if [ $k != ${i} ]
		then
			echo  "O   `head -n ${k} ${Templates_dir}snap.pos|tail -n 1`" >> OO_pos_${i}.dat
		fi
	done


	for ((k = $[$O_num+1]; k <= $natoms; k++)) #copy the H atomic positions
	do
		echo  "H   `head -n ${k} ${Templates_dir}snap.pos|tail -n 1`" >> OO_pos_${i}.dat
	done


	cat OO_pos_${i}.dat >> scf.in
    cat OO_pos_${i}.dat >> cp-scf.in
	cat OO_pos_${i}.dat >> nscf.in
    cat OO_pos_${i}.dat >> cp-nscf.in
    cat OO_pos_${i}.dat >> cp-nscf-wf.in
	cat OO_pos_${i}.dat >> gw.in

	cd ../

done
