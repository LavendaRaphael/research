#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

echo "#-----------------------------------------------------[extract]"
for N in ${loopfile[*]}
do
    echo $N
    cd atom_${N}/

    nline_1=$(awk '/frequency dependent IMAGINARY/{print NR}' OUTCAR)
    nline_2=$(awk '/frequency dependent      REAL/{print NR}' OUTCAR)
    echo "# E(ev)      X         Y         Z        XY        YZ        ZX" > xas.dat
    awk 'NR-'$nline_1'-2>0 && NR-'$nline_2'+1<0 {
        $2=$2*$1;
        $3=$3*$1;
        $4=$4*$1;
        $5=$5*$1;
        $6=$6*$1;
        $7=$7*$1;
        printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
    }' OUTCAR >> xas.dat

    cd ..
done


echo "#-------------------------------------------------[sft]"
for N in ${loopfile[*]}
do
    echo $N
    cd atom_${N}/
    fenergy_1=$(grep energy ../atom_1/OUTCAR | tail -1 | awk '{print $7}')
    fenergy_2=$(grep energy OUTCAR | tail -1 | awk '{print $7}')
    fenergy_sft=$(bc <<< "($fenergy_2)-($fenergy_1)")
    echo fenergy_sft=$fenergy_sft

    awk '{
        if (!NF || /^#/)
            print $0;
        else {
            $1=$1+('$fenergy_sft');
            printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
        }
    }' xas.dat > xas_sft.dat

    awk '{
        if (!NF || /^#/)
            print $0;
        else {
            $1=$1+('$fenergy_sft');
            printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%8d\n",$1,$2,$3,$4,$5,$6,$7,$8
        }
    }' MYCARXAS > xas.tm_sft.dat    
    
    cd ..
done

echo "#-------------------------------------------------[tt]"
rm -f xas_tt.dat
for N in ${loopfile[*]}
do
    echo $N
    cat atom_${N}/xas_sft.dat >> xas_tt.dat
done

#echo "#-------------------------------------------------[ave]"
#${software_bin}xas_ave.x xas_tt.dat
