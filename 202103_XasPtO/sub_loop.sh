#!/bin/bash
set -euo pipefail
homedir=`find ~ -maxdepth 3 -name "server.me.sh" -print -quit|xargs dirname`/
source ${homedir}codes/groupcodes/202103_XasPtO/local_env.sh

cd $work_dir
for N in $loopfile
do
	echo $N
	cd O_${N}/
	sed -i "s/xNUMx/$N/g"  $subfile
	./$subfile
    rm ${subfile}
	cd ../
done
