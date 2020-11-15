!=====================[USE]=========================
!./boo_2d.x boo_2d.in
!===================[DATAFILE]====================
!q4.boo
!q6.boo
!====================[boo_2d.in]====================
!l 4 6
!===================[OUTFILE]===========================
!q4_q6.boo_2d
!===================================================
program boo_2d
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 :: bin(2)=0.01d0, q(2)
real(DP), allocatable    :: p(:,:)
integer(DP)              :: i, j, ios, atom_tot, timestep(2), atom_num(2), temp_int(2), l(2), n_bin(2)
character(len=40)        :: infile, head, datafile(2), outfile

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
n_bin = nint( 1.d0 / bin(2) )
write(*,'(A25, 2F)') 'bin', bin
write(*,'(A25, 2I25)') 'n_bin', n_bin
allocate( p( n_bin(1), n_bin(2) ))

write(datafile(1), '(A1,I1,A4)') 'q',l(1),'.boo'
write(datafile(2), '(A1,I1,A4)') 'q',l(2),'.boo'
write(*,'(A80)') '============================[read from data]==================================='
write(*, '(3A25)') 'datafile',trim(datafile(1)),trim(datafile(2))

open( 2, file = datafile(1), status = 'old' )
do while (.true.)
        read(2, *) head
        if (head(1:1) == '#') cycle
        backspace(2)
        exit
enddo
open( 3, file = datafile(2), status = 'old' )
do while (.true.)
        read(3, *) head
        if (head(1:1) == '#') cycle
        backspace(3)
        exit
enddo

atom_tot = 0
atom_num = 0
p = 0.d0
timestep = 0
write(*,'(2A25)') 'timestep','atom_num'
do while (.true.)
        read(2, *, iostat = ios) timestep(1), atom_num(1), q(1)
        if (ios<0) exit
        if (timestep(1) /= timestep(2)) then
                write(*,'(3I25)') timestep(1), atom_num
        endif
        read(3, *) timestep(2), atom_num(2), q(2)
        if ( timestep(1) /= timestep(2) .or. atom_num(1) /= atom_num(2) ) then
                print *,'err two files not match'
                stop
        endif
        atom_tot = atom_tot + 1
        temp_int = nint( q / bin )
        p( temp_int(1), temp_int(2) ) = p( temp_int(1), temp_int(2) ) + 1.d0
enddo
close(2)
close(3)
write(*,'(A25,I25)') 'atom_tot', atom_tot
p = p / (atom_tot * bin(1) * bin(2))

outfile = datafile(1)(1:2)//'_'//datafile(2)(1:2)//'.boo_2d'
write(*,'(A80)') '============================[RESULT]==================================='
write(*,'(2A25)') 'outfile', trim(outfile)
open(4, file = outfile, status='replace')
write(4,'(A1,A24,2A25)') '#',datafile(1)(1:2),datafile(2)(1:2), 'p_density'
do i = 1, n_bin(1)
        do j = 1, n_bin(2)
                if (p(i,j)==0.d0) cycle
                write(4,'(3F)') i*bin(1), j*bin(2), p(i,j)
        enddo
enddo
close(4)

deallocate(p)
endprogram boo_2d 
