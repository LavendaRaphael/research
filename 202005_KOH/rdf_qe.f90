!=========================================================================================
!===============================================================[USE]
!./rdf_qe.x rdf.in
!===============================================================[rdf.in]
!datafile       water.pos                                    #ps bohr
!cell_size      18.73479726765 18.73479726765 18.73479726765 #bohr
!atomtype_tot   2
! O             32
! H             64
!atomtarg_name  O       O
!tstart         0                                            #ps
!tend           5                                            #ps
!rc             18.0                                         #bohr
!dr             0.01                                         #angstrom
!===============================================================[OUTFILES]
!0to5ps_OO.rdf
!===============================================================[0to5_OO.rdf]
!#      ri_angstrom         rdf              rdf_int
!=========================================================================================
program get_rdf
implicit  none

integer, parameter              :: DP = 8
real (DP), parameter            :: pi = 3.14159265359, bohr2angstrom=0.529177210903
integer                         :: clock_start, clock_end, clock_rate
integer (DP)                    :: i, j, k, l, m, ios, temp_int0
real (DP)                       :: temp_real0, temp_real (3)
character (len=40)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile, logfile='mylog'

real (DP)                       :: dist, dr, rc, cell_size(3), delta(3), tstart, tend
real (DP), allocatable          :: ri(:), rdf(:), posi_1(:,:), posi_2(:,:), rdf_int(:)
integer (DP)                    :: atomtype_tot, atomtarg_num (2), atom_tot, dr_num, cell_abc(3), snap_num
integer (DP), allocatable       :: atomtype_num (:)
character (len=40)              :: atomtarg_name (2), tstart_char, tend_char
character (len=40), allocatable :: atomtype_name (:)
logical, allocatable            :: logilist (:,:)
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
                write (21, ' (3A25)') trim (temp_char0), trim (atomtarg_name (1)), trim (atomtarg_name (2))
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
        case ('dr')
                read(11, *) temp_char0, dr
                write(21, ' (A25, F)') trim(temp_char0), dr
                dr = dr / bohr2angstrom
        end select
end do
close(11)
atomtarg_num = 0
allocate (logilist (2, atomtype_tot))
atom_tot = 0
do i = 1, atomtype_tot
        atom_tot = atom_tot + atomtype_num (i)
        if (atomtype_name (i) == atomtarg_name (1)) then
                atomtarg_num (1) = atomtarg_num (1) + atomtype_num (i)
                logilist (1, i) = .true.
        endif
        if (atomtype_name (i) == atomtarg_name (2)) then
                atomtarg_num (2) = atomtarg_num (2) + atomtype_num (i)
                logilist (2, i) = .true.
        endif
enddo
write (21, ' (A25, I25)') 'atom_tot', atom_tot
write (21, ' (A25)') 'atomtarg'
write (21, " (25 (' '), A25, I25)") trim (atomtarg_name (1)), atomtarg_num (1)
write (21, " (25 (' '), A25, I25)") trim (atomtarg_name (2)), atomtarg_num (2)
write (temp_char0, *) atomtype_tot
write (21, ' (A25)') 'logilist'
write (21, " (A25, "//temp_char0//"A25)") '', atomtype_name
write (21, " (A25, "//temp_char0//"L25)") trim (atomtarg_name (1)), logilist (1, :)
write (21, " (A25, "//temp_char0//"L25)") trim (atomtarg_name (2)), logilist (2, :)
allocate (posi_1 (atomtarg_num (1), 3), posi_2 (atomtarg_num (2), 3))
cell_abc = nint (rc / cell_size)
dr_num = nint( rc / dr)
allocate (rdf (dr_num), ri (dr_num), rdf_int(dr_num))
!===============================================================[READ DATEFILE]
write (21, leng//"'[READ DATAFILE]: "//datafile//"')")
open(12, file = datafile, status = 'old')
rdf = 0.d0
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
k=0
do l = 1, atomtype_tot
        do i = 1, atomtype_num (l)
                read (12, *) temp_real
                if (logilist (1, l)) then
                        j = j + 1
                        posi_1(j, :) = temp_real
                endif
                if (logilist (2, l)) then
                        k = k + 1
                        posi_2(k, :) = temp_real
                endif
        enddo
end do
do i = 1, atomtarg_num(1)
        do j = 1, atomtarg_num(2)
                delta(:) = posi_1(i,:) - posi_2(j,:)
                delta(:) = delta(:) - nint (delta(:) / cell_size) * cell_size
                do k = -cell_abc(1), cell_abc(1)
                        do l = -cell_abc(2), cell_abc(2)
                                do m = -cell_abc(3), cell_abc(3)
                                        if ( atomtarg_name(1) == atomtarg_name(2) .and. i == j .and. k==0 .and. l==0 .and. m==0) cycle
                                        temp_real(:) = delta(:) + cell_size*(/k,l,m/)
                                        dist = sqrt(temp_real(1)**2 + temp_real(2)**2 + temp_real(3)**2)
                                        temp_int0 = nint ( dist / dr)
                                        if ( temp_int0 .gt. dr_num) cycle
                                        if ( temp_int0 < 1) then
                                                write(21,'(A25,F, I25)') 'err',dist,temp_int0
                                                stop
                                        end if
                                        rdf(temp_int0) = rdf(temp_int0) + 1.d0
                                enddo
                        enddo
                enddo
        enddo
enddo
enddo loop0
close(12)
!===============================================================[OUTPUT]
write (21, leng//"'[OUTPUT]')")
write (21, ' (A25, I25)') 'snap_num', snap_num
ri = (/( i * dr, i = 1, dr_num)/)
rdf = rdf / (snap_num * atomtarg_num(1))
rdf_int = (/( sum( rdf(1 : i)), i = 1, dr_num)/)
rdf = rdf * cell_size(1) * cell_size(2) * cell_size(3) / (atomtarg_num(2) * pi * dr * (4.d0 * ri**2 + dr**2 / 3.d0))
outfile = 'rdf_'//trim(atomtarg_name(1))//trim(atomtarg_name(2))//'_'//trim(tstart_char)//'to'//trim(tend_char)//'ps.out'
logfile = 'rdf_'//trim(atomtarg_name(1))//trim(atomtarg_name(2))//'_'//trim(tstart_char)//'to'//trim(tend_char)//'ps.log'
write (21, "(2A25)") 'outfile', trim(outfile)
open(unit = 13, file = outfile, status = 'replace')
write(13, "(A, A24, A25, A25)") '#','ri_angstrom','rdf','rdf_int'
do i = 1, dr_num
   write(13, "(F25.10, F25.10, F25.10)") ri(i)*bohr2angstrom, rdf(i), rdf_int(i)
enddo
close(13)

!===============================================================[FINALIZE]
deallocate (atomtype_name, atomtype_num)
deallocate (posi_1, posi_2)
deallocate (rdf, ri, rdf_int)
deallocate (logilist)
call system_clock (clock_end, clock_rate)
write (21, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(21)
call rename('mylog', logfile)

end program get_rdf
