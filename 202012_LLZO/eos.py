# Fit equations of state (EOS) to energy vs volume curves and plot the results.
# Modified from http://www.jyhuang.idv.tw/JYH_QESimulation_files/1_tutorials/1a_stropt/eos-fit.py
# Only for simple cubic !!
# 2020.12.25 @tianff

import sys, numpy, math
from scipy.optimize import least_squares

# Murnaghan equation of state
def eos_murnaghan(params, vol):
    'From Phys. Rev. B 28, 5480 (1983)'
    E0, B0, Bp, V0 = params 
    E = E0 + B0/Bp * vol * ((V0/vol)**Bp/(Bp-1.0)+1.0) - V0*B0/(Bp-1.0)
    return E

# Birch-Murnaghan equation of state
def eos_birch_murnaghan(params, vol):
    'From Phys. Rev. B 70, 224107'
    E0, B0, Bp, V0 = params 
    eta = (vol/V0)**(1.0/3.0)
    E = E0 + 9.0*B0*V0/16.0 * (eta**2-1.0)**2 * (6.0 + Bp*(eta**2-1.0) - 4.0*eta**2)
    return E

# Birch equation of state
def eos_birch(params, vol):
    '''
    From Intermetallic compounds: Principles and Practice, Vol. I: Princples
    Chapter 9 pages 195-210 by M. Mehl. B. Klein, D. Papaconstantopoulos
    '''
    E0, B0, Bp, V0 = params 
    E = (E0 + 9.0/8.0*B0*V0*((V0/vol)**(2.0/3.0) - 1.0)**2
            + 9.0/16.0*B0*V0*(Bp-4.)*((V0/vol)**(2.0/3.0) - 1.0)**3)
    return E

# Vinet equation of state
def eos_vinet(params, vol):
    'From Phys. Rev. B 70, 224107'
    E0, B0, Bp, V0 = params 
    eta = (vol/V0)**(1.0/3.0)
    E = E0 + 2.0*B0*V0/(Bp-1.0)**2 * \
        (2.0 - (5.0 + 3.0*Bp*(eta-1.0) - 3.0*eta)*numpy.exp(-3.0*(Bp-1.0)*(eta-1.0)/2.0))
    return E


#fname = input("Filename containing energy vs volume [volume.dat]: ")
fname = 'E0_a.dat'

try:
    f = open(fname, 'rt')
except IOError:
    sys.stderr.write("Error opening or reading file %s\n" % (fname))
    sys.exit(1)

# read data from file
print()
print("Data read from file:",fname)
vol = []
ene = []
while True:
    line = f.readline().strip()
    if line == '': break
    if line[0] == '#' or line[0] == '!': continue
#    v, e = [float(x) for x in line.split()[:2]]
    v = float(line.split()[0])**3
    e = float(line.split()[5])
    vol.append(v)
    ene.append(e)
    print(v, e)
print()
f.close()

# transform to numpy arrays
vol = numpy.array(vol)
ene = numpy.array(ene)

vol_unit = "ang3"
ene_unit = "eV"
print()

# fit a parabola to the data and get inital guess for equilibirum volume
# and bulk modulus
a, b, c = numpy.polyfit(vol, ene, 2)
V0 = -b/(2*a)
E0 = a*V0**2 + b*V0 + c
B0 = 2*a*V0
Bp = 4.0

# initial guesses in the same order used in the Murnaghan function
x0 = [E0, B0, Bp, V0]

def print_params(label, params):
    E0, B0, Bp, V0 = params
    print(label, ": E0 = %f eV" % (E0))
    print(label, ": B0 = %f eV*ang^-3" % (B0))
    print(label, ": B0 = %f GPa" % (B0*160.21765))
    print(label, ": Bp = %f" % (Bp))
    print(label, ": V0 = %f angstrom^3" % (V0))
    print(label, ": a0 = %f angstrom" % (V0**(1.0/3.0)))
    print()

# fit the equations of state
target = lambda params, y, x: y - eos_murnaghan(params, x)
murn = least_squares(target, x0, args=(ene,vol), method='lm').x
print_params("Murnaghan", murn)

target = lambda params, y, x: y - eos_birch_murnaghan(params, x)
birch_murn = least_squares(target, x0, args=(ene,vol), method='lm').x
print_params("Birch-Murnaghan", birch_murn)

target = lambda params, y, x: y - eos_birch(params, x)
birch = least_squares(target, x0, args=(ene,vol), method='lm').x
print_params("Birch", birch)

target = lambda params, y, x: y - eos_vinet(params, x)
vinet = least_squares(target, x0, args=(ene,vol), method='lm').x
print_params("Vinet", vinet)


try:
    import pylab
except ImportError:
    sys.stderr.write("pylab module non available, skipping plot")
    sys.exit(0)

# plotting
#ans = myinput("Do you want to plot the result (yes/no)", "yes", ["yes", "no"])
ans = "yes"
if ans == "no": sys.exit(0)

import pylab
vfit = numpy.linspace(min(vol),max(vol),100)

pylab.plot(vol, ene-E0, 'ro')
pylab.plot(vfit, a*vfit**2 + b*vfit + c - E0,'--',label='parabolic fit')
pylab.plot(vfit, eos_murnaghan(murn,vfit)-E0, label='Murnaghan')
pylab.plot(vfit, eos_birch_murnaghan(birch_murn,vfit)-E0, label='Birch-Murnaghan')
pylab.plot(vfit, eos_birch(birch,vfit)-E0, label='Birch')
pylab.plot(vfit, eos_vinet(vinet,vfit)-E0, label='Vinet')
pylab.xlabel('Volume ($\AA^3$)')
pylab.ylabel('Energy (eV)')
pylab.legend(loc='best')
#pylab.show()
pylab.savefig('a-eos.png')
quit()
