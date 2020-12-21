!==========================================================================================[README]
!---------------------------------------------------------------[VERSION]
!2020.12.21
!@tianff
!---------------------------------------------------------------[NOTES]
!Compute H-bond between Proton and water.
!---------------------------------------------------------------[Compile]
!mpiifort protonhbond_gro.f90 -o protonhbond_gro.x
!---------------------------------------------------------------[INFILE]
!datafile       'frame350.gro'  # Gromacs trjectory format
!time_range     100000.000 100000.00
!---------------------------------------------------------------[USE]
!mpirun ./protonhbond_gro.x protonhbond_gro.in
!---------------------------------------------------------------[DATAFILE]
!---------------------------------------------------------------[OUTFILE]
![my.err]
!protonhbond_gro.log
!protonhbond_gro.out
!==========================================================================================[main]
program main
use mpi
implicit none
!---------------------------------------------------------------[通用变量]
integer, parameter                  :: q = 8
real (q), parameter                 :: pi = acos(-1.0_q)
integer                             :: clock_start, clock_end, clock_rate
integer (q)                         :: i, j, k, l, m, ios, temp_int0, input_tot, temp_int(10)
real (q)                            :: temp_real0, temp_real (10)
character (len=100)                 :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile, outfile=".out", errfile='my.err',logfile=".log"
integer, parameter                  :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=100), allocatable    :: input_list(:)
character (len=100), parameter      :: prefix = "protonhbond_gro"
!---------------------------------------------------------------[输入变量]
real(q)                             :: time_range(2)    !时间范围
real(q), parameter                  :: dist_cut=0.35_q, theta_cut=pi/6.0_q !氢键判据
real(q), parameter                  :: dist_cutsquare=dist_cut**2, costheta_cut=cos(theta_cut)
character (len=100), parameter      :: cno_name(1:3)=(/'C','N','O'/)  ! 氢键可能原子
character (len=100), parameter      :: water_name='SOL' !水分子名
!---------------------------------------------------------------[内部变量]
integer (q)                         :: cno_tot, atom_tot, proton_tot    !CNO原子数，原子总数，proton原子数
integer (q), allocatable            :: cno_nh(:), cno_id(:) !CNO对应H个数，CNO对应原子ID
integer (q)                         :: water_form(0:3)  !水分子格式
real (q)                            :: cellpara(1:3)    !晶胞参数
real (q), allocatable               :: proton_pos(:,:), water_pos(:,:) !Proton原子坐标，水原子坐标
integer (q), allocatable            :: vecoh_cno(:) !记录水中O-H矢量是否已经归一化处理
integer (q)                         :: vecoh_water  !记录proton中O-H矢量是否已经归一化处理
real (q)                            :: time_onset   !frame时间
real (q)                            :: vec_d2a(3)   !donor-acceptor矢量
real (q)                            :: costheta_hda !costhe_H-Donor-Acceptor
integer (q)                         :: cno_idonset  !当前proton原子ID
character (len=100)                 :: mol_type, atom_type  !Datafile中读取的分子名，原子名
integer (q)                         :: snap_onset   !当前的frame序号
integer (q)                         :: nreadchange  !改变每行读取参数原子序数
!---------------------------------------------------------------[MPI变量]
character (len=100)                 :: outfile_rank !各进程的输出文件
integer                   :: ntasks, rank, ierr, stat (MPI_STATUS_SIZE)
!---------------------------------------------------------------[MPI初始化]
call MPI_INIT (ierr)
call MPI_COMM_SIZE (MPI_COMM_WORLD, ntasks, ierr)
call MPI_COMM_RANK (MPI_COMM_WORLD, rank, ierr)
!---------------------------------------------------------------[文件名生成]
write (temp_char0, '(I25)') rank
outfile_rank = trim(prefix)//trim(adjustl(temp_char0))//outfile
outfile = trim(prefix)//outfile
logfile = trim(prefix)//logfile
!---------------------------------------------------------------[进程0记录日志]
if (rank==0) then
open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!---------------------------------------------------------------[读取输入文件]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'datafile','time_range'/)
do i = 1, input_tot
do while (.true.)
    read (infile_unit, *, iostat = ios) temp_char0
    if (ios < 0) then
        write (*, *) "ERROR: see 'my.err' for details!"
        write (errfile_unit, *) "ERROR: parameter '"//trim(input_list(i))//"' not found in "//trim(infile)//"!"
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
    read (temp_char(2),*) datafile
