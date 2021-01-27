#!/bin/bash
# 2021.01.27
if [ ! -z ${environment+x} ]; then
if [ "$environment" == 'pass' ] ;then
    return
fi
fi
echo "------------------------------------[~/tianff/codes/common/environment.sh]"

#---------------------------------------------[vim]
export VIMINIT='source ~/tianff/codes/common/vimrc.vim'
#---------------------------------------------[alias]
cdl() {
    cd "${1}";
    ll -a;
}
alias cpi="cp -i"
#---------------------------------------------[dir]
software_bin=~/tianff/software/bin/
echo "software_bin="${software_bin}
vasp_pot=~/tianff/software/vasp/potpaw_PBE.54/
echo "vasp_pot=${vasp_pot}"
#---------------------------------------------[myserver]
source ~/tianff/server/server.sh

environment='pass'
echo "========================================================================="
