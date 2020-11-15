
      SUBROUTINE exx_es(nfi, c )
!===============================================================
! modified from exact_exchange.f90 written by Zhaofeng and Xifan.
! Lingzhu Kong
!===============================================================

      USE kinds,                   ONLY  : DP
      USE mp,                      ONLY  : mp_barrier 
      USE mp_global,               ONLY  : nproc_image, me_image, intra_image_comm
      USE parallel_include
      USE io_global,               ONLY  : stdout
      USE smooth_grid_dimensions,  ONLY  : nr1s, nr2s, nr3s, nr1sx, nr2sx, nr3sx,nnrsx
      USE grid_dimensions,         ONLY  : nr1, nr2, nr3, nr1x, nr2x, nr3x, nnrx
      USE cell_base,               ONLY  : a1, a2, a3, omega
      use cell_base,               only  : r_to_s, s_to_r, ainv, h
      USE electrons_base,          ONLY  : nbsp, nbspx, f, nspin, ispin
      USE gvecw,                   ONLY  : ngw
      USE wannier_module,          ONLY  : wfc
      USE cp_main_variables,       ONLY  : vpsig=>exx_potential, pairv, n_exx, lmax, clm, vwc, rhor
      USE cp_main_variables,       ONLY  : my_nbspx, odtothd_in_sp, thdtood_in_sp, thdtood, np_in_sp, np_in_sp2, np_in_sps
!, odtothd_in_sps
      USE constants,               ONLY  : fpi, pi
      USE printout_base,           ONLY  : printout_base_open, printout_base_unit, printout_base_close
      USE wannier_base,            ONLY  : neigh, dis_cutoff, vnbsp 
      USE control_flags,           ONLY  : lwfpbe0nscf, lwfcohsex, lwfHF
      USE fft_base,                ONLY  : dffts
      USE mp_wave,                  ONLY : redistwfr
      USE wavefunctions_module,     ONLY : cv0 

      IMPLICIT NONE
      COMPLEX(DP)   c(ngw, nbspx)
!, cv(ngw, vnbsp)

      INTEGER  :: istatus(MPI_STATUS_SIZE)

      INTEGER     ir, i, j,nfi, ierr, nnrtot,njj(nbsp),  nj_max, overlap3(neigh,nbsp)
      REAl(DP)    wc(3, nbsp), middle(3), alength(3)
      REAl(DP)    ha, hb, hc, sa1, hcub
      
      REAL(DP),    ALLOCATABLE ::   vpsil(:,:)
      REAL(DP),    ALLOCATABLE ::   rho_in_sp(:), rho_in_sps(:), v(:)
      REAL(DP),    ALLOCATABLE ::   psi(:,:), psi_tbs(:)
      REAL(DP),    ALLOCATABLE ::   psi_v(:,:), psi_pair(:,:), psi_pairtmp(:)
      INTEGER,     ALLOCATABLE ::   my_nbsp(:), my_vnbsp(:), my_nxyz(:)
      INTEGER,     ALLOCATABLE ::   index_my_nbsp (:, :), rk_of_vobtl (:), lindex_of_vobtl(:)

      INTEGER   iobtl, gindex_of_iobtl, irank, rk_of_obtl_trcv, rk_of_obtl_tbs
      INTEGER   obtl_tbs, lindex_obtl_tbs, obtl_trcv, lindex_obtl_trcv, me
      REAL(DP)  totalenergy, totalenergyg, tmp(3), tmp2(3)

!     INTEGER, allocatable  :: irecvreq(:,:)

      INTEGER   tran(3), trann(3), proc, tmp_iobtl

      REAL(DP) ::  alpha, epsilon0, epslon, gama, div, inv_epsilon0

      REAL(DP),     ALLOCATABLE :: rhor_global(:)

