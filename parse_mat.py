import scipy.io as sio


def parse(file_name):
    mat = sio.loadmat(file_name)
    return mat
