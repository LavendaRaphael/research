!=======================================================================
   program main
!=======================================================================
!
   USE xas_module2   
   IMPLICIT NONE

   INCLUDE  'mpif.h'

      INTEGER  status(MPI_STATUS_SIZE)
      INTEGER myrank, nprocs, ierr

      CALL MPI_INIT(ierr)
      CALL MPI_COMM_SIZE(MPI_COMM_WORLD,nprocs,ierr)
      CALL MPI_COMM_RANK(MPI_COMM_WORLD,myrank,ierr)

   print *, 'nprocs, myrank = ', nprocs, myrank

   call init_var
   call init_atomic
   call orthonormal_test
   call init_psi_g
   call radial_int 
   call cal_TM(myrank, nprocs)

   CALL MPI_FINALIZE(ierr)

   end program main 
!=======================================================================

!=======================================================================
   subroutine init_var
!=======================================================================
!
   USE xas_module2
   IMPLICIT NONE
   
   integer crap
   double precision tmp

   read(10,*)v_cell,a0,celldm2,celldm3
   read(10,*)n_g,n_st_v,n_st_c
   read(10,*)k_x,k_y,k_z           ! in unit 2pi/a0
   read(10,*)o_x,o_y,o_z           ! atomic unit, as well as r, QE bohr
  !o_x = o_x / 0.5291772d0   !angstrom to bohr convert  
  !o_y = o_y / 0.5291772d0
  !o_z = o_z / 0.5291772d0

   if (n_g>n_g_m) then
      write(20,*) 'error: n_g > n_g_m =', n_g_m
      STOP
   endif
  
   rv_cell_sqt = 1.d0/dsqrt(v_cell)
   tpiba = 2.d0*pi/a0
   k_x  = k_x*tpiba
   k_y  = k_y*tpiba
   k_z  = k_z*tpiba
   n_st = n_st_c

   write(20,*)'cell volume:                       ',v_cell
   write(20,*)'a0,b/a0,c/a0:                      ',a0,celldm2,celldm3
   write(20,*)'no. of g-vectors:                  ',n_g
   write(20,*)'# of valence states (discarded):   ',n_st_v
   write(20,*)'# of conduction states:            ',n_st_c
   write(20,*)'coordinates of excited Oxygen atom:',o_x,o_y,o_z
   write(20,*)'single k-point calculated:         ',k_x,k_y,k_z
   write(20,*)'   '
   write(20,*)'   '
   write(20,*)'   '   

!=======================================================================
   end subroutine init_var
!=======================================================================

!=======================================================================
   subroutine init_atomic
!=======================================================================
!
   USE xas_module2
   IMPLICIT NONE

   integer l_dm
   integer i_m
   double precision dum, r_dm

!=======================================================================
   read(88,*)a_logmesh,b_logmesh
   write(20,*)'Grid parameters for oxygen, a, b(=dx)'
   write(20,'(e12.5,x,e12.5)')a_logmesh,b_logmesh
   dx = b_logmesh
      
   read(88,*)n_avs,n_r
   write(20,*)'Number of beta fns. ',n_avs
   write(20,*)'Number of grid points ',n_r
   if (n_r>n_r_m) then
      write(20,*) 'error: n_r > n_r_m =', n_r_m
      STOP
   endif   

   do i_r = 1,n_r
      read(87,*)r(i_r),psi_1s(i_r)
      psi_1s(i_r) = psi_1s(i_r)/(r(i_r)+1.0E-25)              !  checked
      r2(i_r)=r(i_r)**2
   enddo
 
   n_ast = 0

   do i_avs = 1,n_avs
      write(20,*)'reading for state:',i_avs
      read(89,*)l_dm
      write(20,*)'l=',l_dm
      do i_r = 1,n_r
         read(89,*)dum,phi(i_r,i_avs),psi(i_r,i_avs)
         phi(i_r,i_avs) = phi(i_r,i_avs)/(r(i_r)+1.0E-25)     ! checked
         psi(i_r,i_avs) = psi(i_r,i_avs)/(r(i_r)+1.0E-25)     ! checked
         dff(i_r,i_avs) = psi(i_r,i_avs) - phi(i_r,i_avs)
      enddo
      do i_r = 1,n_r
         read(90,*)dum,bet(i_r,i_avs)
         bet(i_r,i_avs) = bet(i_r,i_avs)/(r(i_r)+1.0E-25)     ! checked
      enddo
      do i_m = -l_dm,l_dm
         n_ast = n_ast + 1
         lll(n_ast) = l_dm
         mmm(n_ast) = i_m
         eee(n_ast) = i_avs
         write(20,*) 'n_ast,eee(n_ast)=',n_ast,eee(n_ast)
         write(20,*) 'n_ast,lll(n_ast)=',n_ast,lll(n_ast)
         write(20,*) 'n_ast,mmm(n_ast)=',n_ast,mmm(n_ast)
      enddo
   enddo
   write(20,*)'   '
   write(20,*)'   '

   end subroutine init_atomic
