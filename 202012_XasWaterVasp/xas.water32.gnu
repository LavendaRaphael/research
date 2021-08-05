colors='black red blue green cyan magenta yellow'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle

workhome1="~/tianff/202011_XasWater32Qe/server/"
workhome0="~/tianff/202011_XasWater32Vasp/server/"
#===============================[]
if (1==1) {
set output workhome0."../log/XasWater32.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:546]
set yrange [0:20]
p \
workhome1.'../asist/zrsun/20201130_Expt_ambient.dat' u 1:2:(0.05) w circle lc ''.word(colors,1) t 'Exp.',\
workhome1.'cohsex/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,3) t 'COHSEX',\
workhome0.'xas_alignorm_nosft.dat' w l lw 3 lc ''.word(colors,2) t 'SCH'
}
#===============================[]
if (0==1) {
set output workhome0."../log/XasWater32.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:546]
set yrange [0:20]
p \
workhome1.'../asist/zrsun/20201130_Expt_ambient.dat' u 1:2:(0.05) w circle lc ''.word(colors,1) t 'Exp.',\
workhome1.'pbe/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,2) t 'PBE',\
workhome1.'cohsex/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,3) t 'COHSEX',\
workhome0.'xas_alignorm_nosft.dat' w l lw 3 lc ''.word(colors,4) t 'SCH',\
}
#===============================[]
if (0==1) {
set output workhome0."../log/xasft_O.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [514:530]
#set yrange [:]
p for [i=1:32] \
workhome0.'O_'.i.'/xas_sft.dat' w l
}
#===============================[]
if (1==1) {
set output workhome0."../log/XasWater32_sft.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:546]
set yrange [0:20]
p \
workhome1.'../asist/zrsun/20201130_Expt_ambient.dat' u 1:2:(0.05) w circle lc ''.word(colors,1) t 'Exp.',\
workhome1.'pbe/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,2) t 'PBE',\
workhome1.'cohsex/tmsftbroadalignorm_all.dat' w l lw 3 lc ''.word(colors,3) t 'COHSEX',\
workhome0.'xas_alignorm_nosft.dat' w l lw 3 lc ''.word(colors,4) t 'SCH\_nosft',\
workhome0.'xas_alignorm.dat' w l lw 3 lc ''.word(colors,5) t 'SCH\_sft'
}
#===============================[]
if (0==1) {
set output workhome0."../log/xasnosft_O.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [514:528]
unset yrange
p for [i=1:32] \
workhome0.'O_'.i.'/CORE_DIELECTRIC_IMAG.dat' w l
}
