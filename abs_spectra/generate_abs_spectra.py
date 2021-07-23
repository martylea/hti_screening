import sys, os, time, subprocess
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def generate_abs_spectra(outfilename, startwavelength, endwavelength):
    bashcmd = 'which orca'
    process = subprocess.Popen(bashcmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.system(output[0:-1]+'_mapspc '+str(outfilename)+' ABS -x0'+str(1e+6/int(startwavelength))+' -x1'+str(1e+6/int(endwavelength)))
    time.sleep(2)
    print('Spectra files generated')

def wavenumber_to_wavelength(outfilename)
    spectra = np.loadtxt(outfilename+'.abs.dat')
    spectra[:,0] = 1e+6/spectra[:,0]
    pd.DataFrame(spectra).to_csv('spectra.csv', index=None, header=None)

def abs_plot():
    wl = spectra[:,0]
    intensity = spectra[:,1]
    fig = plt.figure()
    plt.show()
    
    
generate_abs_spectra(sys.argv[1], sys.argv[2], sys.argv[3])
wavenumber_to_wavelength(sys.arg[1])