!=======================================================================

!=======================================================================
   subroutine orthonormal_test
!=======================================================================
!
   USE xas_module2
   IMPLICIT NONE

   double precision :: sum_tmp,sum_tmp1, r_test(n_r_m)
   double precision :: int_0_inf_dr
   double precision :: f1_test(n_r_m),f2_test(n_r_m)
!=======================================================================
   write(20,*) '**********  orthonormal_test  **********'

   sum_tmp=0.0d0
   sum_tmp1=0.0d0
   do i_r = 1, n_r
      f1_test(i_r) = (r(i_r)**2)*psi_1s(i_r)**2            !  checked 
      sum_tmp=sum_tmp+f1_test(i_r)*dx*r(i_r)
      sum_tmp1=sum_tmp1+f1_test(i_r)*dx*(r(i_r)+a_logmesh)   ! the correct sum rule to use
   enddo
   write(20,*) 'sum     <psi_1s|psi_1s> = ', sum_tmp,sum_tmp1
!--simpson integral:  int_0_inf_dr(f,r,r2,dx,mesh_m,mesh,nst)
   write(20,*) 'simpson <psi_1s|psi_1s> = ', int_0_inf_dr(f1_test,r,dx,n_r_m,n_r,a_logmesh)
   write(20,*)'   '

!--test <bet|phi> = 1
   do i_avs = 1, n_avs
      sum_tmp=0.0d0
      sum_tmp1=0.0d0
      do i_r = 1, n_r
         f1_test(i_r) = (r(i_r)**2)*phi(i_r,i_avs)*bet(i_r,i_avs)       !  checked, bet is real, so are psi, phi, psi_1s
         sum_tmp=sum_tmp+f1_test(i_r)*dx*r(i_r)
         sum_tmp1=sum_tmp1+f1_test(i_r)*dx*(r(i_r)+a_logmesh)
      enddo
      write(20,*) 'sum     <bet|phi> = ', sum_tmp,sum_tmp1
      write(20,*) 'simpson <bet|phi> = ', int_0_inf_dr(f1_test,r,dx,n_r_m,n_r,a_logmesh)
   enddo
   write(20,*)'   '
   write(20,*)'   '

   end subroutine orthonormal_test
!=======================================================================


!=======================================================================
   subroutine init_psi_g
!
   USE xas_module2
   IMPLICIT NONE

   double precision :: eps_dm
   double complex   :: sum_orthonorm

!=======================================================================
   write(20,*) '**********  init_psi_g  **********'

!--read g-vectors
   OPEN(51,file='g.dat',status='old',form='formatted')
   OPEN(53,file='eigc.dat',status='old',form='formatted')

   do i_g = 1,n_g
      read(51,*)gx(i_g),gy(i_g),gz(i_g) 
      gx(i_g) = gx(i_g)*tpiba           ! change to atomic unit
      gy(i_g) = gy(i_g)*tpiba/celldm2   ! scale the orthorhombic cell, checked.
      gz(i_g) = gz(i_g)*tpiba/celldm3   ! ..
   enddo
  
!--gama point
   do i_g = 2,n_g
       gx(i_g+n_g-1) = -gx(i_g)
       gy(i_g+n_g-1) = -gy(i_g)
       gz(i_g+n_g-1) = -gz(i_g)
   enddo

   do i_st = 1,n_st_c
      read(53,*) eps(i_st)
   enddo

   n_g = 2*(n_g-1)+1

   write(20,*)'   '
   write(20,*)'   '
 
   close(51)
   close(53)
   end subroutine init_psi_g
