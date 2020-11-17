workhome='~/tianff/201903/'
colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term svg font "Arial-Bold,25" size 800,650

#set xlabel ' '
#set ylabel ' '
#set label 'Energy (eV)' at 539,-6 center
#set label 'Intensity (Arb. Units)' at 530.5,17.5 center rotate
set xlabel 'Energy (eV)'
set ylabel 'Intensity (Arb. Units)'
set key box
set key samplen 2

set output 'xasice8_vasp.svg'
p [532:546] [0:45]\
workhome.'asist/zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t 'COHSEX',\
workhome.'vasp/0k_mod/CORE_DIELECTRIC_IMAG.dat.norm' w l lw 2 lc ''.word(colors,3) t 'VASP, CH\_SIGMA=0.4',\
workhome.'vasp/0k_mod/tmsftbroad.dat.norm' w l lw 2 lc ''.word(colors,4) t 'VASP\_mod, GAUSSIAN\_SIGMA=0.4'

#pause -1
