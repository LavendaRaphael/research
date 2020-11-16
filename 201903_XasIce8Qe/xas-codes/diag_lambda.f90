!=======================================================================
   program main
   IMPLICIT NONE

   INTEGER      N, nv, npw

   DOUBLE PRECISION ,  ALLOCATABLE :: A(:, :), W(:) 

   DOUBLE PRECISION ::  dum_swap, dum_sum, hartree_to_ev, fac_lambda
   PARAMETER (hartree_to_ev = 27.2113845d0)
   
   INTEGER ::  i, j, k, l, nbnd, nelec

   OPEN(70,file='cp_lambda.dat',status='old',form='formatted')
   OPEN(40,file='eig.dat',status='unknown',form='formatted')
   OPEN(50,file='diag_lambda.dat',status='unknown',form='unformatted')

   read(11,*) N, nv, npw

   nbnd = N
   nelec = 2*nv
   fac_lambda = 1.0d0*nelec/nbnd

   ALLOCATE(A(N, N), W(N))

   do j = 1, nbnd
      read(70,*)(A(i,j),i=1,nbnd)         ! lambda
   enddo

   print *, A(10, 1), A(nbnd, 1)

   write(*,*) "fac_lambda = ", fac_lambda
   write(*,*) "nbnd=", nbnd, "nv=", nv

   A = A/fac_lambda
   
! check if lambda is symmetric 
   do i = 1, nbnd
      do j = i+1, nbnd
         if ( ABS(A(i,j) - A(j,i) ) .GT. 1.D-7 )   then  
            write(*,*)'WARNING: unsymmetric A', i, j, A(i,j), A(j,i)  
         endif
      enddo
   enddo
     
   call diaglambda( N, A, W)

! output eigenvalues in W
   write(40,*)'valence eigenvalues follows'
   do i = 1, nv
      write(40,'(f15.8)')  W(i)*hartree_to_ev
   enddo
   write(40,*)'empty eigenvalues follows'
   do i = nv+1, nbnd
      write(40,'(f15.8)')  W(i)*hartree_to_ev
   enddo
   close(40)

   do i = 1, nbnd
      write(50)(A(j,i),j=1,nbnd)
   enddo
 
   deallocate(A, W)
   close(50)
   close(70)

   end program main 
!=======================================================================


!=======================================================================
   subroutine diaglambda(N, A, W)

   IMPLICIT NONE

   INTEGER ::      N, LDA, LWORK, LIWORK, INFO, i, j
   DOUBLE PRECISION :: A(N, N), W(N)

   INTEGER, ALLOCATABLE ::   IWORK(:)  
   DOUBLE PRECISION, ALLOCATABLE ::  WORK(:)

   LDA = N
   LWORK  = 1 + 6*N + 2*N**2
   LIWORK = 3 + 5*N

   ALLOCATE ( IWORK( LIWORK ) )
   ALLOCATE ( WORK ( LWORK  ) )

   call DSYEVD( 'V', 'U', N, A, LDA, W, WORK, LWORK, IWORK, LIWORK, INFO )
   DEALLOCATE ( IWORK, WORK)

   return
   end
