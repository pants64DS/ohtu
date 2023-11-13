class PlayerStats:
	def __init__(self, reader):
		self.reader = reader

	def top_scorers_by_nationality(self, nationality):
		players = [player for player in self.reader.read()]

		players.sort(key=lambda p: -(p.goals + p.assists))

		return players