!=============================================================================================
! General variables used in this subroutine
      nnrtot = nr1s * nr2s * nr3s
      alength(1) = sqrt( a1(1)**2 + a1(2)**2 + a1(3)**2 )
      alength(2) = sqrt( a2(1)**2 + a2(2)**2 + a2(3)**2 )
      alength(3) = sqrt( a3(1)**2 + a3(2)**2 + a3(3)**2 )
      ha = alength(1) / nr1s  !nr1s in the parallel case
      hb = alength(2) / nr2s  !nr1s in the parallel case
      hc = alength(3) / nr3s  !nr1s in the parallel case
      hcub = omega / DBLE(nnrtot) !nnrtot in parallel
      sa1 = 1.0d0/omega

!      epsilon0 = 1.7d0 !tianff
      epsilon0 = 3.0d0 !tianff
      inv_epsilon0 = 1.d0/epsilon0
!      alpha = 2.3d0 !tianff
      alpha = 1.242d0 !tianff
    WRITE(stdout,*) '#tianff exx_es.f90: alpha =', alpha ! tianff

      allocate(rhor_global(nnrtot))

      call gather_rho(rhor, rhor_global)
!     write(12,'(10f10.4)')rhor_global

      WRITE(stdout,*) 'entering exx_es', n_exx, nfi
      if(n_exx == 0)then
         call exx_setup_nscf( nnrtot, lmax, clm, fpi, wc, vwc, nbsp, vnbsp ) 
      end if

!-------------------------------------------------------------------------

      if (n_exx /= 0) then
         wc(:, :) = wfc(:, :)
         do ir = 1, nbsp
            tmp = wc(:,ir)
            call r_to_s(tmp,  tmp2, ainv)
!           call pbcs(tmp2, tmp,1)
            do i = 1, 3
               tmp(i) = tmp2(i) - int(tmp2(i))
               if(tmp(i) < 0)then
                  tmp(i) = tmp(i) + 1
               endif
            enddo

            call s_to_r(tmp,  tmp2, h)
            wc(:,ir) = tmp2(:)
         end do
      endif

! initialize the output as zero
      vpsig(:, :) = 0.0d0
      totalenergy = 0.0d0

      ALLOCATE( my_nxyz ( nproc_image ) )
      ALLOCATE( my_nbsp ( nproc_image ) )
      ALLOCATE( my_vnbsp( nproc_image ) )

      my_nbsp(:) = nbsp / nproc_image

      IF( MOD(nbsp, nproc_image) /= 0)THEN
         DO i = 1, nproc_image
            IF( (i-1) < MOD(nbsp, nproc_image) ) my_nbsp(i) = my_nbsp(i)+1
         END DO
      ENDIF

      my_vnbsp(:) = vnbsp / nproc_image
      DO i = 1, nproc_image
         IF( (i-1) < MOD(vnbsp, nproc_image) )my_vnbsp(i)=my_vnbsp(i)+1
      END DO

      my_nxyz(:) = nr1sx*nr2sx*dffts%npp

!     WRITE(stdout,*) 'me_nbsp  = ',  my_nbsp
!     WRITE(stdout,*) 'me_vnbsp = ', my_vnbsp
!     WRITE(stdout,*) 'my_nxyz  = ',  my_nxyz

      ALLOCATE( index_my_nbsp (my_nbspx, nproc_image) )
      ALLOCATE( rk_of_vobtl ( vnbsp ) )
      ALLOCATE( lindex_of_vobtl( vnbsp ) )

      index_my_nbsp(:, :) = nbsp + 1
      do irank = 1, nproc_image
         do iobtl = 1, my_nbsp(irank)
            gindex_of_iobtl = iobtl
            do proc = 1, irank - 1, 1
               gindex_of_iobtl = gindex_of_iobtl + my_nbsp(proc)
            enddo
            if( gindex_of_iobtl > nbsp)exit
            index_my_nbsp(iobtl, irank) = gindex_of_iobtl
         enddo
      enddo
        
!     WRITE(stdout,*) 'index_my_nbsp = ', index_my_nbsp

      do iobtl = 1, vnbsp 
         rk_of_vobtl(iobtl) = 0
         tmp_iobtl = iobtl
         do proc = 1, nproc_image
            tmp_iobtl = tmp_iobtl - my_vnbsp(proc)
            if(tmp_iobtl <= 0)THEN
              rk_of_vobtl(iobtl) = proc - 1
              exit
            endif
         enddo
      enddo

