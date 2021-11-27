colors='black red blue green cyan magenta yellow'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

mode=0
#===============================[]
if (mode==5) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/tmsftbroad_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
#set xrange [:]
unset key
#set yrange [:]
p for [i=1:32] \
workhome0.'pbe/Oxygen_'.i.'/tmsftbroad.dat' w l
}
#===============================[]
if (mode==4) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/tmsft_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
#set xrange [:]
unset key
#set yrange [:]
p for [i=1:32] \
workhome0.'pbe/Oxygen_'.i.'/tmsft.dat' w l
}
#===============================[]
if (mode==3) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/tm_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
#set xrange [:]
unset key
#set yrange [:]
p for [i=1:32] \
workhome0.'pbe/Oxygen_'.i.'/tm.dat' w l
}
#===============================[]
if (mode==2) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/eig_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
#unset key
set key c r
set xlabel "Oxygen" offset 0,0
set ylabel "GAP (eV)" offset 1,0
#set xrange [:]
#set yrange [:]
p \
workhome0.'pbe/eig_O.dat' u 1:($10-$9):(0.25)  w circle lw 3 lc ''.word(colors,2) t 'PBE',\
workhome0.'cohsex/eig_O.dat' u 1:($10-$9):(0.25) w circle lw 3 lc ''.word(colors,3) t 'COHSEX'
}
#===============================[]
if (mode==1) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/tml1_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Oxygen" offset 0,0
set ylabel "tm.dat line1 Intensity (Arb. Units)" offset 1,0
#set xrange [:]
#unset key
#set yrange [:]
p \
workhome0.'pbe/tml1_O.dat' u 1:3:(0.25) w circle lc ''.word(colors,2) t 'PBE',\
workhome0.'cohsex/tml1_O.dat' u 1:3:(0.25) w circle lc ''.word(colors,3) t 'COHSEX'
}

#===============================[]
if (mode==0) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/XasWater.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:546]
set yrange [0:20]
p \
workhome0.'../asist/zrsun/20201130_Expt_ambient.dat' u 1:2:(0.05) w circle lc ''.word(colors,1) t 'Exp.',\
workhome0.'../asist/zrsun/20201201_XasWater32.dat.norm' w l lw 3 lc ''.word(colors,2) t 'COHSEX\_zrsun',\
workhome0.'pbe/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,3) t 'PBE\_all',\
workhome0.'cohsex/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,4) t 'COHSEX\_all',\
workhome0.'pbe/tmsftbroadalignorm_no8.dat' w l lw 3 lc ''.word(colors,5) t 'PBE\_no8',\
workhome0.'cohsex/tmsftbroadalignorm_no8.dat' w l lw 3 lc ''.word(colors,6) t 'COHSEX\_no8'
}
