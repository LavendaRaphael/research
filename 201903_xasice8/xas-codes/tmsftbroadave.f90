
      program ave

      implicit none
      integer i, j, k, n , i1, i2, npts, lines
      parameter (npts = 3000)
      double precision e, norm, sum_inten, emin, emax, e_onset, inten_onset
      double precision intensity(npts), energy(npts), area, de
      double precision energy2(npts), intensity2(npts)
        
        real(8) :: e_begin=532.d0, e_end=546.d0 !tianff add
!        real(8) :: e_align=535.0d0, norm_area=88.3d0 !water tianff add
!        real(8) :: e_align=535.57d0, norm_area=87.7428d0 !ice_VIII tianff add
        real(8) :: e_align=535.57d0, norm_area=87.7428d0 !ice_Ih tianff add

      open (10,file='tmsftbroadave.dat',status='unknown',form='formatted')
      open (20,file='tmsftbroad_tt.dat', status='old',form='formatted')
      
!      print *, 'enter number of excitations to average'
!      read(*,*)n
      call findlines('tmsftbroad_tt.dat',lines)
      n=lines/npts
      print *, 'lines =', lines
      print *, 'number of excitations =', n
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
      enddo

      ! find the first local maximum, which will be the xas onset ~ 535eV
      e_onset     = 0.0d0
      inten_onset = 0.0d0
      do i = 1, npts
        if ( intensity2(i) >= inten_onset ) then
           inten_onset = intensity2(i)
           e_onset     = energy2(i)
        else
           write(*,*) "onset is found at ", e_onset
           write(*,*) "eV and intensity is ",inten_onset
           GOTO 10
        end if 
      end do
  10 CONTINUE

!     shift the averaged spectra to the onset and normalize the area betwee (530:550) to be 100
        i1=1 !tianff add
        i2=1 !tianff add
        do i = 1, npts
!         energy2(i) = energy2(i) + 535.0d0 - e_onset !tianff comment
         energy2(i) = energy2(i) + e_align - e_onset !tianff add
!         if( abs(energy2(i) - 532) .lt. 1E-3)i1 = i !tianff comment
!         if( abs(energy2(i) - 546) .lt. 1E-3)i2 = i !tianff comment
        if (energy2(i) <= e_begin) i1=i !tianff add
        if (energy2(i) <= e_end) i2=i !tianff add
      end do
      
      print *, energy2(i1), energy2(i2)

      area = 0.d0
      do i = i1, i2
         area = area + intensity2(i)
      enddo
      area = area * (energy2(2)-energy2(1))
!      norm = 88.3/area !tianff comment
      norm = norm_area/area !tianff add

!      do i = 1, npts !tianff comment
        do i = i1, i2 !tianff add
!         if((energy2(i) .ge. 532) .and. (energy2(i) .le. 546)) then !tianff comment
           write(10,*) energy2(i),intensity2(i)*norm
!         end if !tianff comment
      enddo

      close(10)
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
