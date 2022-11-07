#!/usr/bin/env python
# coding: utf-8

# In[88]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
parameters = pd.DataFrame(pd.read_excel(r"ConstraintParameters.xlsx")).loc[:,:'Value']
parameters


# <b> The parameters are defined below </b> </br>
# rho: air density (at ground level) </br>
# vs: stall speed </br>
# clmax: maximum lift coefficient </br>
# vmax: maximum speed </br>
# cd0: zero-lift drag coefficient </br>
# e: oswald span efficiency </br>
# ar: aspect ratio </br>
# k: induced drag factor </br>
# np: propeller efficiency </br>
# vt: engine thrust speed at catapult takeoff </br>
# vw: wind-over-deck speed at catapult takeoff </br>
# ve: end speed at catapult takeoff </br>
# roc: rate of climb </br>
# ldmax: maximum lift-to-drag ratio </br>

# In[89]:


[rho, vs, clmax, vmax, cd0, e, ar, k, pe, vt, vw, ve, roc, ldmax] = parameters['Value']


# In[90]:


# W/S as x-axis
WingLoading = np.arange(5,2000,0.1)
# stall equation - might change to follow Gudmunsson
stallEq = (1/2)*rho*clmax*vs**2
# Maximum speed equation
vmaxEq = pe/((rho*(vmax**3)*cd0/(2*WingLoading))+(2*k*WingLoading)/(rho*vmax))
# Catapult Takeoff equation
catapultEq = (clmax*rho*(ve+vw+vt)**2)/(2*1.21)
# Rate of Climb equation
# prop efficiency is 0.5 in climb
rocEq = 1/((roc/0.5) +np.sqrt(2*WingLoading/(rho*np.sqrt(3*cd0/k)))*(1.155/(ldmax*0.5)))
# Turn rate eq.
# Service ceiling eq.?


# In[93]:


constraint = plt.figure()
ax = constraint.add_axes([0,0,1,1])
ax.set_xlabel("W/S")
ax.set_ylabel("P/W")
ax.set_title("Constraint Diagram")
ax.plot(WingLoading, vmaxEq, label = "Maximum Speed")
ax.plot(WingLoading, rocEq, label = "Rate of Climb")
ax.axvline(stallEq, label = "Stall Speed", color = 'red')
ax.axvline(catapultEq, label = "Takeoff")
ax.legend()
# ax.set_xlim(0,stallEq+25)


# In[ ]:




