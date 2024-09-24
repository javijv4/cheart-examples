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

mesh = chio.read_mesh('mesh/cube_quad', meshio=True)         # Read the mesh
# mesh.points is a numpy array with the coordinates of the nodes
# mesh.cells[0].data is a numpy array with the connectivity of the elements


for i in range(1, 10):
    displacement = chio.read_dfile(f'out/Disp-{i}.D')          # Read the displacement field of the timestep
    mesh.point_data['displacement'] = displacement             # Add the displacement field to the mesh

    io.write(f'out/results-{i}.vtu', mesh)                        # Write the mesh with the displacement field
