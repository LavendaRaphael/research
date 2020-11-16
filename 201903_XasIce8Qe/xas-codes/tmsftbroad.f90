   program broad

   implicit none

   double precision alpha,ra2,eps(5500),tm2(5500)
   double precision emin,emax,de,spec_sum,exx,fact
   double precision , parameter :: pi = 3.1415926535897932385d0
   integer i_pts, i_st, n_st
   character c

   OPEN(30,file='tmsft.dat',status='old',form='formatted')
   OPEN(60,file='tmsftbroad.dat',status='unknown',form='formatted')

   alpha = 0.4d0
   n_st  = 272

   read(12,*)alpha, n_st

   emin = -10.0d0
   emax =  30.d0

   ra2   = 0.5d0/alpha/alpha
   fact  = 1.0d0/sqrt(2.0d0*pi)/alpha

   do i_st = 1,n_st
      read(30,*) eps(i_st), tm2(i_st)
   enddo

   de   =  (emax-emin)/3000

   do i_pts = 1,3000

      exx = emin + de*i_pts
      spec_sum = 0.d0
      do i_st = 1,n_st
         spec_sum = spec_sum + dexp(-1.0d0*ra2*(exx-eps(i_st))**2)*tm2(i_st)
         ! print *, i_st, exx, 'dexp', dexp(-1.0d0*ra2*(exx-eps(i_st))**2)*tm2(i_st), 'spec_sum', spec_sum, spec_sum*fact 
         ! print *, 'count', i_st, spec_sum 
      enddo
       
      write(60,*)exx,spec_sum*fact

   enddo

   close(30)
   close(60)
   end program broad
