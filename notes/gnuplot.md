
# 模板

```gnuplot
array pic[100]
do for [i=1:100] {pic[i]=0}

pic[1]=1 # test.pdf

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
goto_work=homedir.'group/x/server/'
goto_log=homedir.'group/x/log/server/'
#----------------------------------------------------------------------------[]
if (pic[1]==1) {

outfile=goto_log.'x.pdf'

datfilenum=4
array datfile[datfilenum]
datdir=goto_work_2.'x/'
do for [i=1:datfilenum] {datfile[i]=datdir.'x.dat'}

titlnum=datfilenum
array titl=['']
do for [i=1:titlnum] {titl[i]='x '.titl[i]}

colornum=titlnum
array colo[colornum]
colo[1]='black'
colorstart=1
colorwant=3
do for [i=1:colorwant] {
    if (colorwant==2) {colo[colorstart+i]=colors2[i]}
    if (colorwant==3) {colo[colorstart+i]=colors3[i]}
    if (colorwant==4) {colo[colorstart+i]=colors4[i]}
    if (colorwant==5 || colornum==6) {colo[colorstart+i]=colors6[i]}
}

#set term x11 persist
set term pdfcairo font "Arial,25" size 6*1,5*1
set output outfile
set xlabel "" offset 0,0
set ylabel "" offset 1,0
set xrange [*:*]
set yrange [*:*]
set format x "%7.3f"
set format y "%7.3f"
set style line 1 lw 2
p \
for [i=1:datfilenum] datfile[i] u 1:2 ls 1 lc ''.colo[i] t titl[i],\
#pause -1
}
```
# 杂项
set datafile separator ","

## size]
scaling=1.4
set size scaling , scaling
set origin .5-scaling/2.0,.5-scaling/2.0

## arrow]
set arrow from 0,1,1 to 0,0,0 linecolor ''.colo[2]

## label]
set label 1 'x' at 1,0,1 center textcolor ''.colo[2]
unset label 1
## datablocks]
$Mydata << EOD
11 22 33 first line of data
44 55 66 second line of data
# comments work just as in a data file
77 88 99
EOD
plot $Mydata using 1:3 with points, $Mydata using 1:2 with impulses

# 不能用在 if 里

## multiplot]
set multiplot

set size 1,1
plot sin(x)

set size 0.5,0.5
set origin 0,0.3
set mapping spherical
set angles degrees
r=1.0
theta=90.0
phi=0.0
rx=r*sin(theta)*cos(phi)
ry=r*sin(theta)*sin(phi)
rz=r*cos(theta)
set arrow to rx,ry,rz

set zeroaxis
set xtics axis
set xtics nomirror
set xrange [-1:1]
set arrow from -.9,0,0 to -1,0,0
set arrow from  .9,0,0 to  1,0,0

set zeroaxis
set ytics axis
set ytics nomirror
set yrange [-1:1]
set arrow from 0,-.9,0 to 0,-1,0
set arrow from 0,.9,0  to 0,1,0

set zzeroaxis
set ztics axis
set ztics nomirror
set zrange [-1:1]
set arrow from 0,0,-.9 to 0,0,-1
set arrow from 0,0,.9  to 0,0,1

set border 0
set xyplane at 0

splot NaN

unset multiplot
pause -1
## 间断线]
$ datfile <<EOF
1   1
2   1
3   x
4   1
5   1
<<EOF
$

p datfile u 1:2 # 不间断
p datfile u (column(1)):(column(2)) # 间断

## tics]
set xtics ('CH_3*'  1,'TS1'  4)

## circle]
p 'x.dat' u 1:2:(0.05) w circle lc 'black'

## color]
array colors=['#FE7D6A', '#81B8E9', '#4D85BD', '#F7903D', '#59A95A', '#D22027', '#384589', '#7FA5B7']

p x lc ''.colors[1]

## array]
array a=['S',2]
a[1]

array b[2]

|b| # 2
## 符号]
set encoding iso_8859_1
# angstrom
"{\305}"

