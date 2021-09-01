#!/user/bin/env python
from ase.visualize import view
from ase.io import read
import sys

cont = []
for x in sys.argv[1:]:
    cont.extend(read(str(x),index=":"))
view(cont,repeat=(3,3,1))
