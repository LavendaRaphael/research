!==========================================================================================
!===============================================================[VERSION]
!2020.12.03
!===============================================================[NOTES]
!===============================================================[USE]
!./xas_sft.x xas_sft.in
!===============================================================[xas_norm.in]
!datafile       "CORE_DIELECTRIC_IMAG.dat"
!datafile1      "fort13"
!datafile2      "fort777"
!===============================================================[DATAFILE]
!CORE_DIELECTRIC_IMAG.dat
!fort13
!fort777
!===============================================================[OUTFILE]
!xas_sft.dat
!xas_sft.log
![my.err]
!==========================================================================================
program main
implicit none

integer, parameter               :: q = 8
real (q), parameter              :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0, hartree2ev=27.211386245988_q
integer                          :: clock_start, clock_end, clock_rate
integer (q)                      :: i, j, k, l, m, ios, temp_int0, input_tot
real (q)                         :: temp_real0, temp_real (3)
character (len=100)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile='xas_sft.dat', errfile='my.err', logfile='xas_sft.log',datafilen(2)
integer, parameter               :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14, datafilen_unit(1:2)=(/15,16/)
character (len=100), allocatable :: input_list(:)

!integer (q)                     :: 
!integer (q), allocatable        ::
!character (len=100), allocatable ::
!real (q), allocatable           :: 
real (q)                        :: fort13, fort777, sft

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 3
allocate(input_list(input_tot))
input_list = (/'datafile', 'datafile1', 'datafile2'/)
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
        read (temp_char(2), *) datafilen(1)
case (3)
        read (infile_unit, *) temp_char(1:2)
        write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
        read (temp_char(2), *) datafilen(2)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafilen(1))//"')")
open(datafilen_unit(1), file = datafilen(1), status = 'old')
read(datafilen_unit(1),*) temp_char(1:2)
write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
read (temp_char(2), *) fort13
close(datafilen_unit(1))
!===============================================================[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafilen(2))//"')")
open(datafilen_unit(2), file = datafilen(2), status = 'old')
read(datafilen_unit(2),*) temp_char(2)
write (errfile_unit, "(A25)") trim(temp_char(2))
read (temp_char(2), *) fort777
close(datafilen_unit(2))

sft=(fort777-fort13)*hartree2ev
write (errfile_unit, "(A25,F25.10)") "sft",sft
!===============================================================[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile)//"')")
open(datafile_unit, file = datafile, status = 'old')
!===============================================================[OUTDATA]
write(errfile_unit, leng//"'[OUTDATA]: "//trim(outfile)//"')")
open(outfile_unit, file = outfile, status = 'replace')
temp_int0 = 0
do while (.true.)
        read (datafile_unit, *, iostat = ios) temp_real0, temp_char0
        if (ios < 0) exit
        temp_int0 = temp_int0 + 1
        write(outfile_unit, '(F25.10,A25)') temp_real0+sft, trim(temp_char0)
enddo
close(datafile_unit)
close(outfile_unit)
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