# degree
'{\260}'

# greek
# http://lowrank.net/gnuplot/label-e.html
'{/Symbol a}'

## histogram]
set style data histogram
set style fill solid 0.25 noborder
# solid 填充
# 0.25 透明度
# 无边界
p \
datfile u 2:xtic(1),\
datfile u 0:2:2 w labels offset char 0,0.5 tc 'black',\
}
# xtic(1) 以第一列作为xtic
# $0 代表数据序列号
# 0:2:2 = <x>:<y>:<label name>
# char 0,0.5 以字体大小作为offset坐标标度

$ datfile <<EOF
33  98.4
53  34.7
<<EOF
$

## key box]
set key box
set key nobox
## 调用系统命令]
#-------------------------------------------------------------[system]
output = system("command string")
#-----------------------------------------[ref]
# https://runebook.dev/zh-CN/docs/gnuplot/system
#-------------------------------------------------------------[转义符]
`awk 'BEGIN{print "plot sin(x)"}'`
#-----------------------------------------[ref]
# https://www.coder.work/article/1889083

#--------------------------------------------------------------------------------[函数]
f(v) = v
p f(x) w l lc ''.word(colors,2) lw 2 t ""

#--------------------------------------------------------------------------------[坐标轴相等]
set view equal xyz
#--------------------------------------------------------------------------------[窗口保持]
	set term x11 persist
# https://holz.gitbooks.io/gnuplot5help/content/122-bao-chi.html
#--------------------------------------------------------------------------------[双坐标轴]
set ylabel "mag"
set y2label "F"
set ytics nomirror
set y2tics
set y2range [0:6.0]
set format y2 "%7.1f"

p 'temp' u 1:10 t "mag" axis x1y1,\
'temp' u 1:3 t "F" axis x1y2

# http://blog.sina.com.cn/s/blog_5d2054d90101ahda.html
#--------------------------------------------------------------------------------[key]
	set key b r
	t/l   t/c   t/r


    c/l    c    c/r


    b/l   b/c   b/r
#--------------------------------------------------------------------------------[for]
do for [i=1:6] {}
#=================================================[#gnuplot，零碎#]
workdir='~/tianff/20191021/'
p plot
u use
w with
l line
p points
lc linecolor
lw linewidth
pt pointtype
ps pointsize
t title
term terminal
512/36
p [][0:5] for [i = 2:6] 'O.d' u 1:i w l lc 1 lw 2 t columnhead
p for [i in '40'] 't'.i.'.d'
p 'i.d' w p pt 3 ps 1 lc 'black' t 'EXP'
p 'i.d' u 1:(1) w circles
gnuplot -c t.p 't.d' #plt脚本传参
p ARG1 #plt内参数使用
!ls #gnuplot命令行内执行linux命令
\ #换行
set xlabel 'x'
set term pdfcairo font "Arial,12"
set output 't.pdf'
replot
unset output

plot 'file' using 1:($2+$3) #
#第几行
plot "my.dat" every A:B:C:D:E:F
A: line increment
B: data block increment
C: The first line
D: The first data block
E: The last line
F: The last data block
# 第10-100 行
plot "my.dat" every ::10::100
#脚本
pause -1
#================================================================================================[3d]
## cube]
$cube << EOD
-1 -1   0
 1 -1   0
 1  1   0
-1  1   0
-1 -1   0

-1 -1 -.5
 1 -1 -.5
 1  1 -.5
-1  1 -.5
-1 -1 -.5

-1 -1   0
 1 -1   0
 1 -1 -.5
-1 -1 -.5
-1 -1   0

-1  1   0
 1  1   0
 1  1 -.5
-1  1 -.5
-1  1   0
EOD

splot $cube u 1:2:3

## circle]
# curle
splot sample [degr=0:360] '+' using (cos(degr)):(sin(degr)):(0)

# plane
splot sample [degr=0:360][r=0:1] '++' using (r*cos(degr)):(r*sin(degr)):(0)

## view]
set view azimuth 90
set view 270,270
