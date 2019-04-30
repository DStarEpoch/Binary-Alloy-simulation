import pygame
from pygame.locals import *
import sys
import os
import random
import math


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (74, 112, 150)
GREY = (130, 130, 130)


class Block:
	ratio = 4.0

	mtx = []

	J = [1, 1.5, 1]

	left_at = 100
	top_at = 100

	def __init__(self, screen):
		self.screen = screen

		for i in range(150):
			self.mtx.append([])
			for j in range(150):
				if (j >= 75):
					self.mtx[i].append(1)
				else:
					self.mtx[i].append(0)

	def update(self):
		kT = -self.ratio * (self.J[0] + self.J[2] - 2*self.J[1])

		for i in range(150):
			for j in range(150):
				#right direction
				if (self.mtx[i][j] != self.mtx[i][(j+1)%150]):
					spin1 = self.mtx[i][j]
					spin2 = self.mtx[i][(j+1)%150]
					E1 = 0
					E2 = 0

					E1 += self.J[(spin1 + self.mtx[(i+149)%150][j])]
					E2 += self.J[(spin2 + self.mtx[(i+149)%150][j])]

					E1 += self.J[(spin1 + self.mtx[i][(j+149)%150])]
					E2 += self.J[(spin2 + self.mtx[i][(j+149)%150])]

					E1 += self.J[(spin1 + self.mtx[(i+1)%150][j])]
					E2 += self.J[(spin2 + self.mtx[(i+1)%150][j])]

					E1 += self.J[(spin2 + self.mtx[(i+1)%150][(j+1)%150])]
					E2 += self.J[(spin1 + self.mtx[(i+1)%150][(j+1)%150])]

					E1 += self.J[(spin2 + self.mtx[i][(j+2)%150])]
					E2 += self.J[(spin1 + self.mtx[i][(j+2)%150])]

					E1 += self.J[(spin2 + self.mtx[(i+149)%150][(j+1)%150])]
					E2 += self.J[(spin1 + self.mtx[(i+149)%150][(j+1)%150])]

					rt = 1 / (1 + math.exp(-(E1-E2)/kT))
					banchmark = random.randint(1, 100000)
					if (banchmark / 100000 <= rt):
						self.mtx[i][j] = spin2
						self.mtx[i][(j+1)%150] = spin1

				#down direction
				if (self.mtx[i][j] != self.mtx[(i+1)%150][j]):
					spin1 = self.mtx[i][j]
					spin2 = self.mtx[(i+1)%150][j]
					E1 = 0
					E2 = 0

					E1 += self.J[(spin1 + self.mtx[(i+149)%150][j])]
					E2 += self.J[(spin2 + self.mtx[(i+149)%150][j])]

					E1 += self.J[(spin1 + self.mtx[i][(j+149)%150])]
					E2 += self.J[(spin2 + self.mtx[i][(j+149)%150])]

					E1 += self.J[(spin1 + self.mtx[i][(j+1)%150])]
					E2 += self.J[(spin2 + self.mtx[i][(j+1)%150])]

					E1 += self.J[(spin2 + self.mtx[(i+1)%150][(j+1)%150])]
					E2 += self.J[(spin1 + self.mtx[(i+1)%150][(j+1)%150])]

					E1 += self.J[(spin2 + self.mtx[(i+1)%150][j])]
					E2 += self.J[(spin1 + self.mtx[(i+1)%150][j])]

					E1 += self.J[(spin2 + self.mtx[(i+1)%150][(j+149)%150])]
					E2 += self.J[(spin1 + self.mtx[(i+1)%150][(j+149)%150])]

					rt = 1 / (1 + math.exp(-(E1-E2)/kT))
					banchmark = random.randint(1, 100000)
					if (banchmark / 100000 <= rt):
						self.mtx[i][j] = spin2
						self.mtx[(i+1)%150][j] = spin1


	def blk_show(self):
		pygame.draw.rect(self.screen, WHITE, (self.left_at, self.top_at, 750, 750), 0)
		for i in range(150):
			for j in range(150):
				if (self.mtx[i][j] == 1):
					pygame.draw.rect(self.screen, BLACK, (self.left_at + j*5, self.top_at + i*5, 5, 5), 0)


class Background:

	def __init__(self, screen):
		pass

	def bg_show(self):
		pass


