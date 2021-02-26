"----------------------------------[Gnuplot]
au BufNewFile,BufRead *.gnu         setf gnuplot
"----------------------------------[记录打开位置]
if has("autocmd")                                                          
  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif                                                        
endif 
"----------------------------------
set nosmartindent "自动缩进
set noautoindent
set tw=0 "断行
colorscheme evening "主题
set hlsearch "搜索高亮
let b:fortran_fixed_source=0 "fortran语法断行
set fenc=utf-8 "编码
set fencs=utf-8,usc-bom,euc-jp,gb18030,gbk,gb2312,cp936
syntax on "语法
set expandtab "使用空格来替换Tab"
set tabstop=4 "设置所有的Tab和缩进为4个空格"
set laststatus=2 "显示状态栏（默认值为1，表示无法显示状态栏）"
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ %{strftime(\"%d/%m/%y\ -\ %H:%M\")} "状态栏配置"
set nocompatible "关闭vi兼容
set backspace=2 "删除
