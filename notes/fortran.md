# Fortran

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Fortran](#fortran)
  - [杂项](#杂项)
    - [数组内循环](#数组内循环)
    - [数组查找](#数组查找)
    - [点积](#点积)
    - [整行读取](#整行读取)
    - [I/O](#io)
    - [bug](#bug)
  - [读取行参数个数](#读取行参数个数)
  - [读取文件行数](#读取文件行数)
  - [mpi](#mpi)
  - [模板](#模板)
  - [SUBROUTINE](#subroutine)

<!-- /code_chunk_output -->

## 杂项

### 数组内循环

```fortran
(/(i,i=1,2)/)
```

### 数组查找

```fortran
findloc (ARRAY, VALUE, DIM )
```

### 点积

```fortran
dot_product (a,b)
```

### 整行读取

```fortran
read(datafile_unit, '(a)') temp_char0
temp_char0 = adjustl(temp_char0)
```

### I/O

*infile中的string最好加引号，以免被“/”隔断  
`datafile       '../water.pos'`

### bug

- 服务器本身的module很有问题，建议用source
- 莫名奇妙的bug一般都是编译器的问题

## 读取行参数个数

```fotran
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
```

## 读取文件行数

```fortran
subroutine sub_nlines(file_unit,nlines)
    implicit none
    integer, parameter                  :: q = 8
    
    integer, intent(in)                 :: file_unit
    
    integer(q), intent(out)             :: nlines
    
    integer(q)                          :: ios
    character(100)                      :: temp

    nlines = 0
    do while (.true.)
        read (file_unit, *, iostat = ios) temp
        if (ios < 0) exit
!        if (temp(1:1) == '#') cycle    ! 忽略注释行
        nlines = nlines + 1
    enddo
    rewind(file_unit)
    
end subroutine sub_nlines
```

## mpi

```fortan
use mpi
```

 MPI变量

```fortran
character (len=100)                 :: outfile_rank !各进程的输出文件
integer                             :: ntasks, rank, ierr, stat (MPI_STATUS_SIZE)
```

MPI初始化

```fortran
call MPI_INIT (ierr)
call MPI_COMM_SIZE (MPI_COMM_WORLD, ntasks, ierr)
call MPI_COMM_RANK (MPI_COMM_WORLD, rank, ierr)
```

进程0记录日志

```fortran
if (rank==0) then
    open (errfile_unit, file=errfile, status='replace')
    call system_clock (clock_start)
endif
```

由进程0分发获取到的参数信息

```fortran
call MPI_BCAST (X, 100, MPI_CHARACTER, 0, MPI_COMM_WORLD, ierr)
call MPI_BCAST (X, 1, MPI_REAL8, 0, MPI_COMM_WORLD, ierr)
call MPI_SEND (X, 100, MPI_CHARACTER, 0, 1, MPI_COMM_WORLD, ierr)
call MPI_RECV (X, 100, MPI_CHARACTER, i, 1, MPI_COMM_WORLD, stat, ierr)
```

根据 snap 序号分发计算任务

```fortran
if (mod (snap_onset, ntasks) /= rank) then
endif
```

合并各进程产生的outfile

```fortran
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
```

重命名log文件，添加时间

```fortan
if (rank==0) then
    call system_clock (clock_end, clock_rate)
    write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
    close(errfile_unit)
    call rename(errfile, logfile)
endif
call mpi_finalize (ierr)
```

## 模板

```fortran
!------------[VERSION]
!2020.12.21
!@tianff
!------------[NOTES]
!------------[Compile]
!mpiifort *.f90 -o *.x
!------------[INFILE]
!datafile 'datafile'
!atom_type
!    O   32
!    H   64
!end atom_type
!------------[USE]
!mpirun ./*.x *.in
!------------[DATAFILE]
!------------[OUTFILE]
![my.err]
!*.log
!*.out
!------------[main]
program main
implicit none
!----------------------------------------------------------------[CommonVariable]
integer, parameter                  :: q = 8
real (q), parameter                 :: pi = acos(-1.0_q), bohr2angstrom=0.529177210903d0, eang2debye=4.799d0
integer                             :: clock_start, clock_end, clock_rate
integer (q)                         :: i, j, k, l, m, ios, temp_int0, input_tot
real (q)                            :: temp_real0, temp_real (10)
character (len=500)                 :: temp_char0, temp_char (10), leng=" (65 ('='), ", infile, datafile, outfile=".out", errfile='my.err',logfile=".log"
integer, parameter                  :: errfile_unit=11, infile_unit=12, datafile_unit=13, outfile_unit=14
character (len=500), allocatable    :: input_list(:)
character (len=500), parameter      :: prefix = "prefix"
### InputVariable]
character (len=500),parameter       :: 
real(q), parameter                  ::
### InternalVariable] 
integer, parameter                  ::
integer (q)                         :: 
integer (q), allocatable            ::
character (len=500)                 ::
character (len=500), allocatable    ::
real (q), allocatable               :: 
real (q)                            ::
!------------[文件名生成]
write (temp_char0, '(I25)') rank
outfile_rank = trim(prefix)//trim(adjustl(temp_char0))//outfile
outfile = trim(prefix)//outfile
logfile = trim(prefix)//logfile

open (errfile_unit, file=errfile, status='replace')
call system_clock (clock_start)
!------------[READ INFILE]
call get_command_argument(1,infile)
write (errfile_unit, leng//"'[READ INFILE]: "//trim(infile)//"')")
open(infile_unit, file = infile, status = 'old')
input_tot = 2
allocate(input_list(input_tot))
input_list = (/'datafile','atom_type'/)
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
    read (infile_unit, *) temp_char0
    write (errfile_unit, "(A25)") trim(temp_char0)
    atomtype_tot = 0
    do while (.true.)
          read (infile_unit, *) temp_char0
          if (temp_char0 == 'end') then
              do j = 1, atomtype_tot+1
                  backspace(infile_unit)
              enddo
              exit
          else
              atomtype_tot = atomtype_tot + 1
          endif
    enddo
    allocate(atomtype_name(atomtype_tot),atomtype_num(atomtype_tot))
    do j = 1, atomtype_tot
        read (infile_unit, *) atomtype_name(j), atomtype_num(j)
        write (errfile_unit, "(2A25,I25)") '',trim(atomtype_name(j)),atomtype_num(j)
    enddo
    atom_tot = sum(atomtype_num)
endselect
rewind (infile_unit)
enddo
close (infile_unit)
!------------[READ DATAFILE]
!------------[COMPUTE]
write (errfile_unit, leng//"'[COMPUTE]')")
!------------[OUTPUT]
write (errfile_unit, leng//"'[OUTPUT]: "//trim(outfile)//"')")
open (outfile_unit, file = outfile, status = 'replace')
!------------[FINALIZE]
deallocate()
call system_clock (clock_end, clock_rate)
write (errfile_unit, ' (A25, F)') 'Elapsed time (s)', (clock_end-clock_start)/real(clock_rate)
close(errfile_unit)
call rename(errfile, logfile)
end program main
```

## SUBROUTINE

```fortran
function func_()
implicit none
integer, parameter                  :: q = 8

end function func_
```

```fortran
subroutine sub_()
implicit none
integer, parameter                  :: q = 8

real(q), intent(in)                 ::
integer(q), intent(in)              ::
character(*), intent(in)            :: 

real(q), intent(out)                :: 

end subroutine sub_
```