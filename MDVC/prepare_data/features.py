# %%
import os
import h5py
import numpy as np

# %%
c3d_path = "../YouMakeup_data/makeup_c3d_rgb_stride_1s.hdf5"
i3d_path = "../YouMakeup_data/makeup_i3d_rgb_stride_1s.hdf5"
c3d_output_dir = "../data/youMakeUp/features/c3d"
i3d_output_dir = "../data/youMakeUp/features/i3d"

# %%
def unzip(path, output_dir, ft_name):
    h5 = h5py.File(path)
    if os.path.exists(output_dir)==False:
        os.mkdir(output_dir)
    for key in h5.keys():
        if ft_name=='c3d_rgb_features':
            output_path = os.path.join(output_dir, key+'.npy')
        else:
            output_path = os.path.join(output_dir, key+'_rgb.npy')
        if os.path.exists(output_path):
            continue
        v = np.array(h5[key][ft_name]).astype(np.float32)
        np.save(output_path, v)

# %%
unzip(c3d_path, c3d_output_dir, 'c3d_rgb_features')

# %%
unzip(i3d_path, i3d_output_dir, 'i3d_rgb_features')


