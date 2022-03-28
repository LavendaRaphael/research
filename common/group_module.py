import os
import math
import subprocess
import shutil
import server

class class_subparas():
    def __init__(self):
        self._str_dirformat = 'sub_%05d'

    @property
    def str_workdir(self):
        return self._str_workdir
    @str_workdir.setter
    def str_workdir(self, value):
        self._str_workdir = value

    @property
    def str_dirformat(self):
        return self._str_dirformat
    @str_dirformat.setter
    def str_dirformat(self, value):
        self._str_dirformat = value

    @property
    def array_id(self):
        return self._array_id
    @array_id.setter
    def array_id(self, value):
        self._array_id = value

    def def_id2dir( self, value ):
        return (self._str_dirformat % value)

def def_subloop( class_subparas ):
    with open( 'sub.py','r' ) as file_sub:
        str_subfile = file_sub.read()
    os.chdir( class_subparas.str_workdir )

    for int_id in class_subparas.array_id:
        print(int_id)
        os.chdir( class_subparas.def_id2dir(int_id) )

        with open( 'sub.py','w' ) as file_sub:
            str_subfile_new = re.sub( 'xNUMx', str(int_id), str_subfile )
            file_sub.write( str_subfile_new )

        subprocess.run( ['python','sub.py'] )
        os.chdir('..')

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
    dict_pot['Pt']=['Pt',18]
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
        str_excute,
        Instance_mpi,
        ):

    str_homedir = os.environ[ 'homedir' ]
    str_mycluster = os.environ[ 'mycluster' ]

    str_jobqueue = Instance_mpi.str_jobqueue
    int_nodes = Instance_mpi.int_nodes
    int_ppn = Instance_mpi.int_ppn

    str_jobname = 'tff.'+str_jobname
    str_nodefile = str_jobname+'.nodelist'
    str_subfile = str_jobname + '.sh'

    #-----------------------------[cluster]
    dict_subconfig = {}
    dict_subconfig[ 'qsub' ] = (
        '#PBS -l nodes='+str(int_nodes)+':ppn='+str(int_ppn)+'\n'+
        '#PBS -l walltime=240:00:00\n'+
        '#PBS -N '+str_jobname+'\n'+
        '#PBS -q '+str_jobqueue+'\n'+
        '#PBS -j oe\n'+
        'cd $PBS_O_WORKDIR\n'+
        'cat $PBS_NODEFILE > '+str_nodefile+'\n'
        )
    dict_jobsub = {}
    dict_jobsub[ 'qsub' ] = 'qsub '+str_subfile


    #-----------------------------[headend]
    str_subhead = (
        'source '+str_homedir+'codes/common/set_env.sh\n'+
        'set -euo pipefail\n'+
        'SECONDS=0\n'+
        'sort -u '+str_nodefile+' > '+str_nodefile+'.tmp && mv '+str_nodefile+'.tmp '+str_nodefile+'\n'
        )
    str_timecount='echo "TotalTime $((${SECONDS} / 60)) m $((${SECONDS} % 60)) s."'

    #-----------------------------[program]
    str_subvasp = (
        'if [ -f "INCAR" ]; then\n'+
        '   sed -i "/NCORE/c\  NCORE = '+ str(int(int_ppn/2)) +'" INCAR\n'+
        'fi\n'
        )

    #-----------------------------[]
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

class Class_mpi():
    
    def __init__(self):
        _class_cluster = server.class_cluster()
        self._str_jobqueue = _class_cluster.str_jobqueue
        self._dict_maxppn = _class_cluster.dict_maxppn

        self._int_maxppn = self._dict_maxppn[ self._str_jobqueue ]
        self._int_nodes = 1
        self._int_ppn = self._int_maxppn
    
        self._int_mpippn = 4
        self._int_ompthread = math.ceil(self._int_ppn / self._int_mpippn)
        self._int_np = self._int_mpippn * self._int_nodes

    @property
    def str_jobqueue(self):
        return self._str_jobqueue
    @str_jobqueue.setter
    def str_jobqueue(self, _temp):
        self._str_jobqueue = _temp
        self._int_maxppn = self._dict_maxppn[ self._str_jobqueue ]
        self._int_ppn = self._int_maxppn
        self._int_ompthread = math.ceil(self._int_ppn / self._int_mpippn)

    @property
    def int_maxppn(self):
        return self._int_maxppn
    @int_maxppn.setter
    def int_maxppn(self, _temp):
        self._int_maxppn = _temp

    @property
    def int_nodes(self):
        return self._int_nodes
    @int_nodes.setter
    def int_nodes(self, _temp):
        self._int_nodes = _temp
        self._int_np = self._int_mpippn * self._int_nodes

    #@property
    #def int_ncore(self):
    #    return self._int_ncore
    #@int_ncore.setter
    #def int_ncore(self, _temp):
    #    self._int_ncore = _temp
    #    self._int_nodes = math.ceil( _temp/self._int_maxppn )
    #    self._int_ppn = math.ceil( _temp/self._int_nodes )

    @property
    def int_ppn(self):
        return self._int_ppn
    @int_ppn.setter
    def int_ppn(self, _temp):
        self._int_ppn = _temp

    @property
    def int_mpippn(self):
        return self._int_mpippn

    @property
    def int_ompthread(self):
        return self._int_ompthread

    @property
    def int_np(self):
        return self._int_np

    @property
    def str_mpiomp(self):
        return 'mpirun -np '+ str(self._int_np) +' -ppn '+str(self._int_mpippn)+' -genv OMP_NUM_THREADS='+str(self._int_ompthread)+' -genv OMP_STACKSIZE=512m '
