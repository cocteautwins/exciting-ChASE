#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys

#-------------------------------------------------------------------------------

def shell_value(variable,vlist,default):
    v = default
    e = False
    for i in range(len(vlist)):
        if ( vlist[i] == variable ): v = os.environ[variable] ; e = True ; break
    return v, e
    
#-------------------------------------------------------------------------------

current = os.environ['PWD']
ev_list = os.environ.keys()

rundir = shell_value('EXCITINGRUNDIR',ev_list,current)[0]
rlabel = shell_value('RLABEL',ev_list,"rundir-")[0]
showpyplot = shell_value('SHOWPYPLOT',ev_list,"")[1]
dpipng = int(shell_value('DPIPNG',ev_list,300)[0])

#-------------------------------------------------------------------------------
fname="MOKE_NLF_FXCRPA_QMT001.OUT"
#-------------------------------------------------------------------------------
#Parse LOSS function data files
w=[]
sr=[]
si=[]

print "Parsing "+fname

f = open(fname)
lines = f.readlines()
for l in lines:
    ls=l.split()
    if len(ls)==3:
        if '#' not in ls[0]:
            w.append(float(ls[0]))
            sr.append(float(ls[1]))
            si.append(float(ls[2]))
    
f.close()

#-------------------------------------------------------------------------------
#Plot LOSS function/s 
colors=['k','r','g','b','y','c','m']
fig=plt.figure(1,figsize=(8,5.5))

params = {'font.size':15,
          'xtick.major.size': 5,
          'ytick.major.size': 5,
          'patch.linewidth': 1.5,
          'axes.linewidth': 2.,
          'axes.formatter.limits': (-4, 6),
          'lines.linewidth': 1.8,
          'lines.markeredgewidth':2.0,
          'lines.markersize':18,
          'legend.fontsize':11,
          'legend.borderaxespad':1,
          'legend.borderpad':0.5,
          'savefig.dpi':80}

plt.rcParams.update(params)

ax=fig.add_subplot(111)

ax.plot(w,sr,color="black",label="$\\theta_K$")
ax.plot(w,si,color="red",label="$\\gamma_K$")

ax.legend(loc=1)
#ax.legend()

#ax.set_xlim(0.0,54.0)
#ax.set_ylim(0)
ax.set_xlabel("Energy [eV]")
ax.set_ylabel("deg")

plt.savefig('PLOT.ps',  orientation='portrait',format='eps')
plt.savefig('PLOT.png', orientation='portrait',format='png',dpi=dpipng)

if (showpyplot): plt.show()
