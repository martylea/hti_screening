
import sys
def freqcalc(functional, basis, xyz, procs):
    inp = open('./tddft_calc.inp', 'w+')
    inp.write('! RKS '+str(functional)+' '+str(basis)+' 'str(basis)+'/c def2/J RIJCOSX \n'
              '! Numfreq \n'
              '%pal nprocs '+str(procs)+' end \n'
              '* xyzfile 0 1 '+str(xyz)+' \n')
    inp.close()
freqcalc(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
