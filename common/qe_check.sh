#!/bin/bash
set -euo pipefail

while [[ $# -gt 0 ]]
do

scf_stdout="$1/scf.log"
xspectra_stdout="$1/xspectra.log"

if [ -f "$scf_stdout" ];then
    echo "#------------------------------------[$scf_stdout]"
    awk '
    BEGIN{
        ORS=" "
    }
    {
        if ($1=="iteration"){
            if ($2=="#")
                print $3;
            else
                print substr($2,2)
        }
        else if ($1=="total" && $2=="energy")
            print $4;
        else if ($1=="estimated")
            print $5,"\n"
    }' $scf_stdout

fi


if [ -f "$xspectra_stdout" ];then
    echo "#------------------------------------[$xspectra_stdout]"
    awk '
    BEGIN{
        ORS=" "
    }
    {
        if ($2=="k-point")
            print $2,$4;
        else if ($4=="converged")
            print $3,$4,"\n";
        else if ($3=="CONVERGED")
            print $3,"\n"
    }' $xspectra_stdout

fi

shift

done
