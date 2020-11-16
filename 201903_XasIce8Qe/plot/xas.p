workhome='~/tianff/201903/tianff/'
colors='black red blue green brown'

#set term pdfcairo font "Arial,12"
set term svg font "Arial-Bold,25" size 800,500

#set xlabel ' '
#set ylabel ' '
#set label 'Energy (eV)' at 539,-6 center
#set label 'Intensity (Arb. Units)' at 530.5,17.5 center rotate
set xlabel 'Energy (eV)'
set ylabel 'Intensity (Arb. Units)'
set key box
set key samplen 2

#set output 'chenw.svg'
#p [532:546] [0:2.5]\
workhome.'../chenw/wernet2004_water.dat.norm' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'../chenw/chenw2009_water_fch.dat.norm' w l lw 2 lc ''.word(colors,2) t 'FCH',\
workhome.'../chenw/chenw2009_water_cohsex.dat.norm' w l lw 2 lc ''.word(colors,3) t 'COHSEX'

#set output 'md.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Exp.',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc 'red' t '0K',\
workhome.'../zrsun/xas-ice8/ice8/xas-snap32960/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t '271K'

#set output 'COHSEX.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Exp.',\
workhome.'xas_snap00_PBE/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t 'DFT',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t '(es)COHSEX'

#set output 'DFT.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Exp.',\
workhome.'xas_snap00_PBE/tmsftbroadave.dat' w l lw 2 lc 'red' t 'DFT'

#set output 'epsilon0.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Exp.',\
workhome.'epsilon0_1.7+alpha0_1.563_xas_snap00/tmsftbroadave.dat' w l lw 2 lc 'red' t '{/Symbol e}_0=1.7,{/Symbol a}=1.563',\
workhome.'epsilon0_3.0+alpha0_1.563_xas_snap00/tmsftbroadave.dat' w l lw 2 lc 'blue' t '{/Symbol e}_0=3.0,{/Symbol a}=1.563'

#set output 'alpha.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'epsilon0_3.0+alpha0_2.3_xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t '{/Symbol e}_0=3.0,{/Symbol a}=2.30',\
workhome.'epsilon0_3.0+alpha0_1.563_xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t '{/Symbol e}_0=3.0,{/Symbol a}=1.563',\
workhome.'epsilon0_3.0+alpha_xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,4) t '{/Symbol e}_0=3.0,{/Symbol a}=1.24'

#set output 'dielect.svg'
#p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t '{/Symbol e}_0=1.7,{/Symbol a}=2.30',\
workhome.'xas_snap00_epsilon0_3.0+alpha_1.242.bak/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t '{/Symbol e}_0=3.0,{/Symbol a}=1.24,bak',\
workhome.'xas_snap00_epsilon0_3.0+alpha/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,4) t '{/Symbol e}_0=3.0,{/Symbol a}',\
workhome.'xas_snap00_epsilon0_3.0+alpha_1.242/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,5) t '{/Symbol e}_0=3.0,{/Symbol a}=1.24'

set output 'dielect.svg'
p [532:546] [0:35] \
workhome.'../zrsun/xas-ice8/ice8/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'xas_snap00/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,2) t '{/Symbol e}_0=1.7,{/Symbol a}=2.30',\
workhome.'xas_snap00_epsilon0_3.0+alpha_2.3/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,3) t '{/Symbol e}_0=3.0,{/Symbol a}=2.30',\
workhome.'xas_snap00_epsilon0_3.0+alpha_1.242/tmsftbroadave.dat' w l lw 2 lc ''.word(colors,4) t '{/Symbol e}_0=3.0,{/Symbol a}=1.24'

#pause -1
#unset output
