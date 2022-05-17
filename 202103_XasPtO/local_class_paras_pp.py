import math
from tf_xas_kit import class_paras

def def_instance_paras_code2xas():

    instance_paras = class_paras.class_paras()

    # generate xas from MYCARXAS
    #instance_paras.log_tm2xas = False
    instance_paras.log_tm2xas = True
    instance_paras.str_broadmethod = 'gaussian'
    #instance_paras.str_broadmethod = 'lorentzian'
    #instance_paras.float_hwhm = 0.45*math.sqrt( math.log(2) )
    #instance_paras.float_hwhm = 0.225
    instance_paras.float_hwhm = 0.4*math.sqrt( 2*math.log(2) )
    instance_paras.int_broadnbin = 3000

    str_temp = ''
    instance_paras.str_xasfile = 'xas'+str_temp+'.csv'
    instance_paras.str_avefile = 'xas'+str_temp+'.ave.csv'

    return instance_paras

def def_instance_paras_alphabeta():
   
    instance_paras = class_paras.class_paras()
     
    str_temp = ''
    instance_paras.str_avefile = 'xas'+str_temp+'.ave.csv'
    instance_paras.str_alphafile = 'xas'+str_temp+'.alpha.csv'
    
    list2d_angle = []
    list2d_angle.append( [ 20, 90, 'trigonal' ] )
    list2d_angle.append( [ 90, 45, 'trigonal' ] )
    list2d_angle.append( [  0, 90, 'trigonal' ] )
    list2d_angle.append( [ 41, 90, 'trigonal' ] )
    list2d_angle.append( [ 90,  0, 'orthorhombic' ] )
    list2d_angle.append( [ 90, 90, 'orthorhombic' ] )
    instance_paras.list2d_angle = list2d_angle

    list1d_alignangle = [ 20, 90, 'trigonal']
    instance_paras.list1d_alignangle = list1d_alignangle

    #instance_paras.str_scalingmethod = 'float_mainscaling'
    instance_paras.str_scalingmethod = 'float_postscaling'

    return instance_paras
