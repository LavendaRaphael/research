!===================USE=========================
!./boo_lmp.x boo.in
!===================DATAFILE====================
!dump.lammpstrj
!==================INFILE ====================
!atom_name      1
!rc             4.0
!coor           12
!ts_start       80000
!ts_end         2000000
!l              6
!===================OUTFILE===========================
!q6.boo
!===================================================
program get_boo
implicit  none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 :: dist, cell_size(3), delta(3), temp_real(3), rc, ql, costheta, sintheta, phi
real(DP), allocatable    :: posi(:,:), neig_dist(:,:,:), qi(:)
integer(DP)              :: i, j, atom_num, atom_tot, ios, l, temp_int, ts_start, ts_end, snap_num=0, coor, fact, npr, m, k, ts_on, const
integer(DP), allocatable :: neig_id(:,:)
character(len=40)        :: infile, atom_name, head, outfile
complex(DP), allocatable :: ylm(:,:,:)

call get_command_argument(1,infile)
write(*,'(A25, A25)') 'inputfile', trim(infile)
write(*,"(A80)") '=============================[read from infile]=================================='
open(1, file = infile, status = 'old')
do while (.true.)
        read( 1 , * , iostat = ios ) head
        if ( ios < 0 ) exit
        backspace(1)
        select case( head )
        case( 'atom_name' )
                read(1,*) head, atom_name
                write(*,'(A25, A25)') trim(head),trim(atom_name)
        case('rc')
                read(1,*) head, rc
                write(*,'(A25, F)') trim(head), rc
        case('coor')
                read(1,*) head, coor
                write(*,'(A25, I25)') trim(head), coor
        case('ts_start')
                read(1,*) head, ts_start
                write(*,'(A25, I25)') trim(head), ts_start
        case('ts_end')
                read(1,*) head, ts_end
                write(*,'(A25, I25)') trim(head), ts_end
        case('l')
                read(1,*) head, l
                write(*,'(A25, I25)') trim(head), l
        end select
end do
close(1)

write(*, '(A25,A25)') 'datafile','dump.lammpstrj'
write(*,'(A80)') '============================[read from data]==================================='
open( 2, file = 'dump.lammpstrj', status = 'old' )
do i = 1, 3
        read( 2, * )
end do
read( 2, * ) atom_tot
write(*, '(A25, I25)') 'atom_tot', atom_tot
read( 2, * )
do i = 1, 3
        read( 2, * ) head, cell_size( i )
end do
write( *, '(A25, F, F, F)' ) 'cell_size', cell_size
read( 2, * )
atom_num = 0
do i = 1, atom_tot
        read(2, *) head, head
        if (head == atom_name) then
                atom_num = atom_num + 1
        end if
end do
close(2)
write(*, '(A25, I25)') trim(atom_name), atom_num
allocate( posi( atom_num, 3 ), neig_dist( atom_num, coor, 0:3 ), neig_id( atom_num, 0:coor ))
allocate( ylm( atom_num, coor, 0:l ))
allocate( qi( atom_num ))
const = coor * 2**l * fact(l)

write(*,'(A80)') '==============================[compute log]====================================='
open(3, file = 'dump.lammpstrj', status = 'old')
read(3, *) 
write(head, *) l
outfile = 'q'//trim(adjustl(head))//'.boo'
open(4, file = outfile, status = 'replace', form='formatted')
write(4, *) head
write(4, '(A1,A24,A25,A25)') '#','timestep','atom_id','q'//trim(adjustl(head))
loop0: do while (.true.)
do while (.true.)
        read(3, *) ts_on
        if (ts_on < ts_start) then
                do i = 1, 8 + atom_tot
                        read(3, *)
                end do
        elseif (ts_start <= ts_on .and. ts_on <= ts_end) then
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
do i = 1, atom_tot
        read(3, *) head, head, temp_real
        if (head == atom_name) then
                j = j + 1
                posi(j, :) = temp_real
        end if
end do

