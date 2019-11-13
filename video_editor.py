#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Created on Sept 2019

    Elecetric Dynmatic Chapter 2
    
    @author: Z.Y.Wang @ BNU
    '''

import numpy as np
import os
from moviepy.editor import *
from moviepy.audio.fx import all
from matplotlib import font_manager as fm, rcParams
from PIL import Image

fps = 60 
save_path = './videos/saveVideo.mp4'
final_path = './videos/finalVideo.mp4'
img_path='./figures/'
frames = len(os.listdir(img_path))
time = frames/fps
music_start = 7

fpath = os.path.join(rcParams["datapath"], "fonts/ttf/cmr10.ttf")
FONT_URL = fm.FontProperties(fname=fpath)

FONT_URL = 'fonts/ttf/cmr10.ttf'
img_list=os.listdir(img_path)
image = Image.open('./figures/' + img_list[0])


audio_clip = AudioFileClip('./music/DIDIDI.mp3').subclip(music_start,music_start+time)
background_clip1 = VideoFileClip(save_path,target_resolution=(2400,3200)).subclip(0,10)

text_clip1 = TextClip('GitHub:Wang-ZhengYi', fontsize = 100, color = 'black',font = FONT_URL)
text_clip0 = TextClip('E field of a dipole radiation', fontsize = 100, color = 'black',font = FONT_URL)

text_clip1 = text_clip1.set_position('bottom')
text_clip0 = text_clip0.set_position('top')

text_clip1 = text_clip1.set_duration(time).set_audio(audio_clip)
text_clip0 = text_clip0.set_duration(time).set_audio(audio_clip)

CompositeVideoClip([background_clip1,text_clip1,text_clip0]).write_videofile(final_path,codec = 'libx264', fps = fps)