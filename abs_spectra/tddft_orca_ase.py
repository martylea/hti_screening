import sys
import ase
from ase.io import read,write
from ase.calculators.orca import ORCA
def tddft_calc(functional, basis, roots, system, procs):
    system = read(str(system))
    system.calc = ORCA(label='orca',
    maxiter = 200,
    charge = 0, mult=1,
    orcasimpleinput = str(functional)+' '+str(basis),
    orcablocks = '%pal nprocs '+str(procs)+' end \n'
    '%tddft nroots '+str(roots)+' maxdim 10 end \n')
    try:
        print(system.get_potential_energy())
    except:
        print('Calculation was not successful')

tddft_calc(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])