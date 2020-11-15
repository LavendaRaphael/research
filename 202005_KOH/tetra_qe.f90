!==========================================================================================
!===============================================================[NOTES]
!未完成程序
!===============================================================[USE]
!./tetra_qe.x tetra.in
!===============================================================[tetra.in]
!datafile       'water.pos'                                     #ps bohr
!cell_size      18.73479726765 18.73479726765 18.73479726765    #bohr
!atomtype_tot   2
! O             32
! H             64
!atomtarg_name  O
!tstart         10                                              #ps
!tend           28                                              #ps
!rc             3.29                                            #angstrom
!===============================================================[OUTFILE]
!tetra_10to30ps.out
!=========================================================================================
program get_tadf
implicit none

integer, parameter              :: DP = 8
real (DP), parameter            :: pi = 3.14159265359, bohr2angstrom=0.529177210903
integer                         :: clock_start, clock_end, clock_rate
integer (DP)                    :: i, j, k, l, m, ios, temp_int0
real (DP)                       :: temp_real0, temp_real (3)
character (len=40)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile, logfile='mylog'

real (DP), parameter            :: rad2deg=180.d0/pi
real (DP)                       :: dist, dtheta, rc, cell_size(3), delta(3), tstart, tend, di
real (DP), allocatable          :: tadf(:), posi(:,:), delta_xyz (:, :, :), ri(:)
integer (DP)                    :: atomtype_tot, atomtarg_num, atom_tot, di_num, snap_num, coor_max
integer (DP), allocatable       :: atomtype_num (:), coor_num(:)
character (len=40)              :: atomtarg_name, tstart_char, tend_char
character (len=40), allocatable :: atomtype_name (:)
logical, allocatable            :: logilist (:)

