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
  work_dir=${gotowork_3}vasp_sch/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/aimd2000.qe_fch_scf/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/aimd2000.qe_hch_scf/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_fch_scf/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/vasp_sch/

echo "work_dir=$work_dir"

# O_num=$(awk 'NR-7==0 {print $1}' ${work_dir}template/POSCAR)
# echo "O_num=$O_num"
# O_num=4

# sub_dir="xspectra/"
# sub_dir="xspectra.epsilon010/"
# sub_dir="xspectra.epsilon100/"
# sub_dir="xspectra.epsilon110/"
# sub_dir="xspectra.epsilon1-10/"
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
  loopfile="1 3"
echo "loopfile=$loopfile"

  tensorxyz="X Y Z"
echo "tensorxyz=$tensorxyz"

echo "#=========================================================================<<<"

local_env=true
