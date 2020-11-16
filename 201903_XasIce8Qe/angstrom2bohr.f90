program angstrom2bohr
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359
integer(DP)               :: ios
real (DP)                 :: temp_real, temp_real1, temp_real2, temp_real3
character (len=40)        :: temp_char, infile, outfile, leng=" (65 ('='), "

real (DP)                 :: coef = 0.52917721067

call get_command_argument (1, infile)
outfile = 'out.'//adjustl(infile)
write (*, leng//"'[READ INFILE]: "//infile//"')")
write (*, leng//"'[OUTFILE]: "//outfile//"')")
open (11, file = infile, status = 'old')
open (12, file = outfile, status = 'replace')
do while (.true.)
        read (11, *, iostat = ios) temp_char, temp_real1, temp_real2, temp_real3
        if (ios < 0) exit
        write (*, "(A25,3F)") temp_char, temp_real1, temp_real2, temp_real3
        temp_real1 = temp_real1/coef
        temp_real2 = temp_real2/coef
        temp_real3 = temp_real3/coef
        write (12, "(A25,3F)") temp_char, temp_real1, temp_real2, temp_real3
        write (*, "(A25,3F)") 'bohr', temp_real1, temp_real2, temp_real3
end do
close(11)
close(12)

end program angstrom2bohr
