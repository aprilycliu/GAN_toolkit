import json
import os
import numpy as np

'''create label json file for conditional model of StyleGAN+DiffAugment
example:
{"labels": [["00017154.jpg", 1], ["00000414.jpg", 1], ["00017342.jpg", 1],....}
'''

train_dir=r'/Task2/'

#Two classes, one for with tool, another for without tool
classes=['256-with-tool-small', '256-without-tool-small']

filename=[]
for i in range(len(classes)):
    for file in os.listdir(os.path.join(train_dir, classes[i])):
        filename.append(os.path.join(classes[i], file))

labels=[]
for i in range(len(filename)):
    #modified by case, to capture the key words for two classes
    if filename[i][:13]=='256-with-tool':
        labels.append(1)
    else:
        labels.append(0)

arr = np.char.replace(filename, '256-with-tool-small/', '')
arr = np.char.replace(arr, '256-without-tool-small/', '')

items=[]
for i in range(len(labels)):
    items.append([list(arr)[i], labels[i]])

js = {"labels": items}
with open("dataset.json", "w") as outfile:
    json.dump(js, outfile)
