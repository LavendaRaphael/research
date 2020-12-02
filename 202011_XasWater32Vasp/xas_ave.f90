!==========================================================================================
!===============================================================[VERSION]
!2020.12.02
!===============================================================[NOTES]
!===============================================================[USE]
!./xas_ave.x xas_ave.in
!===============================================================[xas_norm.in]
!datafile       "xas_tt.dat"
!npiece         3000
!===============================================================[DATAFILE]
!xas_tt.dat
!===============================================================[OUTFILE]
!xas_ave.dat
!xas_ave.log
![my.err]
!==========================================================================================
program main
implicit none

integer, parameter               :: q = 8
real (q), parameter              :: pi = 3.14159265359d0, bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer                          :: clock_start, clock_end, clock_rate
integer (q)                      :: i, j, k, l, m, ios, temp_int0, input_tot
real (q)                         :: temp_real0, temp_real (3)
character (len=100)              :: temp_char0, temp_char (2), leng=" (65 ('='), ", infile, datafile, outfile='xas_ave.dat', errfile='my.err', logfile='xas_ave.log'
integer, parameter               :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=100), allocatable :: input_list(:)

integer (q)                     :: npiece, natom
!integer (q), allocatable        ::
!character (len=100), allocatable ::
real (q), allocatable           :: energy(:,:), intensity(:,:), eminn(:), emaxn(:), deltaEn(:), xas(:,:)
real (q)                        :: emin0, emax0, deltaE0

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'datafile','npiece'/)
do i = 1, input_tot
do while (.true.)
        read (infile_unit, *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case (i)
case (1)
        read (infile_unit, *) temp_char(1:2)
        write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
        read (temp_char(2), *) datafile
case (2)
        read (infile_unit, *) temp_char(1:2)
        write (errfile_unit, "(2A25)") trim(temp_char(1)), trim(temp_char(2))
        read (temp_char(2), *) npiece
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE]
write (errfile_unit, leng//"'[READ DATAFILE]: "//trim(datafile)//"')")
open(datafile_unit, file = datafile, status = 'old')
temp_int0 = 0
do while (.true.)
        read (datafile_unit, *, iostat = ios)
        if (ios < 0) exit
        temp_int0 = temp_int0 + 1
enddo
write(errfile_unit, '(A25,I25)') 'nline',temp_int0
if (mod(temp_int0,npiece) /=0) then
    write (errfile_unit, *) "mod(nline,npiece) /= 0"
    stop
endif
natom = temp_int0/npiece
write(errfile_unit, '(A25,I25)') 'natom',natom
rewind (datafile_unit)
allocate( energy(natom,npiece), intensity(natom,npiece))
do i=1, natom
do j=1, npiece
        read (datafile_unit, *, iostat = ios) energy(i,j), intensity(i,j)
enddo
enddo
close(datafile_unit)
!===============================================================[ave]
allocate( deltaEn(natom), eminn(natom), emaxn(natom) )
do i=1, natom
    eminn(i) = minval(energy(i,:))
    emaxn(i) = maxval(energy(i,:))
    deltaEn(i) = (emaxn(i) -eminn(i))/(npiece-1)
enddo
emin0 = minval(eminn(:))
emax0 = maxval(emaxn(:))
deltaE0 = (emax0-emin0)/(npiece-1)
allocate( xas(npiece,2) )
xas(:,2) = 0.0_q
do j=1, npiece
    xas(j,1) = emin0 + (j-1)*deltaE0
    do i=1, natom
        temp_real0 = (xas(j,1) -eminn(i)) /deltaEn(i)+1.0_q
        temp_int0 = floor(temp_real0)
        temp_real0 = temp_real0 - temp_int0
        if (temp_int0<1) then
            xas(j,2) =xas(j,2) +intensity(i,1)
        elseif (temp_int0>=npiece) then
            xas(j,2) =xas(j,2) +intensity(i,npiece)
        else
            xas(j,2) =xas(j,2) +intensity(i,temp_int0)*(1.0_q-temp_real0) +intensity(i,temp_int0+1)*temp_real0
        endif
    enddo
enddo
xas(:,2) = xas(:,2)/natom
!===============================================================[OUTDATA]
write(errfile_unit, leng//"'[OUTDATA]: "//trim(outfile)//"')")
open(outfile_unit, file = outfile, status = 'replace')
do i = 1, npiece
        write(outfile_unit, '(2F25.10)') xas(i,1:2)
enddo
close(outfile_unit)
!===============================================================[FINALIZE
deallocate(energy, intensity, eminn, emaxn, deltaEn, xas)
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
