#!/bin/bash
for i in *; do
if [ -e $i/OUTCAR ]; then
echo -e  $i "\t" $(grep '  without' $i/OUTCAR |tail -n 1 | awk '{print $7}')
fi
done
