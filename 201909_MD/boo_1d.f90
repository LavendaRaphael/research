!=====================[USE]=========================
!./boo_2d.x boo_1d.in
!===================[DATAFILE]====================
!q4.boo
!====================[boo_1d.in]====================
!l 4
!===================[OUTFILE]===========================
!q4.boo_1d
!===================================================
program boo_1d
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 :: bin=0.01d0, q
real(DP), allocatable    :: p(:)
integer(DP)              :: i, ios, atom_tot, timestep, atom_num, temp_int, l, n_bin
character(len=40)        :: infile, head, datafile, outfile

call get_command_argument(1,infile)
write(*,"(A80)") '=============================[READ FROM INFILE]=================================='
write(*,'(A25, A25)') 'inputfile', trim(infile)
open(1, file = infile, status = 'old')
do while (.true.)
        read( 1 , *, iostat = ios ) head
        if ( ios < 0 ) exit
        backspace(1)
        select case( head )
        case('l')
                read(1,*) head, l
                write(*,'(A25, 2I25)') trim(head), l
        end select
end do
close(1)
n_bin = nint( 1.d0 / bin )
write(*,'(A25, F)') 'bin', bin
write(*,'(A25, I25)') 'n_bin', n_bin
allocate( p( n_bin ))

write(datafile, '(A1,I1,A4)') 'q',l,'.boo'
write(*,'(A80)') '============================[read from data]==================================='
write(*, '(2A25)') 'datafile',trim(datafile)

open( 2, file = datafile, status = 'old' )
do while (.true.)
        read(2, *) head
        if (head(1:1) == '#') cycle
        backspace(2)
        exit
enddo

atom_tot = 0
atom_num = 0
p = 0.d0
timestep = 0
write(*,'(2A25)') 'timestep','atom_num'
do while (.true.)
        read(2, *, iostat = ios) timestep, atom_num, q
        if (ios<0) exit
        atom_tot = atom_tot + 1
        temp_int = nint( q / bin )
        p( temp_int ) = p( temp_int ) + 1.d0
enddo
close(2)
write(*,'(A25,I25)') 'atom_tot', atom_tot
p = p / (atom_tot * bin)

outfile = datafile(1:6)//'_1d'
write(*,'(A80)') '============================[RESULT]==================================='
write(*,'(A25)') 'outfile', trim(outfile)
open(4, file = outfile, status='replace')
write(4,'(A1,A24,A25)') '#',datafile(1:2), 'p_density'
do i = 1, n_bin
        write(4,'(2F)') i*bin, p(i)
enddo
close(4)

deallocate(p)
endprogram boo_1d 
