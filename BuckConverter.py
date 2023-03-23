#!/usr/bin/env python
# coding: utf-8

# # The Buck Converter

# ## Introduction
# 
# The Buck Converter is a form of DC to DC power electronics converter that always has an output voltage lower than the input voltage. It has the topology as shown in the figure below:
# ![image.png](attachment:image.png)
# The operation of the Buck converter depends on the high frequency switching of the power switch (in this case shown as a MOSFET) and we can analyse its behaviour making some basic assumptions.

# ## Analysis Assumptions
# The basic assumptions that we make are defined as follows:
# * The Converter has reached steady state operation
# * The load is resistive
# * The power switch and diode are ideal (zero voltage drop and zero resistance in the on state)
# * The output voltage ripple is negligible compared to the average output voltage
# * The inductor and capacitor are ideal, with no parasitic resistance or inductance

# Taking these assumptions into account, we can define the operation of the converter using the periods when the transistor is turned on (The "ON state") and when it is turned off (the "OFF state"). The switching frequency of the converter is defined using the term Fs or Fsw, and is usually in the order of 10's of kHz.

# ## The "Duty Ratio"
# 
# The key design parameter that determines the output voltage is called the "Duty Ratio" and this mwans the ratio of the on time during the ON state, divided by the overall switching period (1/Fsw).
# 
# We can therefore define the Duty ratio (D) using the following expression:
# 
# $$D = t_{on}/F_{sw}$$

# This will always be in the range of 0 to 1, and is often converted to a percentage, therefore the ratio needs to be multiplied by 100 to obtain the duty ratio as a percentage.

# ## Derivation of the voltage transformation ratio
# 
# The procedure for deriving the output voltage (and hence the voltage transformation ratio) is based on calculating the behaviour of the current in the inductor in both the ON and OFF states.
# 
# If we return to the assumptions, the most important is that we have reached steady state. This implies that the average current will be a constant value, and therefore the nett effect of the ON and OFF states will be the same. I.e. that the rise of the inductor current during the ON state will be equal to the fall of the inductor current during the OFF state.
# 
# The behaviour of the inductor current during the ON and OFF states is defined by the fundamental equation of the inductor $$V = L \frac{di}{dt}$$ where the inductor current for a fixed value of inductor voltage during the ON and OFF states will result in a sloping current value.
# 
# The inductor current slope is defined by rearranging the basic inductor equation in terms of the voltage and inductance $$\frac{di}{dt} = \frac{V}{L}$$
# 

# ## Calculation of the inductor current during the ON state
# 
# During the on state, the rise in current is defined from the equation: $$\frac{di}{dt} = \frac{V}{L}$$
# 
# When the transistor is ON, the left hand side of the inductor is at the input voltage Vin and the right hand side of the inductor is at the output voltage V. Therefore the inductor Voltage is defined by $$V_L = V_{in} - V$$
# 
# The on time of the current is defined by dt, which is the on time ton, which can be defined in terms of the Duty and Period using the equation $$t_{on} = D * Period = \frac{D}{F_{sw}}$$
# 
# Therefore we can express the change in current in terms of these parameters using the following equation: $$\frac{\Delta I}{dt} = \frac{V}{L}$$ and replacing the terms for dt and V using: $$\frac{\Delta I}{D * Period} = \frac{V_{in}-V}{L}$$
# 
# Rearranging this equation, and substituting the switching frequency we therefore can obtain the expression for the rise in current during the ON state as $$\Delta I = \frac{V_{in}-V}{L} * \frac{D}{F_{sw}}$$

# ## Calculation of the inductor current during the OFF state
# 
# 
# During the off state, the fall in current is defined from the same fundamental inductor equation: $$\frac{di}{dt} = \frac{V}{L}$$
# 
# During the off state, the left hand side of the inductor is connected to the reference node via the diode, and therefore the voltage across the inductor (using the same polarity as before) is defined by $$V_L=0-V=-V$$. 
# 
# The off time of the current is defined by dt, which is the off time toff, which can be defined in terms of the Duty and Period using the equation $$t_{off} = (1-D) * Period = \frac{1-D}{F_{sw}}$$ as the off time is the remainder of the period NOT being used by the ON state, therefore is the proprtion of the period NOT occupied by the ON state and can therefore be defined as 1-D.
# 

# ## Equating the inductor current during the ON and OFF states
# 
# As we noted with our first assumption, the inductor current rise and fall are equal to achieve steady state operation, and therefore we can equate our equations for the change in current from the previous 2 sections:
# 
# $$\Delta I = \frac{V_{in}-V}{L} * \frac{D}{F_{sw}}$$
# 
# and
# 
# $$\Delta I = \frac{-V}{L} * \frac{(1-D)}{F_{sw}}$$
# 
# However, first we need to multiply the second equation by -1, as this is a falling current.
# 
# Which gives :
# 
# $$\Delta I = \frac{V_{in}-V}{L} * \frac{D}{F_{sw}} = - \frac{-V}{L} * \frac{(1-D)}{F_{sw}}$$
# 
# The first aspect to notice is that we can cancel out both the L and Fsw terms as they appear on both sides of the equation, and this simplifies to:
# 
# $$(V_{in} - V ) * D = V * (1-D) $$
# 

