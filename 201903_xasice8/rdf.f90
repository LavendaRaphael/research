!===================USE=================================
!./rdf.x snap00.pos_rdf.in
!==================INFILE ====================
!prefix     snap00
!atom_1     O               64
!atom_2     H               128
!cell_size  17.631329       17.631329       25.655553
!rc         50.0
!dr         0.1
!scheme     10
!O    1 2.203916 2.203916 11.032247
!O    1 2.203916 2.203916 23.860024
!...
!H    10 15.427413 9.532545 15.374826
!H    10 15.427413 12.506616 15.374826
!===================OUTFILE===========================
!snap00.pos_OH_rdf.dat
!==========================================================
program get_rdf
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 :: dist, dr, rc, cell_size(3), delta(2,3), temp_f(3)
real(DP), allocatable    :: ri(:), rdf(:), posi_1(:,:,:), posi_2(:,:,:)
integer(DP)              :: i, j, atom_num(2), ios, dr_num, cell_klm(3), k, l, m, temp_int, scheme, n
integer(DP), allocatable :: cell_count(:,:,:), bin(:), o(:,:)
character(len=40)        :: infile, atom_name(2), head, prefix

call get_command_argument(1,infile)
write(*,'(A25, A25)') 'inputfile', trim(infile)
write(*,'(A80)') '=============================read from head=================================='
open(1, file = infile, status = 'old')
do i = 1, 7
        read(1,*) head
        backspace(1)
        select case ( head )
        case('prefix')
                read(1,*) head, prefix
                write(*,'(A25, A25)') trim(head),trim(prefix)
        case('atom_1')
                read(1,*) head, atom_name(1), atom_num(1)
                write(*,'(A25, A25, I25)') trim(head),trim(atom_name(1)),atom_num(1)
        case('atom_2')
                read(1,*) head, atom_name(2), atom_num(2)
                write(*,'(A25, A25, I25)') trim(head), trim(atom_name(2)), atom_num(2)
        case('cell_size')
                read(1,*) head, cell_size
                write(*,'(A25, F,F,F)') trim(head), cell_size
        case('rc')
                read(1,*) head, rc
                write(*,'(A25, F)') trim(head), rc
        case('dr')
                read(1,*) head, dr
                write(*,'(A25, F)') trim(head), dr
        case('scheme')
                read(1,*) head, scheme
                write(*,'(A25, I25)') trim(head), scheme
        end select
end do
allocate(posi_1(scheme, atom_num(1), 3), posi_2(scheme, atom_num(2), 3), o(2,scheme))
write(*,'(A80)') '===========================read from data==================================='
o=0
do while (.true.)
        read(1, *, iostat=ios) head, temp_int, temp_f !considering the situation of atom_name(1) == atom_name(2)
        if (ios < 0) exit
        if (head == atom_name(1)) then
                o(1,temp_int) = o(1,temp_int) + 1
                posi_1(temp_int,o(1,temp_int),:)=temp_f
        end if
        if (head == atom_name(2)) then
                o(2,temp_int) = o(2,temp_int) + 1
                posi_2(temp_int,o(2,temp_int),:)=temp_f
        end if
end do
close(1)
write(*,'(A25, A25, A25)') 'scheme',trim(atom_name(1)),trim(atom_name(2))
do i = 1, scheme
        write(*,'(I25,I25,I25)') i, o(:,i)
end do

cell_klm = nint (rc / cell_size)
allocate( cell_count (-cell_klm(1) : cell_klm(1), -cell_klm(2) : cell_klm(2), -cell_klm(3) : cell_klm(3)))
cell_count=0
dr_num = ceiling( rc / dr)
write(*,'(A25, I25)') 'dr_num', dr_num
allocate( rdf (dr_num), ri (dr_num), bin(dr_num))

bin=0
do n = 1, scheme
do i = 1, atom_num(1)
        do j = 1, atom_num(2)
                delta(0,:) = posi_1(n,i,:) - posi_2(n,j,:)
                delta(0,:) = delta(0,:) - nint (delta(0,:) / cell_size) * cell_size
                do k = -cell_klm(1), cell_klm(1)
                        do l = -cell_klm(2), cell_klm(2)
                                do m = -cell_klm(3), cell_klm(3)
                                        if ( atom_name(1) == atom_name(2) .and. i == j .and. k==0 .and. l==0 .and. m==0 ) cycle
                                        delta(1,:) = delta(0,:) + cell_size*(/k,l,m/)
                                        dist = sqrt(delta(1,1)**2 + delta(1,2)**2 + delta(1,3)**2)
                                        if ( dist .gt. rc ) cycle
                                        temp_int = ceiling ( dist / dr )
                                        if (temp_int > dr_num .or. temp_int < 1) then
                                                write(*,'(A25,F, I25)') 'err',dist,temp_int
                                                stop
                                        endif
                                        bin(temp_int) = bin(temp_int) + 1
                                        cell_count(k,l,m) = cell_count(k,l,m) + 1
                                enddo
                        enddo
                enddo
        enddo
enddo
enddo

write(*,'(A25, I25,I25,I25)') 'cell_klm', cell_klm
write(*,'(A25)') 'cell_count'
do k = -cell_klm(1), cell_klm(1)
        do l = -cell_klm(2), cell_klm(2)
                do m = -cell_klm(3), cell_klm(3)
                        write(*,'(I25,I25,I25,I25)') k,l,m,cell_count(k,l,m)
                enddo
        enddo
enddo

ri = (/( i * dr, i = 1, dr_num )/)
rdf = bin * cell_size(1) * cell_size(2) * cell_size(3) / (4.d0 / 3.d0 * pi * ( 3.d0 * ri * ( ri - dr) + dr * dr) * dr * atom_num(1) * atom_num(2) * scheme)

open(unit = 3, file = trim(prefix)//'_'//trim(atom_name(1))//trim(atom_name(2))//'_rdf.dat', status = 'replace')
write(*,'(A25, A25)') 'outfile_rdf',trim(prefix)//'_'//trim(atom_name(1))//trim(atom_name(2))//'_rdf.dat'
write(3, "(A, A7, A12, A10)") '#','ri','rdf','bin'
do i = 1, dr_num
   write(3, "(F8.4, F12.6, I10)") ri(i), rdf(i), bin(i)
enddo
close(3)

deallocate(ri, rdf, posi_1, posi_2, cell_count ,bin)
end program get_rdf
