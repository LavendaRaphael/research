import sys
sys.path.append(r'/home/faye/codes/group/202103_XasPtO')
from from_ase_render import *
import os

list_paras=[]
list_paras.append([1,11,4,15, 'Pt.110.x12y2z4.5_O22_vac15/'])
list_paras.append([1,1.5,2,4, 'Pt.110.x2y3z4.5_O1_vac15/'  ])
list_paras.append([1,1.5,2,4,'Pt.110.x2y3z4.5_O2.13_vac15/'  ])
list_paras.append([1,2.5,2,4,'Pt.110.x2y4z4.5_O3.137_vac15/' ])
list_paras.append([1,0.5,2,4,'Pt.110.x2y3z4.5_O3.135_vac15/' ])
list_paras.append([1,1.5,2,4,'Pt.110.x2y3z4.5_O2.12_vac15/'  ])
list_paras.append([1,1.5,2,4,'Pt.110.x2y3z4.5_O2.14_vac15/'  ])
list_paras.append([1,2.5,2,4,'Pt.110.x2y4z4.5_O3.148_vac15/' ])
list_paras.append([1,0.5,2,4,'Pt.110.x2y4z4.5_O4.1458_vac15/'])
list_paras.append([1,1.5,2,4,'Pt.110.x2y3z4.5_O3.123_vac15/' ])
list_paras.append([1,2.5,2,4,'Pt.110.x2y4z4.5_O4.1237_vac15/'])
list_paras.append([1,1.5,2,4,'Pt.110.x2y3z4.5_O4.v56_vac15/' ])
list_paras.append([1,2.5,2,4,'Pt.110.x2y4z4.5_O6.v56_vac15/' ])
list_paras.append([1,0.5,2,4,'Pt.110.x2y3z4.5_O6_vac15/'   ])

ax = 7.934514/2.0
ay = 2.80527433
str_poscar = 'POSCAR'

for list_para in list_paras:

    str_dir = '/home/faye/group/202103_XasPtO/server/Pt.110_O_vac/'+list_para[4]+'vasp_sch/template/'
    os.chdir(str_dir)
    x1 = list_para[0]*ax
    y1 = list_para[1]*ay
    x2 = list_para[2]*ax + x1
    y2 = list_para[3]*ay + y1
    tup_bbox=(x1, y1, x2, y2)

    def_render( tup_bbox=tup_bbox, str_poscar=str_poscar)

