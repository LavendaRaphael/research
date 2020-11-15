workhome='./'
colors='black red blue green brown'
set term persist

set term x11 persist
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

#set output 'x.svg'
set xrange []
set yrange []
#p \
workhome.'exp.dat.norm' u 1:2:(0.05) w circle lw 2 lc ''.word(colors,1) t 'Exp.',\
workhome.'fch.dat.norm' w l lw 2 lc ''.word(colors,2) t 'FCH',\
workhome.'cohsex.dat.norm' w l lw 2 lc ''.word(colors,3) t 'COHSEX'

