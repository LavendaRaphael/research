#!/user/bin/env python
import os
from tf_xas_kit import class_structure

def def_list1d_key():
    list1d_key=[]
   
    #----------------------------------
    #list1d_key.append('111.a2b2_O1_feffk')
    #list1d_key.append('111.x4y4_O4')
    #list1d_key.append('111.x4y4_O4_hch')
    #list1d_key.append('111.x4y4_O4_gw')
    #list1d_key.append('111.x4y4_O4_new_gw')

    #----------------------------------
    #list1d_key.append('110.x1y1.a2b2_O2_a1b2')
    #list1d_key.append('110.x2y12_O22')
    #list1d_key.append('110.x2y12_O22_aimd')
    list1d_key.append('110.x2y12_O22_gw')
    #list1d_key.append('110.x2y1_O1_a1b3')
    #list1d_key.append('110.x2y1_O2_feffk')
    #list1d_key.append('110.x2y1_O2_a1b3')
    #list1d_key.append('110.x2y2_O1_a1b2')
    #list1d_key.append('110.x2y2_O2.14_a1b2')
    #list1d_key.append('110.x2y2_O3_a1b2')
    #list1d_key.append('110.x2y3_O1')
    #list1d_key.append('110.x2y3_O1_a1b2')
    #list1d_key.append('110.x2y3_O2.12')
    #list1d_key.append('110.x2y3_O2.13')
    #list1d_key.append('110.x2y3_O2.14')
    #list1d_key.append('110.x2y3_O3.123')
    #list1d_key.append('110.x2y3_O3.136')
    #list1d_key.append('110.x2y3_O4.v56')
    #list1d_key.append('110.x2y3_O5')
    #list1d_key.append('110.x2y4_O2.16')
    #list1d_key.append('110.x2y4_O3.137')
    #list1d_key.append('110.x2y4_O3.148')
    #list1d_key.append('110.x2y4_O4.1237')
    #list1d_key.append('110.x2y4_O6.v56')
    #list1d_key.append('110.x2y6_O2.18')
    #list1d_key.append('110.x4y3_O2.12')
    #list1d_key.append('110.x4y3_O6')

    return list1d_key

def def_dict_structure():
    
    dict_structure = {}
    #===================================================================================
    str_key='111.a2b2_O1_feff'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.111.a2b2_O1_vac/feff/',
        }
    #------------------------------------------
    str_key='111.a2b2_O1_feffk'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.111.a2b2_O1_vac/feff_kspace/',
        }
    #------------------------------------------
    str_key='111.x4y4_O4'
    dict_structure[ str_key ] = {
        'str_code': 'vasp',
        'str_surface': '111',
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='111.x4y4_O4_hch'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.111.x4y4_O4_vac/vasp_sch.hch/'
        }
    #------------------------------------------
    str_key='111.x4y4_O4_gw'
    dict_structure[ str_key ] = {
        'str_code': 'vasp',
        'str_surface': '111',
        'str_workdir': 'Pt.111.x4y4_O4_vac/vasp_sch.gw/',
        }
    #------------------------------------------
    str_key='111.x4y4_O4_new_gw'
    dict_structure[ str_key ] = {
        'str_code': 'vasp',
        'str_surface': '111',
        'str_workdir': 'Pt.111.x4y4_O4_vac/vasp_sch_new.gw/',
        }
    #===================================================================================
    str_key='110.x1y1.a2b2_O2_a1b2'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y12_O22'
    dict_atom = {}
    dict_atom[1] = 4.0
    dict_atom[3] = 4.0
    dict_atom[5] = 4.0
    dict_atom[7] = 4.0
    dict_atom[9] = 4.0
    dict_atom[11] = 2.0
    dict_structure[ str_key ] = {
        'str_surface': '110',
        'str_code': 'vasp', 
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y12_O22_aimd'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 1.0
    dict_atom[3] = 1.0
    dict_atom[4] = 1.0
    dict_atom[5] = 1.0
    dict_atom[6] = 1.0
    dict_atom[7] = 1.0
    dict_atom[8] = 1.0
    dict_atom[9] = 1.0
    dict_atom[10]=1.0
    dict_atom[11]=1.0
    dict_atom[12]=1.0
    dict_structure[ str_key ] = { 
        'str_workdir': 'Pt.110.x2y12_O22_vac/vasp_sch.aimd2_932/', 
        'dict_atom': dict_atom
        }
    #------------------------------------------
    str_key='110.x2y12_O22_gw'
    dict_atom = {}
    dict_atom[1] = 4.0
    dict_atom[3] = 4.0
    dict_atom[5] = 4.0
    dict_atom[7] = 4.0
    dict_atom[9] = 4.0
    dict_atom[11] = 2.0
    dict_structure[ str_key ] = { 
        'str_code': 'vasp',
        'str_surface': '110',
        'str_workdir': 'Pt.110.x2y12_O22_vac/vasp_sch_new.gw/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y1_O1_a1b3'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y1_O2_feffk'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.110.x2y1_O2_vac/feff_k/',
        }
    #------------------------------------------
    str_key='110.x2y1_O2_a1b3'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y1_O2_a1b3'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
   #------------------------------------------
    str_key='110.x2y2_O1_a1b2'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y2_O2.14_a1b2'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y2_O3_a1b2'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 1.0
    dict_atom[3] = 1.0
    dict_structure[ str_key ] = { 
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom, 
        }
    #------------------------------------------
    str_key='110.x2y3_O1'
    dict_structure[ str_key ] = { 
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/', 
        }
    #------------------------------------------
    str_key='110.x2y3_O1_a1b2'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+ str_key +'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y3_O2.12'
    dict_structure[ str_key ] = { 
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/', 
        }
    #------------------------------------------
    str_key='110.x2y3_O2.13'
    dict_structure[ str_key ] = { 
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/', 
        }
    #------------------------------------------
    str_key='110.x2y3_O2.14'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y3_O3.123'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 1.0
    dict_atom[3] = 1.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y3_O3.136'
    dict_atom = {}
    dict_atom[1] = 2.0
    dict_atom[3] = 1.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y3_O4.v56'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y3_O5'
    dict_atom = {}
    dict_atom[1] = 2.0
    dict_atom[2] = 2.0
    dict_atom[5] = 1.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y4_O2.16'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x2y4_O3.137'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 2.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y4_O3.148'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 2.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y4_O4.1237'
    dict_atom = {}
    dict_atom[1] = 1.0
    dict_atom[2] = 1.0
    dict_atom[3] = 2.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y4_O6.v56'
    dict_atom = {}
    dict_atom[1] = 2.0
    dict_atom[3] = 4.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    str_key='110.x2y6_O2.18'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+ str_key +'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x4y3_O2.12'
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        }
    #------------------------------------------
    str_key='110.x4y3_O6'
    dict_atom = {}
    dict_atom[1] = 2.0
    dict_structure[ str_key ] = {
        'str_workdir': 'Pt.'+str_key+'_vac/vasp_sch/',
        'dict_atom': dict_atom,
        }
    #------------------------------------------
    return dict_structure

