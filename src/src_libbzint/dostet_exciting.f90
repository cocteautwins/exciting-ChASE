
real(8) function dostet_exciting(nbd,nik,eband,ntet,tetc,wtet,vt,e)
    use order
    implicit none     
    ! input parameters
    integer(4), intent(in) :: nbd            ! Maximum number of bands
    integer(4), intent(in) :: nik            ! Number of irreducible k-points
    real(8),    intent(in) :: eband(nbd,nik) ! Band energies
    integer(4), intent(in) :: ntet           ! Number of tetrahedra
    integer(4), intent(in) :: tetc(4,*)      ! id. numbers of the corners  of the tetrahedra
    integer(4), intent(in) :: wtet(*)        ! weight of each tetrahedron
    real(8),    intent(in) :: vt             ! the volume of the tetrahedra
    real(8),    intent(in) :: e              ! energy
    ! local variables
    integer(4) :: itet,i,ib,isp
    real(8)    :: dostet, ee(4)
    real(8), external :: dos1t

    dostet = 0.d0
    do itet = 1, ntet
      do ib = 1, nbd 
        do i = 1, 4
          ee(i) = eband(ib,tetc(i,itet))
        end do
        call sort(4,ee)
        dostet = dostet+wtet(itet)*dos1t(ee,e,vt)
      enddo
    enddo
    dostet_exciting = dostet
    return
end function
