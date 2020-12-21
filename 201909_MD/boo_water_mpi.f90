!==========================================================================================
!===============================================================[USE]
!mpirun -n 10 ./boo_water_mpi.x boo.in
!===============================================================[boo.in]
!O              1
!H              2
!rc             6.0
!coor           4
!ts_start       1
!ts_end         5000000
!l              6
!datafile       1124_ala_265nvt.lammpstrj
!===============================================================[1124_ala_265nvt.lammpstrj]
!ITEM: TIMESTEP
!20000
!ITEM: NUMBER OF ATOMS
!10630
!ITEM: BOX BOUNDS pp pp pp
!-5.0000000000000000e+00 6.7855000000000004e+01
!0.0000000000000000e+00 4.6991999999999997e+01
!0.0000000000000000e+00 4.4171999999999997e+01
!ITEM: ATOMS id mol type x y z vx vy vz 
!1 1 1 1.6757 2.46622 2.19259 0.00685243 0.00498661 -0.00126291 
!2 1 2 1.64156 2.42943 3.18519 0.0143634 -0.0328255 -0.00349937 
!...
!===============================================================[OUTFILE]
!q6.boo
!===============================================================[q6.boo]
!# q6       0.5370115464555060
!#                timestep                  atom_id                       q6
!                   900000                        1       0.4807685411028426
!                   900000                        2       0.4405812840680084
!...
!=========================================================================================
program get_boo
use mpi
implicit none

integer                   :: ntasks, rank, ierr, stat (MPI_STATUS_SIZE)
integer, parameter        :: DP = 8
real (DP), parameter      :: pi = 3.14159265359
integer                   :: clock_start, clock_end, clock_rate
integer (DP)              :: i, j, k
real (DP)                 :: temp_real, temp_real1, temp_real2, temp_real3
character (len=40)        :: temp_char

real (DP)                 :: dist, cell_size (3), delta (3), rc, ql, costheta, sintheta, phi, q_rank=0.d0, const
real (DP), allocatable    :: posi (:, :), delta_xyz (:, :, :), delta_r (:, :), qi (:)
integer (DP)              :: water_tot, atom_tot, ios, l, m, ts_start, ts_end, snap_num=0, coor, fact, npr, ts_on, mol_tot
integer (DP), allocatable :: coor_id (:, :), rc_id(:), mol (:, :)
character (len=40)        :: infile, O, H, outfile, datafile, temp_file, leng=" (65 ('='), "
complex (DP), allocatable :: ylm (:, :, :)

