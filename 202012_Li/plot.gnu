colors='black red blue green cyan magenta yellow'
set term pdfcairo font "Arial,25" size 6*1,5*1
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
set encoding iso_8859_1
#===============================[]
if (1==2) {
workhome0="~/tianff/202012_Li/server/Li-bcc-001p16sn_Li2O-fcc-001p9s2/"
set output workhome0."Li_Li2O.pdf"
set xlabel "Li layers" offset 0,0
set ylabel "Interface energy (meV/{\305}^2)" offset 1,0
set xrange [-0.5:6.5]
set yrange [:]
set key c r
set key width -1
p \
workhome0.'myresult.dat' u 1:2:(0.05) w lp lc ''.word(colors,1) pt 6 lw 2 t 'My results',\
workhome0.'2020_zheng.dat' u 1:2:(0.08) w circle lc ''.word(colors,2) lw 2 t 'H.Zheng et al. (2020)',\
workhome0.'2018_fan.dat' u 1:2:(0.08) w circle lc ''.word(colors,3) lw 2 t 'X.Fan et al. (2018)',\
workhome0.'2015_lepley.dat' u 1:2:(0.08) w circle lc ''.word(colors,4) lw 2 t "N.D.Lepley et al. (2015)"
unset output
}
#===============================[]
if (1==1) {
workhome0="~/tianff/202012_Li/server/Li-bcc-001p15sn_Li2CO3-001p4s2/"
set output workhome0."Li_Li2CO3.pdf"
set xlabel "Li layers" offset 0,0
set ylabel "Interface energy (meV/{\305}^2)" offset 1,0
set xrange [-0.5:6.5]
set yrange [-42:62]
p \
workhome0.'myresult.dat' u 1:2:(0.05) w lp lc ''.word(colors,1) pt 6 lw 2 t 'Myresult',\
workhome0.'2020_zheng.dat' u 1:2:(0.08) w circle lc ''.word(colors,2) lw 2 t 'H.Zheng et al. (2020)',\
workhome0.'2018_fan.dat' u 1:2:(0.08) w circle lc ''.word(colors,3) lw 2 t 'X.Fan et al. (2018)'
unset output
}
