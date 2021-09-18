#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}code/common/environment.sh
set -euo pipefail

echo "#-----------------------------------------------------[alignorm]"
${software_bin}xas_alignorm.x xas_alignorm.in

align_delta=$(awk '/align_delta/{print $2}' xas_alignorm.log)
norm_scale=$(awk '/norm_scale/{print $2}' xas_alignorm.log)
echo align_delta=$align_delta
echo norm_scale=$norm_scale

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
}' xas_ave.dat > xas_alignorm.dat

