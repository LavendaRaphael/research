colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

mode=2
#===============================[]
if (mode==2) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
set output workhome0."../log/eig_O.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Oxygen" offset 0,0
set ylabel "GAP (eV)" offset 1,0
#set xrange [:]
#unset key
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
workhome1='~/tianff/202011_XasWater32Vasp/server/'
set output workhome0."../log/XasWater32.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:550]
#unset key
#set yrange [0:]
p \
workhome0.'pbe/tmsftbroadave.dat' w l lw 3 lc ''.word(colors,2) t 'PBE',\
workhome0.'cohsex/tmsftbroadave.dat' w l lw 3 lc ''.word(colors,3) t 'COHSEX'
}
