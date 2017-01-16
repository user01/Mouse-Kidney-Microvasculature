
print("Starting Image Process")

import os
import numpy as np
from skimage import measure
import matplotlib.image as mpimg
from stl import mesh


def downsample_array(nn, side_start, chunk_size):
    """Downsample a square numpy array"""
    nn1 = np.resize(nn, (int(side_start**2 / chunk_size), chunk_size))
    nn2 = np.sum(nn1, axis=1)
    nn3 = np.resize(nn2, (side_start, int(side_start / chunk_size)))
    nn4 = np.transpose(nn3)
    nn5 = np.hstack(nn4)
    nn6 = np.resize(
        nn5, (int(side_start**2 / chunk_size**2), chunk_size))
    nn7 = np.sum(nn6, axis=1)
    nn8 = np.resize(nn7 / chunk_size**2, (int(side_start /
                                              chunk_size), int(side_start / chunk_size)))
    return nn8


def image_load(filename):
    data = mpimg.imread(os.path.join(
        'ii-3001-1-mouse-kidney_1GV', 'source', filename))
    return downsample_array(data, 2048, 8)


faces = sorted(os.listdir(os.path.join(
    'ii-3001-1-mouse-kidney_1GV', 'source')))

images = np.array(list(map(image_load, faces)))

verts, faces = measure.marching_cubes(images, 0.5, spacing=(0.7*8, 0.7*8, 6.0))



new_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        new_mesh.vectors[i][j] = verts[f[j],:]

new_mesh.save('simple.stl')
