#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on 2024/09/20 10:08:51

@author: Javiera Jilberto Vallejos 
'''

import meshio as io
import pygmsh
import cheartio as chio
import numpy as np


def get_surface_mesh(mesh):
    ien = mesh.cells[0].data

    if ien.shape[1] == 3:   # Assuming tetra
        array = np.array([[0,1],[1,2],[2,0]])
        nelems = np.repeat(np.arange(ien.shape[0]),3)
        faces = np.vstack(ien[:,array])
        sort_faces = np.sort(faces,axis=1)

        f, i, c = np.unique(sort_faces, axis=0, return_counts=True, return_index=True)
        ind = i[np.where(c==1)[0]]
        bfaces = faces[ind]
        belem = nelems[ind]


    elif ien.shape[1] == 4:   # Assuming tetra
        array = np.array([[0,1,2],[1,2,3],[0,1,3],[2,0,3]])
        nelems = np.repeat(np.arange(ien.shape[0]),4)
        faces = np.vstack(ien[:,array])
        sort_faces = np.sort(faces,axis=1)

        f, i, c = np.unique(sort_faces, axis=0, return_counts=True, return_index=True)
        ind = i[np.where(c==1)[0]]
        bfaces = faces[ind]
        belem = nelems[ind]

    elif ien.shape[1] == 27:   # Assuming hex27
        array = np.array([[0,1,5,4,8,17,12,16,22],
                          [1,2,6,5,9,18,13,17,21],
                          [2,3,7,6,10,19,14,18,23],
                          [3,0,4,7,11,16,15,19,20],
                          [0,1,2,3,8,9,10,11,24],
                          [4,5,6,7,12,13,14,15,25]])
        nelems = np.repeat(np.arange(ien.shape[0]),6)
        faces = np.vstack(ien[:,array])
        sort_faces = np.sort(faces,axis=1)

        f, i, c = np.unique(sort_faces, axis=0, return_counts=True, return_index=True)
        ind = i[np.where(c==1)[0]]
        bfaces = faces[ind]
        belem = nelems[ind]
        
    return belem, bfaces

x0, y0, z0 = -3, -3, -3
x1, y1, z1 = 3, 3, 3

with pygmsh.geo.Geometry() as geom:
    geom.add_box(x0, x1, y0, y1, z0, z1, mesh_size=1)
    mesh = geom.generate_mesh()
    
vol_mesh = io.Mesh(points=mesh.points, cells={"tetra": mesh.cells_dict["tetra"]})

surf_mesh = get_surface_mesh(vol_mesh)
belem, bfaces = surf_mesh

xyz = vol_mesh.points
tri_points = xyz[bfaces]

# Mark faces
mark_faces = np.zeros(bfaces.shape[0])

# Face 1: x = x0
face1 = np.where(np.all(np.isclose(tri_points[:,:,0], x0), axis=1))[0]
mark_faces[face1] = 1

# Face 2: x = x1
face2 = np.where(np.all(np.isclose(tri_points[:,:,0], x1), axis=1))[0]
mark_faces[face2] = 2

# Face 3: y = y0
face3 = np.where(np.all(np.isclose(tri_points[:,:,1], y0), axis=1))[0]
mark_faces[face3] = 3

# Face 4: y = y1
face4 = np.where(np.all(np.isclose(tri_points[:,:,1], y1), axis=1))[0]
mark_faces[face4] = 4

# Face 5: z = z0
face5 = np.where(np.all(np.isclose(tri_points[:,:,2], z0), axis=1))[0]
mark_faces[face5] = 5

# Face 6: z = z1
face6 = np.where(np.all(np.isclose(tri_points[:,:,2], z1), axis=1))[0]
mark_faces[face6] = 6

bdata = np.column_stack((belem, bfaces, mark_faces))

chio.write_mesh('cube', xyz, vol_mesh.cells_dict['tetra'])
chio.write_bfile('cube', bdata)