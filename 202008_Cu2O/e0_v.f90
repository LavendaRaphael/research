!==========================================================================================
!===============================================================[VERSION]
!2020.09.06
!===============================================================[NOTES]
!e0_a.dat to e0_v.dat
!===============================================================[USE]
!./*.x e0_v.in
!===============================================================[INFILE]
!datafile 'e0_a.dat'
!===============================================================[DATAFILE]
!e0_a.dat
!POSCAR
!===============================================================[OUTFILE]
![my.err]
!e0_v.dat
!e0_v.log
!==========================================================================================
program main
implicit none

integer, parameter              :: DP = 8
real (DP), parameter            :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer                         :: clock_start, clock_end, clock_rate
integer (DP)                    :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)                       :: temp_real0, temp_real (10)
character (len=40)              :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile, outfile, errfile="my.err", logfile
integer, parameter              :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=40), allocatable :: input_list(:)
logical                         :: iexist
!top
!integer (DP)                    ::
!integer (DP), allocatable       ::
!character (len=40), allocatable ::
!real (DP), allocatable          ::
real (DP)                       :: cell_size(3,3), volume_unit
open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
outfile = "e0_v.dat"
logfile = "e0_v.log"
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 1
allocate(input_list(input_tot))
input_list = (/'datafile'/)
do i = 1, input_tot
do while (.true.)
        read (infile_unit, *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                write (*, *) "ERROR: check errfile 'my.err'" 
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case (i)
case (1)
        read (infile_unit, *) temp_char0, datafile
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(datafile)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ POSCAR]
write (errfile_unit, leng//"'[READ POSCAR]:')")
inquire(file="POSCAR", exist=iexist)
if (.not. iexist) then
    write (errfile_unit, *) "ERROR: 'POSCAR' not found!"
    write (*, *) "ERROR: check errfile 'my.err'"
    stop
endif
open(datafile_unit, file = "POSCAR", status = 'old')
read(datafile_unit, *) !title
read(datafile_unit, *) !scale
read (datafile_unit, *) cell_size(1,:) 
read (datafile_unit, *) cell_size(2,:)
read (datafile_unit, *) cell_size(3,:)
write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(1,:)
write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(2,:)
write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(3,:)
call cross(cell_size(1,:),cell_size(2,:), temp_real(1:3))
volume_unit = dot_product(temp_real(1:3),cell_size(3,:))
volume_unit = abs(volume_unit)
write (errfile_unit, "(A25, F25.10)") "volume_unit", volume_unit
close(datafile_unit)
!===============================================================[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile)//"')")
open(datafile_unit, file = datafile, status = 'old')
open(outfile_unit, file = outfile, status = 'replace')
do while (.true.)
        read (datafile_unit, *, iostat = ios) temp_char0
        if (ios < 0) exit
        if (temp_char0(0:1) == "#") cycle
        backspace(datafile_unit)
        read (datafile_unit, *) temp_real0, temp_char(1:5)
        write(outfile_unit, "(F25.10, A25)") volume_unit*temp_real0**3, trim(temp_char(5))
enddo
close(outfile_unit)
close(datafile_unit)
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main

subroutine cross(a, b, results)
  real(8), DIMENSION(3) :: results
  real(8), DIMENSION(3), INTENT(IN) :: a, b

  results(1) = a(2) * b(3) - a(3) * b(2)
  results(2) = a(3) * b(1) - a(1) * b(3)
  results(3) = a(1) * b(2) - a(2) * b(1)

END subroutine cross
