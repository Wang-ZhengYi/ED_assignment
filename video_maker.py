#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	Created on Sept 2019

	Elecetric Dynmatic Chapter 2
	
	@author: Z.Y.Wang @ BNU
	'''

import numpy as np
import os
import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
from moviepy.editor import *
from moviepy.audio.fx import all
from PIL import Image

fps = 60 
save_path = './videos/saveVideo.mp4'
img_path='./figures/'
frames = len(os.listdir(img_path))
time = frames/fps
music_start = 0



img_list=os.listdir(img_path)
img_list.sort()
img_list.sort(key = lambda x: int(x[3:-4]))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
image = Image.open('./figures/' + img_list[0])
videoWriter = cv2.VideoWriter(save_path,fourcc,fps,image.size)
print(image.size)
for i in range(frames):
    img_name=img_path+img_list[i]
    frame = cv2.imread(img_name)
    videoWriter.write(frame)

videoWriter.release()
exit()