class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics
		pass

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
		print "------END-------"
		pass

happy_bday = Song(["happy bday to you", "I dont want to get sued",
					"So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family", 
						"With pockets full of shells"])

luna_lunera = Song(["Luna lunera cascabelera", "Eso es lo que se", "la la la"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
luna_lunera.sing_me_a_song()
