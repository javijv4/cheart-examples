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

fibers = chio.read_dfile('out/Fibers-1.D')
mesh.point_data['fibers'] = fibers[:,0:3]

for i in range(1, 11):
    disp = chio.read_dfile(f'out/Disp-{i}.D')
    mesh.point_data['disp'] = disp[map_quad]

    fibstretch = chio.read_dfile(f'out/FibStretch-{i}.D')
    mesh.point_data['fibstretch'] = fibstretch

    io.write(f'out/results-{i}.vtu', mesh)

