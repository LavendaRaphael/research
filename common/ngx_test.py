import math
float_hbar = 1.054571817*10**(-34)  # J*s
float_emass = 9.1093837015 * 10**(-31)  # Kg
float_ecut = 2611 # eV
float_ev = 1.602176634 * 10**(-19) # J
float_ecut_j = float_ecut * float_ev # J
float_gcut = math.sqrt( 2 * float_emass * float_ecut_j / float_hbar**2 ) # m^-1
float_gcut_perang = float_gcut*10**(-10) # ang^-1
float_gcut_perang /= 2*math.pi
float_ng = float_gcut_perang * 4
float_ngf = float_ng * 2
float_ngf_inverse = 1/float_ngf # ang
print( float_ngf_inverse )
