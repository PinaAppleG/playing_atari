import sys
import random
from scipy.misc import imresize
import cv2

class ScreenPreprocessor:
	"""
	:description: class for preprocessing screens. It's a class b/c needs to maintain
					state from previous screens.
	"""

	def preprocess():
		raise NotImplementedError("Override me")

class GrayscaleScreenPreprocessor(ScreenPreprocessor):
	"""
	:description: preprocesses grayscale screens
	"""

	def __init__(self, dim=32):
		self.screens = []
		self.dim = dim
		self.channels = 1

	def preprocess(self, screen):
		"""
		:description: rescales grayscale screen to be a square of height, width dim
		"""
		# currently this just takes the section of the screen with the ball and the block
		height, width, channels = screen.shape
		screen = screen.reshape(screen.shape[0], screen.shape[1])
		screen = screen[height*.5:, width*.05: width*.95]
		if True:
			cv2.imshow('screen', screen)
			cv2.waitKey(1)
		return screen

