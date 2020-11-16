#!/bin/bash
set -eo pipefail
source ~/tianff/myscript/environment.sh

dir=(\
"Cu-111p29s4_Cu2O-111p6s1t00-1_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t0001_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t-100_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t0100_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t-1-1_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t-101_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t01-1_vacuum12" \
"Cu-111p29s4_Cu2O-111p6s1t0101_vacuum12" \
)

subfile="vasp.$mycluster"

for var in ${dir[@]}
do
    
    echo $var
    
    cd ~/tianff/202006_Cu2O/
    if [ ! -d "$var" ]; then
        mkdir "$var"
    fi
    cd $var
    if [ ! -f ${var}.xsd ]; then
        mv ../${var}.xsd ./
    fi
    python ../script/xsd2pos.py ${var}.xsd
    cp ../script/INCAR ./
    cp ../script/POTCAR ./
    cp ../script/KPOINTS ./
    cp ../script/$subfile ./
    sed -i "s/xNAMEx/${var}/g" $subfile

    if [ "$mycluster" = "sbatch" ]; then
            sbatch < $subfile
    elif [ "$mycluster" = "pbs" ]; then
            qsub $subfile
    elif [ "$mycluster" = "lsf" ]; then
            bsub < $subfile
    fi

done

