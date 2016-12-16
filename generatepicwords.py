from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.font import Font

class combinepicword(object):
	def __init__(self):
		self.width = 0
		self.height = 0
		self.big = 1000
		#self.font_size = int(self.big*15/400)

	def estimate(self, length):
		lenPerLine = int(self.width/self.font_size)*1.8 #char number per line
		height = int(length*self.font_size*2/lenPerLine)+int(2*self.font_size)
		return(height)

	def combine(self, string, pics):
		
		#self.width = self.big
		#self.height = self.big
		#self.increase = self.estimate(len(string))
		index1 = pics.find('.')
		index2 = pics.find('_thumbnail')
		pics = pics[0:index2]+pics[-4:]
		picname = pics[0:index2] + '_combine' + pics[-4:]
		print(pics)
		print(picname)

		with Image(filename = pics) as image0:
			self.width = image0.size[0]
			self.height = image0.size[1]
			self.font_size = int(self.width*15)/400
			self.increase = self.estimate(len(string))

		
		with Image(width=self.width, height = self.height + self.increase) as img:
			img.save(filename = picname)

			with Image(filename = pics) as image1:
				#image1.resize(self.big, self.big)
				img.composite_channel(channel='sync_channels', image = image1, operator='overlay', left = 0, top = 0)

			splits = string.split(' ')
			with Drawing() as draw:	

				with Color('ivory') as color:
					draw.fill_color = color
					draw.rectangle(left = 0, top =self.height, width = self.width, height = self.increase)
				draw(img)
				img.save(filename = picname)

		with Image(filename = picname) as img:
			with Color('black') as color1:
				with Drawing() as draw:
					draw.font = './font/Americana Bold BT.ttf' 
					draw.font_size = self.font_size
					length = int(self.width/draw.font_size)*1.8
					height = int(self.height+draw.font_size)
					count = 0
					current_string = ''
					for word in splits:
						if count < length - len(word):
							current_string += word+' '
							count += len(word) + 1
						else:
							draw.text(1, height, current_string)
							current_string = word +' '
							height =int(height + draw.font_size + self.font_size)
							count = len(word)
					draw.text(1, height, current_string)
					draw(img)
			'''
			newwidth = 0
			newheight = 0
			if img.size[0] > img.size[1]:
				newwidth = 400
				newheight = int(400*img.size[1]/img.size[0])
			else:
				newheight = 400
				newwidth = int(400*img.size[0]/img.size[1])
			img.resize(newwidth, newheight)
			'''
			img.save(filename = picname)



			
