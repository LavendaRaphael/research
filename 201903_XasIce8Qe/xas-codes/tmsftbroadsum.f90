      program sum

      implicit none
      integer i, j, k, n , i1, i2, npts, lines
      parameter (npts = 3000)
      double precision e, norm, sum_inten, emin, emax, e_onset, inten_onset
      double precision intensity(npts), energy(npts), area, de
      double precision energy2(npts), intensity2(npts)

     open (9,file='tmsftbroadsum.dat',status='unknown',form='formatted')
      open (20,file='tmsftbroad_tt.dat', status='old',form='formatted')
      
!      print *, 'enter number of excitations to average'
!      read(*,*)n

      call findlines('tmsftbroad_tt.dat',lines)
      n=lines/npts
      print *,'lines =', lines, 'number of excitations =', n
      intensity2(:) = 0.d0

      do j = 1, n
         do i = 1, npts
            read(20,*) energy(i), intensity(i)
            intensity2(i) = intensity2(i) + intensity(i)
         enddo
      enddo

      do i = 1, npts
         intensity2(i) = intensity2(i)/n
         energy2(i) = energy(i)
         write(9,*) energy2(i),intensity2(i)
      enddo

      close(9)
      close(20)

      end

subroutine findlines(filename,lines)
implicit none

  real :: line
  integer :: i
  character(len=20),intent(in) :: filename
  integer,intent(out) :: lines
  i=0
  open(673,file=filename,status='old')
  do while (.true.)
    read(673,*,end=100) line
    i=i+1
  enddo
  100 continue
  lines=i
  close(673)

end subroutine
