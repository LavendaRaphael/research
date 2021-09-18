#!/bin/env python
import math
from from_xas_mix import def_xas_mix

def def_weight (alpha,beta):
    alpha = math.radians (alpha)
    beta = math.radians (beta)
    result = []
    result.append (0.5 * (math.cos(beta)**2 + math.sin(alpha)**2 * math.sin(beta)**2))
    result.append (result[0])
    result.append (math.cos(alpha)**2 * math.sin(beta)**2)
    return result

#alpha=20
alpha = 41
float_frac = 0.7
#str_datfile = 'xas_ave.dat'
str_datfile = 'xas_alignorm.a'+str(alpha)+'.dat'

beta = 90
str_prefix = 'xas_mix.a' +str(alpha) +'_b' +str(beta)
list_weight = def_weight (alpha,beta)
list_weight_1 = list_weight
list_files = []
list_files.append( (str_datfile, 1, list_weight[0]) )
list_files.append( (str_datfile, 2, list_weight[1]) )
list_files.append( (str_datfile, 3, list_weight[2]) )
def_xas_mix( list_files=list_files, str_prefix=str_prefix )

beta = 45
str_prefix = 'xas_mix.a' +str(alpha) +'_b' +str(beta)
list_weight = def_weight (alpha,beta)
list_weight_2 = list_weight
list_files = []
list_files.append( (str_datfile, 1, list_weight[0]) )
list_files.append( (str_datfile, 2, list_weight[1]) )
list_files.append( (str_datfile, 3, list_weight[2]) )
def_xas_mix( list_files=list_files, str_prefix=str_prefix )

str_prefix = 'xas_mix.a' +str(alpha) +'_frac'
list_weight = [ list_weight_1[i]*float_frac + list_weight_2[i]*(1.0-float_frac) for i in range(3) ]
list_files = []
list_files.append( (str_datfile, 1, list_weight[0]) )
list_files.append( (str_datfile, 2, list_weight[1]) )
list_files.append( (str_datfile, 3, list_weight[2]) )
def_xas_mix( list_files=list_files, str_prefix=str_prefix )

