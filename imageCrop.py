import pyscreenshot as ImageGrab
import pygame
import os
import keyboard
import sys
from PIL import Image
import time


projectName = input("Project Name: ")

screenshot_dimensions = [[512,512],[1000,250],[800,450],[800,450]]
AR_dimensions = [[10,10],[20,5],[16,9],[16,9]]
names = ['Thumbnail','Banner','Screenshot1','Screenshot2']

for i in range(4):

	while True:
		if keyboard.read_key() == "`":
			break

	im=ImageGrab.grab(bbox=(0,0,1920,1080)) # X1,Y1,X2,Y2
	im.save("images/tempscreenshot.png")

	pygame.init()
	clock = pygame.time.Clock()
	os.environ['SDL_VIDEO_CENTERED'] = '1'
	win = pygame.display.set_mode((1920,1080), pygame.NOFRAME)

	tempscreenshot = pygame.image.load('images/tempscreenshot.png')

	factorDimensions = AR_dimensions[i]
	factor = 50
	factorScale = 2

	time_start = time.time()

	exit = False
	while True:
		mouseX, mouseY = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1 and time.time() - time_start > 2:
					top = mouseY-factorDimensions[1]*factor/2
					bottom = (mouseY+factorDimensions[1]*factor/2)
					left = mouseX-factorDimensions[0]*factor/2
					right = (mouseX+factorDimensions[0]*factor/2)
					exit = True
				if event.button == 3 and time.time() - time_start > 2:
					top = (1080/2)-factorDimensions[1]*factor/2
					bottom = ((1080/2)+factorDimensions[1]*factor/2)
					left = (1920/2)-factorDimensions[0]*factor/2
					right = ((1920/2)+factorDimensions[0]*factor/2)
					exit = True
				if event.button == 4: #scroll up
					factor += factorScale
				if event.button == 5: #scroll down
					factor -= factorScale

		win.blit(tempscreenshot, (0,0))
		pygame.draw.rect(win, (255,0,0), (mouseX-factorDimensions[0]*factor/2,mouseY-factorDimensions[1]*factor/2,factorDimensions[0]*factor,factorDimensions[1]*factor), 1)
		pygame.display.update()

		if exit:
			pygame.quit()
			break

	img = Image.open('images/tempscreenshot.png')
	img = img.crop((left,top,right,bottom))
	img = img.resize(screenshot_dimensions[i], Image.Resampling.LANCZOS)
	img.save(f"images/{projectName}{names[i]}.png")

	print(f"Saved {projectName}{names[i]}.png")



