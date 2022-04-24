# find all configs in configs/
config_file=configs/pool_makeup_i3d.yaml
# the dir of the saved weight
weight_dir=outputs/pool_makeup_i3d
# select weight to evaluate
weight_file=outputs/pool_makeup_i3d/pool_model_20e.pth
# test batch size
batch_size=16
# set your gpu id
gpus=0
# number of gpus
gpun=1
# please modify it with different value (e.g., 127.0.0.2, 29502) when you run multi mmn task on the same machine
master_addr=127.0.0.2
master_port=29578

CUDA_VISIBLE_DEVICES=$gpus python -m torch.distributed.launch \
--nproc_per_node=$gpun --master_addr $master_addr --master_port $master_port \
test_net.py --config-file $config_file --ckpt $weight_file OUTPUT_DIR $weight_dir TEST.BATCH_SIZE $batch_size

