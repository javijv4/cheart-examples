#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Sat Jun 11 17:14:00 2022

@author: Javiera Jilberto Vallejos
"""

import argparse
import cheartio as chio
from tqdm import tqdm
import glob

def main(argv=None):
    parser = argparse.ArgumentParser(description='CHeart python functions.')
    parser.add_argument('-m', '--mesh', type=str, help='mesh file')
    parser.add_argument('-x', '--xfile', type=str, help='specify CH .X file (overrides -m)')
    parser.add_argument('-d', '--data', type=str, help='data file')
    parser.add_argument('-b', '--boundary', type=str, help='data file')
    parser.add_argument('-f', '--fibers', type=str, help='fiber data file')
    parser.add_argument('-e', '--element', type=str, help='element type')
    parser.add_argument('-t', '--datatype', type=str, help='data type: points or cells')
    parser.add_argument('-vn', '--varname', type=str, help='variable name')
    parser.add_argument('-ts', '--timesteps', type=str, help='time range: st:et:inc')
    parser.add_argument('-st', '--start', type=int, help='start time step')
    parser.add_argument('-et', '--end', type=int, help='end time step')
    parser.add_argument('-inc', '--increment', type=int, help='increment time step')
    parser.add_argument('-inverse', '--inverse', action='store_true', help='flag for inverse mechanics')
    parser.add_argument('-res2', type=str, help='residual data')
    parser.add_argument('-intermediate', type=str, help='intermediate data')
    args = parser.parse_args()

    data = args.data if args.data else None
    elem = args.element if args.element else None
    dtype = args.datatype if args.datatype else 'points'
    vname = args.varname if args.varname else 'f'
    inverse = True if args.inverse else False

    st = args.start if args.start else None
    et = args.end if args.end else None
    increment = args.increment if args.increment else 1
    if args.timesteps:
        st, et, increment = [int(i) for i in args.timesteps.split(':')]

    if args.mesh and (not args.data) and (not args.fibers) and (not args.boundary) and (not args.res2) and (not args.intermediate):
        import pathlib
        path = pathlib.Path().resolve()
        print(path)
        chio.mesh_to_vtu(args.mesh, args.mesh + '.vtu', elem, args.xfile)

    elif args.boundary:
        chio.bfile_to_vtu(args.boundary, args.boundary + '_b.vtu', elem)

    elif args.fibers:
        extension = args.fibers.split('.')[-1]
        iname = args.fibers.replace('.' + extension, '')
        chio.fibers_to_vtu(args.fibers, iname + '.vtu', args.mesh, array_type=dtype, element=elem)

    elif args.data:

        if st is None:     # Only one file

            extension = args.data.split('.')[-1]
            iname = args.data.replace('.' + extension, '')
            chio.dfile_to_vtu(args.data, iname + '.vtu', mesh_path = args.mesh, var_name = vname,
                              element=elem, array_type=dtype, inverse=inverse, xfile=args.xfile)
        else:
            mesh = chio.read_mesh(args.mesh, meshio=True, element=elem)
            for i in tqdm(range(st, et+1, increment)):
                chio.dfile_to_vtu(args.data + '-%i' % i + '.D', args.data + '-%i' % i + '.vtu', mesh = mesh,
                                  var_name = vname, element=elem, array_type=dtype, inverse=inverse, xfile=args.xfile)
                if args.intermediate:
                    flist = glob.glob(fname + '.*.D')
                    for f in flist:
                        if args.intermediate is not None:
                            it = f.split('.')[1]
                            if int(it) > 0:
                                itd = args.intermediate + '-%i' % i + '.' + it + '.D'
                                var.append(itd)
                                name.append('itd')


    elif args.res2:
        mesh = chio.read_mesh(args.mesh, meshio=True, element=elem)
        for i in tqdm(range(st, et+1, increment)):
            fname = args.res2 + '-%i' % i
            flist = glob.glob(fname + '.*.res2')
            for f in flist:
                var = [f]
                name = ['res2']
                if data is not None:
                    d = args.data + '-%i' % i + '.D'
                    var.append(d)
                    name.append('d')
                if args.intermediate is not None:
                    it = f.split('.')[1]
                    if int(it) > 0:
                        itd = args.intermediate + '-%i' % i + '.' + it + '.D'
                        var.append(itd)
                        name.append('itd')

                chio.dfile_to_vtu(var, f + '.vtu', mesh = mesh,
                                  var_name = name, element=elem, array_type=dtype, inverse=inverse)

    elif args.intermediate:
        mesh = chio.read_mesh(args.mesh, meshio=True, element=elem)
        for i in tqdm(range(st, et+1, increment)):
            fname = args.intermediate + '-%i' % i
            flist = glob.glob(fname + '.*.D')
            for f in flist:
                var = [f]
                name = ['itd']
                if data is not None:
                    d = args.data + '-%i' % i + '.D'
                    var.append(d)
                    name.append('d')
                if args.intermediate is not None:
                    it = f.split('.')[1]
                    if int(it) > 0:
                        itd = args.intermediate + '-%i' % i + '.' + it + '.D'
                        var.append(itd)
                        name.append('itd')

                chio.dfile_to_vtu(var, f + '.vtu', mesh = mesh,
                                  var_name = name, element=elem, array_type=dtype, inverse=inverse)
