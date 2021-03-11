colors='black red blue green cyan magenta yellow'
set term pdfcairo font "Arial,25" size 6*1,5*1
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
set encoding iso_8859_1

#-------------------------------------[]
if (4==4) {
workhome0="~/tianff/202012_LLZO/server/Li-bcc-001p1sn_vac/"
set term pdfcairo font "Arial,25" size 8*1,5*1
set output workhome0."Li_sigma.pdf"
set xlabel "N: Number of Li " offset 0,0
set ylabel "Energy (eV)" offset 3,0
set xrange [:]
set yrange [:]
set format x "%7.0f"
set format y "%7.0f"
set key t r
set key width 0
S=11.867
f(x)=2*S*b+x*a
fit f(x) workhome0."e0_n.dat" using 1:2 via a,b
p \
workhome0.'e0_n.dat' u 1:2:(0.5) w circle lc ''.word(colors,1) lw 2 t 'Computational Data',\
f(x) w l lc ''.word(colors,2) lw 2 t sprintf("E_{slab}=2*%2.3f*%2.4f+N*(%2.2f)",S,b,a)
unset output
}
#-------------------------------------[]
if (0==3) {
workhome0="~/tianff/202012_LLZO/server/Li-bcc-bulk/cellopt/"
set output workhome0."Li_eos.pdf"
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "Energy (eV)" offset 1,0
set xrange [:]
set yrange [:]
set format x "%7.1f"
set format y "%7.4f"
set key t r
set key width 0
E0=-3.780752
B0=13.830743/160.21765
Bp=0.532870
V0=40.880362
f(v) = E0 + 9.0*B0*V0/16.0* ((v/V0)**(2.0/3.0)-1.0)**2.0 * (6.0 + Bp*((v/V0)**(2.0/3.0)-1.0) - 4.0*(v/V0)**(2.0/3.0))
p \
workhome0.'e0_a.dat' u ($1**3):6:(0.015) w circle lc ''.word(colors,1) lw 2 t 'Computational Data',\
f(x) w l lc ''.word(colors,2) lw 2 t "Birch-Murnaghan EOS"
unset output
}
#-------------------------------------[]
if (0==2) {
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
#-------------------------------------[]
if (0==1) {
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