case (2)
    read (infile_unit, *) temp_char0, temp_char(1:2)
    write (errfile_unit, "(3A25)") trim(temp_char0), (/(trim(temp_char(j)),j=1,2)/)
    read (temp_char(1:2),*) time_range(1:2)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!---------------------------------------------------------------[首次读取Datafile，获取参数信息]
open(datafile_unit, file = datafile, status = 'old')
write (errfile_unit, leng//"'[First-Read Datafile]: "//trim(datafile)//"')")
read (datafile_unit, *)
!-------------------------------[读取原子总数]
read (datafile_unit, *) atom_tot
write (errfile_unit, "(A25,I25)") 'atomtot', atom_tot
!-------------------------------[数proton中原子总数及CNO原子数目]
proton_tot = 0
cno_tot = 0
do while (.true.)
    read (datafile_unit, *) mol_type, atom_type
    if (mol_type(len_trim(mol_type)-2:) == water_name) exit
    proton_tot = proton_tot + 1
    if (any(cno_name == atom_type(1:1))) then
        cno_tot = cno_tot + 1
    endif
enddo
write (errfile_unit, '(A25,I25)') 'proton_tot', proton_tot
write (errfile_unit, "(A25, I25)") 'cno_tot',cno_tot
backspace(datafile_unit)
!-------------------------------[获取CNO原子标号，计算共价H数量]
do i=1, proton_tot
    backspace(datafile_unit)
enddo
allocate(cno_id(1:cno_tot))
allocate(cno_nh(1:cno_tot))
cno_nh = 0
j = 0
do i=1, proton_tot
    read (datafile_unit, *) mol_type, atom_type
    if (any(cno_name == atom_type(1:1))) then
        j = j + 1
        cno_id(j) = i
    elseif (atom_type(1:1)=='H') then
        cno_nh(j) = cno_nh(j) + 1
    endif
enddo
write (errfile_unit, "(A25, I25)") 'H_tot', sum(cno_nh)
!-------------------------------[获取水分子排列格式]
water_form = 0
read (datafile_unit, *) temp_char0, atom_type
backspace(datafile_unit)
do while (.true.)
    read (datafile_unit, *) mol_type, atom_type
    if (temp_char0 /= mol_type) exit
    water_form(0) = water_form(0) + 1
    if (atom_type(1:1) == 'O') then
        if (water_form(1) /=0) then
            write (*, *) "ERROR: see 'my.err' for details!"
            write (errfile_unit, *) "ERROR!!"
            stop
        endif
        water_form(1) = water_form(0)
    elseif (atom_type(1:1) == 'H') then
        if (water_form(2)==0) then
            water_form(2) = water_form(0)
        elseif (water_form(3)==0) then
            water_form(3) = water_form(0)
        else
            write (*, *) "ERROR: see 'my.err' for details!"
            write (errfile_unit, *) "ERROR!!"
            stop
        endif
    endif
enddo
backspace(datafile_unit)
write (errfile_unit, '(A25,4I25)') 'water_form(0:3)',water_form(0:3)
if (any(water_form==0)) then
    write (*, *) "ERROR: see 'my.err' for details!"
    write (errfile_unit, *) "ERROR!!"
    stop
endif
!-------------------------------[获取晶胞参数]
do i = proton_tot+water_form(0)+1, atom_tot
    read (datafile_unit, *)
enddo
read (datafile_unit, *) cellpara(1:3)
write (errfile_unit, '(A25, 3F25.10)') 'cellpara', cellpara(1:3)
!-------------------------------[获取改变每行读取参数原子序数]
rewind (datafile_unit)
read (datafile_unit, *)
read (datafile_unit, *)
temp_int(1:2) = 0
do i=1,atom_tot
    read(datafile_unit, '(a)') temp_char0
    call sub_splitline(temp_char0, temp_int(1))
    if (temp_int(1) < temp_int(2)) exit
    temp_int(2) = temp_int(1)
enddo
nreadchange = i
write (errfile_unit, '(A25, I25)') 'nreadchange', nreadchange

close (datafile_unit)
write (errfile_unit, leng//"'[OUTPUT]: "//trim(outfile)//"')")
endif
!---------------------------------------------------------------[由进程0分发获取到的参数信息]
call MPI_BCAST (datafile, 100, MPI_CHARACTER, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (time_range, 2, MPI_REAL8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (atom_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (proton_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (cno_tot, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
if (rank /= 0) then
    allocate(cno_id(1:cno_tot))
    allocate(cno_nh(1:cno_tot))
endif
call MPI_BCAST (cno_id, cno_tot, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (cno_nh, cno_tot, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (water_form, 4, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (cellpara, 3, MPI_REAL8, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (nreadchange, 1, MPI_INTEGER8, 0, MPI_COMM_WORLD, ierr)
allocate(proton_pos(1:proton_tot,3))
allocate(water_pos(1:water_form(0),3))
allocate(vecoh_cno(1:cno_tot))
!---------------------------------------------------------------[读取Datafile，计算氢键]
open(datafile_unit, file = datafile, status = 'old')
open (outfile_unit, file = outfile_rank, status = 'replace')

snap_onset = 0
do while (.true.)
!------------------------------[读取frame时间,判断是否计算]
read (datafile_unit, *, iostat=ios) temp_char(1:2), time_onset
if (ios<0) exit
read (datafile_unit, *)
snap_onset = snap_onset + 1
if (time_onset < time_range(1)) then
    do i=1, 1+atom_tot
        read (datafile_unit, *)
    enddo
    cycle
elseif (time_onset > time_range(2)) then
    exit
!------------------------------[根据 snap 序号分发计算任务]
elseif (mod (snap_onset, ntasks) /= rank) then 
    do i=1, 1+atom_tot
        read (datafile_unit, *)
    enddo
    cycle
endif
if (rank==0) then
    write (errfile_unit, '(F15.5)') time_onset
endif

!------------------------------[读取proton位置信息]
do i=1, proton_tot
    if (i<nreadchange) then
        temp_int0 = 3
    else
        temp_int0 = 2
    endif
    read (datafile_unit, *) temp_char(1:temp_int0), proton_pos(i, 1:3)
enddo
!------------------------------[读取水分子位置，计算氢键]
vecoh_cno = 0
do i=proton_tot+1, atom_tot, water_form(0)
!------------------------------[原子序号大于10000原子名与序号粘连]
    if (i<nreadchange) then
        temp_int0 = 3
    else
        temp_int0 = 2
    endif
    do j = 1, water_form(0)
        read (datafile_unit, *) temp_char(1:temp_int0), water_pos(j,1:3)
    enddo
!------------------------------[循环CNO序号，计算氢键]
    vecoh_water = 0
    loop1: do k=1, cno_tot
        cno_idonset = cno_id(k)
!------------------------------[边界条件]
        vec_d2a = proton_pos(cno_idonset,1:3) - water_pos(water_form(1),1:3)
        vec_d2a = vec_d2a - nint (vec_d2a / cellpara) * cellpara
!------------------------------[氢键距离判据]
        if (maxval (abs (vec_d2a)) >= dist_cut) cycle
        temp_real0 = dot_product(vec_d2a, vec_d2a)
        if (temp_real0 >= dist_cutsquare) cycle
!------------------------------[氢键夹角判据]
        vec_d2a = vec_d2a/ sqrt(temp_real0)
!--------------[水作donor]
        do j = 1, 2
!--------------[判断O-H矢量是否已经归一化]
            if (vecoh_water < j) then
                vecoh_water = j
                call sub_vecnorm(water_pos(water_form(1),:), water_pos(water_form(1+j),:), cellpara)
            endif
            costheta_hda = dot_product(vec_d2a, water_pos(water_form(1+j),:))
            if (costheta_hda <= costheta_cut) cycle
            write (outfile_unit, '(F15.5,A15,3I15)') time_onset, 'Acceptor', cno_idonset, i+j, i
            cycle loop1
        enddo
!--------------[proton作donor]
        vec_d2a = -vec_d2a
!--------------[判断C-H矢量是否已经归一化]
        do j = 1, cno_nh(k)
            if (vecoh_cno(k) < j) then
                vecoh_cno(k) = j
                call sub_vecnorm(proton_pos (cno_idonset,:), proton_pos (cno_idonset+j,:), cellpara)
            endif
            costheta_hda = dot_product(proton_pos (cno_idonset+j,1:3), vec_d2a)
            if (costheta_hda <= costheta_cut) cycle
            write (outfile_unit, '(F15.5,A15,3I15)') time_onset, 'Donor', cno_idonset, cno_idonset+j, i
            cycle loop1
        enddo
    enddo loop1
enddo
read (datafile_unit, *)
enddo
close(datafile_unit)
close(outfile_unit)
!---------------------------------------------------------------[FINALIZE]
deallocate( cno_nh, cno_id)
deallocate( proton_pos, water_pos)
deallocate( vecoh_cno)
!------------------------------[合并各进程产生的outfile]
call MPI_SEND (outfile_rank, 100, MPI_CHARACTER, 0, 1, MPI_COMM_WORLD, ierr)
if (rank==0) then
    open (outfile_unit, file = outfile, status = 'replace')
    write (outfile_unit, '(A1,A14,4A15)') '#',"time",'donor/acceptor','Proton','H','O'
    close (outfile_unit)
    call system('cat '//outfile_rank//'>>'//outfile)
    open(outfile_unit, file=outfile_rank, status='old')
    close(outfile_unit, status='delete')
    do i = 1, ntasks-1
        call MPI_RECV (outfile_rank, 100, MPI_CHARACTER, i, 1, MPI_COMM_WORLD, stat, ierr)
        call system('cat '//outfile_rank//'>>'//outfile)
        open(outfile_unit, file=outfile_rank, status='old')
        close(outfile_unit, status='delete')
    enddo
endif
!------------------------------[重命名log文件，添加时间]
if (rank==0) then
    call system_clock (clock_end, clock_rate)
    write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
    close(errfile_unit)
    call rename(errfile, logfile)
endif
call mpi_finalize (ierr)
end program main
!===================================================================================================[SUBROUTINE]
!---------------------------------------------------------------[处理边界条件，并归一化]
subroutine sub_vecnorm(vec_a,vec_b,cellpara)
implicit none
integer, parameter                  :: q = 8

real(q), intent(in)                 :: vec_a(3)
real(q), intent(in)                 :: cellpara(3)

real(q), intent(inout)              :: vec_b(3)

vec_b = vec_b - vec_a
vec_b = vec_b - nint (vec_b / cellpara) * cellpara
vec_b = vec_b/sqrt(dot_product(vec_b, vec_b))

end subroutine sub_vecnorm
!---------------------------------------------------------------[]
subroutine sub_splitline(line, n)
implicit none
integer, parameter                  :: q = 8

character(*), intent(in)            :: line

integer(q), intent(out)             :: n

integer(q)                          :: i, ios
character(100)                      :: buff(10000)

do n=1, 10000
    read(line,*,iostat=ios) buff(1:n)
    if (ios<0) exit
enddo
n=n-1

end subroutine sub_splitline

