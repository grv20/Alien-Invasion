import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	def __init__(self, ai_settings, screen):
		"""Initialize the ship and set its starting position."""
		super().__init__()
		self.screen = screen

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		# rect stores the coordinates of image on screen.
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		# Start each new ship at the bottom center of the screen.
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		#Rect can store only int values, to store exact position of ship we are using float now
		self.center = float(self.rect.centerx)
		self.moving_right = False
		self.moving_left = False
		
	def update(self):
		"""Update the ship's position based on the movement flag."""
		if self.moving_right and self.rect.right < self.screen_rect.right: #self.rect.right returns x coordinate of right edge of ship's rect
			#if moving_right made True by check_events then center is updated by ship speed factor
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor
		self.rect.centerx = self.center #only int value will be updated to rect but thats fine
		
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Center the ship on the screen."""
		self.center = self.screen_rect.centerx
