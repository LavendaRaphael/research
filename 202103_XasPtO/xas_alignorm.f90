!==========================================================================================
!---------------------------------------------------------------[VERSION]
! 2021.05.12
!---------------------------------------------------------------[NOTES]
!---------------------------------------------------------------[USE]
! ./xas_alignorm.x xas_alignorm.in
!---------------------------------------------------------------[xas_alignorm.in]
! datafile   "*.dat"
! e_align    535.0d0             #eV
! area       10.d0
! e_begin    532.d0              #eV
! e_end      546.d0              #eV
! predge_tolera  0.1                 #%
!---------------------------------------------------------------[DATAFILE]
! *.dat
!---------------------------------------------------------------[OUTFILE]
! xas_alignorm.dat
! xas_alignorm.log
! [my.err]
!==========================================================================================
program main
implicit none

integer, parameter       :: DP = 8
real (DP), parameter         :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer              :: clock_start, clock_end, clock_rate
integer (DP)             :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)            :: temp_real0, temp_real (3)
character (len=500)      :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile="xas_alignorm.dat", errfile='my.err', logfile="xas_alignorm.log"
integer, parameter       :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=500), allocatable :: input_list(:)

integer (DP)             :: ei_tot, i_begin, i_end
!integer (DP), allocatable    ::
!character (len=100), allocatable ::
real (DP), allocatable       :: xas(:,:)
real (DP)            :: e_align, area, e_begin, e_end, xas_sum, e_onset, predge_tolera

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!---------------------------------------------------------------[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 6
allocate(input_list(input_tot))
input_list = (/'datafile','e_align','area','e_begin','e_end','predge_tolera'/)
do i = 1, input_tot
do while (.true.)
    read (infile_unit, *, iostat = ios) temp_char0
    if (ios < 0) then
        write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
        stop
    endif
    if (temp_char0 /= input_list(i)) cycle
    backspace(infile_unit)
    exit
enddo
select case (i)
case (1)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) datafile
case (2)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) e_align
case (3)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) area
case (4)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) e_begin
case (5)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) e_end
case (6)
    read (infile_unit, *) temp_char(1:2)
    write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
    read (temp_char(2), *) predge_tolera
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!---------------------------------------------------------------[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile)//"')")
open(datafile_unit, file = datafile, status = 'old')
ei_tot = 0
do while (.true.)
    read (datafile_unit, *, iostat = ios)
    if (ios < 0) exit
    ei_tot = ei_tot + 1
enddo
write(errfile_unit, '(A25,I25)') 'ei_tot',ei_tot
rewind (datafile_unit)
allocate( xas(ei_tot,2))
i = 0
do while (.true.)
    read (datafile_unit, *, iostat = ios) temp_real(1:2)
    if (ios < 0) exit
    i = i + 1
    xas(i, 1:2) = temp_real(1:2)
enddo
close(datafile_unit)
!---------------------------------------------------------------[ALIGN TO PRE-EDGE]
do i=2, ei_tot
    if (xas(i,2) < xas(i-1,2)) then
        temp_real0=xas(i-1,2)/maxval(xas(:,2))
        if (temp_real0 >predge_tolera) exit
    endif
enddo
e_onset = xas(i-1,1)
write(errfile_unit, '(A25,F25.10)') 'e_onset', e_onset
write(errfile_unit, '(A25,F25.10)') 'predge/max', temp_real0
xas(:,1) = xas(:,1) - e_onset + e_align
!---------------------------------------------------------------[NORMALIZATION]
do i = 1, ei_tot
    if (xas(i,1) >= e_begin) exit
enddo
i_begin = i
write(errfile_unit, '(A25,I25)') 'i_begin', i_begin
xas_sum = 0.d0
do i= i_begin, ei_tot-1
    if (xas(i+1,1) > e_end) exit
    xas_sum = xas_sum + (xas(i+1,1)-xas(i,1))*(xas(i+1,2)+xas(i,2))/2.d0
enddo
i_end = i
write(errfile_unit, '(A25,I25)') 'i_end', i_end
write(errfile_unit, '(A25,F25.10)') 'xas_sum',xas_sum
! do i = i_begin, i_end
!     xas(i,2) = xas(i,2) / xas_sum * area
! enddo
xas(:,2) = xas(:,2) / xas_sum * area
!---------------------------------------------------------------[OUTDATA]
write(errfile_unit, leng//"'[OUTDATA]: "//trim(outfile)//"')")
open(outfile_unit, file = outfile, status = 'replace')
! do i = i_begin, i_end
!     write(outfile_unit, '(2F25.10)') xas(i,1:2)
! enddo
do i = 1, ei_tot
    write(outfile_unit, '(2F25.10)') xas(i,1:2)
enddo

close(outfile_unit)
!---------------------------------------------------------------[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
