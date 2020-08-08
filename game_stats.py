filename = 'high_score.txt'

class GameStats():	
	"""Track statistics for Alien Invasion."""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		# Start Alien Invasion in an inactive state.
		self.game_active = False
		# High score should never be reset.
		with open(filename) as f_obj:
			highscore= int(f_obj.read())
		self.high_score = highscore
		
		
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
