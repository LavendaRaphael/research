colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

mode=1
#===============================[]
if (mode==1) {
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
unset key
#set yrange [:]
p for [i=17:32] \
workhome0.'O_'.i.'/CORE_DIELECTRIC_IMAG.dat' w l
}
