#!/bin/bash
set -euo pipefail

jobname=tff.${jobname}
echo "jobname=${jobname}"
echo "ncore=$ncore"
jobnodes=$[($ncore/$maxppn)+($ncore%$maxppn>0)]
echo "jobnodes=$jobnodes"
jobppn=$[($ncore/$jobnodes)+($ncore%$jobnodes>0)]
echo "jobppn=$jobppn"

str_nodefile=${jobname}.nodelist
#========================================[mycluster]
if [ "$mycluster" = "qsub" ]; then
    cat > ${jobname}.sh <<eof
#!/bin/bash
#PBS -l nodes=${jobnodes}:ppn=${jobppn}
#PBS -l walltime=240:00:00
#PBS -N ${jobname}
#PBS -q ${jobqueue}
#PBS -j oe
cd \$PBS_O_WORKDIR
cat \$PBS_NODEFILE > ${str_nodefile}
eof

elif [ "$mycluster" = "sbatch" ]; then
    cat > ${jobname}.sh <<eof
#!/bin/bash
#SBATCH -N ${jobnodes}
#SBATCH --ntasks-per-node=${jobppn}
#SBATCH -J ${jobname}
#SBATCH -p ${jobqueue}
#SBATCH -o %x.oe%j
cat \$SLURM_JOB_NODELIST > ${str_nodefile}
eof

elif [ "$mycluster" = "bsub" ]; then
    cat > ${jobname}.sh <<eof
#!/bin/bash
#BSUB -q ${jobqueue}
#BSUB -n ${ncore}
#BSUB -J ${jobname}
eof

else
    echo "ERROR: 'mycluster' not exist!"
    exit
fi

#=========================================================[head]
cat >>${jobname}.sh<<eof
source ${homedir}codes/common/environment.sh
set -euo pipefail
SECONDS=0
sort -u ${str_nodefile} > tmp && mv tmp ${str_nodefile}

eof


