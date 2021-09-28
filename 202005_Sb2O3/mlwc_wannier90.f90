!==========================================================================================
!===============================================================[VERSION]
!2020.07.06
!===============================================================[NOTES]
!Using the intel compiler version >= 2019
!===============================================================[USE]
!./mlwc_wannier90.x mlwc.in
!===============================================================[mlwc.in]
!winfile 'wannier90.win'
!xyzfile 'wannier90_centres.xyz'
!atom_type
!       Sb              5.d0            1.0d0   #atomtype_name, atomtype_charge, mlwc_rc
!       O               6.d0            1.0d0
!end atom_type
!bond_type
!       Sb              O               2.5d0    #atom_name1, atom_name2, bond_length
!end bond_type
!===============================================================[DATAFILE]
!wannier90.win
!wannier90_centres.xyz
!===============================================================[OUTFILE]
![my.err]       #if program exit unexpected
!mlwc.log
!mlwc_dipole.out
!mlwc_mol.xyz
!=========================================================================================
module my_subs

implicit none

contains

FUNCTION cross(a, b)
  real(8), DIMENSION(3) :: cross
  real(8), DIMENSION(3), INTENT(IN) :: a, b

  cross(1) = a(2) * b(3) - a(3) * b(2)
  cross(2) = a(3) * b(1) - a(1) * b(3)
  cross(3) = a(1) * b(2) - a(2) * b(1)
END FUNCTION cross

end module my_subs
!=========================================================================================
program main

use my_subs
implicit none

integer, parameter               :: DP = 8
real (DP), parameter             :: pi = 3.14159265359, bohr2angstrom=0.529177210903, eang2debye=4.799d0
integer                          :: clock_start, clock_end, clock_rate
integer (DP)                     :: i, j, k, l, m, ios, temp_int0, input_tot
real (DP)                        :: temp_real0, temp_real (10)
character (len=100)              :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile(2), outfile(2), errfile='my.err', logfile
integer, parameter               :: errfile_unit=11, infile_unit=12, datafile_unit(2)=(/13,14/), outfile_unit(2)=(/15,16/)
character (len=100), allocatable :: input_list(:)
integer (DP), allocatable        :: temp_intarray(:)

