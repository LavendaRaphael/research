import os
import math
import subprocess
import server
import shutil

def def_vasp_potgen():
    if os.path.isfile('POTCAR'):
        print('POTCAR has exist.')
        return 

    str_poscar = 'POSCAR'
    with open( str_poscar, 'r' ) as obj_poscar:
        for i in range(5):
            next(obj_poscar)
        list1d_atomsymbol = obj_poscar.readline().split()
    print(list1d_atomsymbol)

    dict_pot = def_dict_pot()
    list1d_pot = [ dict_pot[i][0] for i in list1d_atomsymbol ]
    print(list1d_pot)

    dir_vasppot = os.environ['vasp_pot']

    with open('POTCAR','wb') as obj_potcar:
        for str_pottype in list1d_pot:
            file_inpot = dir_vasppot + str_pottype +'/POTCAR'
            with open(file_inpot,'rb') as obj_inpot:
                shutil.copyfileobj(obj_inpot, obj_potcar)
    
def def_dict_pot():
    dict_pot = {}
    dict_pot['H' ]='H'
    dict_pot['Li']='Li_sv'
    dict_pot['B' ]='B'
    dict_pot['C' ]='C'
    dict_pot['N' ]='N'
    dict_pot['O' ]=['O',6]
    dict_pot['F' ]='F'
    dict_pot['Ne']='Ne'
    dict_pot['Na']='Na_pv'
    dict_pot['Mg']='Mg'
    dict_pot['Al']='Al'
    dict_pot['Si']='Si'
    dict_pot['P' ]='P '
    dict_pot['S' ]='S'
    dict_pot['Cl']='Cl'
    dict_pot['Ar']='Ar'
    dict_pot['K' ]='K_sv'
    dict_pot['Ca']='Ca_sv'
    dict_pot['Sc']='Sc_sv'
    dict_pot['Ti']='Ti_sv'
    dict_pot['V' ]='V_sv'
    dict_pot['Cr']='Cr_pv'
    dict_pot['Mn']='Mn_pv'
    dict_pot['Fe']='Fe'
    dict_pot['Co']='Co'
    dict_pot['Ni']='Ni'
    dict_pot['Cu']='Cu'
    dict_pot['Zn']='Zn'
    dict_pot['Ga']='Ga_d'
    dict_pot['Ge']='Ge_d'
    dict_pot['As']='As'
    dict_pot['Se']='Se'
    dict_pot['Br']='Br'
    dict_pot['Kr']='Kr'
    dict_pot['Rb']='Rb_sv'
    dict_pot['Sr']='Sr_sv'
    dict_pot['Y' ]='Y_sv'
    dict_pot['Zr']='Zr_sv'
    dict_pot['Nb']='Nb_sv'
    dict_pot['Mo']='Mo_sv'
    dict_pot['Tc']='Tc_pv'
    dict_pot['Ru']='Ru_pv'
    dict_pot['Rh']='Rh_pv'
    dict_pot['Pd']='Pd'
    dict_pot['Ag']='Ag'
    dict_pot['Cd']='Cd'
    dict_pot['In']='In_d'
    dict_pot['Sn']='Sn_d'
    dict_pot['Sb']='Sb'
    dict_pot['Te']='Te'
    dict_pot['I' ]='I'
    dict_pot['Xe']='Xe'
    dict_pot['Cs']='Cs_sv'
    dict_pot['Ba']='Ba_sv'
    dict_pot['La']='La'
    dict_pot['Ce']='Ce'
    dict_pot['Pr']='Pr_3'
    dict_pot['Nd']='Nd_3'
    dict_pot['Pm']='Pm_3'
    dict_pot['Sm']='Sm_3'
    dict_pot['Eu']='Eu_2'
    dict_pot['Gd']='Gd_3'
    dict_pot['Tb']='Tb_3'
    dict_pot['Dy']='Dy_3'
    dict_pot['Ho']='Ho_3'
    dict_pot['Er']='Er_3'
    dict_pot['Tm']='Tm_3'
    dict_pot['Yb']='Yb_2'
    dict_pot['Lu']='Lu_3'
    dict_pot['Hf']='Hf_pv'
    dict_pot['Ta']='Ta_pv'
    dict_pot['W' ]='W_sv'
    dict_pot['Re']='Re'
    dict_pot['Os']='Os'
    dict_pot['Ir']='Ir'
    dict_pot['Pt']=['Pt',10]
    dict_pot['Au']='Au'
    dict_pot['Hg']='Hg'
    dict_pot['Tl']='Tl_d'
    dict_pot['Pb']='Pb_d'
    dict_pot['Bi']='Bi_d'
    dict_pot['Po']='Po_d'
    dict_pot['At']='At'
    dict_pot['Rn']='Rn'
    dict_pot['Fr']='Fr_sv'
    dict_pot['Ra']='Ra_sv'
    dict_pot['Ac']='Ac'
    dict_pot['Th']='Th'
    dict_pot['Pa']='Pa'
    dict_pot['U' ]='U'
    dict_pot['Np']='Np'
    dict_pot['Pu']='Pu'
    dict_pot['Am']='Am'
    dict_pot['Cm']='Cm'
    return dict_pot

