#colors='black red blue green cyan magenta yellow'
array colors=['#FE7D6A', '#81B8E9', '#4D85BD', '#F7903D', '#59A95A', '#D22027', '#384589', '#7FA5B7']

set samples 500
# set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
set encoding iso_8859_1
set style data lines


datdir="~/group/202103_XasPtO/server/"
outdir="~/group/202103_XasPtO/log/server/"

#-------------------------------------------------------------------------------------[]
if (0==1) {
subdir='Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_11/'
outfile=outdir.subdir.'xspectra.epsilon.pdf'

array datfile=['xspectra/','xspectra.epsilon010/', 'xspectra.epsilon100/']
num=|datfile|
do for [i=1:num] {datfile[i]=datdir.subdir.datfile[i].'xanes.dat'}

array titl=['{/Symbol e}-001','{/Symbol e}-010','{/Symbol e}-100']
array colornum=[1,2,5]

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]

p \
for [i=1:num] datfile[i] u 1:2 lw 1 lc ''.colors[colornum[i]] t titl[i]
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
subdir='Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_1/'
outfile=outdir.subdir.'xspectra.epsilon.pdf'

array datfile=['xspectra/','xspectra.epsilon010/', 'xspectra.epsilon100/']
num=|datfile|
do for [i=1:num] {datfile[i]=datdir.subdir.datfile[i].'xanes.dat'}

array titl=['{/Symbol e}-001','{/Symbol e}-010','{/Symbol e}-100']
array colornum=[1,2,5]

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]

p \
for [i=1:num] datfile[i] u 1:2 lw 1 lc ''.colors[colornum[i]] t titl[i]
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
subdir='Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/'
outfile=outdir.subdir.'xspectra.epsilon.pdf'

array datfile=['xspectra/','xspectra.epsilon010/', 'xspectra.epsilon100/']
num=|datfile|
do for [i=1:num] {datfile[i]=datdir.subdir.datfile[i].'xanes.dat'}

array titl=['{/Symbol e}-001','{/Symbol e}-010','{/Symbol e}-100']
array colornum=[1,2,5]

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]

p \
for [i=1:num] datfile[i] u 1:2 lw 1 lc ''.colors[colornum[i]] t titl[i]
}

#-------------------------------------------------------------------------------------[]
if (1==1) {
subdir='Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/aimd/'
outfile=outdir.subdir.'aimd_temperature_time.pdf'

array datfile=['aimd1','aimd2', 'aimd3']
num=|datfile|
do for [i=1:num] {datfile[i]=datdir.subdir.datfile[i].'/step.dat'}

array titl=['SMASS=1.0','SMASS=0.1','SMASS=0.025']
array num1=[0,212,212+497]
array colornum=[1,2,5]

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "time (fs)" offset 0,0
set ylabel "Free energy (eV)" offset 1,0
set xrange [*:*]
set yrange [*:*]
set key r b

p \
for [i=1:num] datfile[i] u (($1+num1[i])*0.5):3 w l lw 2 lc ''.colors[colornum[i]] t titl[i]
}

#-------------------------------------------------------------------------------------[]
if (1==1) {
subdir='Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/aimd/'
outfile=outdir.subdir.'aimd_energy_time.pdf'

array datfile=['aimd1','aimd2', 'aimd3']
num=|datfile|
do for [i=1:num] {datfile[i]=datdir.subdir.datfile[i].'/step.dat'}

array titl=['SMASS=1.0','SMASS=0.1','SMASS=0.025']
array num1=[0,212,212+497]
array colornum=[1,2,5]

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "time (fs)" offset 0,0
set ylabel "Temperature (K)" offset 1,0
set xrange [*:*]
set yrange [*:*]

p \
for [i=1:num] datfile[i] u (($1+num1[i])*0.5):2 w l lw 2 lc ''.colors[colornum[i]] t titl[i]
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../zrsun/20210512.Pt-110_ysft.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_1/xspectra/xas_alignorm.dat'
datfile3=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_11/xspectra/xas_alignorm.dat'

# titl1='Exp. (Xiaobao, Li)'
# titl2='Theory-O1 {/Symbol e}-001 (Feifei, Tian)'
# titl3='Theory-O11 {/Symbol e}-001 (Feifei, Tian)'

titl1='Exp.'
titl2='Theory-O1'
titl3='Theory-O11'


outfile=outdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/xspectra.theory-O1-O11_exp.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:*]
p \
datfile3 w l lw 2 lc ''.word(colors,1) t titl3,\
datfile2 w l lw 2 lc ''.word(colors,2) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 1 lc ''.word(colors,5) t titl1,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../zrsun/20210512.Pt-110_ysft.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_11/xspectra/xas_alignorm.dat'

