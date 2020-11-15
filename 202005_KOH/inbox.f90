!==========================================================================================
!===============================================================[VERSION]
!2020.06.23
!===============================================================[NOTES]
!===============================================================[USE]
!./inbox_xyz.x inbox.in
!===============================================================[INFILE]
!winfile 'wannier90.win'
!xyzfile 'wannier90_centres.xyz'
!===============================================================[DATAFILE]
!wannier90.win
!wannier90_centres.xyz
!===============================================================[OUTFILE]
!inbox.xyz
!inbox.log
![my.err]       #if program exit unexpected
!=========================================================================================
program main
implicit none

integer, parameter               :: DP = 8
real (DP), parameter             :: pi = 3.14159265359, bohr2angstrom=0.529177210903, eang2debye=4.799d0
integer                          :: clock_start, clock_end, clock_rate
integer (DP)                     :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)                        :: temp_real0, temp_real (3)
character (len=100)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile(2), outfile, errfile='my.err', logfile
integer, parameter               :: errfile_unit=11, infile_unit=12, datafile_unit(2)=(/13,14/), outfile_unit=15
character (len=100), allocatable :: input_list(:)

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//infile//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'winfile', 'xyzfile'/)
do i = 1, input_tot
do while (.true.)
        read (infile_unit, *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) "ERROR: parameter'"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case (i)
case (1)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(1)
case (2)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(2)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE-1]
write (errfile_unit, leng//"'[READ DATAFILE-1]: "//datafile(1)//"')")
open(datafile_unit(1), file = datafile(1), status = 'old')

do while (.true.)
        read (datafile_unit(1), *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) 'ERROR: datafile-1 is not formatted'
                stop
        endif        
        select case (temp_char0)
        case ('begin')
                backspace(datafile_unit(1))
                read (datafile_unit(1), *) temp_char(1:2)
                select case (temp_char(2))
                case ('unit_cell_cart')
                        read (datafile_unit(1), *) cell_size(1)
                        read (datafile_unit(1), *) temp_char(1),cell_size(2)
                        read (datafile_unit(1), *) temp_char(1:2),cell_size(3)
                        write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size
                        exit
                endselect
        endselect
enddo
close (datafile_unit(1))
!===============================================================[READ DATAFILE-2]
write (errfile_unit, leng//"'[READ DATAFILE-2]: "//datafile(2)//"')")
open (datafile_unit(2), file = datafile(2), status = 'old')
outfile = "inbox.xyz"
open (outfile_unit, file = outfile, status = 'replace')
read (datafile_unit(2), *) temp_char0
write(outfile_unit, '(A25)') temp_char0
read (datafile_unit(2), *)
write(outfile_unit, '(A25)') "inbox"
do while (.true.)
        read (datafile_unit(2), *, iostat = ios) temp_char0, temp_real(1:3)
        if (ios < 0) exit
        temp_real(1:3) = temp_real(1:3) - floor(temp_real(1:3)/cell_size)*cell_size
        write(outfile_unit, "(A10, 3F20.10)") trim(temp_char0), temp_real(1:3)
enddo
close(datafile_unit(2))
close(outfile_unit)
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
logfile='inbox.log'
call rename(errfile, logfile)
end program main
