import subprocess
import os

subprocess_qstat = subprocess.run( args=['qstat -f ${PBS_JOBID}|grep exec_gpus'], shell=True ,stdout=subprocess.PIPE, encoding="utf-8")
list_gpu = subprocess_qstat.stdout.split(' ')[-1][:-1].split('+')
print( list_gpu[ int(os.environ['CUDA_VISIBLE_DEVICES']) ].split('/')[-1] )
