
import sys
def tddft_input_gen(functional, basis, roots, xyz, procs):
    inp = open('./tddft_calc.inp', 'w+')
    inp.write('! RKS '+str(functional)+' '+str(basis)+' 'str(basis)+'/c def2/J RIJCOSX \n'
              '%pal nprocs '+str(procs)+' end \n'
              '%tddft nroots '+str(roots)+' maxdim 10 end \n'
              '* xyzfile 0 1 '+str(xyz)+' \n')
    inp.close()
tddft_input_gen(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
print('Generated file: tddft_calc.inp')