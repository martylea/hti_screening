import sys
import ase
from ase.io import read,write,iread
from ase.calculators.orca import ORCA
def orca_numfreq(functional, basis, system, procs):
    system = read(str(system))
    system.calc = ORCA(label='orca',
    maxiter = 200,
    charge = 0, mult=1,
    orcasimpleinput = str(functional)+' '+str(basis)+' '+'Numfreq',
    orcablocks = '%pal nprocs '+str(procs)+' end \n')
    try:
        print(system.get_potential_energy())
    except:
        print('Frequency calculation was not successful')
orca_numfreq(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
