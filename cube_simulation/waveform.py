#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2024/10/10 18:33:39

@author: Javiera Jilberto Vallejos 
'''

import numpy as np
import matplotlib.pyplot as plt


pres_value = 10.0
act_value = 10

# Time
t = np.linspace(0, 1, 1000)

# Pressure traces
pressure1 = ( np.sin(2 * np.pi * (t-0.25)) )*0.025 + 0.025
pressure2_0 = ( np.sin(2 * np.pi * (t-0.25)/0.4) )*0.1 
pressure2 = pressure2_0 * (pressure2_0 > 0) * (t > 0.2) * (t < 0.5) * (pressure2_0 > pressure1)
pressure3 = np.sin(2 * np.pi * (t-0.35)/0.8) 
pressure_norm = pressure1*(pressure1 > pressure2)*(pressure1 > pressure3) \
        + pressure2*(pressure2 > pressure1)*(pressure2 > pressure3) \
        + pressure3*(pressure3 > pressure1)*(pressure3 > pressure2)

# Normalizing pressure
pressure = pressure_norm * pres_value

plt.figure(1, clear=True)
plt.plot(t, pressure1, label='pressure trace 1')
plt.plot(t, pressure2, label='pressure trace 2')
plt.plot(t, pressure3, label='pressure trace 3')
plt.plot(t, pressure_norm, 'k.', lw = 2, label='pressure trace')
plt.xlabel('time (s)')
plt.ylabel('pressure (kPa)')
plt.legend()
plt.savefig('pressure_waveform.png', bbox_inches='tight')

# Activation traces
act_0 = np.sin(2 * np.pi * (t-0.35)/0.8) 
act_1 = act_0 * (act_0 > 0) * (t < 0.8)

# Normalizing activation
act = act_1 * act_value

plt.figure(1, clear=True)
plt.plot(t, act, 'r', lw = 2, label='activation trace')
plt.xlabel('time (s)')
plt.ylabel('activation [kPa]')
plt.legend()
plt.savefig('activation_waveform.png', bbox_inches='tight')