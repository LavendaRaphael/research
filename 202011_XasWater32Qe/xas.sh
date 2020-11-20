#!/bin/bash
set -euo pipefail
source ~/tianff/codes/202011_XasWater32Qe/local_env.sh
jobname=xasxNUMx
#========================================[myserver]
if [ "$myserver" = "SHTU" ]; then
    jobqueue=sbp_1
elif [ "$myserver" = "KUNLUN" ]; then
    jobnodes=1
    jobppn=6
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

set -euo pipefail
source ~/tianff/codes/common/environment.sh
SECONDS=0

cp ${Oxygen1swf_dir}fort.* ./

${xascodes_bin}diag_lambda.x
tail -${cbands}  eig.dat > eigc.dat
mpirun ${xascodes_bin}xas.x > xas.out
${xascodes_bin}tmsft.x
${xascodes_bin}tmsftbroad.x

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof
