import pygame
from pygame.sprite import Sprite
#When you use sprites, you can group related elements in your game and act on all the grouped elements at once.

class Bullet(Sprite): #Bullet is inherited from Sprite Class
	"""A class to manage bullets fired from the ship"""
	def __init__(self, ai_settings, screen, ship):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = screen
		# Create a bullet rect at (0, 0) and then set correct position.
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height) #Since bullet is not based on image we use Rect to create it.
		self.rect.centerx = ship.rect.centerx #x position of bullet need to be same as that of ship
		self.rect.top = ship.rect.top #bullet top must meet ship top, so that it will seem to emerge from ship.
		self.y = float(self.rect.y) # Store the bullet's position as a decimal value.
		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
		
	def update(self):
		"""Move the bullet up the screen."""
		# Update the decimal position of the bullet.
		self.y -= self.speed_factor
		# Update the rect position.
		self.rect.y = self.y
			
	def draw_bullet(self):
		"""Draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)