def def_serversub( 
         str_jobname,
         dict_input,
         str_excute,
         #int_ncore = None,
         #int_nodes = None,
         #str_jobqueue = None,
         #int_maxppn = None
         ):

    str_homedir = os.environ[ 'homedir' ]
    str_mycluster = os.environ[ 'mycluster' ]

    if ('str_jobqueue' in dict_input):
        str_jobqueue = dict_input[ 'str_jobqueue' ]
    else:
        str_jobqueue = server.str_jobqueue
    if ('int_maxppn' in dict_input):
        int_maxppn = dict_input[ 'int_maxppn' ]
    else:
        int_maxppn = server.dict_maxppn[ str_jobqueue ]
    if ('int_nodes' in dict_input):
        int_nodes = dict_input[ 'int_nodes' ]
        int_ppn = int_maxppn 
    if ('int_ncore' in dict_input):
        int_ncore = dict_input[ 'int_ncore' ]
        int_nodes = math.ceil( int_ncore/int_maxppn )
        int_ppn = math.ceil( int_ncore/int_nodes )

    str_jobname = 'tff.'+str_jobname
    str_nodefile = str_jobname+'.nodelist'
    str_subfile = str_jobname + '.sh'

    dict_subconfig = {}
    dict_jobsub = {}
    dict_subconfig[ 'qsub' ] = (
        '#PBS -l nodes='+str(int_nodes)+':ppn='+str(int_ppn)+'\n'+
        #'#PBS -l walltime=240:00:00\n'+
        '#PBS -N '+str_jobname+'\n'+
        '#PBS -q '+str_jobqueue+'\n'+
        '#PBS -j oe\n'+
        'cd $PBS_O_WORKDIR\n'+
        'cat $PBS_NODEFILE > '+str_nodefile+'\n'
        )
    dict_jobsub[ 'qsub' ] = 'qsub '+str_subfile

    str_timecount='echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s."'

    str_subhead = (
        'source '+str_homedir+'codes/common/environment.sh\n'+
        'set -euo pipefail\n'+
        'SECONDS=0\n'+
        'sort -u '+str_nodefile+' > '+str_nodefile+'.tmp && mv '+str_nodefile+'.tmp '+str_nodefile+'\n'
        )

    str_subvasp = (
        'if [ -f "INCAR" ]; then\n'+
        '   sed -i "/NCORE/c\  NCORE = '+ str(int(int_maxppn/2)) +'" INCAR\n'+
        '   '+
        'fi\n'
        )

    with open( str_subfile, 'w' ) as obj_subfile:
        obj_subfile.write( dict_subconfig[ str_mycluster ] ) 
        obj_subfile.write( str_subhead )
        if (('vasp' in str_excute) and (( '_std' in str_excute ) or ('_gam' in str_excute))) :
            obj_subfile.write( str_subvasp)
            def_vasp_potgen()
        obj_subfile.write( str_excute )
        obj_subfile.write( '\n' )
        obj_subfile.write( str_timecount )
    subprocess.run( dict_jobsub[ str_mycluster ].split()  )

