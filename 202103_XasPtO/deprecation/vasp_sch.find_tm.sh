#!/bin/bash 
set -euo pipefail

peak_energy=529.6647579888
peak_bottom=0.001
peak_radius=0.5
peak_energy=531.7059162567
peak_bottom=0.0007
peak_radius=0.5
peak_energy=534.9951163806
peak_bottom=0.0007
peak_radius=0.6
awk '
    (($1-"'$peak_energy'"+"'$peak_radius'">0) && ($1-"'$peak_energy'"-"'$peak_radius'"<0) && ($2-"'$peak_bottom'">0 || $3-"'$peak_bottom'">0)) || ($2=="Transition") {
        print $0
    }
' xas.tm_align.dat

