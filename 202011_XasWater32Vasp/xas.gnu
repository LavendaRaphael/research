colors='black red blue green cyan magenta yellow'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

#===============================[]
if (1==1) {
workhome0="~/tianff/202011_XasWater32Qe/server/"
workhome1="~/tianff/202011_XasWater32Vasp/server/"
set output workhome1."../log/XasWater32.pdf"
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
workhome0.'pbe/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,2) t 'PBE',\
workhome0.'cohsex/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,3) t 'COHSEX',\
workhome1.'xas_alignorm.dat' w l lw 3 lc ''.word(colors,4) t 'SCH'
}
#===============================[]
if (1==2) {
workhome0="~/tianff/202011_XasWater32Vasp/server/"
set output workhome0."../log/xas_O32.pdf"
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [514:528]
#set yrange [:]
set key noautotitle
p for [i=17:32] \
workhome0.'O_'.i.'/CORE_DIELECTRIC_IMAG.dat' w l dt 5,\
workhome0.'xas_ave.dat' w l t "ave"
}
