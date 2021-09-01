#!/bin/bash
if [ ! -z ${local_env+x} ]; then
if $local_env;then
    return
fi
fi

homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/group/common/groupenv.sh
set -euo pipefail

local_env=false
echo "#=========================================================================[local_env.sh]"
# work_dir='Pt.110.x12y2z4.5_O22_vac15/'
# work_dir='Pt.110.x12y2z4.5_O22_vac15/vasp_sch.aimd2_932/'
# work_dir='Pt.110.x2y3z4.5_O6_vac15/'
  work_dir='Pt.110.x2y3z4.5_O1_vac15/'
# work_dir='Pt.110.x2y3z4.5_O2.12_vac15/'
# work_dir='Pt.110.x2y3z4.5_O2.13_vac15/'
# work_dir='Pt.110.x2y3z4.5_O2.14_vac15/'
# work_dir='Pt.110.x2y3z4.5_O3.123_vac15/'
# work_dir='Pt.110.x2y3z4.5_O3.135_vac15/'
# work_dir='Pt.110.x2y3z4.5_O3.136_vac15/'
# work_dir='Pt.110.x2y3z4.5_O4.v56_vac15/'
# work_dir='Pt.110.x2y3z4.5_O5_vac15/'
# work_dir='Pt.110.x2y4z4.5_O2.13_vac15/'
# work_dir='Pt.110.x2y4z4.5_O2.15_vac15/'
# work_dir='Pt.110.x2y4z4.5_O2.16_vac15/'
# work_dir='Pt.110.x2y4z4.5_O3.137_vac15/'
# work_dir='Pt.110.x2y4z4.5_O3.148_vac15/'
# work_dir='Pt.110.x2y4z4.5_O4.1237_vac15/'
# work_dir='Pt.110.x2y4z4.5_O4.1458_vac15/'
# work_dir='Pt.110.x2y4z4.5_O6.v56_vac15/'
# work_dir='Pt.110.x4y3z4.5_O2.12_vac15/'
# work_dir='Pt.110.x4y3z4.5_O2.14_vac15/'
 work_dir=${goto_pto_work_110}${work_dir}
 work_dir=${work_dir}vasp_sch/
echo "work_dir=$work_dir"

# O_num=$(awk 'NR-7==0 {print $1}' ${work_dir}template/POSCAR)
# echo "O_num=$O_num"

  loopfile=(1)
# loopfile=`seq 1 $O_num`
# loopfile=(1 1 3 3 5 5 7 7 9 9 11)
# loopfile=$(seq 1 22)
# loopfile=(1 3 3)
 echo "loopfile=$loopfile"

  subfile=vasp_sub.sh
# subfile=xspectra_sub.sh
# subfile=scf_sub.sh
echo "subfile=$subfile"

# sub_dir="xspectra/"
# sub_dir="xspectra.epsilon010/"
# sub_dir="xspectra.epsilon100/"
  sub_dir=""
echo "sub_dir=$sub_dir"

echo "#=========================================================================<<<"

local_env=true
