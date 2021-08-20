#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source local_env.sh
set -euo pipefail

cd $work_dir

echo "#-----------------------------------------------------[alignorm]"
${software_bin}xas_alignorm.x xas_alignorm.in

align_delta=$(awk '/align_delta/{print $2}' xas_alignorm.log)
norm_scale=$(awk '/norm_scale/{print $2}' xas_alignorm.log)
echo align_delta=$align_delta
echo norm_scale=$norm_scale

for N in ${loopfile[*]}
do
    echo $N
    cd atom_${N}/
    awk '{
        if (!NF || $1 ~ /^#/)
            print $0;
        else {
            $1=$1+('$align_delta');
            $2=$2*'$norm_scale';
            $3=$3*'$norm_scale';
            $4=$4*'$norm_scale';
            $5=$5*'$norm_scale';
            $6=$6*'$norm_scale';
            $7=$7*'$norm_scale';
            printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
        }
    }' xas_sft.dat > xas_alignorm.dat
    
    cd ..
done

echo "#-----------------------------------------------------[symmetry]"
sym=$(awk '$1 !~ /^#/{print $1}' xas_sym.in)
echo sym=$sym
case $sym in
    "triclinic")
        cat xas_alignorm.dat > xas_sym.dat
        ;;
    "monoclinic")
        awk '{
            if (!NF || $1 ~ /^#/)
                print $0;
            else {
                $6=0.0;
                $7=0.0;
                printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
            }
        }' xas_alignorm.dat > xas_sym.dat
        ;;
    "orthorhombic")
        awk '{
            if (!NF || $1 ~ /^#/)
                print $0;
            else {
                $5=0.0;
                $6=0.0;
                $7=0.0;
                printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
            }
        }' xas_alignorm.dat > xas_sym.dat
        ;;
    "tetragonal"|"trigonal"|"hexagonal")
        awk '{
            if (!NF || $1 ~ /^#/)
                print $0;
            else {
                $2=($2+$3)/2.0;
                $3=$2;
                $5=0.0;
                $6=0.0;
                $7=0.0;
                printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
            }
        }' xas_alignorm.dat > xas_sym.dat
        ;;
    "cubic")
        awk '{
            if (!NF || $1 ~ /^#/)
                print $0;
            else {
                $2=($2+$3+$4)/3.0;
                $3=$2;
                $4=$2;
                $5=0.0;
                $6=0.0;
                $7=0.0;
                printf "%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f%20.12f\n",$1,$2,$3,$4,$5,$6,$7
            }
        }' xas_alignorm.dat > xas_sym.dat
        ;;
    *)
        echo "ERROR in xas_sym.in"
        stop
        ;;
esac
