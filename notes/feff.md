# feff

## feff.inp

```inp
*--------------------------------------[structure]

CIF feff.cif
TARGET 1

RECIPROCAL

TITLE test

*--------------------------------------[spectrum]

* p70
* XANES [xkmax xkstep vixan]
* XANES 8 0.07 0.0 (default)
XANES 4.0

* p71
* ELLIPTICITY elpty x y z
* ELLIPTICITY 0.0 (default)
* ELLIPTICITY 1.0 0.0 0.0 -1.0

* p71
* POLARIZATION x y z
* Spherically average (default)
POLARIZATION 1.0 0.0 0.0

*--------------------------------------[general]

* p74
*          ipot    ixsph   ifms    ipath   igenfmt iff2x
* CONTROL    1       1       1       1       1       1     (default)

* p75
* KMESH nkp(x) [nkpy nkpz [ktype [usesym] ] ]
KMESH 15 15 1

* p76
EGRID
* grid_type grid_min grid_max grid_step
e_grid -10 20 0.1

*--------------------------------------[ipot: atomic, pot, screen]

* p77
* COREHOLE FSR (default)
COREHOLE RPA
EDGE K

* p77
* SCF rfms1 [lfms1 nscmt ca nmix]
* SCF None 0 30 0.2 1 (default)
SCF 7.0

* p80
* EXCHANGE ixc vr0 vi0 [ixc0]
* EXCHANGE 0 0 0.0 (default)

* p82
* CHBROADENING igammach
* CHBROADENING 0 (default)

* p83
* CHWIDTH 0.45

*--------------------------------------[ifms: fms, mkgtr]

* p90
* FMS rfms [lfms2 minv toler1 toler2 rdirec]
* FMS None 0 0 0.001 0.001 (default)
FMS 9.0 0 2

*--------------------------------------[iff2x: ff2x, sfconv, eels]

* p98
* CORRECTIONS vrcorr vicorr

ABSOLUTE

```
