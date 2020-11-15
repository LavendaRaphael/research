!==========================================================================================
!===============================================================[VERSION]
!2020.11.04
!===============================================================[NOTES]
!===============================================================[USE]
!./*.x *.in
!===============================================================[INFILE]
!datafile 'datafile'
!atom_type
!    O   32
!    H   64
!end atom_type
!===============================================================[DATAFILE]
!===============================================================[OUTFILE]
![my.err]
!*.log
!*.out
!==========================================================================================
program main
implicit none

integer, parameter                  :: DP = 8
real (DP), parameter                :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer                             :: clock_start, clock_end, clock_rate
integer (DP)                        :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)                           :: temp_real0, temp_real (3)
character (len=100)                 :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile="*.out", errfile='my.err',logfile="*.log"
integer, parameter                  :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=100), allocatable    :: input_list(:)

!integer (DP)                        ::
!integer (DP), allocatable           ::
!character (len=100), allocatable    ::
!real (DP), allocatable              ::
!real (DP)                           ::
open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'datafile','atom_type'/)
do i = 1, input_tot
do while (.true.)
    read (infile_unit, *, iostat = ios) temp_char0
    if (ios < 0) then
        write (*, *) "ERROR: see 'my.err' for details!"
        write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
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
    read (temp_char(2),*) datafile
case (2)
    read (infile_unit, *) temp_char0
    write (errfile_unit, "(A25)") trim(temp_char0)
    atomtype_tot = 0
    do while (.true.)
          read (infile_unit, *) temp_char0
          if (temp_char0 == 'end') then
              do j = 1, atomtype_tot+1
                  backspace(infile_unit)
              enddo
              exit
          else
              atomtype_tot = atomtype_tot + 1
          endif
    enddo
    allocate(atomtype_name(atomtype_tot),atomtype_num(atomtype_tot))
    do j = 1, atomtype_tot
        read (infile_unit, *) atomtype_name(j), atomtype_num(j)
        write (errfile_unit, "(2A25,I25)") '',trim(atomtype_name(j)),atomtype_num(j)
    enddo
    atom_tot = sum(atomtype_num)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE]
!===============================================================[COMPUTE]
write (errfile_unit, leng//"'[COMPUTE]')")
!===============================================================[OUTPUT]
write (errfile_unit, leng//"'[OUTPUT]: "//trim(outfile)//"')")
open (outfile_unit, file = outfile, status = 'replace')
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
