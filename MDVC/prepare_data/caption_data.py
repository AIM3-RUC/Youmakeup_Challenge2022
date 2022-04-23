# %%
import json
import os
import time

# %%

train_dir = "../YouMakeup_data/train"
val_dir = "../YouMakeup_data/val"

output_dir = "../data/youMakeUp/captiondata"

# %%
def savejson(data, path):
    with open(path, "w") as f:
        json.dump(data, f)
    f.close()

def toSec(timeStr):
    t = time.strptime(timeStr, "%H:%M:%S")
    return t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec

def captiondata_modify(steps):
    modify_data = {} #{video_name(str): caption_info(dict)}
    for i, step in enumerate(steps):
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

# %%
with open(train_dir+"/steps.json", "r") as f:
    train_steps = json.load(f)
f.close()

# %%
with open(val_dir+"/dev_step.json", "r") as f:
    val_steps = json.load(f)
f.close()

# %%
train_data = captiondata_modify(train_steps)
savejson(train_data, os.path.join(output_dir, "train.json"))

# %%
val_data = captiondata_modify(val_steps)
savejson(val_data, os.path.join(output_dir, "val.json"))

# %%
def generate_paragraph(steps):
    paras = {}
    for i, step in enumerate(steps):
        name = step["video_id"]
        para = ""
        for k, v in step["step"].items():
            v["caption"] = v["caption"].replace("  "," ").strip(' ')
            if v["caption"][-1] == '.':
                para = para + v["caption"]
            else:
                para = para + v["caption"] + '. '
        paras[name] = para
    return paras


train_para = generate_paragraph(train_steps)
val_para = generate_paragraph(val_steps)

if os.path.exists(os.path.join(output_dir, "para"))==False:
    os.mkdir(os.path.join(output_dir, "para"))

savejson(train_para, os.path.join(output_dir, "para/train_para.json"))
savejson(val_para, os.path.join(output_dir, "para/val_para.json"))