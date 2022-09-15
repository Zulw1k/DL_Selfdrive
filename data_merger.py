import numpy as np
import os


path = ''


def data_merger(path):
    traindata = np.zeros((1000,2))
    for i in os.listdir(path):
      data = np.load(path+i, allow_pickle=True)
      traindata = np.append(traindata, data, axis=0)
    traindata = traindata[1000:,:]
    np.save('',traindata)


data_merger(path)