!=======================================================================


!=======================================================================
   subroutine radial_int
!=======================================================================
!
   USE xas_module2
   IMPLICIT NONE

   integer          :: i_dm, l_dm
   double precision :: &
      kgr_dm,                              &! |k+G|r
      int_0_inf_dr, bessj,                 &! functions
      f_r_int(n_r_m),f_r_int1(n_r_m)        ! radial func to integrate

!=======================================================================
   write(20,*) '**********  radial_int  **********'
    
   do i_g = 1,n_g
!-----k+G
      kg_x(i_g)   = k_x + gx(i_g) 
      kg_y(i_g)   = k_y + gy(i_g)
      kg_z(i_g)   = k_z + gz(i_g)

!-----exp(i*(k+G)*R)
      e_ikgR(i_g) = exp( 1.0d0*eye*(kg_x(i_g)*o_x + kg_y(i_g)*o_y + kg_z(i_g)*o_z) )

!-----norm of k+G     
      l_kg(i_g) = dsqrt(kg_x(i_g)**2 + kg_y(i_g)**2 + kg_z(i_g)**2) 
      
!-----radial integration of psi_1s*j0(|k+G|r), A1 = psi_1s*r*j1(|k+G|r)       
      do i_r = 1,n_r
         kgr_dm        = l_kg(i_g) * r(i_r)
         f_r_int(i_r)  = (r(i_r)**2)*psi_1s(i_r)*bessj(kgr_dm,0)  ! 
         f_r_int1(i_r) = (r(i_r)**3)*psi_1s(i_r)*bessj(kgr_dm,1)  ! A1
      enddo
         int_psi1s_j0(i_g)   = int_0_inf_dr(f_r_int, r,dx,n_r_m,n_r,a_logmesh)  ! not used 
         int_psi1s_r_j1(i_g) = int_0_inf_dr(f_r_int1,r,dx,n_r_m,n_r,a_logmesh)
  
!-----radial integration of A2 = bet*j_l(|k+G|r)   
      do i_avs = 1,n_avs
         
         do i_dm = 1, n_ast
            if ( eee(i_dm)==i_avs ) l_dm = lll(i_dm) ! find l
         enddo
         
         if (l_dm.ne.0 .AND. l_dm.ne.1) then
            write(20,*) 'error prep_int: l_dm must be 0,1.'
            STOP    
         endif
 
         do i_r = 1,n_r
            kgr_dm        = l_kg(i_g) * r(i_r)
            f_r_int1(i_r) = (r(i_r)**2)*bet(i_r,i_avs)*bessj(kgr_dm,l_dm)
            ! l_dm = 0,0,1,1 for i_avs = 1,2,3,4    
         enddo
         int_bet_jl(i_g,i_avs) = int_0_inf_dr(f_r_int1,r,dx,n_r_m,n_r,a_logmesh)
      
      enddo
   enddo
   

!--integrate A3 = psi_1s*r*dff, psi_1s*dff
   do i_avs = 1,n_avs 
      do i_r = 1,n_r
         f_r_int(i_r)  = psi_1s(i_r)*(r(i_r)**3)*dff(i_r,i_avs)
         f_r_int1(i_r) = psi_1s(i_r)*(r(i_r)**2)*dff(i_r,i_avs)
      enddo
      int_psi1s_r_dff(i_avs) = int_0_inf_dr(f_r_int, r,dx,n_r_m,n_r,a_logmesh) 
      int_psi1s_dff(i_avs)   = int_0_inf_dr(f_r_int1,r,dx,n_r_m,n_r,a_logmesh) ! not used
      write(20,*)'i_avs,A3 = int_psi1s_r_dff, int_psi1s_dff:'
      write(20,*) i_avs,int_psi1s_r_dff(i_avs), int_psi1s_dff(i_avs)
   enddo

   write(20,*)'   '
   write(20,*)'   '
   write(20,*)'   '
 
!=======================================================================
   end subroutine radial_int
!=======================================================================

   
!=======================================================================
   subroutine cal_TM(myrank, nprocs)
!=======================================================================
!
   USE xas_module2
   IMPLICIT NONE

   INCLUDE  'mpif.h'

   integer  nprocs, myrank, ierr, info
