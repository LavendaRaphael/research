#!/bin/bash
set -eo pipefail
source ~/tianff/codes/common/environment.sh

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

set -eo pipefail
source ~/tianff/codes/common/environment.sh
SECONDS=0

xas_bin=~/tianff/201903/tianff/xas-codes/
cp ~/tianff/201903/tianff/Oxygen-1s-wf/fort.* ./
echo "\${xas_bin}"

\${xas_bin}/diag_lambda.x
tail -256  eig.dat > eigc.dat
mpirun \${xas_bin}/xas.x > xas.out
\${xas_bin}/tmsft.x
\${xas_bin}/tmsftbroad.x

echo "TotalTime \$((\${SECONDS} / 60)) m \$((\${SECONDS} % 60)) s."
eof
