#!\usr\bin\python3
# -*- coding: utf-8 -*-
'''
	Created on Nov. 2019
	
	Electric Dynamic Chapter 5

	@author: ZYW @ BNU
'''
from moviepy.editor import *

final_path = './videos/finalVideo.mp4'

clip = (VideoFileClip(final_path).subclip(0,6.28).resize(0.2))

clip.write_gif("dipole_E_field.gif") 
