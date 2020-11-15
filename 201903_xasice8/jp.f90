
program japanese
implicit none

  real(8) :: r
  integer :: x,y,i
  character(len=3) :: fifty(46,3),input,medium(3)
  call random_single

  fifty(1,:)=(/ '  a','あ','ア' /)
  fifty(2,:)=(/ '  i','い','イ' /)
  fifty(3,:)=(/ '  u','う','ウ' /)
  fifty(4,:)=(/ '  e','え','エ' /)
  fifty(5,:)=(/ '  o','お','オ' /)
  fifty(6,:)=(/ ' ka','か','カ' /)
  fifty(7,:)=(/ ' ki','き','キ' /)
  fifty(8,:)=(/ ' ku','く','ク' /)
  fifty(9,:)=(/ ' ke','け','ケ' /)
  fifty(10,:)=(/ ' ko','こ','コ' /)
  fifty(11,:)=(/ ' sa','さ','サ' /)
  fifty(12,:)=(/ ' si','し','シ' /)
  fifty(13,:)=(/ ' su','す','ス' /)
  fifty(14,:)=(/ ' se','せ','セ' /)
  fifty(15,:)=(/ ' so','そ','ソ' /)
  fifty(16,:)=(/ ' ta','た','タ' /)
  fifty(17,:)=(/ ' ti','ち','チ' /)
  fifty(18,:)=(/ ' tu','つ','ツ' /)
  fifty(19,:)=(/ ' te','て','テ' /)
  fifty(20,:)=(/ ' to','と','ト' /)
  fifty(21,:)=(/ ' na','な','ナ' /)
  fifty(22,:)=(/ ' ni','に','ニ' /)
  fifty(23,:)=(/ ' nu','ぬ','ヌ' /)
  fifty(24,:)=(/ ' ne','ね','ネ' /)
  fifty(25,:)=(/ ' no','の','ノ' /)
  fifty(26,:)=(/ ' ha','は','ハ' /)
  fifty(27,:)=(/ ' hi','ひ','ヒ' /)
  fifty(28,:)=(/ ' hu','ふ','フ' /)
  fifty(29,:)=(/ ' he','へ','ヘ' /)
  fifty(30,:)=(/ ' ho','ほ','ホ' /)
  fifty(31,:)=(/ ' ma','ま','マ' /)
  fifty(32,:)=(/ ' mi','み','ミ' /)
  fifty(33,:)=(/ ' mu','む','ム' /)
  fifty(34,:)=(/ ' me','め','メ' /)
  fifty(35,:)=(/ ' mo','も','モ' /)
  fifty(36,:)=(/ ' ya','や','ヤ' /)
  fifty(37,:)=(/ ' yu','ゆ','ユ' /)
  fifty(38,:)=(/ ' yo','よ','ヨ' /)
  fifty(39,:)=(/ ' ra','ら','ラ' /)
  fifty(40,:)=(/ ' ri','り','リ' /)
  fifty(41,:)=(/ ' ru','る','ル' /)
  fifty(42,:)=(/ ' re','れ','レ' /)
  fifty(43,:)=(/ ' ro','ろ','ロ' /)
  fifty(44,:)=(/ ' wa','わ','ワ' /)
  fifty(45,:)=(/ ' wo','を','ヲ' /)
  fifty(46,:)=(/ '  n','ん','ン' /)
  
  do while (.true.)
    do i=1,46
      call random_number(r)
      x=ceiling(r*(47-i))
      call random_number(r)
      y=ceiling(r*3)
      medium=fifty(i,:)
      fifty(i,:)=fifty((47-x),:)
      fifty((47-x),:)=medium
      print *,i,fifty(i,y)
      read(*,*)
      print *,fifty(i,:)
    enddo
  enddo

end program japanese
subroutine random_single
implicit none

  integer :: n,i,clock,Nin=0
  real :: x
  integer,allocatable :: seed(:)

  call SYSTEM_CLOCk(clock)
  call RANDOM_SEED(size=n)
  allocate(seed(n))
  do i=1,n
    seed(i)=clock+37*i
  end do
  call random_seed(PUT=seed)
  deallocate(seed)

end subroutine random_single
