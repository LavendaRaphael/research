#!/bin/sh
#================[USE]============================
#./rdf_infile.sh snap00.pos
#=================snap00.pos======================
#       2.203916        2.203916       11.032247
#       2.203916        2.203916       23.860024
#==============[OUTFILE]==========================
#snap00_rdf.in
#=================================================
set -eo pipefail

#spst
workhome=/home/tianff/201903/tianff

posfile=./$1
prefix=`echo ${posfile##*/}|cut -d '.' -f1`
echo 'prefix  ' ${prefix}
oIFS="$IFS"
IFS=$'\n'
atom=($(< ${posfile} ))
scheme=$[`wc -l < $posfile` / 192]
echo 'scheme  ' ${scheme}
rm -f ${prefix}_rdf.in

echo 'prefix     '${prefix}					>> ${prefix}_rdf.in
echo 'atom_1     O               64' 				>> ${prefix}_rdf.in
echo 'atom_2     H               128'		 		>> ${prefix}_rdf.in
echo 'cell_size  17.631329       17.631329       25.655553'	>> ${prefix}_rdf.in
echo 'rc         50.0' 						>> ${prefix}_rdf.in
echo 'dr         0.1'	 					>> ${prefix}_rdf.in
echo 'scheme     '${scheme}					>> ${prefix}_rdf.in

for ((s = 1; s <= ${scheme}; s++)); do

for k in {1..64}   #copy the O atomic positions
do
        echo 'O   ' $s ${atom[$[$k-193+${s}*192]]} >> ${prefix}_rdf.in
done
for k in {65..192}   #copy the H atomic positions
do
        echo 'H   ' $s ${atom[$[$k-193+${s}*192]]} >> ${prefix}_rdf.in
done

done

IFS=${oIFS}

