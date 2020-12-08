colors='black red blue green cyan magenta yellow'
set term pdfcairo font "Arial,25" size 8*1,5*1
set samples 500
set key box
set key samplen 2
set key width 2
set key height 0.5
set key noautotitle
workhome0="~/tianff/202012_XasDiamond/server/"
#===============================[]
if (1==1) {
set output workhome0."../log/XasDiamond.pdf"
set xlabel "Energy (eV)" offset 0,0
set ylabel "Intensity (Arb. Units)" offset 1,0
unset ytics
set xrange [280:310]
p \
workhome0.'../asist/XANES_Diamond/SUPERCELL_4x4x4/C_XAS_aligned_to_4x4x4.dat' w l lw 3 lc ''.word(colors,1) t 'Exp.',\
workhome0.'444/CORE_DIELECTRIC_IMAG.dat' w l lw 3 lc ''.word(colors,2) t 'SCH'
}