!  double precision :: 
   double complex   ::  &                
      sum_tm1x,sum_tm1y,sum_tm1z,       &
      sum_c_alpha,y_lm_dm,              &
      tm_tot_x,tm_tot_y,tm_tot_z,       &
      fac, factor
   double complex   :: Y_lm             ! spherical harmonic function
   double precision :: delta
   double precision :: bessj

   integer nbnd, nv, npw, i, j, k, ista, iend
   DOUBLE PRECISION, allocatable ::  A(:, :)
   complex*16,  allocatable  :: psi_cp(:), psi_ks(:,:), psi_ks2(:,:)

   OPEN(54,file='diag_lambda.dat',status='old',form='unformatted')
   OPEN(50,file='cp_wf.dat',status='old',form='unformatted')
   OPEN(30,file='tm.dat',status='unknown',form='formatted')

!=======================================================================
   write(20,*) '**********  cal_TM  **********'

   tm2(:) = 0.d0

   read(11,*) nbnd, nv, npw
   allocate(A(nbnd,nbnd))

   do i = 1, nbnd
      read(54)(A(j,i),j=1,nbnd)
   enddo

   allocate (psi_cp(npw))
   allocate (psi_ks(npw,n_st))

   call para_range(1, n_st, nprocs, myrank, ista, iend)

   psi_ks(:,:) = (0.d0,0.d0)
   do j = 1, nbnd
      read(50)(psi_cp(k),k=1,npw)
      do i_st = ista, iend    
         do k = 1, npw
            psi_ks(k,i_st) = psi_ks(k,i_st) +psi_cp(k)*A(j,i_st+nv)
         enddo
      enddo
   enddo
   
   deallocate ( psi_cp )

   do i_st = ista, iend    ! main loop (states) 

!--orthonormal test for wfc in G space
!     write(20,*)'orthonormal test for wfc in G space (smooth part):'
!     do i_st = 1,n_st
!        sum_orthonorm = 0.0d0
!        do i_g = 1,n_g
!           sum_orthonorm = sum_orthonorm + conjg( psi_ks(i_g) )*psi_ks(i_g)
!        enddo
!        write(20,*) i_st, n_g, real(sum_orthonorm)
!     enddo
!     write(20,*)'   '
!     write(20,*)'   '

!-----TM r part1
      sum_tm1x = (0.0d0, 0.0d0)
      sum_tm1y = (0.0d0, 0.0d0) 
      sum_tm1z = (0.0d0, 0.0d0)
      do i_g = 2, npw                   !-- gama point

         A1 = int_psi1s_r_j1(i_g)

         sum_tm1x = sum_tm1x + psi_ks(i_g,i_st)*e_ikgR(i_g)* ( A1*eye*kg_x(i_g)/l_kg(i_g) )
         sum_tm1y = sum_tm1y + psi_ks(i_g,i_st)*e_ikgR(i_g)* ( A1*eye*kg_y(i_g)/l_kg(i_g) )   
         sum_tm1z = sum_tm1z + psi_ks(i_g,i_st)*e_ikgR(i_g)* ( A1*eye*kg_z(i_g)/l_kg(i_g) )
      
      enddo    
      
      do i_g = npw+1, n_g                   !-- gama point

         A1 = int_psi1s_r_j1(i_g)

         sum_tm1x = sum_tm1x + conjg(psi_ks(i_g-npw+1,i_st))*e_ikgR(i_g)* ( A1*eye*kg_x(i_g)/l_kg(i_g) )
         sum_tm1y = sum_tm1y + conjg(psi_ks(i_g-npw+1,i_st))*e_ikgR(i_g)* ( A1*eye*kg_y(i_g)/l_kg(i_g) )
         sum_tm1z = sum_tm1z + conjg(psi_ks(i_g-npw+1,i_st))*e_ikgR(i_g)* ( A1*eye*kg_z(i_g)/l_kg(i_g) )

      enddo

      factor = dsqrt(4.0d0*pi)*rv_cell_sqt
      
      tm1r_x(i_st) = sum_tm1x*factor 
      tm1r_y(i_st) = sum_tm1y*factor
      tm1r_z(i_st) = sum_tm1z*factor

!-----TM r part1 done


