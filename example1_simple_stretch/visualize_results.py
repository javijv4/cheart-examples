#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2024/09/20 16:08:09

@author: Javiera Jilberto Vallejos 
'''
import meshio as io
import cheartio as chio
import numpy as np
import matplotlib.pyplot as plt

mesh = chio.read_mesh('mesh/cube', meshio=True)         # Read the mesh
# mesh.points is a numpy array with the coordinates of the nodes
# mesh.cells[0].data is a numpy array with the connectivity of the elements

displacement = chio.read_dfile('out/Disp-1.D')          # Read the displacement field

# 1. Use matplotlib to plot the nodes in the mesh (this might be helpful https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html)
# 2. Use matplotlib to plot the deform nodal position. x = X + u, where X is the original position and u is the displacement field
