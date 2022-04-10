#!/usr/bin/env python3

import os
import glob
import argparse

import numpy
import ase.io

def is_upper_triangular(mat):
    """
    test if 3x3 matrix is upper triangular
    LAMMPS has a rule for cell matrix definition
    """
    def near0(x):
        """Test if a float is within .00001 of 0"""
        return abs(x) < 0.00001
    return near0(mat[1, 0]) and near0(mat[2, 0]) and near0(mat[2, 1])


def convert_cell(ase_cell):
    """
    Convert a parallel piped (forming right hand basis)
    to lower triangular matrix LAMMPS can accept. This
    function transposes cell matrix so the bases are column vectors
    """

    # if ase_cell is lower triangular, cell is upper tri-angular
    cell = numpy.matrix.transpose(ase_cell) 

    if not is_upper_triangular(cell):
        # rotate bases into triangular matrix
        tri_mat = numpy.zeros((3, 3))
        A = cell[:, 0]
        B = cell[:, 1]
        C = cell[:, 2]
        tri_mat[0, 0] = numpy.linalg.norm(A)
        Ahat = A / numpy.linalg.norm(A)
        AxBhat = numpy.cross(A, B) / numpy.linalg.norm(numpy.cross(A, B))
        tri_mat[0, 1] = numpy.dot(B, Ahat)
        tri_mat[1, 1] = numpy.linalg.norm(numpy.cross(Ahat, B))
        tri_mat[0, 2] = numpy.dot(C, Ahat)
        tri_mat[1, 2] = numpy.dot(C, numpy.cross(AxBhat, Ahat))
        tri_mat[2, 2] = numpy.linalg.norm(numpy.dot(C, AxBhat))

        # create and save the transformation for coordinates
        volume = numpy.linalg.det(ase_cell)
        trans = numpy.array([numpy.cross(B, C), numpy.cross(C, A), numpy.cross(A, B)])
        trans = trans / volume
        coord_transform = tri_mat * trans
        return tri_mat.T # return the lower-tri-angular
    else:
        return ase_cell

def random_range(a, b, ndata=1):
    data = numpy.random.random(ndata) * (b - a) + a
    return data

def gen_random_disturb(dmax, a, b, dstyle='uniform'):
    d0 = numpy.random.rand(3) * (b - a) + a
    dnorm = numpy.linalg.norm(d0)
    if dstyle == 'normal':
        dmax = numpy.random.standard_normal(0, 0.5) * dmax
    elif dstyle == 'constant':
        pass
    else:
        # use if we just wanna a disturb in a range of [0, dmax),
        dmax = numpy.random.random() * dmax
    dr = dmax / dnorm * d0
    return dr

def gen_random_emat(etmax, diag=0):
    if numpy.abs(etmax) >= 1e-6:
        e = random_range(-etmax, etmax, 6)
    else:
        e = numpy.zeros(6)
    if diag != 0:
        # isotropic behavior
        e[3], e[4], e[5] = 0, 0, 0
    emat = numpy.array(
        [[e[0], 0.5 * e[5], 0.5 * e[4]],
         [0.5 * e[5], e[1], 0.5 * e[3]],
         [0.5 * e[4], 0.5 * e[3], e[2]]]
    )
    emat = emat + numpy.eye(3)
    return emat


def create_disturbs_ase_dev(fin, nfile, dmax=1.0, etmax=0.1, ofmt="lmp", dstyle='uniform', write_d=False, diag=0):
    # removing the exists files
    flist = glob.glob('*.' + ofmt)
    for f in flist:
        os.remove(f)

    # read-in by ase
    atoms = ase.io.read(fin)
    natoms = atoms.get_number_of_atoms()
    cell0 = atoms.get_cell()

    # creat nfile ofmt files.
    for fid in range(nfile):
        # Use copy(), otherwise it will modify the inumpyut atoms every time.
        atoms_d = atoms.copy()

        # random flux for atomic positions
        dpos = numpy.zeros((natoms, 3))
        for i in range(natoms):
            dr = gen_random_disturb(dmax, -0.5, 0.5, dstyle)
            dpos[i, :] = dr

        # random flux for volumes
        cell = numpy.dot(cell0, gen_random_emat(etmax, diag))
        atoms_d.set_cell(cell, scale_atoms=True)

        # determine new cell & atomic positions randomiziations
        pos = atoms_d.get_positions() + dpos
        atoms_d.set_positions(pos)

        # pre-converting the Atoms to be in low tri-angular cell matrix
        cell_new = convert_cell(cell)
        #pos_new = io_lammps.convert_positions(pos, cell, cell_new)
        atoms_d.set_cell(cell_new, scale_atoms=True)
        # atoms_d.set_positions(pos_new)

        # Writing it
        fout = 'POSCAR' + f"{fid:03d}"
        print("Creating %s ..." % fout)
        ase.io.write(fout, atoms_d, ofmt)
    return