integer (DP)                    :: atomtype_tot, atom_tot, bond_tot, modify, mol_tot, mlwc_tot, mlwc_alone
integer (DP), allocatable       :: temp_intmax(:), bond_type(:,:), atom_neighbor(:,:), coor_num(:), atom_mol(:), atom_type (:), mol_head(:), mol_structure(:,:), atomtype_count(:), mlwc_mol(:,:), di_tot(:), mlwc_count(:), atom_mark(:)
character (len=100), allocatable :: bond_name(:,:), atomtype_name(:)
real (DP), allocatable          :: bond_rc(:), atomtype_charge(:), atom_posi(:,:), dipole(:,:), mlwc_rc(:), mlwc_posi(:,:), mlwc_atom(:,:), coor_posi(:,:,:)
real (DP)                       :: cell_size(3,3), delta(3), dist, di, reci_vectors(3,3)

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!===============================================================[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//infile//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 4
allocate(input_list(input_tot))
input_list = (/'winfile', 'xyzfile', 'atom_type', 'bond_type'/)
do i = 1, input_tot
do while (.true.)
        read (infile_unit, *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) "ERROR: parameter'"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
                write (*, *) "ERROR: check errfile 'my.err'"
                stop
        endif
        if (temp_char0 /= input_list(i)) cycle
        backspace(infile_unit)
        exit
enddo
select case (i)
case (1)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(1)
case (2)
        read (infile_unit, *) temp_char0, temp_char(2)
        write (errfile_unit, "(2A25)") trim(temp_char0), trim(temp_char(2))
        read (temp_char(2), *) datafile(2)
case (3)
        read (infile_unit, *) temp_char0
        write (errfile_unit, "(A25)") trim(temp_char0)
        temp_int0 = 0
        do while (.true.)
              read (infile_unit, *) temp_char0
              if (temp_char0 == 'end') then
                      do j = 1, temp_int0 + 1
                              backspace(infile_unit)
                      enddo
                      exit
              else
                      temp_int0 = temp_int0 + 1
              endif
        enddo
        allocate(atomtype_name(temp_int0),atomtype_charge(temp_int0),mlwc_rc(temp_int0))
        write (errfile_unit, '(4A25)') '','atomtype_name', 'atomtype_charge', 'mlwc_rc'
        do j = 1, temp_int0
                read (infile_unit, *) temp_char(1:3)
                write (errfile_unit, ' (A25, 3A25)') '', (/(trim(temp_char(k)), k = 1, 3)/)
                read (temp_char(1:3), *) atomtype_name(j),atomtype_charge(j),mlwc_rc(j)
        enddo
        atomtype_tot = temp_int0
case (4)
        read (infile_unit, *) temp_char0
        write (errfile_unit, "(A25)") trim(temp_char0)
        temp_int0 = 0
        do while (.true.)
              read (infile_unit, *) temp_char0
              if (temp_char0 == 'end') then
                      do j = 1, temp_int0 + 1
                              backspace(infile_unit)
                      enddo
                      exit
              else
                      temp_int0 = temp_int0 + 1
              endif
        enddo
        allocate(bond_type(temp_int0,2), bond_rc(temp_int0))
        do j = 1, temp_int0
                read (infile_unit, *) temp_char(1:3)
                write (errfile_unit, ' (A25, 3A25)') '',(/(trim(temp_char(k)), k = 1, 3)/)
                read (temp_char(3), *) bond_rc(j)
                bond_type(j,1) = findloc(atomtype_name, temp_char(1),dim=1)
                bond_type(j,2) = findloc(atomtype_name, temp_char(2),dim=1)
                if (bond_type(j,1) == 0 .or. bond_type(j,2) == 0) then
                       write (errfile_unit, *) "ERROR in 'infile': 'bond_type'"
                       write (*, *) "ERROR: check errfile 'my.err'"
                        stop
                endif
        enddo
        bond_tot = temp_int0
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!===============================================================[READ DATAFILE-1]
write (errfile_unit, leng//"'[READ DATAFILE-1]: "//datafile(1)//"')")
open(datafile_unit(1), file = datafile(1), status = 'old')
do while (.true.)
        read (datafile_unit(1), *, iostat = ios) temp_char0
        if (ios < 0) then
                write (errfile_unit, *) 'ERROR: datafile-1 is not formatted'
                write (*, *) "ERROR: check errfile 'my.err'"
                stop
        endif        
        select case (temp_char0)
        case ('begin')
                backspace(datafile_unit(1))
                read (datafile_unit(1), *) temp_char(1:2)
                select case (temp_char(2))
                case ('unit_cell_cart')
                        read (datafile_unit(1), *) cell_size(1,:)
                        read (datafile_unit(1), *) cell_size(2,:)
                        read (datafile_unit(1), *) cell_size(3,:)
                        write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(1,:)
                        write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(2,:)
                        write (errfile_unit, ' (A25, 3F25.10)') 'cell_size',cell_size(3,:)
                        reci_vectors(1,:) = cross(cell_size(2,:),cell_size(3,:))
                        reci_vectors(2,:) = cross(cell_size(3,:),cell_size(1,:))
                        reci_vectors(3,:) = cross(cell_size(1,:),cell_size(2,:))
                        temp_real0 = dot_product(cell_size(1,:),reci_vectors(1,:))
                        reci_vectors = reci_vectors / temp_real0
                        exit
                endselect
        endselect
enddo
close (datafile_unit(1))
!===============================================================[READ DATAFILE-2]
write (errfile_unit, leng//"'[READ DATAFILE-2]: "//datafile(2)//"')")
open (datafile_unit(2), file = datafile(2), status = 'old')
read (datafile_unit(2), *) atom_tot
read (datafile_unit(2), *)
mlwc_tot = 0
allocate (atomtype_count(atomtype_tot))
atomtype_count = 0
do while (.true.)
        read (datafile_unit(2), *, iostat = ios) temp_char0
        if (ios < 0) exit
        if (temp_char0 == 'X') then
                mlwc_tot = mlwc_tot + 1
        else
                temp_int0 = findloc(atomtype_name, temp_char0, dim=1)
                if (temp_int0 == 0) then
                       write (errfile_unit, *) "ERROR in [infile]: 'atom_type'"
                       write (*, *) "ERROR: check errfile 'my.err'"
                        stop
                endif
                atomtype_count(temp_int0) = atomtype_count(temp_int0) + 1
        endif
enddo
close (datafile_unit(2))
atom_tot = atom_tot - mlwc_tot
write (errfile_unit, ' (A25,I25)') 'mlwc_tot', mlwc_tot
do i = 1, atomtype_tot
        write (errfile_unit, ' (A25,I25)') trim(atomtype_name(i)), atomtype_count(i)
enddo
write (errfile_unit, ' (A25,I25)') 'atom_tot', atom_tot
allocate (mlwc_posi(mlwc_tot, 3))
allocate (atom_posi(atom_tot, 3), atom_type(atom_tot))
open (datafile_unit(2), file = datafile(2), status = 'old')
i = 0
j = 0
do while (.true.)
        read (datafile_unit(2), *, iostat = ios) temp_char0, temp_real(1:3)
        if (ios < 0) exit
        temp_real(1:3) = temp_real(1:3) - floor(dot_product(temp_real(1:3),reci_vectors(1,:)))*cell_size(1,:)
        temp_real(1:3) = temp_real(1:3) - floor(dot_product(temp_real(1:3),reci_vectors(2,:)))*cell_size(2,:)
        temp_real(1:3) = temp_real(1:3) - floor(dot_product(temp_real(1:3),reci_vectors(3,:)))*cell_size(3,:)
        if (temp_char0 == 'X') then
                i = i+1
                mlwc_posi(i,:) = temp_real(1:3)
        elseif (any(atomtype_name == temp_char0)) then
                j = j+1
                atom_type(j) = findloc(atomtype_name,temp_char0,dim=1)
                atom_posi(j,:) = temp_real(1:3)
        endif
enddo
close (datafile_unit(2))
!===============================================================[FIND_MOLECULE]
write (errfile_unit, leng//"'[FIND_MOLECULE]')")
allocate(atom_neighbor(atom_tot,atom_tot),coor_num(atom_tot),coor_posi(atom_tot,atom_tot,3))
coor_num = 0
do i = 1,atom_tot
do j = i+1,atom_tot
do k = 1,bond_tot
        if (not ((bond_type(k,1)==atom_type(i) .and. bond_type(k,2)==atom_type(j)) .or. (bond_type(k,1)==atom_type(j) .and. bond_type(k,2)==atom_type(i)))) cycle
        delta = atom_posi (j, :) - atom_posi (i, :)
        delta = delta - nint(dot_product(delta,reci_vectors(1,:)))*cell_size(1,:)
        delta = delta - nint(dot_product(delta,reci_vectors(2,:)))*cell_size(2,:)
        delta = delta - nint(dot_product(delta,reci_vectors(3,:)))*cell_size(3,:)
        if (maxval (abs (delta)) > bond_rc(k)) cycle
        dist = sqrt (delta (1) ** 2 + delta (2) ** 2 + delta (3) ** 2)
        if (dist > bond_rc(k)) cycle
        coor_num(i) = coor_num(i) + 1
        coor_posi(i, coor_num(i), :) = delta
        atom_neighbor(i,coor_num(i)) = j
enddo
enddo
enddo
allocate(atom_mol(atom_tot))
atom_mol = (/(i,i=1,atom_tot)/)
modify = 1
k=0
write (errfile_unit, '(2A25)') 'iterate','modify'
do while (modify>0)
        modify = 0
        do i = 1, atom_tot
                if ( coor_num(i)==0 ) cycle
                if (any((/(atom_mol(atom_neighbor(i,j)),j=1,coor_num(i))/) /= atom_mol(i))) then
                        modify = modify + 1
                        atom_mol(i) = minval((/(atom_mol(atom_neighbor(i,j)),j=1,coor_num(i))/))
                        do j = 1, coor_num(i)
                                atom_mol(atom_neighbor(i,j)) = atom_mol(i)
                        enddo
                endif
        enddo
        k = k + 1
        write (errfile_unit, '(2I25)') k, modify
enddo
mol_tot = 1
allocate(temp_intmax(atom_tot))
temp_intmax(1) = atom_mol(1)
do i = 2, atom_tot
        if (any(temp_intmax(1:mol_tot) == atom_mol(i))) cycle
        mol_tot = mol_tot + 1
        temp_intmax(mol_tot) = atom_mol(i)
enddo
write (errfile_unit, '(A25,I25)') 'mol_tot', mol_tot
allocate(mol_head(mol_tot))
mol_head = temp_intmax(1:mol_tot)
deallocate(temp_intmax)
allocate(mol_structure(mol_tot,-1:atomtype_tot))
mol_structure = 0
do i = 1, atom_tot
        atom_mol(i) = findloc(mol_head,atom_mol(i),dim=1)
        mol_structure(atom_mol(i),atom_type(i)) = mol_structure(atom_mol(i),atom_type(i)) + 1
enddo
!===============================================================[CONSTRUCT MOL]
allocate(atom_mark(atom_tot))
atom_mark = 0
do i = 1, mol_tot
        atom_mark (mol_head(i)) = 1
enddo
modify = 1
k=0
write (errfile_unit, '(2A25)') 'iterate','modify'
do while (modify>0)
        modify = 0
        do i = 1, atom_tot
                if ( coor_num(i)==0 ) cycle
                if (all((/(atom_mark(atom_neighbor(i,j)),j=1,coor_num(i))/) == atom_mark(i))) cycle
                modify = modify + 1
                if (atom_mark(i)==0) then
                        atom_mark(i)=1
                        temp_int0 = findloc((/(atom_mark(atom_neighbor(i,j)),j=1,coor_num(i))/),1,dim=1)
                        atom_posi(i,:) = atom_posi(atom_neighbor(i,temp_int0),:) - coor_posi(i,temp_int0,:)
                endif
                do j = 1, coor_num(i)
                        atom_posi(atom_neighbor(i,j),:) = atom_posi(i,:) + coor_posi(i,j,:)
                        atom_mark(atom_neighbor(i,j)) = 1 
                enddo
        enddo
        k = k + 1
        write (errfile_unit, '(2I25)') k, modify
enddo
!===============================================================[COMPUTE MLWC_ATOM]
write (errfile_unit, leng//"'[COMPUTE MLWC_ATOM]')")
!allocate(di_tot(atomtype_tot))
!di_tot = nint(mlwc_rc/di)
!allocate(mlwc_atom(atomtype_tot,maxval(di_tot)))
mlwc_atom = 0.d0
allocate (mlwc_mol(mlwc_tot,0:mol_tot))
mlwc_mol = 0
allocate(dipole(0:mol_tot,4))
dipole = 0.d0
do i=1,atom_tot
do j=1,mlwc_tot
        delta = atom_posi(i,:) - mlwc_posi(j,:)
        delta = delta - nint(dot_product(delta,reci_vectors(1,:)))*cell_size(1,:)
        delta = delta - nint(dot_product(delta,reci_vectors(2,:)))*cell_size(2,:)
        delta = delta - nint(dot_product(delta,reci_vectors(3,:)))*cell_size(3,:)
        if (maxval (abs (delta)) > mlwc_rc(atom_type(i))) cycle
        dist = sqrt (delta (1) ** 2 + delta (2) ** 2 + delta (3) ** 2)
        if (dist > mlwc_rc(atom_type(i))) cycle
!        temp_int0 = nint(dist/di)
        !if (temp_int0 > di_tot(atom_type(i))) cycle
!        mlwc_atom (atom_type(i), temp_int0) = mlwc_atom (atom_type(i), temp_int0) + 1.d0
        if (mlwc_mol(j,atom_mol(i)) /= 0) cycle
        mlwc_posi(j,:) = atom_posi(i,:) - delta
        dipole (atom_mol (i), 1:3) = dipole (atom_mol (i), 1:3) + mlwc_posi (j, :) * (-2.d0)
        mlwc_mol (j, atom_mol(i)) = 1
enddo
enddo
!allocate(mlwc_count(atomtype_tot))
!write (errfile_unit, '(A25,I25)') 'mlwc_count'
!do i = 1, atomtype_tot
!        mlwc_count(i) = nint(sum(mlwc_atom(i,:)))
!        mlwc_atom(i,:) = mlwc_atom(i,:)/mlwc_count(i)/di
!        outfile = 'mlwc_'//trim(atomtype_name(i))//'.out'
!        write (errfile_unit, '(2A25,I25,A25)') '',trim(atomtype_name(i))//'_X', mlwc_count(i), trim(outfile)
!        open(unit = outfile_unit, file = outfile, status = 'replace')
!        write(outfile_unit, "(A, A24, 4A25)") '#','ri','mlwc_'//trim(atomtype_name(i))
!        do j = 1, di_tot(i)
!                write(outfile_unit, "(2F25.10)") di*j, mlwc_atom(i,j)
!        enddo
!        close(outfile_unit)
!enddo
!===============================================================[MOLECULE STRUCTURE]
write (errfile_unit, leng//"'[MOLECULE STRUCTURE]')")
mlwc_mol(:,0) = (/(sum(mlwc_mol(i,:)),i=1,mlwc_tot)/)
mol_structure(:,0) = (/(sum(mlwc_mol(1:,i)),i=1,mol_tot)/)
mlwc_alone = count(mlwc_mol(:,0)==0)
do i = 1, mlwc_tot
        if (mlwc_mol(i,0) <=1 ) cycle
        do j=1 ,mol_tot
                if (mlwc_mol(i,j)==0) cycle
                mol_structure(j,-1) = mol_structure(j,-1) + 1
        enddo
enddo
write (errfile_unit, '(A25)') 'mol_structure'
write (temp_char0,*) atomtype_tot+2
write (errfile_unit, "(A25,"//temp_char0//"A25)") '',(/(trim(atomtype_name(i)),i=1,atomtype_tot)/),'X','X_overlap'
do i = 1, mol_tot
        write (errfile_unit, "(I25,"//temp_char0//"I25)") i,mol_structure(i,1:),mol_structure(i,0),mol_structure(i,-1)
!        write (errfile_unit, "(I25,3F25.10)") mol_head(i), atom_posi(i,:)
enddo
write (errfile_unit, "(A25,"//temp_char0//"I25)") 'SUM',(/(sum(mol_structure(:,i)),i=1,atomtype_tot)/),sum(mol_structure(:,0)),sum(mol_structure(:,-1))
write (errfile_unit, "(A25,2I25)") 'X_alone',mlwc_alone,findloc(mlwc_mol(:,0),0,dim=1)
!===============================================================[COMPUTE DIPOLE]
write (errfile_unit, leng//"'[COMPUTE DIPOLE]')")
do i = 1, atom_tot
        dipole(atom_mol(i),1:3) = dipole(atom_mol(i),1:3) + atom_posi(i,:)*atomtype_charge(atom_type(i))
enddo
dipole(0,1) = sum(dipole(1:mol_tot,1))/real(mol_tot)
dipole(0,2) = sum(dipole(1:mol_tot,2))/real(mol_tot)
dipole(0,3) = sum(dipole(1:mol_tot,3))/real(mol_tot)
do i = 0, mol_tot
        dipole(i,4) = sqrt(dipole(i,1)**2 + dipole(i,2)**2 + dipole(i,3)**2)
enddo
outfile(1) = 'mlwc_dipole.out'
write (errfile_unit, "(2A25)") 'dipolefile', trim(outfile(1))
open(unit = outfile_unit(1), file = outfile(1), status = 'replace')
allocate(temp_intarray(mol_tot))
temp_intarray = 0
do i = 1, mol_tot
do j = 1, mol_head(i)
        if (atom_type(j) /= atom_type(mol_head(i))) cycle
        temp_intarray(i) = temp_intarray(i) + 1
enddo
enddo
write(outfile_unit(1), "(A, A24, 6A25)") '#','mol','dipole_x','dipole_y','dipole_z','dipole_r(e*ang)','dipole_r(debye)','mol_head'
write(outfile_unit(1), "(A25, 5F25.10)") 'average',dipole(0,:),dipole(0,4)*eang2debye
!write(outfile_unit(1), "(A, A24, 2A25,A25)") '#','mol','dipole(e*ang)','dipole(debye)','mol_head'
!write(outfile_unit(1), "(A25, 2F25.10)") 'average',dipole(0,4),dipole(0,4)*eang2debye
do i = 1, mol_tot
        write(temp_char0, *) temp_intarray(i)
!        write(outfile_unit(1), "(I25, 2F25.10,A25)") i, dipole(i,4),dipole(i,4)*eang2debye, trim(atomtype_name(atom_type(mol_head(i))))//trim(adjustl(temp_char0))
        write(outfile_unit(1), "(I25, 5F25.10,A25)") i, dipole(i,:),dipole(i,4)*eang2debye, trim(atomtype_name(atom_type(mol_head(i))))//trim(adjustl(temp_char0))
enddo
deallocate(temp_intarray)
close(outfile_unit(1))
!===============================================================[OUTPUT MOLECUE]
open(unit = outfile_unit(2), file = "mlwc_mol.xyz", status = 'replace')
write(outfile_unit(2), "(I25)") atom_tot + mlwc_tot
write(outfile_unit(2), *) "mlwc mol structure"
do i = 1, mlwc_tot
        write(outfile_unit(2), "(A10, 3F20.10)") "X", mlwc_posi(i,:)
enddo
do i = 1, atom_tot
!        write(temp_char0, *) atom_mol(i)
        write(outfile_unit(2), "(A10, 3F20.10)") trim(atomtype_name(atom_type(i))), atom_posi(i,:)
enddo
close(outfile_unit(2))
!===============================================================[FINALIZE]
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
logfile='mlwc.log'
call rename(errfile, logfile)
end program main
