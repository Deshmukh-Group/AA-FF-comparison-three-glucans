import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import scipy as sc
import sklearn.metrics 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from scipy import optimize as opt

a=np.loadtxt("charmm_aml_ac_O2_O3.xvg", dtype=float)#, max_rows=200)
b=np.array(a)


def potential(x,A1,T1,A2,T2,A3,T3):
	return (A1*np.exp(-(x/T1)))+(A2*np.exp(-(x/T2)))+(A3*np.exp(-(x/T3)))
param, pcovar=opt.curve_fit(potential,b[:,0],b[:,1], maxfev = 5000) # curve fitting to quadratic
potfn=potential(b[:,0], param[0], param[1], param[2], param[3], param[4], param[5])
R2=r2_score(b[:,1],potfn) 

print(R2)
plt.plot(b[:,0],b[:,1], 'r+')
plt.plot(b[:,0],potfn, 'b')
plt.show()

print(param[0], param[1], param[2], param[3], param[4], param[5])
