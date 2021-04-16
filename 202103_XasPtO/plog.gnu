colors='black red blue green cyan magenta yellow'
set samples 500
# set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
set encoding iso_8859_1

datdir="~/group/202103_XasPtO/server/"
outdir="~/group/202103_XasPtO/doc/log/Xas_Pt_O_vac/"


#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas_hch/xas_alignorm.dat'
titl1='Pt-111p16\_O4\_vac\_fch'
titl2='Pt-111p16\_O4\_vac\_hch'
outfile=outdir."Pt-111_O_vac/Pt-111p16s4_O4_vac15/Xas.Pt\-111p16_O4_vac.fch_hch.pdf"

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:0.18]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas_hch/xas_alignorm.dat'
titl1='Pt-110p12\_O6\_vac\_fch'
titl2='Pt-110p12\_O6\_vac\_hch'
outfile=outdir."Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/Xas.Pt\-110p12_O6_vac.fch_hch.pdf"

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:0.18]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-111p16\_O4\_vac\_O1'
titl2='Pt-111p48\_O12\_vac\_O1'
outfile=outdir."Pt-111_O_vac/Xas_Pt\-111_O_vac_O1.pdf"

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [512:532]
set yrange [0:9e-5]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/O_2/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-110p12\_O6\_vac\_O1'
titl2='Pt-110p48\_O24\_vac\_O2'
outfile=outdir."Pt-110_O_vac/Xas_Pt\-110_O_vac_O1.pdf"

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [515:535]
set yrange [0:0.00018]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-111p48\_O12\_vac\_ave'
titl2='Pt-111p48\_O12\_vac\_O1'
outfile=outdir."Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/Xas_Pt-111p48_O12_vac.pdf"

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [512:532]
set yrange [0:3e-5]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-111p16\_O4\_vac\_ave'
titl2='Pt-111p16\_O4\_vac\_O1'
outfile=outdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/Xas_Pt-111p16_O4_vac.pdf'

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [512:532]
set yrange [0:9e-5]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/O_2/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-110p48\_O24\_vac\_ave'
titl2='Pt-110p48\_O24\_vac\_O2'
outfile=outdir.'Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/Xas_Pt-110p48_O24_vac.pdf'

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [515:535]
set yrange [0:5e-5]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-110p12\_O6\_vac\_ave'
titl2='Pt-110p12\_O6\_vac\_O1'
outfile=outdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/Xas_Pt-110p12_O6_vac.pdf'

set term pdfcairo font "Arial,25" size 7*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [515:535]
set yrange [0:0.00018]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/xas_alignorm.dat'
titl1='Pt-110p12\_O6\_vac'
titl2='Pt-111p16\_O4\_vac'
outfile=outdir.'Xas_Pt_O_vac.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:0.14]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-110_O_vac/Pt-110p12s4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48s4.5_O24_vac15/xas/xas_alignorm.dat'
titl1='Pt-110p12\_O6\_vac'
titl2='Pt-110p48\_O24\_vac'
outfile=outdir.'Pt-110_O_vac/Xas_Pt-110_O_vac.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:0.14]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {

datfile1=datdir.'Pt-111_O_vac/Pt-111p16s4_O4_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48s4_O12_vac15/xas/xas_alignorm.dat'
titl1='Pt-111p16\_O4\_vac'
titl2='Pt-111p48\_O12\_vac'
outfile=outdir.'Pt-111_O_vac/Xas_Pt-111_O_vac.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:0.12]
p \
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,3) t titl2
}

#-------------------------------------------------------------------------------------[]
if (1==1) {

titl1='KSPACING=0.25 ({\305}^{-1})'
titl3='KSPACING=0.15 ({\305}^{-1})'
outfile=outdir.'Pt/Pt_eos_kpoints.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "E-E0 (eV)" offset 1,0
set xrange [61.5:63.5]
set yrange [-0.002:0.014]
set format x "%7.1f"
set format y "%7.4f"
set key t c

folder_1=datdir."Pt/Pt-a1b1c1_e500k0.25/"
E0_1=system("grep '^Murnaghan : E0.*eV'  ".folder_1."eos.log |awk '{print $5}'")
B0_1=system("grep '^Murnaghan : B0.*eV'  ".folder_1."eos.log |awk '{print $5}'")
Bp_1=system("grep '^Murnaghan : Bp'      ".folder_1."eos.log |awk '{print $5}'")
V0_1=system("grep '^Murnaghan : V0.*ang' ".folder_1."eos.log |awk '{print $5}'")
datfile1=folder_1.'e0_a.dat'

folder_3=datdir."Pt/Pt-a1b1c1_e500k0.15/"
E0_3=system("grep '^Murnaghan : E0.*eV'  ".folder_3."eos.log |awk '{print $5}'")
B0_3=system("grep '^Murnaghan : B0.*eV'  ".folder_3."eos.log |awk '{print $5}'")
Bp_3=system("grep '^Murnaghan : Bp'      ".folder_3."eos.log |awk '{print $5}'")
V0_3=system("grep '^Murnaghan : V0.*ang' ".folder_3."eos.log |awk '{print $5}'")
datfile3=folder_3.'e0_a.dat'

f_1(x) = B0_1/Bp_1 * x * ((V0_1/x)**Bp_1/(Bp_1-1.0)+1.0) - V0_1*B0_1/(Bp_1-1.0)
f_3(x) = B0_3/Bp_3 * x * ((V0_3/x)**Bp_3/(Bp_3-1.0)+1.0) - V0_3*B0_3/(Bp_3-1.0)

p \
datfile1 u ($1**3):($2-E0_1) w p pt 6  ps 0.5 lc ''.word(colors,1) lw 1 t titl1,\
f_1(x) w l lc ''.word(colors,1) lw 1,\
datfile3 u ($1**3):($2-E0_3) w p pt 10 ps 0.5 lc ''.word(colors,2) lw 1 t titl3,\
f_3(x) w l lc ''.word(colors,2) lw 1
}

#-------------------------------------------------------------------------------------[]
if (1==1) {

titl1='ENCUT=500 (eV)'
titl3='ENCUT=700 (eV)'
outfile=outdir.'Pt/Pt_eos_cutoff.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Volume ({\305}^3)" offset 0,0
set ylabel "E-E0 (eV)" offset 1,0
set xrange [61.5:63.5]
set yrange [-0.002:0.014]
set format x "%7.1f"
set format y "%7.4f"
set key t c

folder_1=datdir."Pt/Pt-a1b1c1_e500k0.25/"
E0_1=system("grep '^Murnaghan : E0.*eV'  ".folder_1."eos.log |awk '{print $5}'")
B0_1=system("grep '^Murnaghan : B0.*eV'  ".folder_1."eos.log |awk '{print $5}'")
Bp_1=system("grep '^Murnaghan : Bp'      ".folder_1."eos.log |awk '{print $5}'")
V0_1=system("grep '^Murnaghan : V0.*ang' ".folder_1."eos.log |awk '{print $5}'")
datfile1=folder_1.'e0_a.dat'

folder_3=datdir."Pt/Pt-a1b1c1_e700k0.25/"
E0_3=system("grep '^Murnaghan : E0.*eV'  ".folder_3."eos.log |awk '{print $5}'")
B0_3=system("grep '^Murnaghan : B0.*eV'  ".folder_3."eos.log |awk '{print $5}'")
Bp_3=system("grep '^Murnaghan : Bp'      ".folder_3."eos.log |awk '{print $5}'")
V0_3=system("grep '^Murnaghan : V0.*ang' ".folder_3."eos.log |awk '{print $5}'")
datfile3=folder_3.'e0_a.dat'

f_1(x) = B0_1/Bp_1 * x * ((V0_1/x)**Bp_1/(Bp_1-1.0)+1.0) - V0_1*B0_1/(Bp_1-1.0)
f_3(x) = B0_3/Bp_3 * x * ((V0_3/x)**Bp_3/(Bp_3-1.0)+1.0) - V0_3*B0_3/(Bp_3-1.0)

p \
datfile1 u ($1**3):($2-E0_1) w p pt 6  ps 0.5 lc ''.word(colors,1) lw 1 t titl1,\
f_1(x) w l lc ''.word(colors,1) lw 1,\
datfile3 u ($1**3):($2-E0_3) w p pt 8  ps 0.5 lc ''.word(colors,2) lw 1 t titl3,\
f_3(x) w l lc ''.word(colors,2) lw 1
}

