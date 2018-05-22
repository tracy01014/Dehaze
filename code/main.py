# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:46:34 2018

@author: NBME
"""

from DarkChannelRecover import getRecoverScene
from PIL import Image
import matplotlib.pyplot as plt
import scipy.misc
import numpy as np

#%% implement
input_filename = '5.jpeg'
input_filepath = '../images/'+input_filename
img = np.asarray(Image.open(input_filepath))
# omega:去霧程度，越小去霧越不明顯 / to:最小透射率值 / blockSize:越大去霧效果越不明顯
sceneRadiance = getRecoverScene(img, omega=0.96, t0=0.1, blockSize=3 ,meanMode=False, percent=0.001)
plt.figure()
plt.imshow(img)
plt.figure()
plt.imshow(sceneRadiance)
scipy.misc.toimage(sceneRadiance).save('../result/'+input_filename.split('.')[0]+'output_omega%0.2f_t0%0.1f_blockSize%d.jpg')
