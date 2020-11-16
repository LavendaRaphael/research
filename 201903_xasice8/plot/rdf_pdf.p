reset
set term pdfcairo font "Arial,12"
set output 'OO.pdf'

set xlabel 'Distance r(bohr)'
set ylabel 'gOO(r)'
set key box width 2 height 1
set key samplen 2
p [0:20] [-1:] '/home/tianff/201903/tianff/rdf/snap00_OO_rdf.dat' w l lw 0.5 lc 'blue' t "snap00",\
'/home/tianff/201903/tianff/rdf/snap32960_OO_rdf.dat' w lp ps 0.3 lw 0.5 lc 'red' t 'snap32960',\
'/home/tianff/201903/tianff/rdf/disorder_OO_rdf.dat' w p ps 0.3 lc 'black' t 'disorder',1

unset output