!     WRITE(stdout,*) 'rk_of_vobtl = ', rk_of_vobtl

      do iobtl = 1, vnbsp
         lindex_of_vobtl(iobtl) = iobtl
         do proc = 1, nproc_image
            if(lindex_of_vobtl(iobtl) <= my_vnbsp(proc))exit
            lindex_of_vobtl(iobtl) = lindex_of_vobtl(iobtl) - my_vnbsp(proc)
         enddo
      enddo

!     WRITE(stdout,*) 'lindex_of_vobtl = ', lindex_of_vobtl

      n_exx = n_exx + 1
      me = me_image + 1
!=========================================================================

      allocate ( psi_v(nnrtot, my_vnbsp(me) ) )
      allocate ( psi(  nnrtot, my_nbsp(me ) ) )

      call start_clock('r_orbital')
      call exx_psi(cv0, psi_v, nnrtot, my_vnbsp, my_nxyz, vnbsp) 
      call exx_psi(c,   psi,   nnrtot, my_nbsp , my_nxyz,  nbsp) 
      call stop_clock('r_orbital')

      deallocate(cv0)

      allocate ( vpsil(nnrtot, my_nbsp(me) ) )
      allocate ( v(nnrtot) )
      allocate ( rho_in_sp(np_in_sp), rho_in_sps(np_in_sps) )
!                                
!=========================================================================
!                              PAIR POTENTIAL
!=========================================================================

      call exx_index_pair_nv(wc, overlap3, njj, nj_max)
      WRITE(stdout,*) 'nj_max =', nj_max, my_nbspx

      allocate( psi_tbs(np_in_sp+np_in_sp2) )
      allocate( psi_pairtmp(nnrtot))
!     allocate( irecvreq(nj_max,0:nproc_image-1) )
      allocate( psi_pair(np_in_sp+np_in_sp2, nj_max ) , stat=ierr )   ! largest memory allocation
      if(ierr /= 0)write(*,*)"allocation error for psi_pair"

      vpsil(:,:) = 0.d0
      do iobtl = 1, my_nbspx
 
         WRITE(stdout,*) 'iobtl =', iobtl
         psi_pair(:,:)=0.d0

         call mp_barrier( intra_image_comm )

         call start_clock('send_psi')
         do j = 1, nj_max
            do irank = 1, nproc_image

               gindex_of_iobtl = index_my_nbsp(iobtl, irank)
               if( gindex_of_iobtl > nbsp)exit

               rk_of_obtl_trcv = irank - 1
               obtl_tbs        = overlap3(j, gindex_of_iobtl)

               if(obtl_tbs .ne. 0)then

                  rk_of_obtl_tbs  = rk_of_vobtl(obtl_tbs)
                  lindex_obtl_tbs = lindex_of_vobtl(obtl_tbs)

                  CALL getmiddlewc(wc(1,gindex_of_iobtl),vwc(1,obtl_tbs), middle )
                  CALL getsftv( nr1s, nr2s, nr3s, ha, hb, hc, middle, tran)

                  if( (me_image .eq. rk_of_obtl_trcv) .and. (me_image .eq. rk_of_obtl_tbs ))then
                     CALL getf_insp(tran, np_in_sp+np_in_sp2, nnrtot, psi_pair(1,j), psi_v(1,lindex_obtl_tbs) )

                  elseif( me_image .eq. rk_of_obtl_tbs )then
                     CALL getf_insp(tran, np_in_sp+np_in_sp2, nnrtot, psi_tbs, psi_v(1,lindex_obtl_tbs) )

                     CALL MPI_SEND( psi_tbs, np_in_sp+np_in_sp2, MPI_DOUBLE_PRECISION, & 
 &                                  rk_of_obtl_trcv, j*irank, intra_image_comm,ierr )
                
                  elseif( me_image .eq. rk_of_obtl_trcv )then
                     CALL MPI_RECV( psi_pair(1,j),  np_in_sp+np_in_sp2, MPI_DOUBLE_PRECISION, &
 &                                  rk_of_obtl_tbs,  j*irank, intra_image_comm, istatus,ierr)