ylm = 0.d0
neig_dist(:,:,0) = rc ! set inital cutoff
neig_id(:,0) = 1 ! cutoff index
neig_id(:,1:) = 0
do i = 1, atom_num
        do j = i+1, atom_num
                delta = posi( j, : ) - posi( i, : )
                delta = delta - nint( delta / cell_size ) * cell_size
                if ( maxval( abs(delta) ) >= neig_dist( i, neig_id( i, 0 ), 0 ) .and. maxval( abs(delta) ) >= neig_dist( j, neig_id( j, 0 ), 0 )) cycle
                dist = sqrt(  delta(1) ** 2 + delta(2) ** 2 + delta(3) ** 2 )
                if ( dist < neig_dist( i, neig_id( i, 0 ), 0 ) ) then
                        neig_id( i, neig_id(i,0) ) = j
                        neig_dist( i, neig_id(i,0), 0 ) = dist
                        neig_dist( i, neig_id(i,0), 1: ) = delta
                        neig_id( i, 0 ) = maxloc( neig_dist(i,:,0), dim=1 )
                endif
                if ( dist < neig_dist( j, neig_id( j, 0 ), 0 ) ) then
                        neig_id( j, neig_id(j,0) ) = i
                        neig_dist( j, neig_id(j,0), 0 ) = dist
                        neig_dist( j, neig_id(j,0), 1: ) = -delta
                        neig_id( j, 0 ) = maxloc( neig_dist(j,:,0), dim=1 )
                endif
        enddo
        if ( neig_id(i,coor) == 0 ) then
                write(*,'(A25)') 'err nnn<coor'
                write(*,'(I25,12F)') i,neig_dist(i,:,0)
                stop
        endif
        do j = 1, coor
                temp_int = findloc( neig_id( neig_id(i,j), 1: ), i, 1 )
                if (i > neig_id(i,j) .and. temp_int /= 0 ) then
                        do m = 0, l
                                ylm( i, j, m ) = ylm( neig_id(i,j), temp_int, m )
                        enddo
                        cycle
                endif
                costheta = neig_dist( i, j, 3 ) / neig_dist( i, j, 0 )
                sintheta = sqrt( 1 - costheta ** 2 )
                phi = acos( neig_dist( i, j, 1 ) / sqrt( neig_dist( i, j, 1 ) ** 2 + neig_dist( i, j, 2 ) ** 2 ))
                if ( neig_dist( i, j, 2 ) < 0 ) then
                        phi = -phi
                endif
                do m = 0,l
                        do k = ceiling((l+m)/2.d0), l
                                ylm( i, j, m ) = ylm( i, j, m ) + ( -1 ) ** ( l - k ) * npr( l, k ) / fact( k ) * npr( 2 * k, l + m ) * costheta ** ( 2 * k - l - m )
                        enddo
                        ylm( i, j, m ) = ylm( i, j, m ) * sintheta ** m * cmplx( cos( m * phi ), sin( m * phi ))
                enddo
        enddo
enddo

qi = 0.d0
do i = 1, atom_num
        qi( i ) = abs( sum( ylm( i, :, 0 ))) ** 2
        do m = 1, l
                qi( i ) = qi( i ) + 2 * abs( sum( ylm( i, :, m )))**2 / npr( l + m, 2 * m )
        enddo
        qi( i ) = sqrt( qi( i )) / const
        write(4,'(2I25,F)') ts_on, i, qi(i)
enddo
write(*,*) ts_on
ql = ql + sum(qi)

read( 3, *, iostat = ios )
if ( ios < 0 ) exit loop0
enddo loop0

close(3)
close(4)
ql = ql / snap_num / atom_num

open(5,file = outfile, status='old', access='stream')
write(head,'(A3,I1,F)') '# q',l,ql
write(5) head
close(5)
write(*,'(A80)') '==============================[outfile]====================================='
write(*,'(A25)') outfile
write(*,'(A1,I1,F)') 'q',l,ql

deallocate(posi, neig_dist, qi, neig_id, ylm)
end program get_boo
!=========================[npr function]============================
function npr(n,r)
implicit none

INTEGER, PARAMETER       ::  DP = 8

integer(DP), intent(in)  :: n, r
integer(DP)              :: npr, i

npr = 1
do i = n-r+1, n
       npr = npr * i 
enddo

endfunction
!=========================[factorial function]======================
function fact(n)
implicit none

INTEGER, PARAMETER       ::  DP = 8

integer(DP), intent(in)  :: n
integer(DP)              :: fact, i

fact = 1
do i = 1, n
       fact = fact * i
enddo

endfunction
