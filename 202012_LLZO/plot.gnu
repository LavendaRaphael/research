array pic[100]
do for [i=1:100] {pic[i]=0}

# pic[3]=1   # goto_llzo_log.'Li7La3Zr2O12/Li7La3Zr2O12.a1b1c1_eosfit/eosfit.pdf'
 pic[4]=1   # goto_llzo_log.'Li/Li_sigma.pdf'
# pic[2]=1   # goto_llzo_log.'Li/Li.a1b1c1_eosfit/eosfit.pdf'
# pic[1]=1   # goto_llzo_log.'Au/Au.a1b1c1_eosfit/eosfit.pdf'


array colors2=['#FE7D6A', '#81B8E9']
array colors3=['#4D85BD', '#F7903D', '#59A95A']
array colors3_1=['#D22027', '#384589', '#7FA5B7']
array colors4=['#817F00','#FB7E03','#01FD01','#00FFFF']
array colors6=['#EE3624','#323293','#62BB47','#BC8EC0','#8EDAF8','#C7811F']

set samples 500
# set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
set encoding iso_8859_1
set style data lines

homedir="~/"
goto_llzo=homedir.'group/202012_LLZO/server/'
goto_llzo_log=homedir.'group/202012_LLZO/log/server/'
#=================================================================================================================================

#-------------------------------------------------------------------------------------[]
#if (pic[4]==1) {
outfile=goto_llzo_log.'Li/Li_sigma.pdf'

$Mydata << EOD
10  -.18399986E+02
20  -.37458456E+02
30  -.56535583E+02
40  -.75607528E+02
EOD

S=3.43560900**2
f(x)=2*S*b+x*a
fit f(x) $Mydata via a,b

titlnum=2
array titl[titlnum]
titl[1]='Computational Data'
titl[2]='Linear fit'

colornum=titlnum
array colo[colornum]
do for [i=1:colornum] {
    if (colornum==1) {colo[i]='black'}
    if (colornum==2) {colo[i]=colors2[i]}
    if (colornum==3) {colo[i]=colors3[i]}
    if (colornum==4) {colo[i]=colors4[i]}
    if (colornum==5 || colornum==6) {colo[i]=colors6[i]}
}

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "N: Number of Li " offset 0,0
set ylabel "Energy (eV)" offset 3,0
set xrange [5:45]
set yrange [*:*]
set format x "%7.0f"
set format y "%7.0f"
set style line 1 lw 2
set key t r

p \
    $Mydata w p pt 6 lw 2 lc ''.colo[1] t titl[1],\
    f(x) ls 1 lc ''.colo[2] t titl[2]
#}

#-------------------------------------------------------------------------------------[]
if (pic[3]==1) {
outfile=goto_llzo_log.'Li7La3Zr2O12/Li7La3Zr2O12.a1b1c1_eosfit/eosfit.pdf'

datdir=goto_llzo.'Li7La3Zr2O12/Li7La3Zr2O12.a1b1c1_eosfit/'
datfile=datdir.'E0_a.dat'

titlnum=2
array titl[titlnum]
titl[1]='Computational Data'
titl[2]='Vinet EOS'

colornum=titlnum
array colo[colornum]
do for [i=1:colornum] {
    if (colornum==1) {colo[i]='black'}
    if (colornum==2) {colo[i]=colors2[i]}
    if (colornum==3) {colo[i]=colors3[i]}
    if (colornum==4) {colo[i]=colors4[i]}
    if (colornum==5 || colornum==6) {colo[i]=colors6[i]}
}

#set term X11 persist
set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "Energy (eV)" offset 1,0
set xrange [*:*]
set yrange [*:*]
set format x "%7.0f"
set format y "%7.0f"
set style line 1 lw 2
set key t c

E0_4=-1376.694078
B0_4=0.598558
Bp_4=5.705120
V0_4=2229.599271
EOS_Vinet(v) = E0_4 + 2.0*B0_4*V0_4/(Bp_4-1.0)**2 * (2.0 - (5.0 + 3.0*Bp_4*((v/V0_4)**(1.0/3.0)-1.0) - 3.0*(v/V0_4)**(1.0/3.0))*exp(-3.0*(Bp_4-1.0)*((v/V0_4)**(1.0/3.0)-1.0)/2.0))

p \
datfile u ($1**3):6 w p pt 6 lw 2 lc ''.colo[1] t titl[1],\
EOS_Vinet(x) ls 1 lc ''.colo[2] t titl[2]
}

