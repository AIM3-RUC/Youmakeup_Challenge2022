# 4th PIC Challenge(MTVG & MDVC)

![logo](https://user-images.githubusercontent.com/24662157/165009909-074b8861-2223-43ba-8958-a47753e2f152.png)

This repo provides data downloads and baseline codes for the MTVG and MDVC sub-challenges in the [4th PIC Challenge](http://www.picdataset.com/) held in conjunction with [ACM MM 2022](https://2022.acmmm.org/).

If you have any questions, please contact us with youmakeup2022@163.com.

## 2022.6.10 Update!
**Test Set**

The test sets (MTVG_test.json & MDVC_test.json) for the two sub-challenges are released [here](https://drive.google.com/drive/folders/1FPDE-fiJjBKakTWfG_zeJhTsN7TFOrL4?usp=sharing) or [baidu_cloud(password:fn5f)](https://pan.baidu.com/s/1CSM8jOG1qHF1PiSuU4RwEg).

**Notice**

1) The old MTVG_release.json has been updated to MTVG_test.json

2) There is a key mistake in released I3D features: "yacTEParlnQ.npy" -> "yacTEParlnQ"

**Submission**

The submission website for MTVG challenge is [here](https://codalab.lisn.upsaclay.fr/competitions/5244).

The submission website for MDVC challenge is [here](https://codalab.lisn.upsaclay.fr/competitions/5102).

## Dataset  Introduction

YouMakeup is a large-scale multimodal instructional video dataset introduced in paper: [A Large-Scale Domain-Specific Multimodal Dataset for Fine-Grained Semantic Comprehension](https://www.aclweb.org/anthology/D19-1517/) (EMNLP2019).

It contains 2,800 videos from YouTube, spanning more than 420 hours in total. Each video is annotated with a sequence of steps, including temporal boundaries, grounded facial areas and natural language descriptions of each step.

<img width="954" alt="annotation" src="https://user-images.githubusercontent.com/55971939/164021317-04cc806a-3775-428c-a2f8-de80a55d0625.png">

For more details, you can find them in [YouMakeup Dataset](https://github.com/AIM3-RUC/YouMakeup).

In the PIC Challenges 2022 , we use the following data split. In order to avoid information leakage between the two sub-challenges, we divide the raw test set into two equal parts (containing 420 videos) as the new test set for MTVG and MDVC tasks respectively.

| \# Total | \# Train | \# Val | #Test | Video_len |
| -------- | -------- | ------ | ----- | --------- |
| 2800     | 1680     | 280    | 840   | 15s-1h    |



## Data Download
We provide the **pre-processed features** of raw videos using [c3d](https://arxiv.org/pdf/1412.0767v4.pdf) and [i3d](https://arxiv.org/pdf/1705.07750.pdf):

makeup_c3d_rgb_stride_1s.zip in: [google drive](https://drive.google.com/open?id=1gPGEYej70hKM6e-ftXI0RBNzn4AokMJ1) or [baidu_cloud](https://pan.baidu.com/s/1zaKC2BIw5ARmuYKybcAgDg)  password:hcw8

makeup_i3d_rgb_stride_1s.zip in: [google drive](https://drive.google.com/open?id=1cT5MKcmSmqS6xC_i2dI2wbJ3n7mdFh7o) or [baidu_cloud](https://pan.baidu.com/s/1OH_6LvUWvRTcPO33wcjZ_g)  password:nrlu 

(Optional) You can sign the [data license form](https://github.com/AIM3-RUC/Youmakeup_Challenge2022/blob/main/License%20Agreement.pdf) and send it to youmakeup2022@163.com and we will provide **extracted frames** (three frames per second) from the original 2800 videos.


**Annotations of videos** on train/val set are [here](https://drive.google.com/drive/folders/1vKTZh8eDAJYAtD6AYa7606xu74azd2iY?usp=sharing) or [BaiduNetDisk](https://pan.baidu.com/s/16JUlUoOHDqhuQy9W-0n2kg), password:31jo. An annotated example in  .json  file is as follows:
```
{
    "video_id": "-2FjMSPITn8", # video id
    "name": "Easy_Foundation_Routine_MakeupShayla--2FjMSPITn8.mp4", # video name
    "duration": 434.1003333333333, # total video length (second)
    "step": # annoated make-up steps
        {
          "1": { # step id
                 "query_idx": "1",  # unique id of (video, step query) for grounding task
                 "area": ["face"],  # involved face regions
                 "caption": "Apply foundation on face with brush", # step caption
                 "startime": "00:01:36", # start time of the step
                 "endtime": "00:02:49" # end time of the step
               },
          ...
         },
}
```

[Note]  The test set will be released at  June 10, 2022.



## Make-up Temporal Video Grounding Sub-Challenge

Given an untrimmed make-up video and a step query, the Make-up Temporal Video Grounding(MTVG) aims to localize the target make-up step in the video. This task requires models to align fine-grained video-text semantics and distinguish makeup steps with subtle difference.

![theme_mtvg](https://user-images.githubusercontent.com/24662157/165009554-5ef8101e-ca83-4964-93b0-26ce636a1508.jpg)


#### **Evaluation Metric**

We adopt “R@n, IoU=m” with n in {1} and m in {0.3, 0.5, 0.7} as evaluation metrics. It means that the percentage of at least one of the top-n results having Intersection over Union (IoU) with the ground truth larger than m.

The evaluation code used by the evaluation server can be found [here](https://github.com/AIM3-RUC/Youmakeup_Challenge2022/blob/main/MTVG/evaluation.py).



#### **Submission Format**

Participants need to submit the timestamp candidate for each (video, text query) input. The results should be stored in results.json, with the following format:

```
{
    "query_idx": [start_time, end_time],
     ...
}
```

[Note]  The submission site will be opened at June 10, 2022.



#### **Baseline**

For this task, we provided the code implementation from [Negative Sample Matters: A Renaissance of Metric Learning for Temporal Grounding](https://arxiv.org/pdf/2109.04872v2.pdf). 
To reproduce it, please refer to  the [MTVG folder](https://github.com/AIM3-RUC/YouMakeup_Challenge2022/tree/main/MTVG).

The results of the baseline model on val set is:

| Feature | R@1,IoU=0.3 | R@1,IoU=0.5 | R@1,IoU=0.7 | R@5,IoU=0.3 | R@5,IoU=0.5 | R@5,IoU=0.7 |
| ------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| C3D     | 33.47       | 23.05       | 11.78       | 63.28       | 48.88       | 25.07       |
| I3D     | 48.09       | 35.18       | 20.08       | 76.79       | 64.13       | 36.25       |

 



## Make-up Dense Video Captioning Sub-Challenge

Given an untrimmed make-up video, the Make-up Dense Video Captioning (MDVC) task aims to localize and describe a sequence of makeup steps in the target video.  This task requires models to both detect and describe fine-grained make-up events in a video.

![theme_mdvc](https://user-images.githubusercontent.com/24662157/165009974-967b783a-252a-4c0b-8622-98ade5794d0b.png)


#### **Evaluation Metric**

We measure both localizing and captioning ability of models. For localization performance, we compute the average precision (AP) across tIoU thresholds of {0.3,0.5,0.7,0.9}. For dense captioning performance, we calculate BLEU4, METEOR and CIDEr of the matched pairs between generated captions and the ground truth across tIOU thresholds of {0.3, 0.5, 0.7, 0.9}. 

The evaluation code used by the evaluation server can be [found here](http://github.com/ranjaykrishna/densevid_eval.git).



#### **Submission Format**

Please use the following JSON format when submitting your results.json for the challenge:

```
{
    "video_id": [
        {
            "sentence": sent,
            "timestamp": [st_time, end_time]
        },
		...
    ]
}
```

The submission site will be opened at June 10, 2022.



#### **Baseline**

We prepared the baseline for this task, it is from [End-to-End Dense Video Captioning with Parallel Decoding (ICCV 2021)](https://arxiv.org/abs/2108.07781). 
To reproduce it, please refer to the [MDVC folder](https://github.com/AIM3-RUC/YouMakeup_Challenge2022/tree/main/MDVC).

The results of the baseline model on val set is:

| Model      | Features | Recall | Precision | METEOR | BLEU4 | CIDEr |
| ---------- | -------- | ------ | --------- | ------ | ----- | ----- |
| PDVC_light | C3D      | 21.16  | 26.41     | 9.44   | 3.80  | 41.22 |
| PDVC_light | I3D      | 23.75  | 31.47     | 12.48  | 6.29  | 68.18 |


## Citation

```
@inproceedings{wang2019youmakeup,
  title={YouMakeup: A Large-Scale Domain-Specific Multimodal Dataset for Fine-Grained Semantic Comprehension},
  author={Wang, Weiying and Wang, Yongcheng and Chen, Shizhe and Jin, Qin},
  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  pages={5136--5146},
  year={2019}
}


@inproceedings{chen2020vqabaseline,
  title={YouMakeup VQA Challenge: Towards Fine-grained Action Understanding in Domain-Specific Videos,
  author={Chen, Shizhe and Wang, Weiying and Ruan, Ludan and Yao, Linli and Jin, Qin},
  year={2019}
}
```