# 
# Using a similar analysis to the ON state,  we can express the change in current in terms of these parameters using the following equation: $$\frac{\Delta I}{dt} = \frac{V}{L}$$ and replacing the terms for dt and V using: $$\frac{\Delta I}{(1-D) * Period} = \frac{-V}{L}$$
# 
# Rearranging in terms of the change in current we obtain the equation as follows:
# 
# $$\Delta I = \frac{-V}{L} * \frac{(1-D)}{F_{sw}}$$

# As the goal is to obtain the voltage transformation ratio $$\frac{V}{V_{in}}$$ we need to collect the terms for Vin and V accordingly, therefore we can expand the equation thus $$V_{in}D - VD = V - VD$$ and as can be seen we can cancel out the -VD from both sides leaving $$V_{in}D = V$$ which can be rewritten as the voltage transformation ratio by dividing both sides by Vin to obtain $$\frac{V}{V_{in}} = D$$.
# 
# This equation therefore indicates that the output voltage will be a fraction of the input voltage defined by the duty ratio D.

# ## Voltage Transformation Ratio of a Buck Converter
# 
# In order to demonstrate the voltage transformative behaviour of the Buck converter we can take some examples. 
# 
# ### Example 1 - Calculate the duty ratio required
# 
# In this first example, if we need to calculate the duty ratio required, we need the input and output volatges to be defined

# In[1]:


Vin=12


# In[2]:


Vout=5


# In[3]:


D=Vout/Vin


# In[4]:


print("The Duty Ratio required for an Input Voltage of " + str(Vin) + " and an output voltage of " + str(Vout) + " is " + str(D))


# and if this is required as a percentage needs to be multiplied by 100:

# In[5]:


Dpercentage = D*100


# In[6]:


print("The Duty Ratio in percentage terms is " + str(Dpercentage) + " %")


# ### Example 2: Calculate the output voltage from a Duty Ratio
# 
# In this example, we can calculate the output voltage of a Buck converter if we know the input voltage and the duty ratio.
# 
# $$V_{out} = D * V_{in}$$
# 

# In[7]:


Vin=100


# In[8]:


D = 0.5


# In[9]:


Vout=Vin*D


# In[10]:


print("Output Voltage for Input Voltage of " + str(Vin) + " and Duty of " + str(D) + " is " + str(Vout))


# ## Buck Converter Waveforms
# 
# If we need to visualize the inductor current waveforms, they are a sawtooth where the time of the rising edge is proportional to the duty ratio.
# 
# In order to set the converter behaviour, we need to define the important parameters for the design as follows:

# In[11]:


vin = 100
vout = 50
r = 10
l = 0.002
c = 100.0e-6
fs = 10000


# Derive the key design parameters

# In[12]:


iout = vout/r
il_ave = iout
d = vout/vin
deltaI = (vin-vout)*d/(l*fs)
print("Iaverage = " + str(il_ave) + " delta I = " + str(deltaI))
imin = il_ave - deltaI
imax = il_ave + deltaI
ton = d/fs
toff=(1-d)/fs
ts = 1/fs


# In[13]:


import matplotlib.pyplot  as plt


# In[14]:


t = [0, ton, ts, ton+ts, ts*2, ton+ts*2, ts*3]
i = [imin, imax, imin, imax, imin, imax, imin]

fig, ax = plt.subplots()
ax.plot(t, i)

ax.set(xlabel='time (s)', ylabel='current (A)',
       title='Steady State Inductor Current Waveform')
ax.grid()

plt.show()


# We can also make an estimate of the startup voltage and inductor current waveforms from an initia condition of zero output voltage. In this case we set the duty ratio to whichever value is required.

# In[42]:


l=0.001
fs=20000
vout_target = 30
d = vout_target/vin

ton = d/fs
toff=(1-d)/fs
ts = 1/fs

cycles = 30


# In[43]:


vout = 0
t = []
i = []
v = []
time = 0
current = 0
t.append(time)
i.append(current)
v.append(vout)
for x in range(cycles):
    iout = vout/r
    irise = (vin-vout)*d/(l*fs)
    imin = current
    current=current+irise
    imax = current
    iave = (imax+imin)/2
    vout=iave*r
    time=time+ton
    t.append(time)
    i.append(current)
    v.append(vout)
    ifall = (-vout)*(1-d)/(l*fs)
    imax = current
    current=current+ifall
    imin = current
    iave = (imax+imin)/2
    vout=iave*r
    vout=current*r
    time=time+toff
    
    t.append(time)
    i.append(current)
    v.append(vout)



# In[44]:


mysignals = [i,v]

mysignals = [{'name': 'IL', 'x': t, 'y': i, 'color':'r', 'linewidth':1},
             {'name': 'Vout', 'x': t, 'y': v, 'color':'b', 'linewidth':1}]

fig, ax = plt.subplots()
for signal in mysignals:
    ax.plot(signal['x'], signal['y'], 
            color=signal['color'], 
            linewidth=signal['linewidth'],
            label=signal['name'])

# Enable legend
ax.legend()
ax.set_title("My graph")
plt.grid()
plt.show()


# In[ ]:





# In[ ]:




