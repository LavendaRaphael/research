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
    awk 'NR-"'${i}'"==0{print}' ${Templates_dir}snap.pos >> fort.10
    awk 'NR-"'${i}'"==0                         {print "OO  "$0}' ${Templates_dir}snap.pos > OO_pos_${i}.dat
    awk 'NR-"'${O_num}'"<=0 && NR-"'${i}'"!=0   {print "O   "$0}' ${Templates_dir}snap.pos >> OO_pos_${i}.dat
    awk 'NR-"'${O_num}'">0                      {print "H   "$0}' ${Templates_dir}snap.pos >> OO_pos_${i}.dat

	cat OO_pos_${i}.dat >> scf.in
    cat OO_pos_${i}.dat >> cp-scf.in
	cat OO_pos_${i}.dat >> nscf.in
    cat OO_pos_${i}.dat >> cp-nscf.in
    cat OO_pos_${i}.dat >> cp-nscf-wf.in
	cat OO_pos_${i}.dat >> gw.in

	cd ../

done
