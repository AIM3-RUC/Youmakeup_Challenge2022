import json
import os
import time
import sys

def iou(A, B):
    max0 = max(toSec(A[0]), toSec(B[0]))
    min0 = min(toSec(A[0]), toSec(B[0]))
    max1 = max(toSec(A[1]), toSec(B[1]))
    min1 = min(toSec(A[1]), toSec(B[1]))
    
    return max(min1 - max0, 0) / (max1 - min0)

def toSec(timeStr):
    t = time.strptime(timeStr, "%H:%M:%S")
    return t.tm_hour * 3600 + t.tm_min * 60 + t.tm_sec

def captiondata_modify(steps):
    modify_data = {}
    for i, step in enumerate(steps[0]):
        for key in step["step"].keys():
            name = step["step"][key]["query_idx"]
            modify_data[name] = [[step['step'][key]["startime"], step['step'][key]["endtime"]]]
        
    return modify_data

arg1 = sys.argv[1]
arg2 = sys.argv[2]
with open(arg1, "r") as f:
    answer = f.read()
f.close()
answer = json.loads(answer)
print(answer)

with open(arg2, "r") as f:
    submission = f.read()
f.close()
submission = json.loads(submission)

num = len(answer)
Result = {0.3:0, 0.5:0, 0.7:0}
for c_iou in [0.3, 0.5, 0.7]:
    for key in answer.keys():
        if(iou(answer[key], submission[key]) >= c_iou):
            Result[c_iou] = Result[c_iou] + 1
print("IOU 0.3: {0}\nIOU 0.5: {1}\nIOU 0.7: {2}".format(Result[0.3]*100/num, Result[0.5]*100/num, Result[0.7]*100/num))