call MPI_INIT (ierr)
call MPI_COMM_SIZE (MPI_COMM_WORLD, ntasks, ierr)
call MPI_COMM_RANK (MPI_COMM_WORLD, rank, ierr)
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument (1, infile)
if (rank == 0) then
write (*, leng//"'[READ INFILE]: "//infile//"')")
open (11, file = infile, status = 'old')
do while (.true.)
        read (11, *, iostat = ios) temp_char
        if (ios < 0) exit
        backspace (11)
        select case (temp_char)
        case ('O')
                read (11, *) temp_char, O
                write (*, ' (A25, A25)') trim (temp_char), trim (O)
        case ('H')
                read (11, *) temp_char, H
                write (*, ' (A25, A25)') trim (temp_char), trim (H)
        case ('rc')
                read (11, *) temp_char, rc
                write (*, ' (A25, F)') trim (temp_char), rc
        case ('coor')
                read (11, *) temp_char, coor
                write (*, ' (A25, I25)') trim (temp_char), coor
        case ('ts_start')
                read (11, *) temp_char, ts_start
                write (*, ' (A25, I25)') trim (temp_char), ts_start
        case ('ts_end')
                read (11, *) temp_char, ts_end
                write (*, ' (A25, I25)') trim (temp_char), ts_end
        case ('l')
                read (11, *) temp_char, l
                write (*, ' (A25, I25)') trim (temp_char), l
        case ('datafile')
                read (11, *) temp_char, datafile
                write (*, ' (A25, A25)') trim (temp_char), trim (datafile)
        end select
end do
close (11)
!===============================================================[READ DATEFILE]
write (*, leng//"'[READ DATAFILE]: "//datafile//"')")
open (12, file = datafile, status = 'old')
read (12, *) ! ITEM: TIMESTEP
read (12, *) ! dump_0
read (12, *) ! ITEM: NUMBER OF ATOMS
read (12, *) atom_tot
write (*, ' (A25, I25)') 'atom_tot', atom_tot
read (12, *) ! ITEM: BOX BOUNDS pp pp pp
do i = 1, 3
        read (12, *) temp_real1, temp_real2
        cell_size (i) = temp_real2 - temp_real1
end do
write (*, ' (A25, F, F, F)') 'cell_size', cell_size
read (12, *) ! ITEM: ATOMS id mol type x y z vx vy vz
mol_tot = 0
do i = 1, atom_tot
        read (12, *) temp_char, j
        if (mol_tot < j) then
                mol_tot = j
        end if
end do
write (*, ' (A25, I25)') 'mol_tot', mol_tot
allocate (mol (mol_tot, 4)) ! {mol_id; O, H, others, [1 (iswater), 0 (not)]}
close (12)
!===============================================================[COUNT WATER]
open (13, file = datafile, status = 'old')
do i = 1, 9
    read (13, *)
enddo
mol = 0
do i = 1, atom_tot
        read (13, *) temp_char, j, temp_char
        if (temp_char == O) then
                mol (j, 1) = mol (j, 1) + 1
        elseif (temp_char == H) then
                mol (j, 2) = mol (j, 2) + 1
        else
                mol (j, 3) = mol (j, 3) + 1
        end if
end do
close (13)
do  i = 1, mol_tot
    if (mol (i, 1) == 1 .and. mol (i, 2) == 2 .and. mol (i, 3) == 0) then
        mol (i, 4) = 1
    endif
enddo
water_tot = sum (mol (:, 4))
write (*, ' (A25, I25)') 'water_tot', water_tot
write (*, leng//"'[COMPUTE LOG]')")
write (*, '(3A25)') 'TIMESTEP','ql','CORE_ID'
endif
!===============================================================[MPI_BCAST]
call MPI_BCAST (O, 40, MPI_CHARACTER, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (H, 40, MPI_CHARACTER, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (rc, 1, MPI_REAL8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (coor, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (ts_start, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (ts_end, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (l, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (datafile, 40, MPI_CHARACTER, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (atom_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (cell_size, 3, MPI_REAL8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (mol_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
if (rank /= 0) then
        allocate (mol (mol_tot, 4))
endif
call MPI_BCAST (mol, mol_tot*4, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (water_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
allocate (posi (water_tot, 3), ylm (water_tot, coor, 0:l), qi (water_tot))
allocate (delta_xyz (water_tot, coor, 3), delta_r (water_tot, coor), coor_id (water_tot, coor), rc_id (water_tot))
!===============================================================[COMPUTE]
const = sqrt (4 * pi / real (2*l + 1)) / real(coor)
open (14, file = datafile, status = 'old')
write (temp_char, *) rank
temp_file = 'temp_file_'//trim (adjustl (temp_char))
open (15, file = temp_file, status = 'replace')
loop0: do while (.true.)
do while (.true.)
        read (14, *, iostat=ios)
        if (ios < 0) exit loop0
        read (14, *) ts_on
        do i = 1, 7
                read (14, *)
        end do
        if (ts_on < ts_start) then
                do i = 1, atom_tot
                        read (14, *)
                end do
        elseif (ts_start <= ts_on .and. ts_on <= ts_end) then
                snap_num = snap_num + 1
                if (mod (snap_num, ntasks) == rank) exit
                do i = 1, atom_tot
                        read (14, *)
                end do
        else
                exit loop0
        end if
end do
j = 0
do i = 1, atom_tot
        ! ITEM: ATOMS id mol type x y z
        read (14, *) temp_char, k, temp_char, temp_real1, temp_real2, temp_real3
        if (temp_char == O .and. mol (k, 4) == 1) then
                j = j + 1
                posi (j, :) = (/temp_real1, temp_real2, temp_real3/)
        end if
end do

ylm = 0.d0
delta_r = rc ! set initial cutoff
rc_id = 1 ! cutoff coor_index
coor_id = 0 ! mark initial coor water_index
do i = 1, water_tot
        do j = i+1, water_tot
                delta = posi (j, :) - posi (i, :)
                delta = delta - nint (delta / cell_size) * cell_size
                if (maxval (abs (delta)) >= delta_r (i, rc_id (i)) .and. maxval (abs (delta)) >= delta_r (j, rc_id (j))) cycle
                dist = sqrt (delta (1) ** 2 + delta (2) ** 2 + delta (3) ** 2)
                if (dist < delta_r (i, rc_id (i))) then
                        coor_id (i, rc_id (i)) = j
                        delta_r (i, rc_id (i)) = dist
                        delta_xyz (i, rc_id (i), :) = delta
                        rc_id (i) = maxloc (delta_r (i, :), dim=1)
                endif
                if (dist < delta_r (j, rc_id (j))) then
                        coor_id (j, rc_id (j)) = i
                        delta_r (j, rc_id (j)) = dist
                        delta_xyz (j, rc_id (j), :) = -delta
                        rc_id (j) = maxloc (delta_r (j, :), dim=1)
                endif
        enddo
        if (coor_id (i, coor) == 0) then ! check whether rc is setted too small or not
                write (*, *) 'ERR: nnn < coor, rc is too small.'
                write (temp_char, *) coor
                write (*, ' (I25, '//temp_char//'F)') i, delta_r (i, :)
                stop
        endif
        do j = 1, coor
                k = findloc (coor_id (coor_id (i, j), :), i, 1)
                if (i > coor_id (i, j) .and. k /= 0) then
                        ylm (i, j, :) = ylm (coor_id (i, j), k, :)
                        cycle
                endif
                costheta = delta_xyz (i, j, 3) / delta_r (i, j)
                sintheta = sqrt (1 - costheta ** 2)
                phi = acos (delta_xyz (i, j, 1) / sqrt (delta_xyz (i, j, 1) ** 2 + delta_xyz (i, j, 2) ** 2))
                if (delta_xyz (i, j, 2) < 0) phi = -phi
                call sph_har (l, costheta, sintheta, phi, ylm(i, j, :))
        enddo
enddo

qi = 0.d0
do i = 1, water_tot
        qi (i) = abs (sum (ylm (i, :, 0))) ** 2
        do m = 1, l
                qi (i) = qi (i) + 2 * abs (sum (ylm (i, :, m)))**2
        enddo
        qi (i) = sqrt (qi (i)) * const
        write (15, ' (2I25, F)') ts_on, i, qi (i)
enddo
temp_real  = sum (qi)/water_tot
write (*, ' (I25, F, I25)') ts_on, temp_real , rank
q_rank = q_rank + temp_real 
enddo loop0
close (14)
close (15)
!===============================================================[OUTPUT]
call MPI_REDUCE (q_rank, ql, 1, MPI_REAL8, MPI_SUM, 0, MPI_COMM_WORLD, ierr)

if (rank == 0) then
write (*, leng//"'[OUTPUT]')")
write (*, ' (A25, I25)') 'snap_num', snap_num
ql = ql / snap_num
write (*, ' (A25, F)') 'ql', ql
write (outfile, ' (A1, I1, A4)') 'q', l, '.boo'
write (*, leng//"'[OUTFILE]: "//outfile//"')")
open (16, file = outfile, status='replace')
write (16, ' (A3, I1, F)') '# q', l, ql
write (16, ' (A1, A24, A25, A24, I1)') '#', 'timestep', 'atom_id', 'q', l
close (16)
call system ('cat temp_file_* >> '//outfile)
do i = 0, ntasks-1 
        write (temp_char, *) i
        temp_file = 'temp_file_'//trim (adjustl (temp_char))
        open (17+i, file = temp_file, status = 'old')
        close (17+i, status='delete')
enddo
call system_clock (clock_end, clock_rate)
write (*, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
endif 
!===============================================================[FINALIZE]
deallocate (posi, delta_r, delta_xyz, qi, coor_id, rc_id, ylm, mol)
call mpi_finalize (ierr)

end program get_boo
!==================================================================================================
!===============================================================[NPR FUNCTION]
function npr (n, r)
implicit none

INTEGER, PARAMETER       ::  DP = 8

integer (DP), intent (in)  :: n, r
integer (DP)              :: npr, i

npr = 1
do i = n-r+1, n
       npr = npr * i 
enddo

endfunction
!===============================================================[FUNCTION FACTORIAL]
function fact (n)
implicit none

INTEGER, PARAMETER       ::  DP = 8

integer (DP), intent (in)  :: n
integer (DP)              :: fact, i

fact = 1
do i = 1, n
       fact = fact * i
enddo

endfunction
!===============================================================[FUNCTION Spherical harmonics]
subroutine sph_har (l, costheta, sintheta, phi, ylm)
! Y(l,-m) = (-1)**m * conjg (Y (l, m)), m > 0
implicit none

INTEGER, PARAMETER        :: DP = 8
real (DP), parameter      :: pi = 3.14159265359

integer (DP), intent (in) :: l
real (DP), intent (in)    :: costheta, sintheta, phi
integer (DP)              :: m, i, npr, fact
complex (DP), intent(out) :: ylm (0:l)
real(DP)                  :: const

const = sqrt ((2 * l + 1)/(4 * pi)) / real (2**l * fact (l))
ylm = 0.d0
do m = 0, l
        do i = (l + m + mod (l+m, 2)) / 2, l
                ylm (m) = ylm (m) + (-1)**(l - i) * npr (l, i) / real(fact (i)) * npr (2 * i, l + m) * costheta**(2 * i - l - m)
        enddo
        ylm (m) = ylm (m) * sintheta**m * cmplx (cos (m * phi), sin (m * phi)) * (-1)**m / sqrt( 1.d0 * npr (l+m, 2*m))
enddo
ylm = ylm * const

end subroutine sph_har