titl1='Exp. (Xiaobao, Li)'
titl2='Theory-O11 {/Symbol e}-001 (Feifei, Tian)'

outfile=outdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/xspectra.theory-O11_exp.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:*]
p \
datfile2 w l lw 2 lc ''.word(colors,9) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 2 lc ''.word(colors,8) t titl1,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../zrsun/20210512.Pt-110_ysft.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_1/xspectra/xas_alignorm.dat'

titl1='Exp. (Xiaobao, Li)'
titl2='Theory-O1 {/Symbol e}-001 (Feifei, Tian)'

outfile=outdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/xspectra.theory-O1_exp.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:12]
p \
datfile2 w l lw 2 lc ''.word(colors,9) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 2 lc ''.word(colors,8) t titl1,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../zrsun/20210512.Pt-111_ysft.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xas_alignorm.dat'

# titl1='Exp. (Xiaobao, Li)'
# titl2='Theory {/Symbol e}-001 (Feifei, Tian)'
titl1='Exp.'
titl2='Theory'


outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.theory_exp.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [526:546]
set yrange [0:*]
p \
datfile2 w l lw 2 lc ''.word(colors,1) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 1 lc ''.word(colors,5) t titl1,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../zrsun/20210513.Pt-111_ysft_norm.dat'
datfile2=datdir.'../asist/20210512.exp_inplane_origin_ysft.dat'
datfile3=datdir.'../asist/20210512.exp_outplane_origin_ysft.dat'

# titl1='Exp. (Xiaobao, Li)'
titl1='Li'
# titl2='Exp. in-plane (Miller PRL 2011)'
titl2='Miller (in-plane)'
# titl3='Exp. out-of-plane (Miller PRL 2011)'
titl3='Miller (out-of-plane)'

outfile=outdir.'../zrsun/Pt-111.miller_prl_2011.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [*:*]
set yrange [0:*]
p \
datfile3 w p pt 6 ps 0.5 lw 2 lc ''.word(colors,1) t titl3,\
datfile2 w p pt 10 ps 0.5 lw 2 lc ''.word(colors,2) t titl2,\
datfile1 w l lw 2 lc ''.word(colors,5) t titl1,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_3/xspectra/xanes.dat'
datfile3=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_5/xspectra/xanes.dat'
datfile4=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_7/xspectra/xanes.dat'
datfile5=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_9/xspectra/xanes.dat'
datfile6=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/scf_11/xspectra/xanes.dat'

titl1='O1'
titl2='O3'
titl3='O5'
titl4='O7'
titl5='O9'
titl6='O11'

outfile=outdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac15/qe_hch_scf/xspectra.O_num.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]
p \
datfile6 w l lw 2 lc ''.word(colors,1) t titl6,\
datfile2 w l lw 2 lc ''.word(colors,5) t titl2,\
datfile1 w l lw 2 lc ''.word(colors,2) t titl1,\
}
# datfile3 w l lw 1 lc ''.word(colors,3) t titl3,\
# datfile4 w l lw 1 lc ''.word(colors,4) t titl4,\
# datfile5 w l lw 1 lc ''.word(colors,5) t titl5,\

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/test.wfc50/xspectra/xanes.dat'
datfile3=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/test.wfc40_rho400/xspectra/xanes.dat'

titl1='wfc=40'
titl2='wfc=50'
titl3='wfc=40, rho=400'

outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.wfc_rho.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [*:*]
set yrange [0:*]
p \
datfile1 w l lw 1 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 1 lc ''.word(colors,2) t titl2,\
datfile3 w l lw 1 lc ''.word(colors,3) t titl3,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra_xniter/xanes.dat'
titl1='xniter=50'
titl2='xniter=2000'
outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.xniter.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [*:*]
set yrange [0:*]
p \
datfile1 w l lw 2 lc ''.word(colors,8) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,9) t titl2,\
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a6b8c4_O12_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
titl1='Pt-111a4b4\_O4\_vac'
titl2='Pt-111a6b8\_O12\_vac'
outfile=outdir.'Pt-111_O_vac/xspectra.supercell.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]
p \
datfile1 w l lw 2 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,2) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../asist/20210511.exp_inplane_ysft.dat'
datfile2=datdir.'../asist/20210511.exp_outplane_ysft.dat'
datfile3=datdir.'../asist/20210511.theory_inplane_ysft.dat'
datfile4=datdir.'../asist/20210511.theory_outplane_ysft.dat'
titl1='EXP. (in plane)'
titl2='EXP. (out of plane)'
titl3='Theory (in plane)'
titl4='Theory (out of plane)'
outfile=outdir.'../asist/20210511.2011_prl_miller_ysft.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [*:*]
set yrange [*:*]
p \
datfile4 w l lw 2 lc ''.word(colors,1) t titl4,\
datfile3 w l lw 2 lc ''.word(colors,2) t titl3,\
datfile2 w p pt 10 ps 0.5 lw 2 lc ''.word(colors,1) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 2 lc ''.word(colors,2) t titl1
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'../asist/20210511.exp_inplane.dat'
datfile2=datdir.'../asist/20210511.exp_outplane.dat'
datfile3=datdir.'../asist/20210511.theory_inplane.dat'
datfile4=datdir.'../asist/20210511.theory_outplane.dat'
titl1='EXP. (in plane)'
titl2='EXP. (out of plane)'
titl3='Theory (in plane)'
titl4='Theory (out of plane)'
outfile=outdir.'../asist/20210511.2011_prl_miller.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [*:*]
set yrange [*:18]
unset ytics
p \
datfile4 w l lw 2 lc ''.word(colors,1) t titl4,\
datfile3 w l lw 2 lc ''.word(colors,2) t titl3,\
datfile2 w p pt 10 ps 0.5 lw 2 lc ''.word(colors,1) t titl2,\
datfile1 w p pt 6 ps 0.5 lw 2 lc ''.word(colors,2) t titl1
}
#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/test.nband664/xspectra/xanes.dat'
titl1='nband = 415'
titl2='nband = 664'
outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.nband.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]
p \
datfile1 w l lw 1 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 1 lc ''.word(colors,2) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra.xgamma-0.45/xanes.dat'
titl1='xgamma = 0.225'
titl2='xgamma = 0.45'
outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.xgamma.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]
p \
datfile1 w l lw 2 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,2) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra/xanes.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/scf_1/xspectra.k661/xanes.dat'
titl1='kpoints = 3 3 1'
titl2='kpoints = 6 6 1'
outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/xspectra.kpoints.pdf'

set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "hv-E_f (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [-5:15]
set yrange [0:*]
p \
datfile1 w l lw 1 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 1 lc ''.word(colors,2) t titl2
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile=datdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/test.time_vs_ncore.dat'
titl=''
outfile=outdir.'Pt-111_O_vac/Pt-111a4b4c4_O4_vac15/qe_hch_scf/test.time_vs_ncore.pdf'
set key t c
set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Core numbers" offset 1,0
set ylabel "Wall time (min)" offset 0,0
set xrange [*:*]
set yrange [0:70]

