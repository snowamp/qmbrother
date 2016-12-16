#return the highfreq words


class commonwords(object):
	def words(self):
		with open('highfreq.txt', 'r') as f:
			splits = f.readline().split(' ')
			return(splits)