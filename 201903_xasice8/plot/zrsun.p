workhome='/public/spst/home/tianff/tianff/201903/zrsun/xas-ice8/ice8/'
reset

#set term pdfcairo font "Arial,12"
#set output 'zrsun.pdf'
set term svg font "Arial-Bold,15" size 800,500
set output 'zrsun.svg'

set xlabel 'Energy (eV)'
set ylabel 'Intensity (Arb. Units)'
set key box width 2 height 1
set key samplen 2

#p [532:546] [0:35]\
workhome.'ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Pylkkanen',\
workhome.'xas-snap00/tmsftbroadave.dat' w l lw 2 lc 'red' t 'snap00',\
workhome.'xas-snap23595/ice8-289K.dat' w l lw 2 lc 'yellow' t 'snap23595',\
workhome.'xas-snap32960/tmsftbroadave.dat' w l lw 2 lc 'blue' t 'snap32960'

p [532:546] [0:25] \
workhome.'plt-figures/ice8expallsftNormsft.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Pylkkanen\_sft',\
workhome.'plt-figures/Kong-ice8Normsft.dat' w l lw 2 lc 'green' t 'Kong\_sft' ,\
workhome.'plt-figures/ice8-271K.dat' w l lw 2 lc 'red' t '271K',\
workhome.'plt-figures/ice8-286K.dat' w l lw 2 lc 'blue' t '286K',\
workhome.'xas-snap23595/ice8-289K.dat' w l lw 2 lc 'brown' t '289K'

#p [532:546] [0:25] \
workhome.'plt-figures/ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Pylkkanen',\
workhome.'plt-figures/Kong-ice8Norm.dat' w l lw 2 lc 'green' t 'Kong' ,\
workhome.'plt-figures/ice8-286Ksft.dat'  w l lw 2 lc 'blue' t '286K\_sft'

#p [532:546] [0:35]\
workhome.'ice8expallsftNorm.dat' u 1:2:(0.05) w circle lw 2 lc 'black' t 'Pylkkanen',\
workhome.'xas-snap32960/tmave10.dat' w l lw 2 lc 'red' t '10',\
workhome.'xas-snap32960/tmave32.dat' w l lw 2 lc 'green' t '32',\
workhome.'xas-snap32960/tmsftbroadave.dat' w l lw 2 lc 'blue' t '64'

#unset output
#pause -1