set style data histogram 
set style fill solid 0.25 noborder
p \
datfile u 2:xtic(1),\
datfile u 0:2:2 w labels offset char 0,0.5
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_3/CORE_DIELECTRIC_IMAG.dat'
datfile3=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_5/CORE_DIELECTRIC_IMAG.dat'
datfile4=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_7/CORE_DIELECTRIC_IMAG.dat'
datfile5=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_9/CORE_DIELECTRIC_IMAG.dat'
datfile6=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/O_11/CORE_DIELECTRIC_IMAG.dat'
titl1='O1'
titl2='O3'
titl3='O5'
titl4='O7'
titl5='O9'
titl6='O11'
outfile=outdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/xas.Pt-110a12b2_O22_vac.O.pdf'
set key t c
set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
set xrange [515:535]
set yrange [0:5e-5]
p \
datfile1 w l lw 2 lc ''.word(colors,1) t titl1,\
datfile2 w l lw 2 lc ''.word(colors,2) t titl2,\
datfile3 w l lw 2 lc ''.word(colors,3) t titl3,\
datfile4 w l lw 2 lc ''.word(colors,4) t titl4,\
datfile5 w l lw 2 lc ''.word(colors,5) t titl5,\
datfile6 w l lw 2 lc ''.word(colors,6) t titl6
}

#-------------------------------------------------------------------------------------[]
if (0==1) {
datfile1=datdir.'Pt-110_O_vac/Pt-110a12b2c4.5_O22_vac/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/xas_alignorm.dat'
titl1='Pt-110a12b2\_O22\_vac'
titl2='Pt-110a3b2\_O6\_vac'
outfile=outdir.'Pt-110_O_vac/Xas.Pt-110_O_vac.O22_O6.pdf'

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
datfile1=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas_hch/xas_alignorm.dat'
titl1='Pt-111p16\_O4\_vac\_fch'
titl2='Pt-111p16\_O4\_vac\_hch'
outfile=outdir."Pt-111_O_vac/Pt-111p16c4_O4_vac15/Xas.Pt\-111p16_O4_vac.fch_hch.pdf"

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
datfile1=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas_hch/xas_alignorm.dat'
titl1='Pt-110p12\_O6\_vac\_fch'
titl2='Pt-110p12\_O6\_vac\_hch'
outfile=outdir."Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/Xas.Pt\-110p12_O6_vac.fch_hch.pdf"

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
datfile1=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48c4_O12_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
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
datfile1=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48c4.5_O24_vac15/xas/O_2/CORE_DIELECTRIC_IMAG.dat'
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

datfile1=datdir.'Pt-111_O_vac/Pt-111p48c4_O12_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48c4_O12_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-111p48\_O12\_vac\_ave'
titl2='Pt-111p48\_O12\_vac\_O1'
outfile=outdir."Pt-111_O_vac/Pt-111p48c4_O12_vac15/xas/Xas_Pt-111p48_O12_vac.pdf"

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

datfile1=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-111p16\_O4\_vac\_ave'
titl2='Pt-111p16\_O4\_vac\_O1'
outfile=outdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/Xas_Pt-111p16_O4_vac.pdf'

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

datfile1=datdir.'Pt-110_O_vac/Pt-110p48c4.5_O24_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48c4.5_O24_vac15/xas/O_2/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-110p48\_O24\_vac\_ave'
titl2='Pt-110p48\_O24\_vac\_O2'
outfile=outdir.'Pt-110_O_vac/Pt-110p48c4.5_O24_vac15/xas/Xas_Pt-110p48_O24_vac.pdf'

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

datfile1=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/xas_ave.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/O_1/CORE_DIELECTRIC_IMAG.dat'
titl1='Pt-110p12\_O6\_vac\_ave'
titl2='Pt-110p12\_O6\_vac\_O1'
outfile=outdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/Xas_Pt-110p12_O6_vac.pdf'

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

datfile1=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/xas_alignorm.dat'
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

datfile1=datdir.'Pt-110_O_vac/Pt-110p12c4.5_O6_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-110_O_vac/Pt-110p48c4.5_O24_vac15/xas/xas_alignorm.dat'
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

datfile1=datdir.'Pt-111_O_vac/Pt-111p16c4_O4_vac15/xas/xas_alignorm.dat'
datfile2=datdir.'Pt-111_O_vac/Pt-111p48c4_O12_vac15/xas/xas_alignorm.dat'
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
if (0==1) {

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
if (0==1) {

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

