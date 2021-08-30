#!/bin/bash
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/group/common/groupenv.sh
set -euo pipefail

rm -f POTCAR

latompot=(H He Li_sv B C N O F Ne Na_pv Mg Al Si P S Cl Ar K_sv Ca_sv Sc_sv Ti_sv V_sv Cr_pv Mn_pv Fe Co Ni Cu Zn Ga_d Ge_d As Se Br Kr Rb_sv Sr_sv Y_sv Zr_sv Nb_sv Mo_sv Tc_pv Ru_pv Rh_pv Pd Ag Cd In_d Sn_d Sb Te I Xe Cs_sv Ba_sv La Ce Pr_3 Nd_3 Pm_3 Sm_3 Eu_2 Gd_3 Tb_3 Dy_3 Ho_3 Er_3 Tm_3 Yb_2 Lu_3 Hf_pv Ta_pv W_sv Re Os Ir Pt Au Hg Tl_d Pb_d Bi_d Po_d At Rn Fr_sv Ra_sv Ac Th Pa U Np Pu Am Cm)

latom=$(awk 'NR-6==0{print $0}' POSCAR)
for iatom in $latom
do
    for iatompot in ${latompot[@]}
    do
        if [ $iatom == $iatompot ] || [[ "${iatom}_"* == $iatompot ]]
        then
            echo "$iatom  $iatompot"
            cat ${vasp_pot}${iatompot}/POTCAR >> POTCAR
            continue 2
        fi
    done
    echo "Vasp pot of $iatom not found!!"
    exit
done

