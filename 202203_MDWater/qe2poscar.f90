!==========================================================================================
!===============================================================[VERSION]
!2020.05.29
!===============================================================[NOTES]
!datafile 'datafile'
!===============================================================[USE]
!./qe2poscar.x qe2poscar.in
!===============================================================[qe2poscar.in]
!posfile         'water.pos'     #ps bohr
!title           'H2O_32'
!time            45.0    #ps
!cell_size       #bohr
!   18.73479727    0.00000000    0.00000000
!    0.00000000   18.73479727    0.00000000
!    0.00000000    0.00000000   18.73479727
!atom_type
!        O       32
!        H       64
!end atom_type
!===============================================================[DATAFILE]
!===============================================================[OUTFILE]
!==========================================================================================
program main
implicit none

integer, parameter              :: DP = 8
real (DP), parameter            :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer                         :: clock_start, clock_end, clock_rate
integer (DP)                    :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)                       :: temp_real0, temp_real (3)
character (len=40)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile, logfile='qe2poscar.log'
integer, parameter              :: logfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=40), allocatable :: input_list(:)

integer (DP)                    :: atomtype_tot, atom_tot
integer (DP), allocatable       :: atomtype_num(:)
character (len=40)              :: title, cell_basis(3,3)
character (len=40), allocatable :: atomtype_name(:)
!real (DP), allocatable          ::
real (DP)                       :: time
open (logfile_unit, file=logfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (logfile_unit, leng//"'[READ INFILE]: "//infile//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 5
allocate(input_list(input_tot))
input_list = (/'posfile','title','time','cell_size','atom_type'/)
do i = 1, input_tot
do while (.true.)
        read (infile_unit, *, iostat = ios) temp_char0
        if (ios < 0) then
                write (logfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case (i)
case (1)
        read (infile_unit, *) temp_char0, datafile
        write (logfile_unit, "(2A25)") trim(temp_char0), trim(datafile)
case (2)
        read (infile_unit, *) temp_char0, title
        write (logfile_unit, "(2A25)") trim(temp_char0), trim(title)
case (3)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (logfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        outfile = 'POSCAR_'//trim(temp_char(2))//'ps'
        read (temp_char(2), *) time
case (4)
        read (infile_unit, *) temp_char0
        write (logfile_unit, "(A25)") trim(temp_char0)
        do j = 1, 3
                read (infile_unit, *) cell_basis(j,:)
                write (logfile_unit, "(A25,3A25)") '',cell_basis(j,:)
        enddo
case (5)
        read (infile_unit, *) temp_char0
        write (logfile_unit, "(A25)") trim(temp_char0)
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
                write (logfile_unit, "(2A25,I25)") '',trim(atomtype_name(j)),atomtype_num(j)
        enddo
        atom_tot = sum(atomtype_num)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE]
open(outfile_unit, file = outfile, status = 'replace')
write (logfile_unit, leng//"'[READ DATAFILE]: "//datafile//"')")
open(datafile_unit, file = datafile, status = 'old')
do while (.true.)
        read (datafile_unit, *, iostat = ios) temp_char0,temp_real0
        if (ios<0) then
                write (logfile_unit,*) "ERROR: 'time' is set too large!"
                stop
        endif
        if (temp_real0 > time) exit
        do i = 1, atom_tot
                read (datafile_unit, *)
        enddo
enddo
backspace (datafile_unit)
read (datafile_unit, *) temp_char0, temp_char(2)
title = trim(title)//' '//trim(temp_char(2))//'ps'
write (outfile_unit, *) title
write (outfile_unit, "(F15.12)") bohr2angstrom
do i = 1, 3
        write (outfile_unit, '(3A25)') trim(cell_basis(i,1)),trim(cell_basis(i,2)),trim(cell_basis(i,3))
enddo
write(temp_char0, *) atomtype_tot
write (outfile_unit, "("//temp_char0//"A10)") (/(trim(atomtype_name(i)),i=1,atomtype_tot)/)
write (outfile_unit, "("//temp_char0//"I10)") atomtype_num
write (outfile_unit, *) 'Cartesian'
do i = 1, atomtype_tot
do j = 1, atomtype_num(i)
        read (datafile_unit, *) temp_char(1:3)
        write (outfile_unit, '(3A25)') trim(temp_char(1)),trim(temp_char(2)),trim(temp_char(3))
enddo
enddo
close(datafile_unit)
close(outfile_unit)
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (logfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(logfile_unit)
end program main
