#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2024/09/20 16:08:09

@author: Javiera Jilberto Vallejos 
'''
import meshio as io
import cheartio as chio
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

mesh = chio.read_mesh('mesh/cube', meshio=True)         # Read the mesh
# mesh.points is a numpy array with the coordinates of the nodes
# mesh.cells[0].data is a numpy array with the connectivity of the elements

displacement = chio.read_dfile('out/Disp-1.D')          # Read the displacement field

# 1. Use matplotlib to plot the nodes in the mesh (this might be helpful https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)
# 2. Use matplotlib to plot the deform nodal position. x = X + u, where X is the original position and u is the displacement field
# Extract the original nodal positions
X = mesh.points

# Extract the displacement field
u = displacement

# Compute the deformed nodal positions
x = X + u

# Create a 3D plot for the original nodal positions
fig = plt.figure()
ax = fig.add_subplot(121, projection='3d')
ax.scatter(X[:, 0], X[:, 1], X[:, 2], c='b', marker='o')
ax.set_title('Original Nodal Positions')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Create a 3D plot for the deformed nodal positions
ax2 = fig.add_subplot(122, projection='3d')
ax2.scatter(x[:, 0], x[:, 1], x[:, 2], c='r', marker='o')
ax2.set_title('Deformed Nodal Positions')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')

plt.show()