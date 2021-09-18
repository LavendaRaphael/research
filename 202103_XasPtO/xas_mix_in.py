#!/bin/env python
import math
from from_xas_mix import def_xas_mix

def def_weight (alpha,beta)
    alpha = math.radians (alpha)
    beta = math.radians (beta)
    result = []
    result.append (0.5 * (math.cos(beta)**2 + math.cos(beta)**2 * math.sin(alpha)**2))
    result.append (result[0])
    result.append (math.cos(alpha)**2 * math.sin(beta)**2)

alpha = 20
float_frac = 0.7

beta = 90
str_prefix = 'xas_mix.a' +str(alpha) +'_b' +str(beta)
list_weight = def_weight (alpha,beta)
list_weight_1 = list_weight
list_files = []
list_files.append( ('xas_ave.dat', 1, list_weight[0]) )
list_files.append( ('xas_ave.dat', 2, list_weight[1]) )
list_files.append( ('xas_ave.dat', 3, list_weight[2]) )

beta = 45.0
str_prefix = 'xas_mix.a' +str(alpha) +'_b' +str(beta)
list_weight = def_weight (alpha,beta)
list_weight_2 = list_weight
list_files = []
list_files.append( ('xas_ave.dat', 1, list_weight[0]) )
list_files.append( ('xas_ave.dat', 2, list_weight[1]) )
list_files.append( ('xas_ave.dat', 3, list_weight[2]) )

str_prefix = 'xas_mix.a' +str(alpha) +'_frac'
list_weight = [ list_weight_1[i]*float_frac + list_weight_2[i]*(1.0-float_frac) for i in range(3) ]
list_files = []
list_files.append( ('xas_ave.dat', 1, list_weight[0]) )
list_files.append( ('xas_ave.dat', 2, list_weight[1]) )
list_files.append( ('xas_ave.dat', 3, list_weight[2]) )

