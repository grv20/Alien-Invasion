import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf
from pygame import mixer

def run_game():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	icon = pygame.image.load('ufo.png')
	pygame.display.set_icon(icon)
	pygame.display.set_caption("Alien Invasion")
	background = pygame.image.load('background.png')
	mixer.music.load("background.wav")
	mixer.music.play(-1)
	# Make the Play button.
	play_button = Button(ai_settings, screen, "Play")
	# Create an instance to store game statistics and create a scoreboard.
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	# Make a ship, a group of bullets, and a group of aliens.
	ship =Ship(ai_settings,screen)
	bullets = Group() #Dont create this inside while
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	while True:
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)#check for key-presses, we are also sending bullet group
		if stats.game_active:
			ship.update() #update coordinates of ship as per the key presses
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,bullets) #Remove bullets that are out of screen now and update positions asit is travelling.
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets) #update the coordinates and movement of aliens.
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button,background) #updates the screen with changes
		
run_game()
