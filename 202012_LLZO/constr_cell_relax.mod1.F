!>>notes
!============================================
!2021.01.27
!@tianff
!https://github.com/Chengcheng-Xiao/VASP_OPT_AXIS
!Vasp 6.2.0
!============================================
!<<notes

!-----------------------------------------------------------------------
!
! At present, VASP does not allow to relax the cellshape selectively
! i.e. for instance only cell relaxation in x direction.
! To be more precisse, this behaviour can not be achived via the INCAR
! or POSCAR file.
! However, it is possible to set selected components of the stress tensor
! to zero.
! The most conveninent position to do this is the routines 
! CONSTR_CELL_RELAX  (constraint cell relaxation).
! FCELL contains the forces on the basis vectors.
! These forces are used to modify the basis vectors according
! to the following equations:
!
!      A_OLD(1:3,1:3)=A(1:3,1:3) ! F90 style 
!      DO J=1,3
!      DO I=1,3
!      DO K=1,3
!        A(I,J)=A(I,J) + FCELL(I,K)*A_OLD(K,J)*STEP_SIZE
!      ENDDO
!      ENDDO
!      ENDDO
! where A holds the basis vectors (in cartesian coordinates).
!
!-----------------------------------------------------------------------

      SUBROUTINE CONSTR_CELL_RELAX(IU5,IU0,FCELL)
      USE prec
      IMPLICIT NONE
      REAL(q) FCELL(3,3)

      INTEGER IU5,IU0
      ! local variables
      INTEGER IDUM, N, IERR, I, J
      REAL(q) RDUM
      COMPLEX(q) CDUM
      LOGICAL LOPEN,LDUM
      CHARACTER (1) :: CHARAC
      LOGICAL IOPTCELL
      INTEGER :: ICELL(9)=1

!     just one simple example
!     relaxation in x directions only
!      SAVE=FCELL(1,1)
!      FCELL=0   ! F90 style: set the whole array to zero
!      FCELL(3,3)=SAVE

      LOPEN=.FALSE.
      OPEN(UNIT=IU5,FILE="INCAR",STATUS='OLD')

      IOPTCELL=.FALSE.
      CALL RDATAB(.FALSE.,"INCAR",IU5,'IOPTCELL','=','#',';','I', &
     &            ICELL,RDUM,CDUM,LDUM,CHARAC,N,9,IERR)
      IF (((IERR/=0).AND.(IERR/=3)).OR. &
     &                    ((IERR==0).AND.(N<1))) THEN
         IF (IU0>=0) &
            WRITE(IU0,*)'Error reading item ''IOPTCELL'' from file INCAR.'
         ICELL(6)=1
      ENDIF

      IF (ANY(ICELL .NE. (/1,1,1,1,1,1,1,1,1/) )) THEN
         IOPTCELL=.TRUE.
      IF (IU0>=0) WRITE(IU0,'(X,A,3I3,A,3I3,A,3I3)') 'Constraining cell:',ICELL(1:3),'  |',ICELL(4:6),'  |',ICELL(7:9)
      ENDIF
      CLOSE(IU5)

      IF (IOPTCELL) THEN
         DO J=1,3
         DO I=1,3
            IF (ICELL((I-1)*3+J)==0) FCELL(I,J)=0.0
         ENDDO
         ENDDO
      ENDIF

      RETURN
      END SUBROUTINE