#-------------------------------------------------------------------------------------[]
if (pic[2]==1) {
outfile=goto_llzo_li_log.'Li.a1b1c1_eosfit/eosfit.pdf'

array datdir[1]
datdir[1]=goto_llzo_li.'Li.a1b1c1_eosfit/'
array datfile[1]
datfile[1]=datdir[1].'E0_a.dat'

titlnum=2
array titl[titlnum]
titl[1]='Computational Data'
#titl[2]='Murnaghan EOS'
#titl[3]='Birch-Murnaghan EOS'
#titl[4]='Birch EOS'
titl[2]='Vinet EOS'

colornum=titlnum
array colo[colornum]
do for [i=1:colornum] {
    if (colornum==1) {colo[i]='black'}
    if (colornum==2) {colo[i]=colors2[i]}
    if (colornum==3) {colo[i]=colors3[i]}
    if (colornum==4) {colo[i]=colors4[i]}
    if (colornum==5 || colornum==6) {colo[i]=colors6[i]}
}

#set term X11 persist
set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "Energy (eV)" offset 1,0
set xrange [*:*]
set yrange [*:*]
set format x "%7.0f"
set format y "%7.2f"
set style line 1 lw 2
set key t c

#E0_1=-3.813343
#B0_1=0.085085
#Bp_1=3.321246
#V0_1=40.539219
#EOS_Murnaghan(v) = E0_1 + B0_1/Bp_1 * v * ((V0_1/v)**Bp_1/(Bp_1-1.0)+1.0) - V0_1*B0_1/(Bp_1-1.0)
#E0_2=-3.814797
#B0_2=0.092027
#Bp_2=1.204131
#V0_2=40.659714
#EOS_Birch_Murnaghan(v) = E0_2 + 9.0*B0_2*V0_2/16.0* ((v/V0_2)**(2.0/3.0)-1.0)**2.0 * (6.0 + Bp_2*((v/V0_2)**(2.0/3.0)-1.0) - 4.0*(v/V0_2)**(2.0/3.0))
#E0_3=-3.813792
#B0_3=0.087309
#Bp_3=3.285432
#V0_3=40.547295
#EOS_Birch(v) = (E0_3 + 9.0/8.0*B0_3*V0_3*((V0_3/v)**(2.0/3.0) - 1.0)**2 + 9.0/16.0*B0_3*V0_3*(Bp_3-4.)*((V0_3/v)**(2.0/3.0) - 1.0)**3)
E0_4=-3.813804
B0_4=0.087357
Bp_4=3.264353
V0_4=40.551894
EOS_Vinet(v) = E0_4 + 2.0*B0_4*V0_4/(Bp_4-1.0)**2 * (2.0 - (5.0 + 3.0*Bp_4*((v/V0_4)**(1.0/3.0)-1.0) - 3.0*(v/V0_4)**(1.0/3.0))*exp(-3.0*(Bp_4-1.0)*((v/V0_4)**(1.0/3.0)-1.0)/2.0))

p \
datfile[1] u ($1**3):6 w p pt 6 lw 2 lc ''.colo[1] t titl[1],\
EOS_Vinet(x) ls 1 lc ''.colo[2] t titl[2]
}
#-------------------------------------------------------------------------------------[]
if (pic[1]==1) {
outfile=goto_llzo_au_log.'Au.a1b1c1_eosfit/eosfit.pdf'

array datdir[1]
datdir[1]=goto_llzo_au.'Au.a1b1c1_eosfit/'
array datfile[1]
datfile[1]=datdir[1].'E0_a.dat'

titlnum=2
array titl[titlnum]
titl[1]='Computational Data'
#titl[2]='Murnaghan EOS'
#titl[3]='Birch-Murnaghan EOS'
#titl[4]='Birch EOS'
titl[2]='Vinet EOS'

colornum=titlnum
array colo[colornum]
do for [i=1:colornum] {
    if (colornum==1) {colo[i]='black'}
    if (colornum==2) {colo[i]=colors2[i]}
    if (colornum==3) {colo[i]=colors3[i]}
    if (colornum==4) {colo[i]=colors4[i]}
    if (colornum==5 || colornum==6) {colo[i]=colors6[i]}
}

#set term X11 persist
set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "Energy (eV)" offset 1,0
set xrange [*:*]
set yrange [*:*]
set format x "%7.0f"
set format y "%7.2f"
set style line 1 lw 2
set key t c

#E0_1=-12.842750
#B0_1=0.812546
#Bp_1=5.632738
#V0_1=71.980538
#EOS_Murnaghan(v) = E0_1 + B0_1/Bp_1 * v * ((V0_1/v)**Bp_1/(Bp_1-1.0)+1.0) - V0_1*B0_1/(Bp_1-1.0)
#E0_2=-3.814797
#B0_2=0.092027
#Bp_2=1.204131
#V0_2=40.659714
#EOS_Birch_Murnaghan(v) = E0_2 + 9.0*B0_2*V0_2/16.0* ((v/V0_2)**(2.0/3.0)-1.0)**2.0 * (6.0 + Bp_2*((v/V0_2)**(2.0/3.0)-1.0) - 4.0*(v/V0_2)**(2.0/3.0))
#E0_3=-12.857752
#B0_3=0.865020
#Bp_3=5.958122
#V0_3=71.778272
#EOS_Birch(v) = (E0_3 + 9.0/8.0*B0_3*V0_3*((V0_3/v)**(2.0/3.0) - 1.0)**2 + 9.0/16.0*B0_3*V0_3*(Bp_3-4.)*((V0_3/v)**(2.0/3.0) - 1.0)**3)
E0_4=-12.860871
B0_4=0.875547
Bp_4=6.013859
V0_4=71.744824
EOS_Vinet(v) = E0_4 + 2.0*B0_4*V0_4/(Bp_4-1.0)**2 * (2.0 - (5.0 + 3.0*Bp_4*((v/V0_4)**(1.0/3.0)-1.0) - 3.0*(v/V0_4)**(1.0/3.0))*exp(-3.0*(Bp_4-1.0)*((v/V0_4)**(1.0/3.0)-1.0)/2.0))

p \
datfile[1] u ($1**3):6 w p pt 6 lw 2 lc ''.colo[1] t titl[1],\
EOS_Vinet(x) ls 1 lc ''.colo[2] t titl[2]
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
