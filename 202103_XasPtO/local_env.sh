#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/common/environment.sh

if [ ! -z ${local_env+x} ]; then
if $local_env;then
    return
fi
fi
local_env=false
echo "---------------------------------------------------------------------------[~/tianff/codes/202011_XasWater32Vasp/local_env.sh]"

  work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas_hch/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas_hch/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/
# work_dir=${homedir}group/202103_XasPtO/server/Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/
echo "work_dir=$work_dir"

# O_num=$(awk 'NR-7==0 {print $1}' ${work_dir}template/POSCAR)
# echo "O_num=$O_num"

# sub_dir="xspectra/"
# sub_dir="xspectra.epsilon010/"
# sub_dir="xspectra.epsilon100/"
sub_dir="xspectra.epsilon110/"
# sub_dir="xspectra.epsilon1-10/"
echo "sub_dir=$sub_dir"

  subfile=xspectra_sub.sh
# subfile=job_sub.sh
# subfile=scf_sub.sh
echo "subfile=$subfile"

# loopfile="1"
# loopfile=`seq 1 $O_num`
  loopfile="1 3 5 7 9 11"
echo "loopfile=$loopfile"
echo "#=========================================================================<<<"

local_env=true
