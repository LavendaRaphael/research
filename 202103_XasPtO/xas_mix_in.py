#!/bin/env python
import math

class cla_paras:
    alpha = 20
    beta = 90.0
    alpha = alpha / math.pi
    beta = beta / math.pi
    weight_1 = 0.5 * (math.cos(beta)**2 + math.cos(beta)**2 * math.sin(alpha)**2)
    weight_2 = weight_1
    weight_3 = math.cos(alpha)**2 * math.sin(beta)**2
    list_files = []
    # filename, column[n], weight
    list_files.append( ('xas_ave.dat', 1, weight_1) )
    list_files.append( ('xas_ave.dat', 2, weight_2) )
    list_files.append( ('xas_ave.dat', 3, weight_3) )
