!==========================================================================================
!===============================================================[VERSION]
!2020.06.27
!===============================================================[FUNCTION]
!Statis bond length.
!===============================================================[NOTES]
!===============================================================[USE]
!./bondlength_pp.x bondlength_pp.in
!===============================================================[INFILE]
!datafile1      'mlwc_dipole.out'
!datafile2      'bondlength.out'
!dipole_rc      2.5d0   #debye
!l_begin        1.8d0
!l_end          2.2d0
!dl_tot         10
!===============================================================[DATAFILE]
!bondlength.out
!mlwc_dipole.out
!===============================================================[OUTFILE]
![my.err]       #if program exit unexpected
!bondlength_pp.log
!bondlength_pp.out
!=========================================================================================
program main
implicit none

integer, parameter               :: DP = 8
real (DP), parameter             :: pi = 3.14159265359, bohr2angstrom=0.529177210903, eang2debye=4.799d0
integer                          :: clock_start, clock_end, clock_rate
integer (DP)                     :: i, j, k, l, m, ios, temp_int0,temp_int(10), input_tot
real (DP)                        :: temp_real0, temp_real (10)
character (len=100)              :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile(2), outfile, errfile='my.err', logfile
integer, parameter               :: errfile_unit=11, infile_unit=12, datafile_unit(2)=(/13,14/), outfile_unit=15
character (len=100), allocatable :: input_list(:), temp_chararray(:)
integer (DP), allocatable        :: temp_intarray(:)

integer (DP)                    :: mol_tot, dl_tot
integer (DP), allocatable       :: mol_tof(:)
!character (len=100), allocatable ::
real (DP), allocatable           :: prob(:)
real (DP)                        :: dipole_rc, l_begin, l_end, dl

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 6
allocate(input_list(input_tot))
input_list = (/'datafile1','datafile2', 'dipole_rc', 'l_begin','l_end','dl_tot'/)
do i = 1, input_tot                                               
do while (.true.)                                                 
        read (infile_unit, *, iostat = ios) temp_char0            
        if (ios < 0) then                                         
                write (errfile_unit, *) "ERROR: parameter'"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                write (*, *) "ERROR"
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case(i)
case(1)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(1)
case(2)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(2)
case(3)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) dipole_rc
case(4)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) l_begin
case(5)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) l_end
case(6)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) dl_tot
endselect
rewind (infile_unit)
enddo
close (infile_unit)
deallocate(input_list)
!===============================================================[READ DATAFILE-1]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile(1))//"')")
open(datafile_unit(1), file = datafile(1), status = 'old')
read(datafile_unit(1),*)
read(datafile_unit(1),*)
mol_tot = 0
do while (.true.)
        read (datafile_unit(1), *, iostat = ios)
        if (ios<0) exit
        mol_tot = mol_tot + 1
enddo
write (errfile_unit, "(A25,I25)") "mol_tot",mol_tot
rewind(datafile_unit(1))
read(datafile_unit(1),*)
read(datafile_unit(1),*)
allocate(mol_tof(mol_tot))
mol_tof = 0
write (errfile_unit, "(3A25)") "mol","mol_dipole","mol_tof"
do i = 1, mol_tot
        read (datafile_unit(1), *) temp_char(1:2),temp_real0
        if (temp_real0 >= dipole_rc) then
                mol_tof(i) = 1
        endif
        write (errfile_unit, "(I25,F25.10,I25)") i,temp_real0,mol_tof(i)
enddo
if (sum(mol_tof) ==0 ) then
        write (errfile_unit, *) "ERROR: parameter 'dipole_rc' not proper!"
        write (*, *) "ERROR"
        stop
endif
close (datafile_unit(1))
!===============================================================[READ DATAFILE-2]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile(2))//"')")
open(datafile_unit(2), file = datafile(2), status = 'old')
read(datafile_unit(2),*)
dl = (l_end - l_begin)/dl_tot
allocate(prob(dl_tot))
prob = 0.d0
do while (.true.)
        read (datafile_unit(2), *, iostat = ios) temp_int(1:2), temp_real0
        if (ios<0) exit
        if (mol_tof(temp_int(1)) == 0 ) cycle
        write (errfile_unit, "(2I25,F25.10)") temp_int(1:2),temp_real0
        temp_int0 = ceiling((temp_real0 - l_begin)/dl)
        if (temp_int0 <=0 .or. temp_int0 > dl_tot) then
                write (errfile_unit, *) "ERROR: parameter 'l_begin' or 'l_end' not proper!"
                write (*, *) "ERROR"
                stop
        endif
        prob(temp_int0) = prob(temp_int0) + 1.d0
enddo
write (errfile_unit, "(A25,F25.10)") 'sum_bond',sum(prob)
close (datafile_unit(2))
!===============================================================[OUTPUT]
outfile = 'bondlength_pp.out'
write (errfile_unit, leng//"'[OUTPUT]:"//trim(outfile)//"')")
open (outfile_unit, file=outfile, status='replace')
write(outfile_unit, "('#from l=', F10.5, ' to l=', F10.5,' dl=',F10.5)") l_begin,l_end,dl
write(outfile_unit, "(A, A24, 4A25)") '#','l','prob_density','bond_num'
do i = 1, dl_tot
        write(outfile_unit, "(2F25.10,I25)") l_begin+(i-0.5d0)*dl, prob(i)/sum(prob)/dl, nint(prob(i))
enddo
close(outfile_unit)
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
logfile='bondlength_pp.log'
call rename(errfile, logfile)
end program main