!-----TM r part2      
      
      tm2r_x(i_st) = (0.0d0, 0.0d0)
      tm2r_y(i_st) = (0.0d0, 0.0d0)
      tm2r_z(i_st) = (0.0d0, 0.0d0)

      do i_ast = 1, n_ast

!--------c_alpha
         sum_c_alpha = (0.0d0, 0.0d0)         
         do i_g = 2, npw               !-- gama point
            y_lm_dm = Y_lm( kg_x(i_g),kg_y(i_g),kg_z(i_g),lll(i_ast),mmm(i_ast) ) 
            A2 = int_bet_jl(i_g,eee(i_ast))
            sum_c_alpha = sum_c_alpha + psi_ks(i_g,i_st)*e_ikgR(i_g)*A2*y_lm_dm
         enddo

         do i_g = npw+1, n_g               !-- gama point
            y_lm_dm = Y_lm( kg_x(i_g),kg_y(i_g),kg_z(i_g),lll(i_ast),mmm(i_ast) )
            A2 = int_bet_jl(i_g,eee(i_ast))
            sum_c_alpha = sum_c_alpha + conjg(psi_ks(i_g-npw+1,i_st))*e_ikgR(i_g)*A2*y_lm_dm
         enddo

         c_alpha(i_ast) = sum_c_alpha*rv_cell_sqt*4.0d0*pi*(eye**lll(i_ast)) 
!--------c_alpha done

!--------sum different alpha
         
         A3 = int_psi1s_r_dff(eee(i_ast)) 
     
         tm2r_x(i_st) = tm2r_x(i_st) + c_alpha(i_ast)* &
                         (eye/dsqrt(6.0d0))*A3*( delta(lll(i_ast),1)* &
         delta(mmm(i_ast),-1) - delta(lll(i_ast),1)*delta(mmm(i_ast),1) )
   
         tm2r_y(i_st) = tm2r_y(i_st) + c_alpha(i_ast)* &
                         (1.0/dsqrt(6.0d0))*A3*( delta(lll(i_ast),1)*&
         delta(mmm(i_ast),-1) + delta(lll(i_ast),1)*delta(mmm(i_ast),1) )

         tm2r_z(i_st) = tm2r_z(i_st) + c_alpha(i_ast)* &
                         (eye/dsqrt(3.0d0))*A3*delta(lll(i_ast),1)*&
         delta(mmm(i_ast),0)

      enddo
!-----TM r part done

!--total TM = tm1r + tm2r
   
   tm_tot_x = tm1r_x(i_st)  +  tm2r_x(i_st)
   tm_tot_y = tm1r_y(i_st)  +  tm2r_y(i_st)
   tm_tot_z = tm1r_z(i_st)  +  tm2r_z(i_st)


!--|TM|**2, average over x,y,z
   tm2(i_st) = ( conjg(tm_tot_x)*tm_tot_x + &
                 conjg(tm_tot_y)*tm_tot_y + &
                 conjg(tm_tot_z)*tm_tot_z   ) /3.0d0 

!  write(20, '(5I,6f15.5)')i_st, tm2r_x(i_st), tm2r_y(i_st), tm2r_z(i_st)
   print *, i_st, tm2r_x(i_st), tm2r_y(i_st), tm2r_z(i_st)
   enddo            ! end main loop (states)

   CALL MPI_ALLREDUCE(tm2,tm22,n_st,MPI_REAL8,MPI_SUM,MPI_COMM_WORLD,info)

!--output final results: de v.s. |TM|**2
   if(myrank .eq. 0)then
      do i_st = 1, n_st
         write(30,*) eps(i_st), tm22(i_st)
      enddo
   endif

   deallocate(psi_ks, A )

   write(20,*)'   '
   write(20,*)'   '
   write(20,*)'   '
   write(20,*)'bessj(5.0,1)=',  bessj(5.0d0,1)
   write(20,*)'delta(1,-1)=',   delta(1,-1)
   write(20,*)'delta(1,1)=',    delta(1,1)
   write(20,*)'delta(0,0)=',    delta(0,0)
   write(20,*)'Y_lm(1,0,0,1,1)=', Y_lm(1.0d0,0.0d0,0.0d0,1,1)   
   write(20,*)'Y_lm(1,0,0,0,0)=', Y_lm(1.0d0,0.0d0,0.0d0,0,0)
   write(20,*)'Y_lm(0,0,1,1,0)=', Y_lm(0.0d0,0.0d0,1.0d0,1,0)

   close(30)
   close(50)
   close(54)