!                    CALL MPI_IRECV( psi_pair(1,j),np_in_sp+np_in_sp2, MPI_DOUBLE_PRECISION, &
!                                   rk_of_obtl_tbs,  j*irank, intra_image_comm, irecvreq(j,me_image),ierr)
                  endif
               endif
            enddo  !irank
         enddo  ! j

!        do j = 1, nj_max
!           do irank = 1, nproc_image
!              gindex_of_iobtl = index_my_nbsp(iobtl, irank)

!              if( gindex_of_iobtl > nbsp)exit
!              rk_of_obtl_trcv = irank - 1
!              obtl_tbs        = overlap3(j, gindex_of_iobtl)

!              if(obtl_tbs .ne. 0)then
!                 rk_of_obtl_tbs  = rk_of_vobtl(obtl_tbs)
!                 lindex_obtl_tbs = lindex_of_vobtl(obtl_tbs)

!                 if( (me_image .eq. rk_of_obtl_trcv) .and. (me_image .ne. rk_of_obtl_tbs) )then
!                    CALL MPI_WAIT(irecvreq(j,me_image), istatus, ierr)
!                 endif
!              endif
!           enddo
!        enddo

         call stop_clock('send_psi')
!=======================================================================

         gindex_of_iobtl = index_my_nbsp(iobtl, me) 
         WRITE(stdout,*) 'gindex_of_iobtl = ', gindex_of_iobtl

         call mp_barrier( intra_image_comm )

         if( gindex_of_iobtl <= nbsp)then

         call start_clock('getpairv')
         do j = 1, njj( gindex_of_iobtl )

            WRITE(stdout,*) 'overlap3(j,gindex_of_iobtl) = ', overlap3(j,gindex_of_iobtl)
            IF(overlap3(j,gindex_of_iobtl) /= 0)THEN

               call getmiddlewc(wc(1,gindex_of_iobtl),vwc(1,overlap3(j,gindex_of_iobtl)),middle )

               v(:) = 0.0d0
               call getsftv( nr1s, nr2s, nr3s, ha, hb, hc, middle, tran)
               call getsftv( nr1s, nr2s, nr3s, ha, hb, hc, vwc(1,overlap3(j,gindex_of_iobtl)), trann)

               call getrho(  nnrtot, psi(1, iobtl), psi_pair(1, j), rho_in_sp, tran,sa1)
               WRITE(stdout,*) 'before getvofrcohsex'
               call getvofrcohsex( nnrtot, hcub, n_exx, rho_in_sp, v, tran)

               WRITE(stdout,*) 'before calculating v_local'
!              call getvofr_local( rhor_global, rho_in_sp, v, nnrtot, &
!                   tran, trann, hcub, alpha, epsilon0, ha, hb, hc)
               call getrhos( nnrtot, psi(1, iobtl), psi_pair(1, j), rho_in_sps, tran,sa1)
               call getvofr_locals( rhor_global, rho_in_sps, v, nnrtot, & 
                   tran, trann, hcub, alpha, epsilon0, ha, hb, hc)
               call getf_incel(tran, np_in_sp+np_in_sp2, nnrtot, psi_pair(1,j), psi_pairtmp)

               do ir = 1, nnrtot
                  vpsil(ir,iobtl) = vpsil(ir,iobtl) - v(ir) * psi_pairtmp(ir)
               end do

            END IF
         END DO !for j
         endif
         WRITE(stdout,*)'done iobtl =', iobtl
         call stop_clock('getpairv')
      end do ! iobtl
 
      WRITE(stdout,*) 'done iobtl'

      deallocate(rhor_global)
      deallocate(rho_in_sp, rho_in_sps, v, psi, psi_tbs, psi_v, psi_pair, psi_pairtmp)
      deallocate(my_vnbsp, index_my_nbsp,rk_of_vobtl , lindex_of_vobtl )

      call start_clock('vl2vg')
      call redistwfr( vpsig, vpsil, my_nxyz, my_nbsp, intra_image_comm, -1 )
      call stop_clock('vl2vg')
      WRITE(stdout,*) 'leaving exx_es'
