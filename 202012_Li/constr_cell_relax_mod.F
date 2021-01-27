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

      SUBROUTINE CONSTR_CELL_RELAX(FCELL)
      USE prec
      REAL(q) FCELL(3,3)

!     just one simple example
!     relaxation in x directions only
!      SAVE=FCELL(1,1)
!      FCELL=0   ! F90 style: set the whole array to zero
!      FCELL(1,1)=SAVE
!     relaxation in z direction only
!      SAVE=FCELL(3,3)
!      FCELL=0   ! F90 style: set the whole array to zero
!      FCELL(3,3)=SAVE


!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[]
!-----------------------------[version]
! 2021.01.05 @tianff
!-----------------------------[notes]
! Only for orthogonal cell!
!-----------------------------[ref]
! https://riptutorial.com/fortran/example/3663/implicit-variable-types
!-----------------------------[OPTCELL]
! 1 0 0        # x y z
!-------------------------------------
    REAL(q) fcell_bak(3,3)
    LOGICAL FILFLG
    INTEGER ICELL(3)
    INTEGER I

    INQUIRE(FILE='OPTCELL',EXIST=FILFLG)
    IF (FILFLG) THEN
        OPEN(67,FILE='OPTCELL',STATUS='OLD')
        READ(67,*) ICELL
        CLOSE(67)
        fcell_bak = FCELL
        FCELL = 0.0d0
        DO I=1,3
            IF (ICELL(I)==1) FCELL(I,I)=fcell_bak(I,I)
        ENDDO
    ENDIF
!<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

      RETURN
      END SUBROUTINE

