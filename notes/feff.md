# feff.inp

```feff
*--------------------------------------[structure]

TITLE test

*--------------------------------------[spectrum]

* p70
* XANES [xkmax xkstep vixan]
XANES 6 0.05 0.3

* p71
* ELLIPTICITY elpty x y z
*ELLIPTICITY 1.0 0.0 0.0 -1.0

* p71
POLARIZATION 1.0 0.0 0.0

*--------------------------------------[general]

* p74
*          ipot    ixsph   ifms    ipath   igenfmt iff2x
*CONTROL    1       1       1       1       1       1

* p76
EGRID
e_grid -10 20 0.1

*--------------------------------------[ipot: atomic, pot, screen]

* p77
COREHOLE RPA
EDGE K

* p77
SCF 7.0

* p80
*EXCHANGE 0 0.0 0.0

* p83
*CHWIDTH 0.45

*--------------------------------------[ixsph: xsph]

*--------------------------------------[ifms: fms, mkgtr]

* p90
* FMS rfms [lfms2 minv toler1 toler2 rdirec]
FMS 9.0 0 2

*--------------------------------------[ipath: path]

*--------------------------------------[igenfmt: genfmt]

*--------------------------------------[iff2x: ff2x, sfconv, eels]

ABSOLUTE

```

## K-SPACE

```feff
*--------------------------------------[structure]

CIF feff.cif
RECIPROCAL
TARGET 1
TITLE test

*--------------------------------------[spectrum]

* p70
* XANES [xkmax xkstep vixan]
XANES 6 0.05 0.3

* p71
* ELLIPTICITY elpty x y z
*ELLIPTICITY 1.0 0.0 0.0 -1.0

* p71
POLARIZATION 1.0 0.0 0.0

*--------------------------------------[general]

* p74
*          ipot    ixsph   ifms    ipath   igenfmt iff2x
*CONTROL    1       1       1       1       1       1

* p75
KMESH 15 15 1

* p76
EGRID
e_grid -10 20 0.1

*--------------------------------------[ipot: atomic, pot, screen]

* p77
COREHOLE RPA
EDGE K

* p77
SCF 7.0

* p80
*EXCHANGE 0 0 0.0

*--------------------------------------[ifms: fms, mkgtr]

* p90
* FMS rfms [lfms2 minv toler1 toler2 rdirec]
FMS 9.0 0 2

*--------------------------------------[iff2x: ff2x, sfconv, eels]

ABSOLUTE

```