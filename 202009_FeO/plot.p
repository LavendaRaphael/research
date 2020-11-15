workhome='~/tianff/202009_FeO/server/'
colors='black red blue green brown'

#set term x11 persist
set term pdfcairo font "Arial-Bold,25" size 8*1,5*1
#set term svg font "Arial-Bold,25" size 8*110,5*110

mode=1
#===============================[]
if (mode==2) {
set output "E0_image.pdf"
set samples 500
#set key t c
unset key
set xlabel "image" offset 0,0
set ylabel "E0 (eV)" offset 1,0
set xrange []
set yrange []
p \
workhome."Fe15O21/neb_00-20/E0_image.dat" u 1:2 w l lw 2 lc ''.word(colors,2)
}
#===============================[]
if (mode==1) { 
set output "E0_step.pdf"
set samples 500
unset key
set xlabel "step" offset 0,0
set ylabel "E0 (eV)" offset 1,0
set xrange []
set yrange []
p workhome."Fe15O21/neb_00-20/E0_step.dat" u 1:5 w l lw 2 lc ''.word(colors,2)
}