!=======================================================================
   end subroutine cal_TM
!=======================================================================



!=======================================================================
!  radial integral (Simpson)
!
!  Wei Chen, Jan 2007
!=======================================================================
   function int_0_inf_dr(f,r,dx,mesh_m,mesh,r0)
!---------------------------------------------------------------
!
!      integral of f from 0 to infinity
!      f is given on a logarithmic mesh. 
!      f(r) is assumed to be proportional to r**nst for small r
!
   implicit none
   integer :: mesh, i
   integer :: mesh_m   ! size of array
   double precision :: int_0_inf_dr, f(mesh_m), r(mesh_m), dx
   double precision :: fs(4), b(4), sum1, r0
!  integer :: nst
!  double precision :: r2(mesh_m)
   
!
!      simpson integration (logarithmic mesh: dr ==> r dx)
!
   sum1=0.0d0
   do i=1,mesh-2,2
      sum1 = sum1 + f(i)*r(i) + 4.0d0*f(i+1)*r(i+1) + f(i+2)*r(i+2)
!     sum1 = sum1 + f(i)*(r(i)+r0) + 4.0d0*f(i+1)*(r(i+1)+r0) + f(i+2)*(r(i+2)+r0)
   end do
!  int_0_inf_dr = int_0_inf_dr + sum1*dx/3.0d0
   int_0_inf_dr = sum1*dx/3.0d0
   return
   end function int_0_inf_dr
!---------------------------------------------------------------



!=======================================================================
!  delta function
!
!  Wei Chen, Mar 2009
!=======================================================================
   function delta(i,j)
   implicit none
   integer :: i,j
   double precision :: delta
   if (i == j) then
      delta = 1.0
   else
      delta = 0.0
   endif
  
   return 
   end function delta
!---------------------------------------------------------------



!=======================================================================
!  spherical harmonic functions
!
!  Wei Chen, Jan 2007  
!=======================================================================
   function Y_lm(x,y,z,l,m)

   USE xas_module2, ONLY:  pi, eye
   implicit none
   
   integer :: l, m    
   double precision :: x,y,z,norm
   double complex   :: Y_lm 

   norm = dsqrt( x**2 + y**2 + z**2 )
   
   if     (l == 0 .AND. m ==  0) then

      Y_lm = 1.0d0/dsqrt(4.0d0*pi)
   
   elseif (l == 1 .AND. m ==  1) then
  
      Y_lm = (dsqrt(3.0d0/2.0d0/pi))/2.0d0*(y-x*eye)/norm   
      
   elseif (l == 1 .AND. m == -1) then
   
      Y_lm = (dsqrt(3.0d0/2.0d0/pi))/2.0d0*(y+x*eye)/norm
   
   elseif (l == 1 .AND. m ==  0) then
         
      Y_lm = (dsqrt(3.0d0/4.0d0/pi))*z*eye/norm
     
   else 
      write(20,*) 'error Y_lm: l must be 0,1. m must be 0,1,-1.'
      STOP
   endif
   
   return
   end function Y_lm
!=======================================================================






!=======================================================================
!  spherical Bessel functions
!
!  by Wei Chen, Jan 2007
!=======================================================================
   function bessj(x,l)

   implicit none
   integer :: l 
   double precision :: bessj,x
   double precision, parameter :: eps=1.0e-8

   if      (l == 0)   then 
       
       if (x.lt.eps) then
          bessj = 1.0d0
       else
          bessj = dsin(x)/x
       endif

    elseif (l == 1)   then
   
       if (x.lt.eps) then
          bessj = x/3.0d0
       else
          bessj = (dsin(x)/x - dcos(x))/x
       endif
   
    else 

       write(20,*) 'error bessj: l must be 0,1.'
       STOP
   
   endif    
   
   return
   end function bessj
!=======================================================================

      SUBROUTINE para_range(n1, n2, nprocs, irank, ista, iend)
      INTEGER n1,n2,nprocs,ista,iend,iwork

      iwork = (n2 - n1) / nprocs + 1
      ista = MIN(irank * iwork + n1, n2 + 1)
      iend = MIN(ista + iwork - 1, n2)

      RETURN
      END

