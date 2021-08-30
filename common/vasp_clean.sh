#!/bin/bash
set -euo pipefail

 filelist=(CHG CHGCAR CONTCAR DOSCAR EIGENVAL exts.dat fe.dat IBZKPT INCAR KPOINTS mep.eps movie movie.vasp neb.dat nebef.dat nodelist.log OSZICAR OUTCAR PCDAT POSCAR POSCAR.vasp POSCAR.xyz POTCAR PROCAR REPORT spline.dat stdout STOPCAR tff\* vaspgr vasprun.xml vasp.log vdw_kernel.bindat WAVECAR XDATCAR \*_sub.sh)
#    mode=(0   0      0       0      0        0        0      0      0     0       0       0     0          0       0         0            0       0      0     0      0           0          0      0      0      0          0      0       0     0      0           0        0                 0       0       0       ) # all
#    mode=(0   0      1       0      0        0        0      0      1     1       0       0     0          0       0         0            0       0      0     1      0           0          0      0      0      0          0      0       0     0      0           1        0                 0       0       0       ) # posopt
#    mode=(0   0      0       0      0        0        0      0      1     0       0       0     0          0       0         0            0       1      0     1      0           0          0      0      0      0          0      0       0     0      0           1        0                 0       0       0       ) # sch
     mode=(0   0      0       0      0        0        0      0      1     1       0       0     0          0       0         0            0       0      0     1      0           0          1      0      0      0          0      0       0     0      0           0        0                 0       0       1       ) # init


j=0
for x in ${mode[@]}
do
    if [ "$x" == "0" ]
    then
        rm -rf ${filelist[$j]}
        rm -rf 0*/${filelist[$j]}
        #rm -rf */${filelist[$j]}
    else
        echo "save $j ${filelist[$j]}"
    fi
    j=$((j+1))
done
