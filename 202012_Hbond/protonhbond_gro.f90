!==========================================================================================[README]
!===============================================================[VERSION]
!2020.12.19
!@tianff
!===============================================================[NOTES]
!Compute H-bond between Proton and water
!===============================================================[USE]
!./*.x *.in
!===============================================================[INFILE]
!datafile       'frame350.gro'  # Gromacs trjectory format
!time_range     100000.000 100000.00
!===============================================================[DATAFILE]
!===============================================================[OUTFILE]
![my.err]
!*.log
!*.out
!==========================================================================================[main]
program main
implicit none

integer, parameter                  :: q = 8
real (q), parameter                 :: pi = acos(-1.0_q)
integer                             :: clock_start, clock_end, clock_rate
integer (q)                         :: i, j, k, l, m, ios, temp_int0, input_tot, temp_int(10)
real (q)                            :: temp_real0, temp_real (10)
character (len=100)                 :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile, outfile="protonhbond_gro.out", errfile='my.err',logfile="protonhbond_gro.log"
integer, parameter                  :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=100), allocatable    :: input_list(:)

real(q)                             :: time_range(2)
real(q), parameter                  :: dist_cut=0.35_q, theta_cut=pi/6.0_q
real(q), parameter                  :: dist_cutsquare=dist_cut**2, costheta_cut=cos(theta_cut)
character (len=100), parameter      :: cno_name(1:3)=(/'C','N','O'/)
character (len=100), parameter      :: water_name='SOL'

integer (q)                         :: cno_tot, atom_tot, proton_tot
integer (q), allocatable            :: cno_nh(:), cno_id(:)
integer (q)                         :: water_form(0:3)
real (q)                            :: cellpara(1:3)
real (q), allocatable               :: proton_pos(:,:), water_pos(:,:)
integer (q), allocatable            :: vecoh_cno(:)
integer (q)                         :: vecoh_water
real (q)                            :: time_onset
real (q)                            :: vec_d2a(3)
real (q)                            :: costheta_hda
integer (q)                         :: cno_idonset
character (len=100)                 :: mol_type, atom_type

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'datafile','time_range'/)
do i = 1, input_tot
do while (.true.)
    read (infile_unit, *, iostat = ios) temp_char0
    if (ios < 0) then
        write (*, *) "ERROR: see 'my.err' for details!"
        write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
        stop
    endif
    if (temp_char0 /= input_list(i)) cycle
    backspace(infile_unit)
    exit
enddo
select case (i)
case (1)
    read (infile_unit, *) temp_char0, temp_char(2)
    write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
    read (temp_char(2),*) datafile
case (2)
    read (infile_unit, *) temp_char0, temp_char(1:2)
    write (errfile_unit, "(3A25)") trim(temp_char0), (/(trim(temp_char(j)),j=1,2)/)
    read (temp_char(1:2),*) time_range(1:2)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE]
open(datafile_unit, file = datafile, status = 'old')
write (errfile_unit, leng//"'[FirstRead Datafile]: "//trim(datafile)//"')")
read (datafile_unit, *)
read (datafile_unit, *) atom_tot
write (errfile_unit, "(A25,I25)") 'atomtot', atom_tot

proton_tot = 0
cno_tot = 0
do while (.true.)
    read (datafile_unit, *) mol_type, atom_type
    if (mol_type(len_trim(mol_type)-2:) == water_name) exit
    proton_tot = proton_tot + 1
    if (any(cno_name == atom_type(1:1))) then
        cno_tot = cno_tot + 1
    endif
enddo
write (errfile_unit, '(A25,I25)') 'proton_tot', proton_tot
write (errfile_unit, "(A25, I25)") 'cno_tot',cno_tot
backspace(datafile_unit)

do i=1, proton_tot
    backspace(datafile_unit)
enddo
allocate(cno_id(1:cno_tot))
allocate(cno_nh(1:cno_tot))
cno_nh = 0
j = 0
do i=1, proton_tot
    read (datafile_unit, *) mol_type, atom_type
    if (any(cno_name == atom_type(1:1))) then
        j = j + 1
        cno_id(j) = i
    elseif (atom_type(1:1)=='H') then
        cno_nh(j) = cno_nh(j) + 1
    endif
enddo
write (errfile_unit, "(A25, I25)") 'H_tot', sum(cno_nh)

water_form = 0
read (datafile_unit, *) temp_char0, atom_type
backspace(datafile_unit)
do while (.true.)
    read (datafile_unit, *) mol_type, atom_type
    if (temp_char0 /= mol_type) exit
    water_form(0) = water_form(0) + 1
    if (atom_type(1:1) == 'O') then
        if (water_form(1) /=0) then
            write (*, *) "ERROR: see 'my.err' for details!"
            write (errfile_unit, *) "ERROR!!"
            stop
        endif
        water_form(1) = water_form(0)
    elseif (atom_type(1:1) == 'H') then
        if (water_form(2)==0) then
            water_form(2) = water_form(0)
        elseif (water_form(3)==0) then
            water_form(3) = water_form(0)
        else
            write (*, *) "ERROR: see 'my.err' for details!"
            write (errfile_unit, *) "ERROR!!"
            stop
        endif
    endif
enddo
backspace(datafile_unit)
write (errfile_unit, '(A25,4I25)') 'water_form(0:3)',water_form(0:3)
if (any(water_form==0)) then
    write (*, *) "ERROR: see 'my.err' for details!"
    write (errfile_unit, *) "ERROR!!"
    stop
endif


do while (.true.)
    read (datafile_unit, *) mol_type, atom_type
    if (mol_type(len_trim(mol_type)-2:) /= water_name) exit
enddo
backspace(datafile_unit)
read (datafile_unit, *) cellpara(1:3)
write (errfile_unit, '(A25, 3F25.10)') 'cellpara', cellpara(1:3)

rewind (datafile_unit)
!===============================================================[READ DATAFILE]
allocate(proton_pos(1:proton_tot,3))
allocate(water_pos(1:water_form(0),3))
allocate(vecoh_cno(1:cno_tot))
!===============================================================[OUTPUT]
write (errfile_unit, leng//"'[OUTPUT]: "//trim(outfile)//"')")
open (outfile_unit, file = outfile, status = 'replace')
write (outfile_unit, '(A1,A24,4A25)') '#',"time",'donor/acceptor','Proton','H','O'

do while (.true.)
read (datafile_unit, *, iostat=ios) temp_char(1:2), time_onset
if (ios<0) exit
read (datafile_unit, *)
if (time_onset < time_range(1)) then
    do i=1, 1+atom_tot
        read (datafile_unit, *)
    enddo
    cycle
endif
if (time_onset > time_range(2)) then
    exit
endif
write (errfile_unit, '(F25.10)') time_onset

vecoh_cno = 0
do i=1, proton_tot
    read (datafile_unit, *) temp_char(1:3), proton_pos(i, 1:3)
enddo
do i=proton_tot+1, atom_tot, water_form(0)
    if (i<10000) then
        temp_int0 = 3
    else
        temp_int0 = 2
    endif
    do j = 1, water_form(0)
        read (datafile_unit, *) temp_char(1:temp_int0), water_pos(j,1:3)
    enddo
    vecoh_water = 0
    loop1: do k=1, cno_tot
        cno_idonset = cno_id(k)
        vec_d2a = proton_pos(cno_idonset,1:3) - water_pos(water_form(1),1:3)
        vec_d2a = vec_d2a - nint (vec_d2a / cellpara) * cellpara

        if (maxval (abs (vec_d2a)) >= dist_cut) cycle
        temp_real0 = dot_product(vec_d2a, vec_d2a)
        if (temp_real0 >= dist_cutsquare) cycle
        
        vec_d2a = vec_d2a/ sqrt(temp_real0)
        
        do j = 1, 2
            if (vecoh_water < j) then
                vecoh_water = j
                call sub_vecnorm(water_pos(water_form(1),:), water_pos(water_form(1+j),:), cellpara)
            endif
            costheta_hda = dot_product(vec_d2a, water_pos(water_form(1+j),:))
            if (costheta_hda <= costheta_cut) cycle
            write (outfile_unit, '(F25.10,A25,3I25)') time_onset, 'Acceptor', cno_idonset, i+j, i
            cycle loop1
        enddo
        vec_d2a = -vec_d2a
        do j = 1, cno_nh(k)
            if (vecoh_cno(k) < j) then
                vecoh_cno(k) = j
                call sub_vecnorm(proton_pos (cno_idonset,:), proton_pos (cno_idonset+j,:), cellpara)
            endif
            costheta_hda = dot_product(proton_pos (cno_idonset+j,1:3), vec_d2a)
            if (costheta_hda <= costheta_cut) cycle
            write (outfile_unit, '(F25.10,A25,3I25)') time_onset, 'Donor', cno_idonset, cno_idonset+j, i
            cycle loop1
        enddo
    enddo loop1
enddo
read (datafile_unit, *)
enddo
close(datafile_unit)
!===============================================================[FINALIZE]
deallocate( cno_nh, cno_id)
deallocate( proton_pos, water_pos)
deallocate( vecoh_cno)
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
!===================================================================================================[SUBROUTINE]
!===============================================================[]
subroutine sub_nlines(file_unit,nlines)
implicit none
integer, parameter                  :: q = 8

integer(q), intent(in)              :: file_unit

integer(q), intent(out)             :: nlines

integer(q)                          :: ios

nlines = 0
do while (.true.)
    read (file_unit, *, iostat = ios)
    if (ios < 0) exit
    nlines = nlines + 1
enddo
rewind(file_unit)

end subroutine sub_nlines
!==============================================================[]
subroutine sub_vecnorm(vec_a,vec_b,cellpara)
implicit none
integer, parameter                  :: q = 8

real(q), intent(in)                 :: vec_a(3)
real(q), intent(in)                 :: cellpara(3)

real(q), intent(inout)              :: vec_b(3)

vec_b = vec_b - vec_a
vec_b = vec_b - nint (vec_b / cellpara) * cellpara
vec_b = vec_b/sqrt(dot_product(vec_b, vec_b))

end subroutine sub_vecnorm

