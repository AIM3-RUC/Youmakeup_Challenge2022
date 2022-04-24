"""Centralized catalog of paths."""
import os

class DatasetCatalog(object):
    DATA_DIR = ""

    DATASETS = {
        "makeup_train":{
            "video_dir": "./dataset/makeup/videos",
            "ann_file": "./dataset/makeup/makeup_train.json",
            "feat_file": "./dataset/makeup/makeup_i3d_rgb_stride_1.hdf5",
        },
        "makeup_val":{
            "video_dir": "./dataset/makeup/videos",
            "ann_file": "./dataset/makeup/makeup_val.json",
            "feat_file": "./dataset/makeup/makeup_i3d_rgb_stride_1.hdf5",
        },
        "makeup_test":{
            "video_dir": "./dataset/makeup/videos",
            "ann_file": "./dataset/makeup/makeup_test.json",
            "feat_file": "./dataset/makeup/makeup_i3d_rgb_stride_1.hdf5",
        }
    }

    @staticmethod
    def get(name):
        data_dir = DatasetCatalog.DATA_DIR
        attrs = DatasetCatalog.DATASETS[name]
        args = dict(
            #root=os.path.join(data_dir, attrs["video_dir"]),
            ann_file=os.path.join(data_dir, attrs["ann_file"]),
            feat_file=os.path.join(data_dir, attrs["feat_file"]),
        )
        if "tacos" in name:
            return dict(
                factory="TACoSDataset",
                args=args,
            )
        elif "activitynet" in name:
            return dict(
                factory = "ActivityNetDataset",
                args = args
            )
        elif "charades" in name:
            return dict(
                factory = "CharadesDataset",
                args = args
            )
        elif "makeup" in name:
            return dict(
                factory = "MakeupDataset",
                args = args
            )
        raise RuntimeError("Dataset not available: {}".format(name))

