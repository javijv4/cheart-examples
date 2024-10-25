#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2024/09/20 16:08:09

@author: Javiera Jilberto Vallejos 
'''
import meshio as io
import cheartio as chio
import numpy as np

mesh = chio.read_mesh('mesh/cube', meshio=True)
mesh_quad = chio.read_mesh('mesh/cube_quad', meshio=True)

map_quad = chio.map_between_meshes(mesh_quad, mesh)

fibers = chio.read_dfile('out/fibers-1.D')
mesh.point_data['fibers'] = fibers[:,0:3]
fibers = fibers[:,0:3]

et = 100

disp = chio.read_dfile(f'out/Disp-{et}.D')

# Calculate long axis elongation
apex_id = 0
base_id = 1

disp_apex = disp[apex_id]
disp_base = disp[base_id]

x_apex = mesh.points[apex_id]
x_base = mesh.points[base_id]

# Calculate torsion
adjacent_id = 2
disp_adjacent = disp[adjacent_id]



