
!===========================================================
!         shift the spectra before broadening
!===========================================================

      program shift
 
      implicit none
      integer i,j, neig 
      double precision etot1, e, xas, hatoev, detmp
 
      character   c
 
      OPEN(30,file='tm.dat',status='old',form='formatted')
      OPEN(60,file='tmsft.dat',status='unknown',form='formatted')
     
      neig = 272
      hatoev = 27.21140d0
      etot1  =-1108.22906
 
      read(13,*)neig,etot1
      read(777,*) e
      detmp = (e - etot1)*hatoev
 
      do j = 1, neig
         read(30,*)   e, xas
         write(60,*)  e + detmp, xas
      end do

      close(30)
      close(60)
   
      end
