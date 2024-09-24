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

strain = np.zeros([10, mesh.points.shape[0]])
for i in range(1, 11):
    fibstrain = chio.read_dfile(f'out/FibStrain-{i}.D')
    mesh.point_data['fibstrain'] = fibstrain
    strain[i-1] = fibstrain

diff_strain = np.diff(strain, axis=0)/0.1
diff_strain = np.concatenate((np.zeros([1, mesh.points.shape[0]]), diff_strain), axis=0)

for i in range(1, 11):
    disp = chio.read_dfile(f'out/Disp-{i}.D')
    mesh.point_data['disp'] = disp[map_quad]

    fibstrain = chio.read_dfile(f'out/FibStrain-{i}.D')
    mesh.point_data['fibstrain'] = fibstrain
    mesh.point_data['diff_strain'] = diff_strain[i-1]

    fibstrainrate = chio.read_dfile(f'out/FibStrainRate-{i}.D')
    mesh.point_data['fibstrainrate'] = fibstrainrate


    io.write(f'out/results-{i}.vtu', mesh)

