from pygame import *
from const import *
from Enemy import *
from Animation import *
from math import *

class Fly(Enemy):
	"""Simple enemy fly class"""

	isFlying = True
	pathed = False
	health = 2
	weight = 1
	hurtDistance = 0.8

	def __init__(self, xy, sounds, textures):
		self.x, self.y = xy

		self.sounds = sounds

		self.frames = [textures.subsurface(i*64, 0, 64, 64) for i in range(2)]
		self.deathFrames = [textures.subsurface(i*128 - ((i//4)*128*4), 128 * (i//4 + 1), 128, 128) for i in range(12)]

		self.anim = Animation(self.frames, 0.04)

		self.speed = 1.5/GRATIO

	def die(self):
		if not self.dead:
			self.anim = Animation(self.deathFrames, 0.24)
			self.dead = True
			self.sounds[-1].play() # Play death sound

	def render(self, surface, time, character, nodes, paths, bounds, obsticals):

		if not self.dead:
			if not self.pathed:
				self.pathFind((ix, iy), nodes, paths)
				self.pathed = True
			self.move()

			self.checkHurt(character, time)


			frame = self.anim.render(time)
		else:
			frame = self.anim.render(time)
			if self.anim.looped:
				return False

		surface.blit(frame, (GRIDX+GRATIO*self.x-self.anim.width//2, GRIDY+GRATIO*self.y-self.anim.height//2))
		return True