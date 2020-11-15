!===================USE=========================
!./rdf_lmp.x rdf.in
!===================DATAFILE====================
!dump.lammpstrj
!==================INFILE ====================
!atom_1     1
!atom_2     1
!rc         50.0
!dr         0.1
!ts_start      80000
!ts_end        2000000
!===================OUTFILE===========================
!1_1.rdf
!==========================================================
program get_rdf
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 :: dist, dr, rc, cell_size(3), delta(2,3), temp_real(3)
real(DP), allocatable    :: ri(:), rdf(:), posi_1(:,:), posi_2(:,:), rdf_int(:)
integer(DP)              :: i, j, atom_num(2), atom_tot, ios, dr_num, cell_klm(3), k, l, m, temp_int, ts_start, ts_end, snap_num=0
!integer(DP), allocatable    ::
character(len=40)        :: infile, atom_name(2), head

call get_command_argument(1,infile)
write(*,'(A25, A25)') 'inputfile', trim(infile)
write(*,'(A80)') '=============================read from infile=================================='
open(1, file = infile, status = 'old')
do i = 1, 6
        read(1,*) head
        backspace(1)
        select case ( head )
        case('atom_1')
                read(1,*) head, atom_name(1)
                write(*,'(A25, A25, I25)') trim(head),trim(atom_name(1))
        case('atom_2')
                read(1,*) head, atom_name(2)
                write(*,'(A25, A25, I25)') trim(head), trim(atom_name(2))
        case('rc')
                read(1,*) head, rc
                write(*,'(A25, F)') trim(head), rc
        case('dr')
                read(1,*) head, dr
                write(*,'(A25, F)') trim(head), dr
        case('ts_start')
                read(1,*) head, ts_start
                write(*,'(A25, I25)') trim(head), ts_start
        case('ts_end')
                read(1,*) head, ts_end
                write(*,'(A25, I25)') trim(head), ts_end
        end select
end do
close(1)

write(*, '(A25,A25)') 'datafile','dump.lammpstrj'
write(*,'(A80)') '===========================read from data==================================='
open(2, file = 'dump.lammpstrj', status = 'old')
do i = 1, 3
        read(2, *)
end do
read(2, *) atom_tot
write(*, '(A25, I25)') 'atom_tot', atom_tot
read(2, *)
do i = 1, 3
        read(2, *) head, cell_size(i)
end do
write(*, '(A25, F, F, F)') 'cell_size', cell_size
read(2, *)
do i = 1, atom_tot
        read(2, *) head, head
        if (head == atom_name(1)) then
                atom_num(1) = atom_num(1) + 1
        end if
        if (head == atom_name(2)) then
                atom_num(2) = atom_num(2) + 1
        end if
end do
close(2)
write(*, '(A25, A25)') trim(atom_name(1)),trim(atom_name(2))
write(*, '(I25, I25)') atom_num

allocate(posi_1(atom_num(1), 3), posi_2(atom_num(2), 3))
cell_klm = nint (rc / cell_size)
dr_num = nint( rc / dr)
write(*,'(A25, I25)') 'dr_num', dr_num
allocate( rdf (dr_num), ri (dr_num), rdf_int(dr_num))

open(3, file = 'dump.lammpstrj', status = 'old')
read(3, *)
rdf = 0.d0
loop0: do while (.true.)
do while (.true.)
        read(3, *) temp_int
        if (temp_int < ts_start) then
                do i = 1, 8 + atom_tot
                        read(3, *)
                end do
        elseif (ts_start <= temp_int <= ts_end) then
                do i = 1, 7
                        read(3, *)
                end do
                snap_num = snap_num + 1
                exit
        else
                exit loop0
        end if
end do
j=0
k=0
do i = 1, atom_tot
        read(3, *) head, head, temp_real
        if (head == atom_name(1)) then
                j = j + 1
                posi_1(j, :) = temp_real
        end if
        if (head == atom_name(2)) then
                k = k + 1
                posi_2(k, :) = temp_real
        end if
end do
write(*,'(I25,I25,I25,I25)') snap_num, temp_int, j, k
do i = 1, atom_num(1)
        do j = 1, atom_num(2)
                delta(0,:) = posi_1(i,:) - posi_2(j,:)
                delta(0,:) = delta(0,:) - nint (delta(0,:) / cell_size) * cell_size
                do k = -cell_klm(1), cell_klm(1)
                        do l = -cell_klm(2), cell_klm(2)
                                do m = -cell_klm(3), cell_klm(3)
                                        if ( atom_name(1) == atom_name(2) .and. i == j .and. k==0 .and. l==0 .and. m==0 ) cycle
                                        delta(1,:) = delta(0,:) + cell_size*(/k,l,m/)
                                        dist = sqrt(delta(1,1)**2 + delta(1,2)**2 + delta(1,3)**2)
                                        temp_int = nint ( dist / dr )
                                        if ( temp_int .gt. dr_num ) cycle
                                        if ( temp_int < 1) then
                                                write(*,'(A25,F, I25)') 'err',dist,temp_int
                                                stop
                                        end if
                                        rdf(temp_int) = rdf(temp_int) + 1.d0
                                enddo
                        enddo
                enddo
        enddo
enddo
read(3, *, iostat = ios)
if (ios<0) exit loop0
enddo loop0
close(3)

ri = (/( i * dr, i = 1, dr_num )/)
rdf = rdf / (snap_num * atom_num(1))
rdf_int = (/( sum( rdf(1 : i ) ), i = 1, dr_num )/)
rdf = rdf * cell_size(1) * cell_size(2) * cell_size(3) / (4.d0 * pi * ri * ri * dr * atom_num(2) )

open(unit = 4, file = trim(atom_name(1))//'_'//trim(atom_name(2))//'.rdf', status = 'replace')
write(*,'(A25, A25)') 'outfile',trim(atom_name(1))//'_'//trim(atom_name(2))//'.rdf'
write(4, "(A, A25, A25, A25)") '#','ri','rdf','rdf_int'
do i = 1, dr_num
   write(4, "(F8.4, F12.6, F)") ri(i), rdf(i), rdf_int(i)
enddo
close(4)

deallocate(ri, rdf, rdf_int, posi_1, posi_2)
end program get_rdf
