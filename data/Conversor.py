import numpy as np
import matplotlib.pyplot as plt
import configobj
from matplotlib import dates as mdate
from obspy.imaging.cm import obspy_sequential
from obspy.signal.tf_misfit import cwt
from obspy.core import read
import os
import seaborn #Deixa os graficos do matplotlib mais bonitos
import matplotlib.gridspec as gridspec




LC = np.loadtxt("ha_fit_pg.dat")
times, IntFlux, Gamma, IntFluxErr, GammaErr, TS, retcode, npred = LC.T[0],LC.T[1],LC.T[2],LC.T[3],LC.T[4],LC.T[5],LC.T[6],LC.T[7]


#import scipy.signal as signal
#IntFlux = signal.detrend(IntFlux)

np.savetxt('curva0.dat', np.transpose((times,IntFlux)), fmt="%.10f", header="time,flux", delimiter=' ')




