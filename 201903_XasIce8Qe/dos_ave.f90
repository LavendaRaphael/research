!==================use======================
!./dos_ave.x
!==================inputfile=================
!water_tt.dos
!==================water_tt.dos==============
!#  E (eV)   dos(E)     Int dos(E)
!-28.001  0.1393E-02  0.1393E-03
!...
!#  E (eV)   dos(E)     Int dos(E)
!-28.487  0.1393E-02  0.1393E-03
!...
!==================outfile==================
!water_ave.dos
!===========================================
program dos_ave
implicit none

INTEGER, PARAMETER       ::  DP = 8
real(DP), parameter      ::  pi = 3.14159265359

real(DP)                 ::  de
real(DP), allocatable    ::  dat(:,:), bin(:)
integer(DP)              ::  ios, dat_num=0, i=0, scheme=0, de_num(2), temp_int
character(len=40)        ::  head

open(1,file='water_tt.dos',status='old')
do while (.true.)
        read(1,*,iostat=ios) head
        if (ios<0) exit
        if (head(1:1) == '#') then
                scheme = scheme + 1
        else
                dat_num = dat_num + 1
        end if
end do
close(1)
write(*, '(A25,I25)') 'dat_num',dat_num
write(*, '(A25,I25)') 'scheme',scheme
allocate(dat(dat_num,2))

open(1,file='water_tt.dos',status='old')
do while (.true.)
        read(1,*,iostat=ios) head
        if (ios<0) exit
        if (head(1:1) == '#') cycle
        backspace(1)
        i = i + 1
        read(1,*) dat(i,:)
end do
close(1)

de = dat(2,1)-dat(1,1)
write(*,'(A25,F)') 'de',de
de_num(1) = nint(minval(dat(:,1))/de)
de_num(2) = nint(maxval(dat(:,1))/de)
allocate(bin(de_num(1):de_num(2)))

bin=0.d0
do i = 1, dat_num
        temp_int = nint ( dat(i,1) / de )
        bin(temp_int) = bin(temp_int) + dat(i,2)
end do
bin = bin/scheme
write(*,'(A25,F)') 'stats',sum(bin(:))*de

open(2,file='water_ave.dos',status='replace')
write(2,'(A25,A25,A25)') '#','energy','dos'
do i = de_num(1),de_num(2)
        write(2,'(F,F)') de*i, bin(i)
end do
close(2)

deallocate(dat,bin)
end program dos_ave
