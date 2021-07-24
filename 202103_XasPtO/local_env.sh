#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/common/environment.sh
set -euo pipefail

if [ ! -z ${local_env+x} ]; then
if $local_env;then
    return
fi
fi
local_env=false
echo "---------------------------------------------------------------------------[~/tianff/codes/202011_XasWater32Vasp/local_env.sh]"
# work_dir=${gotowork_3}vasp_sch/
  work_dir=${gotowork_2}vasp_sch_aimd3_snap329/
# work_dir=${gotowork_2}vasp_sch/
echo "work_dir=$work_dir"

# O_num=$(awk 'NR-7==0 {print $1}' ${work_dir}template/POSCAR)
# echo "O_num=$O_num"
# O_num=4

# sub_dir="xspectra/"
# sub_dir="xspectra.epsilon010/"
# sub_dir="xspectra.epsilon100/"
  sub_dir=""
echo "sub_dir=$sub_dir"

# subfile=xspectra_sub.sh
  subfile=vasp_sub.sh
# subfile=scf_sub.sh
echo "subfile=$subfile"

# loopfile="1"
# loopfile=`seq 1 $O_num`
# loopfile="1 3 5 7 9 11"
# loopfile="1 1 3 3 5 5 7 7 9 9 11"
# loopfile="1 3"
# loopfile="3 4 5 11 12 13 14 15 16 17 18 19 20 21 22"
# echo "loopfile=$loopfile"

  tensorxyz="X Y Z"
echo "tensorxyz=$tensorxyz"

echo "#=========================================================================<<<"

local_env=true