!==============================================================================
      deallocate(vpsil, my_nxyz, my_nbsp)
      
      return
   
      END SUBROUTINE exx_es

      SUBROUTINE getsftv(nr1s, nr2s, nr3s, ha, hb, hc, wc, tran)
      USE kinds,     ONLY  : DP
      use cell_base, ONLY  : r_to_s, ainv, a1, a2, a3
      IMPLICIT   none

      INTEGER  nr1s, nr2s, nr3s, tran(3)
      REAL(DP) wc(3), ha, hb, hc, wclat(3), alength(3)

      INTEGER  i, bcm(3), wcm(3)

      alength(1) = sqrt( a1(1)**2 + a1(2)**2 + a1(3)**2 )
      alength(2) = sqrt( a2(1)**2 + a2(2)**2 + a2(3)**2 )
      alength(3) = sqrt( a3(1)**2 + a3(2)**2 + a3(3)**2 )

      ! convert to lattice coordinates
      call r_to_s(wc, wclat, ainv)

      bcm(1) = INT( nr1s/2)
      wcm(1) = INT( wclat(1)*alength(1)/ha  ) + 1

      bcm(2) = INT( nr2s/2)
      wcm(2) = INT( wclat(2)*alength(2)/hb  ) + 1

      bcm(3) = INT(  nr3s/2 )
      wcm(3) = INT( wclat(3)*alength(3)/hc  ) + 1

      DO i = 1, 3
         tran(i) = bcm(i) - wcm(i)
      ENDDO

      RETURN
      END

!====================================================================================
      subroutine getmiddlewc(wc1, wc2, mid)
      USE kinds,      ONLY  : DP
      USE cell_base,  ONLY  : a1, a2, a3, r_to_s, s_to_r, h, ainv

      IMPLICIT none

      real(DP)  wc1(3), wc2(3), mid(3)
      real(DP)  diff(3), diffs(3), mids(3)

      integer i

      do i = 1, 3
         mid(i)  = wc1(i) + wc2(i)
         diff(i) = wc1(i) - wc2(i)
      enddo

      call r_to_s(diff, diffs, ainv)
      call r_to_s(mid , mids , ainv)

      do i = 1, 3
         mids (i) = 0.5d0* (mids(i) - ABS(ANINT(diffs(i))))
      enddo

      call s_to_r(mids, mid, h)

      return
      end

      subroutine gather_rho( rhor, rhor_global)
 
      use kinds,           ONLY: DP
      use parallel_include
      use grid_dimensions, only : nr1x, nr2x, nr3x, nnrx
      USE mp_global,       ONLY : nproc_image, intra_image_comm, me_image
      USE fft_base,        ONLY : dfftp
      USE mp,              ONLY : mp_barrier, mp_gather
      USE io_global,       ONLY : stdout
      !
      implicit none
      !
      real(kind=DP), INTENT(IN)  :: rhor( nnrx )
      real(kind=DP), INTENT(OUT) :: rhor_global( nr1x*nr2x*nr3x)

      !
      integer :: proc, ierr
      integer, allocatable:: displs(:), recvcount(:)
      !     
      ALLOCATE( displs( nproc_image ), recvcount( nproc_image ) )
      !
      do proc=1,nproc_image
         recvcount(proc) =  dfftp%nnp  * ( dfftp%npp(proc) )
         if (proc.eq.1) then
            displs(proc)=0
         else
            displs(proc)=displs(proc-1) + recvcount(proc-1)
         end if
      end do
      !
      call mp_barrier(intra_image_comm)
      call MPI_ALLGATHERV( rhor, recvcount(me_image+1), MPI_DOUBLE_PRECISION, &
      rhor_global,recvcount,displs,MPI_DOUBLE_PRECISION,intra_image_comm, ierr)
      IF (ierr/=0) WRITE(stdout,*) 'something wrong with MPI_gather in gather_rho'

      DEALLOCATE( displs, recvcount )
      return
      end subroutine gather_rho
