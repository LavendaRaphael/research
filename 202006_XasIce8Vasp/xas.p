colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term pdfcairo font "Arial-Bold,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 800,500

mode=2
#===============================[]
if (mode==2) {
workhome0=="~/tianff/201903_XasIce8/server/"
workhome1='~/tianff/202011_XasVasp/'
set output workhome1."log/XasIce8.pdf"
set samples 500
unset key
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [532:546]
set yrange [0:]
p \
workhome0.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome0.'xas_snap00_PBE/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t 'PBE',\
workhome0.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t 'COHSEX',\

workhome.'vasp/0k_mod/CORE_DIELECTRIC_IMAG.dat.norm' w l lw 2 lc ''.word(colors,4) t 'VASP, CH\_SIGMA=0.4',\
workhome.'vasp/0k_mod/tmsftbroad.dat.norm' w l lw 2 lc ''.word(colors,5) t 'VASP\_mod, GAUSSIAN\_SIGMA=0.4'

}
#===============================[]
if (mode==1) {
set xlabel 'Energy (eV)'
set ylabel 'Intensity (Arb. Units)'
set key box
set key samplen 2
set output 'xasice8_vasp.svg'
p [532:546] [0:]\
workhome.'asist/zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t 'COHSEX',\
workhome.'vasp/0k_mod/CORE_DIELECTRIC_IMAG.dat.norm' w l lw 2 lc ''.word(colors,3) t 'VASP, CH\_SIGMA=0.4',\
workhome.'vasp/0k_mod/tmsftbroad.dat.norm' w l lw 2 lc ''.word(colors,4) t 'VASP\_mod, GAUSSIAN\_SIGMA=0.4'
}
