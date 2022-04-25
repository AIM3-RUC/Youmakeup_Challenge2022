# YouMakeup MDVC Baseline

## Introduction
This is the baseline for the MDVC sub-challenge of [PIC Challenge](http://www.picdataset.com/) to generate dense video captions. We applied [PDVC](https://github.com/ttengwang/PDVC.git) to [YouMakeup](https://github.com/AIM3-RUC/YouMakeup) dataset. You can get the details of the model from the paper: [End-to-End Dense Video Captioning with Parallel Decoding (ICCV 2021)](https://arxiv.org/abs/2108.07781)

## Preparation
Environment: <br>
Linux,  GCC>=5.4, CUDA >= 9.2,
Python>=3.7, PyTorch>=1.5.1,
JDK 1.8

1. Create vitual environment by conda
```bash
conda create -n PDVC python=3.7
source activate PDVC
conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=9.2 -c pytorch
conda install ffmpeg
pip install -r requirement.txt
```

2. Compile the deformable attention layer (requires GCC >= 5.4). 
```bash
cd pdvc/ops
sh make.sh
```
3. Download video feature

* c3d_rgb: [google drive](https://drive.google.com/open?id=1gPGEYej70hKM6e-ftXI0RBNzn4AokMJ1) or [baidu_cloud](https://pan.baidu.com/s/1zaKC2BIw5ARmuYKybcAgDg)  password:hcw8

* i3d_rgb: [google drive](https://drive.google.com/open?id=1cT5MKcmSmqS6xC_i2dI2wbJ3n7mdFh7o) or [baidu_cloud](https://pan.baidu.com/s/1OH_6LvUWvRTcPO33wcjZ_g)  password:nrlu

* The hdf5 files should be put into folder "./YouMakeup_data".
Then extract features from hdf5

```bash
#extract features from hdf5.
cd ./prepare_data
python feature.py
```

4. Prepare caption data
```bash
#Modify the format of the raw caption data to the format required by the model.
cd ./prepare_data
python caption_data.py
python build_vocab.py
```
## Training and Validation

* Training
```
#specify the config file
config_path=cfgs/youMakeUp_c3d_pdvcl.yml
GPU_ID=0
python train.py --cfg_path ${config_path} --gpu_id ${GPU_ID}
# The script will evaluate the model for every epoch. The results and logs are saved in `./save`.
```

* Evaluation
```
# specify the folder to be evaluated
eval_folder=youMakeUp_c3d_pdvcl
eval_caption_file=data/youMakeUp/captiondata/val.json
GPU_ID=0
python eval.py --eval_folder ${eval_folder} --eval_transformer_input_type queries --gpu_id ${GPU_ID} --eval_caption_file ${eval_caption_file}
```

## Performance

|  Model | Features | Recall | Precision | METEOR | Bleu_4 | CIDEr |
|  ----  |  ----   |  ----  |  ----  |  ----  |   ----  |  ----  |
| PDVC_light | C3D | 21.16 | 26.41 | 9.44 | 3.80 | 41.22 |
| PDVC_light | I3D | 23.75 | 31.47 | 12.48 | 6.29 | 68.18 |

### Checkpoints are available
* [google drive](https://drive.google.com/file/d/1nJfwikWC0atUwJQptiJq-W4LFpmldewh/view?usp=sharing) 
* [baidu_cloud](https://pan.baidu.com/s/1D-TPQtDxcQwQBlk_dXiZxg) password:18sk