class Button:
	page = 'stop'
	ratio = 4.0

	top_at = 80
	left_at = 80

	circle_x = 1060
	circle_y = 505

	button_down = False
	def __init__(self, screen):
		self.screen = screen
		self.font = pygame.font.SysFont("comicsansms", 60)
		os.chdir('button')

		self.start_button = pygame.image.load('button_blue_start.png')
		self.stop_button = pygame.image.load('button_red_stop.png')
		self.stop_button_pos = self.stop_button.get_rect()
		self.start_button_pos = self.start_button.get_rect()
		self.stop_button_pos.center = (1000,150)
		self.start_button_pos.center = (1250,150)

		self.control_bar = pygame.image.load('control_bar.png')
		self.control_bar_pos = self.control_bar.get_rect()
		self.control_bar_pos.center = (1100, 600)

		self.circle = pygame.image.load('circle.png')
		self.circle_pos = self.circle.get_rect()
		self.circle_pos.center = (self.circle_x, self.circle_y)

	def update(self, mouse_pos, mouse_type):
		pos = mouse_pos

		if (self.page == 'stop'):
			self.start_button = pygame.image.load('button_blue_start.png')
			self.stop_button = pygame.image.load('button_red_stop.png')

			if (mouse_type == 0):

				if ((pos[0] > 890) & (pos[0] < 1110)&(pos[1] > 50) & (pos[1] < 250)):
					self.stop_button = pygame.image.load('button_yellow_stop.png')
				else:
					self.stop_button = pygame.image.load('button_red_stop.png')

				if ((pos[0] > 1140) & (pos[0] < 1360)&(pos[1] > 50) & (pos[1] < 250)):
					self.start_button = pygame.image.load('button_yellow_start.png')
				else:
					self.start_button = pygame.image.load('button_blue_start.png')

			if (mouse_type == 1):

				if ((pos[0] > 890) & (pos[0] < 1110)&(pos[1] > 50) & (pos[1] < 250)):
					self.stop_button = pygame.image.load('button_red_stop.png')
				if ((pos[0] > 1140) & (pos[0] < 1360)&(pos[1] > 50) & (pos[1] < 250)):
					self.start_button = pygame.image.load('button_red_start.png')
					self.stop_button = pygame.image.load('button_blue_stop.png')
					self.page = 'start'

		if (self.page == 'start'):
			self.stop_button = pygame.image.load('button_blue_stop.png')
			self.start_button = pygame.image.load('button_red_start.png')

			if (mouse_type == 0):

				if ((pos[0] > 890) & (pos[0] < 1110)&(pos[1] > 50) & (pos[1] < 250)):
					self.stop_button = pygame.image.load('button_yellow_stop.png')
				else:
					self.stop_button = pygame.image.load('button_blue_stop.png')

				if ((pos[0] > 1140) & (pos[0] < 1360)&(pos[1] > 50) & (pos[1] < 250)):
					self.start_button = pygame.image.load('button_yellow_start.png')
				else:
					self.start_button = pygame.image.load('button_red_start.png')

			if (mouse_type == 1):

				if ((pos[0] > 1140) & (pos[0] < 1360)&(pos[1] > 50) & (pos[1] < 250)):
					self.start_button = pygame.image.load('button_red_start.png')
				if ((pos[0] > 890) & (pos[0] < 1110)&(pos[1] > 50) & (pos[1] < 250)):
					self.stop_button = pygame.image.load('button_red_stop.png')
					self.start_button = pygame.image.load('button_blue_start.png')
					self.page = 'stop'

		self.stop_button_pos = self.stop_button.get_rect()
		self.start_button_pos = self.start_button.get_rect()
		self.stop_button_pos.center = (1000,150)
		self.start_button_pos.center = (1250,150)

		if (mouse_type == 1):
			self.button_down = False
			return(self.page)
		if (mouse_type == -1):
			if ((pos[0] > 1020) and (pos[0] < 1100) and (pos[1] >= 505) and (pos[1] <= 704)):
				self.button_down = True
				self.circle_y = pos[1]
				self.circle_pos.center = (self.circle_x, self.circle_y)
				self.ratio = round(0.02 * (704 - pos[1]) + 0.01, 2)
			return(self.ratio)
		if (mouse_type == 0):
			if (self.button_down):
				if ((pos[0] > 1020) and (pos[0] < 1100) and (pos[1] >= 505) and (pos[1] <= 704)):
					self.circle_y = pos[1]
					self.circle_pos.center = (self.circle_x, self.circle_y)
					self.ratio = round(0.02 * (704 - pos[1]) + 0.01, 2)
				return(self.ratio)
			else:
				return(-1)
			pass


	def btn_show(self):
		pygame.draw.rect(self.screen, BLUE, (self.left_at, self.top_at, 790, 790), 0)

		d = round(self.ratio, 3)
		text = self.font.render('T = ' + str(d) + 'Tc', True, WHITE)
		self.screen.blit(text, (1050, 430))

		self.circle_pos.center = (self.circle_x, self.circle_y)
		self.screen.blit(self.stop_button, self.stop_button_pos)
		self.screen.blit(self.start_button, self.start_button_pos)
		self.screen.blit(self.control_bar, self.control_bar_pos)
		self.screen.blit(self.circle, self.circle_pos)


class Animation:

	size = width, height = 1500, 900

	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Binary_Alloy')
		self.screen = pygame.display.set_mode(self.size)
		self.screen.fill(GREY)
		self.clock = pygame.time.Clock()

	def start_animation(self):
		blk = Block(self.screen)
		bg = Background(self.screen)
		btn = Button(self.screen)

		page = 'stop'
		Frame = 0

		kk = 0
		while True:
			Tempreture_ratio = -1

			for event in pygame.event.get():
				if (event.type == QUIT):
					pygame.quit()
					sys.exit()
				if (event.type == MOUSEMOTION):
					Tempreture_ratio = btn.update(event.pos, 0)
				if (event.type == MOUSEBUTTONUP):
					page = btn.update(event.pos, 1)
				if (event.type == MOUSEBUTTONDOWN):
					Tempreture_ratio = btn.update(event.pos, -1)

			self.screen.fill(GREY)
			bg.bg_show()
			btn.btn_show()

			if (page == 'start'):
				Frame += 1
				if ((blk.ratio > 1) and (Frame > 1500)):
					if (Frame % 1 == 0):
						blk.ratio -= 0.01
						btn.ratio -= 0.01
						kk += 1
						if (kk % 2 == 0):
							btn.circle_y += 1
				if ((blk.ratio <= 1) and (blk.ratio > 0.01)):
					if (Frame % 15 == 0):
						blk.ratio -= 0.01
						btn.ratio -= 0.01
						kk += 1
						if (kk % 2 == 0):
							btn.circle_y += 1
			if (Tempreture_ratio > 0):
				#if (Tempreture_ratio < 1):
				#	blk.ratio = 0.6*Tempreture_ratio
				#else:
				blk.ratio = Tempreture_ratio
			if (page == 'start'):
				blk.update()
			blk.blk_show()

			pygame.display.flip()
			self.clock.tick(50)

if (__name__ == "__main__"):
	anm = Animation()
	anm.start_animation()
