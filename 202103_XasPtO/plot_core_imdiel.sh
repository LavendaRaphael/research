#!/bin/bash

cat > helpscript.perl  <<EOF
#!/bin/perl

use strict;
use warnings;
my \$mode=shift;

while(<>)
{
   chomp;
   if(\$_ =~ /frequency dependent IMAGINARY DIELECTRIC FUNCTION/)
   {
      \$_=<>;
      \$_=<>;
      while (<>)
      {
         my \$sum=0;
         if (\$_ !~ /[0-9]/) {last;}
         chomp;
         \$_=~s/^/ /;
         my @help=split(/[\t,\s]+/);
         if (\$help[2]=~/NaN/||\$help[3]=~/NaN/||\$help[4]=~/NaN/) {next;}
         if (\$help[5]=~/NaN/||\$help[6]=~/NaN/||\$help[4]=~/NaN/) {next;}
         if (\$mode==11) {\$sum=\$help[2];}
         if (\$mode==12) {\$sum=\$help[3];}
         if (\$mode==13) {\$sum=\$help[4];}
         if (\$mode==14) {\$sum=\$help[5];}
         if (\$mode==15) {\$sum=\$help[6];}
         if (\$mode==16) {\$sum=\$help[7];}
         if (\$mode==17) {\$sum=(\$help[2]+\$help[3])/2.0;}
         \$sum=\$help[1]*\$sum
         print \$help[1]," ",\$sum,"\n";
      }
   }
   last if eof;
}
EOF

perl helpscript.perl 11 OUTCAR > xas.x.dat
perl helpscript.perl 12 OUTCAR > xas.y.dat
perl helpscript.perl 17 OUTCAR > xas.x_y.dat
rm helpscript.perl
