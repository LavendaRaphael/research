colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

mode=1
#===============================[]
if (mode==1) {
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
#set xrange [532:546]
#unset key
#set yrange [0:]
p \
workhome0.'pbe/tmsftbroadave.dat' w l lw 3 lc ''.word(colors,2) t 'PBE' 
#p \
workhome0.'pbe/tm_tt.dat' u 1:3:(0.25) w circle
#p for [i=1:32] \
workhome0.'pbe/Oxygen_'.i.'/tm.dat' every ::1::2 u (i):2 t ''.i
}