open (21, file=logfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (21, leng//"'[READ INFILE]: "//infile//"')")
open(11, file = infile, status = 'old')
do while (.true.)
        read (11, *, iostat = ios) temp_char0
        if (ios < 0) exit
        backspace (11)
        select case ( temp_char0)
        case ('datafile')
                read (11, *) temp_char0, datafile
                write (21, ' (A25, A25)') trim (temp_char0), trim (datafile)
        case ('atomtype_tot')
                read (11, *) temp_char0, atomtype_tot
                write (21, ' (A25, I25)') trim (temp_char0), atomtype_tot
                allocate (atomtype_name (atomtype_tot), atomtype_num (atomtype_tot))
                do i = 1, atomtype_tot
                        read (11, *) atomtype_name (i), atomtype_num (i)
                        write (21, ' (A25, I25)') trim (atomtype_name (i)), atomtype_num (i)
                enddo
        case ('cell_size')
                read (11, *) temp_char0, cell_size
                write (21, ' (A25, 3F)') trim (temp_char0), cell_size
        case ('atomtarg_name')
                read (11, *) temp_char0, atomtarg_name
                write (21, ' (2A25)') trim (temp_char0), trim (atomtarg_name)
        case ('tstart')
                read(11, *) temp_char0, tstart_char
                write (21, ' (2A25)') trim(temp_char0), trim(tstart_char)
                read (tstart_char, *) tstart
        case ('tend')
                read (11, *) temp_char0, tend_char
                write (21, ' (2A25)') trim(temp_char0), trim(tend_char)
                read (tend_char, *) tend
        case ('rc')
                read (11, *) temp_char0, rc
                write (21, ' (A25, F)') trim(temp_char0), rc
                rc = rc / bohr2angstrom
        case ('di')
                read(11, *) temp_char0, di
                write(21, ' (A25, F)') trim(temp_char0), di
                di = di / rad2deg
        case ('coor_max')
                read(11, *) temp_char0, coor_max
                write(21, ' (A25, I25)') trim(temp_char0), coor_max
        case DEFAULT
                if (temp_char0(1:1) /= '#') then
                        write(21, ' (A25)') 'unkonwn parameter'
                        stop
                endif
        end select
end do
close(11)
allocate (logilist (atomtype_tot))
atomtarg_num = 0
atom_tot = 0
do i = 1, atomtype_tot
        atom_tot = atom_tot + atomtype_num (i)
        if (atomtype_name (i) == atomtarg_name) then
                atomtarg_num = atomtarg_num + atomtype_num (i)
                logilist (i) = .true.
        endif
enddo
write (21, ' (A25, I25)') 'atom_tot', atom_tot
write (21, ' (A25)') 'atomtarg'
write (21, " (2A25, I25)") '',trim (atomtarg_name), atomtarg_num
write (temp_char0, *) atomtype_tot
write (21, ' (A25)') 'logilist'
write (21, " (A25, "//temp_char0//"A25)") '', atomtype_name
write (21, " (A25, "//temp_char0//"L25)") trim (atomtarg_name), logilist
allocate (posi (atomtarg_num, 3), coor_num (atomtarg_num), delta_xyz (atomtarg_num, coor_max, 3))
di_num = nint( pi / di)
allocate (tadf (0:di_num), ri (0:di_num))
!===============================================================[COMPUTE]
write (21, leng//"'[READ DATAFILE]: "//datafile//"')")
open(12, file = datafile, status = 'old')
tadf = 0.d0
snap_num = 0
write (21, '(2A25)') 'snapshot', 'time_ps'
loop0: do while (.true.)
do while (.true.)
        read(12, *, iostat = ios) temp_int0, temp_real0
        if (ios < 0) exit loop0
        if (temp_real0 < tstart) then
                do i = 1, atom_tot
                        read(12, *)
                end do
        elseif (temp_real0 <= tend) then
                snap_num = snap_num + 1
                exit
        else
                exit loop0
        end if
end do
write (21, '( I25, F)') temp_int0, temp_real0
j=0
do l = 1, atomtype_tot
        do i = 1, atomtype_num (l)
                read (12, *) temp_real
                if (logilist (l)) then
                        j = j + 1
                        posi(j,:) = temp_real
                endif
        enddo
end do
coor_num = 0 ! mark initial coor water_index
do i = 1, atomtarg_num
        do j = i+1, atomtarg_num
                delta = posi (j, :) - posi (i, :)
                delta = delta - nint (delta / cell_size) * cell_size
                if (maxval (abs (delta)) > rc) cycle
                dist = sqrt (delta (1) ** 2 + delta (2) ** 2 + delta (3) ** 2)
                if (dist <= rc) then
                        coor_num(i)=coor_num(i)+1
                        coor_num(j)=coor_num(j)+1
                        if (coor_num(i) > coor_max .or. coor_num(j) > coor_max) then
                                write(21, *) 'coor_max is too small!'
                                stop
                        endif
                        delta_xyz (i, coor_num(i), :) = delta/dist
                        delta_xyz (j, coor_num(j), :) = -delta_xyz (i, coor_num(i), :)
                endif
        enddo
        do j = 1, coor_num(i)
                do k = j+1, coor_num(i)
                        temp_int0 = nint (acos (sum (delta_xyz (i,j,:) * delta_xyz (i,k,:))) / di)
                        tadf(temp_int0)=tadf(temp_int0) + 1.d0
                enddo
        enddo
enddo
enddo loop0
close (12)
tadf = tadf*(/(sin(i*di),i=0,di_num)/)
tadf(0) = tadf(0) * 2.d0
tadf(di_num) = tadf(di_num) / (pi/di - real(di_num) + 0.5d0)
tadf = tadf / (sum (tadf) * di)
!===============================================================[OUTPUT]
write (21, leng//"'[OUTPUT]')")
write (21, ' (A25, I25)') 'snap_num', snap_num
ri = (/( i * di * rad2deg, i = 0, di_num)/)
tadf = tadf / rad2deg 
outfile = 'tadf_'//trim(tstart_char)//'to'//trim(tend_char)//'ps.out'
logfile = 'tadf_'//trim(tstart_char)//'to'//trim(tend_char)//'ps.log'
write (21, "(2A25)") 'outfile', trim(outfile)
open(unit = 13, file = outfile, status = 'replace')
write(13, "(A, A24, A25)") '#','ri_degree','tadf'
do i = 0, di_num
   write(13, "(F25.10, F25.10)") ri(i), tadf(i)
enddo
close(13)
!===============================================================[FINALIZE]
deallocate (atomtype_name, atomtype_num)
deallocate (posi, delta_xyz, coor_num)
deallocate (tadf, ri)
deallocate (logilist)
call system_clock (clock_end, clock_rate)
write (21, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(21)
call rename('mylog', logfile)
end program get_tadf
