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
 work_dir=${goto_pto_110}Pt.110.x2y3z4.5_O6_vac15/
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

 loopfile=(1)
# loopfile=`seq 1 $O_num`
# loopfile=$(seq 1 22)
# loopfile=(1 1 3 3 5 5 7 7 9 9 11)
 echo "loopfile=$loopfile"

echo "#=========================================================================<<<"

local_env=true
