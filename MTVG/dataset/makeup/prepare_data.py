import json
import os
import time

def savejson(data, path):
    with open(path, "w") as f:
        json.dump(data, f)
    f.close()

def toSec(timeStr):
    t = time.strptime(timeStr, "%H:%M:%S")
    return t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec

def captiondata_modify(steps):
    modify_data = {} #{video_name(str): caption_info(dict)}
    for i, step in enumerate(steps[0]):
        tmp_dic = {} #keys = ["duration", "timestamps", "sentences"]
        name = step["video_id"]
        #duration
        tmp_dic["duration"] = step["duration"]
        #timestamps & sentences
        tmp_dic["timestamps"] = []
        tmp_dic["sentences"] = []
        for key in step["step"].keys():
            #sentences
            tmp_dic["sentences"].append(step["step"][key]["caption"])
            #timestamps
            startime = toSec(step['step'][key]["startime"])
            endtime = toSec(step['step'][key]["endtime"])
            tmp_dic["timestamps"].append([startime, endtime])

        modify_data[name] = tmp_dic
    return modify_data

with open("./dataset/makeup/steps.json", "r") as f:
    train_steps = f.readlines()
f.close()
train_steps = [json.loads(x) for x in train_steps]

with open("./dataset/makeup/dev_step.json", "r") as f:
    val_steps = f.readlines()
f.close()
val_steps = [json.loads(x) for x in val_steps]

train_data = captiondata_modify(train_steps)
savejson(train_data, os.path.join("./dataset/makeup/makeup_train.json"))

val_data = captiondata_modify(val_steps)
savejson(val_data, os.path.join("./dataset/makeup/makeup_test.json"))
