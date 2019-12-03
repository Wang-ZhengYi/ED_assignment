#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Created on Sept 2019

    Elecetric Dynmatic Chapter 5
    
    @author: Z.Y.Wang @ BNU
    '''

import numpy as np
import os
from matplotlib import font_manager as fm, rcParams
import cv2
from cv2 import VideoWriter,VideoWriter_fourcc,imread,resize
from moviepy.editor import *
from moviepy.audio.fx import all
from PIL import Image

def vframe(img_path,save_path,fps,coding):
	frames = len(os.listdir(img_path))
	img_list=os.listdir(img_path)
	img_list.sort()
	img_list.sort(key = lambda x: int(x[3:-4]))
	fourcc = cv2.VideoWriter_fourcc(*coding)
	image = Image.open(img_path + img_list[0])
	videoWriter = cv2.VideoWriter(save_path,fourcc,fps,image.size)
	for i in range(frames):
	    img_name=img_path+img_list[i]
	    frame = cv2.imread(img_name)
	    videoWriter.write(frame)
	return videoWriter.release()

def veditor(fps,adding,font,music_start,music_path,load_path,final_path):
	time = VideoFileClip(load_path).duration
	audio_clip = AudioFileClip(music_path).subclip(music_start,music_start+time)
	background_clip1 = VideoFileClip(load_path,target_resolution=(2400,3200)).subclip(0,time)

	text_clip1 = TextClip(adding[0], fontsize = adding[2], color = 'black',font = font)
	text_clip0 = TextClip(adding[1], fontsize = adding[3], color = 'black',font = font)
	
	text_clip1 = text_clip1.set_position('bottom')
	text_clip0 = text_clip0.set_position('top')

	text_clip1 = text_clip1.set_duration(time).set_audio(audio_clip)
	text_clip0 = text_clip0.set_duration(time).set_audio(audio_clip)

	return CompositeVideoClip([background_clip1,text_clip1,text_clip0]).write_videofile(final_path,codec = 'libx264', fps = fps)