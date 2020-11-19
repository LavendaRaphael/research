#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh
source ~/codes/202011_XasWater32Qe/local_env.sh

jobname=gwxNUMx
#========================================[myserver]
if [ "$myserver" = "SHTU" ]; then
    jobqueue=sbp_1
elif [ "$myserver" = "KUNLUN" ]; then
    jobnodes=16
    jobppn=32
    jobqueue=ssct
else
    echo "ERROR: 'myserver' not exist!"
    exit
fi
#========================================[mycluster]
if [ "$mycluster" = "pbs" ]; then
    alias jobsub="qsub"
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#PBS -l nodes=${jobnodes}:ppn=${jobppn}
#PBS -N ${jobname}
#PBS -q ${jobqueue}
cd \$PBS_O_WORKDIR
eof
elif [ "$mycluster" = "sbatch" ]; then
    alias jobsub="sbatch <"
    cat > ${jobname}_sub.sh <<eof
#!/bin/bash
#SBATCH -N ${jobnodes}
#SBATCH --ntasks-per-node=${jobppn}
#SBATCH -J ${jobname}
#SBATCH -p ${jobqueue}
eof
else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi
#========================================[main script]
cat >>${jobname}_sub.sh<<eof

set -eo pipefail
source ~/tianff/codes/common/environment.sh
SECONDS=0

CP=${qe_cohsex_water_bin}cp.x
echo \$CP

mpirun \$CP < gw.in > gw.out

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof
