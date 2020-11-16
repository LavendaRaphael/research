!===================================================================
!  Module for global variables for xas.f90
!
!  by Wei Chen,   Jan 2007
!===================================================================
!
   MODULE xas_module2
!
!  global variables
!
   IMPLICIT NONE
   SAVE
   PUBLIC
!
!
!---------------------------------------------------------------------------

!--init_var
   DOUBLE PRECISION, PARAMETER :: &
      pi=3.14159265358979d0,                  &
      hartree_to_ev= 27.2113845d0
      
   DOUBLE COMPLEX, PARAMETER :: &
      eye=(0.d0,1.d0)                          ! imaginary i=(0,1)
   
   INTEGER :: &
      n_g,i_g,                                &! # of g-vectors
      n_st_v,n_st_c,                          &! # of states
      n_st,i_st                                
       
   DOUBLE PRECISION :: &
      v_cell,a0,celldm2,celldm3,              &! cell dimensions
      l_cell,rl_cell,rv_cell_sqt,rv_cell,     &!
      tpiba,                                  &! 2pi/a0
      o_x,o_y,o_z,                            &! coordinates of excited O
      k_x,k_y,k_z                              ! k-point calculated
!     eps_b,e_shift                            ! broaden sigma, e_shift (eV)
!---------------------------------------------------------------------------

!--init_atomic
   INTEGER, PARAMETER :: &
      n_r_m=2000,                             &!
      n_ast_m=10
     
   INTEGER :: &
      n_r, i_r,                               &! # of grid points
      n_ast,i_ast,                            &! # of atomic ref states (elm)=2*4=8
      i_avs,n_avs,                            &! # index and # of bet,(phi,psi), n_avs=4
      eee(n_ast_m),lll(n_ast_m),mmm(n_ast_m)   ! e, l, m of atomic ref states
   
   DOUBLE PRECISION :: &
      a_logmesh,b_logmesh,                    &! Grid parameters for oxygen
      dx,                                     &! step in log mesh = b_logmesh
      r(n_r_m), r2(n_r_m),                    &! radial grid r, r**2 
      psi(n_r_m,n_ast_m),phi(n_r_m,n_ast_m),  &! atomic all-e, pseudo wfc
      dff(n_r_m,n_ast_m),                     &! diff of above
      bet(n_r_m,n_ast_m),                     &! beta function
      psi_1s(n_r_m)                            ! 1s radial wfc
!---------------------------------------------------------------------------

!--init_psi_g
   INTEGER, PARAMETER :: &
      n_g_m=560000, n_st_m=1200                 ! n_g_m at least TWICE the size of # of g, for Gamma point
    
   DOUBLE PRECISION :: &
      gx(n_g_m),gy(n_g_m),gz(n_g_m),          &! g-vectors (1/Bohr)
      eps(n_st_m)                              ! energy (eV)
!     de_ev(n_st_m)                            ! e_shift + eps_au (ev)
   
!---------------------------------------------------------------------------

!--radial_int
   DOUBLE PRECISION :: &
      kg_x(n_g_m),kg_y(n_g_m),kg_z(n_g_m),    &! (k+G)_x, _y, _z
      l_kg(n_g_m),                            &! norm of k+G
      int_psi1s_j0(n_g_m),                    &! radial integration of psi_1s*j0
      int_psi1s_r_j1(n_g_m),                  &! radial integration of psi_1s*r*j1
      int_bet_jl(n_g_m,n_ast_m),              &! radial integration of bet*jl
      int_psi1s_r_dff(n_ast_m),               &! radial integration of psi_1s*r*dff
      int_psi1s_dff(n_ast_m)                   ! radial integration of psi_1s*dff
  
   DOUBLE COMPLEX :: &
      e_ikgR(n_g_m)                            ! exp(i(K+G)R)
      

!---------------------------------------------------------------------------

!--cal_TM
!   DOUBLE PRECISION :: &
   
   DOUBLE COMPLEX :: &
      tm1r_x(n_st_m),tm1r_y(n_st_m),tm1r_z(n_st_m), &! TM r part1, <psi_1s|r|psi_pseudo>
      tm2r_x(n_st_m),tm2r_y(n_st_m),tm2r_z(n_st_m), &! TM r part2, sum of 8 atomic ref states
      c_alpha(n_ast_m)                               ! c_alpha
      
   DOUBLE PRECISION :: tm2(n_st_m),tm22(n_st_m)
   DOUBLE PRECISION :: A1, A2, A3                    ! integrated values, see paw.tex

!---------------------------------------------------------------------------

!
!******************************************
   END MODULE xas_module2
!******************************************
