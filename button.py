class Button():         
	def __init__(self, image, pos):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.rect = self.image.get_rect(center=(self.x_pos,self.y_pos))
		
	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.image.get_rect(center=(self.x_pos,self.y_pos)))
	
	def mousePos(self, pos):
		if pos[0] in range(self.rect.left, 
						   self.rect.right) and pos[1] in range(self.rect.top,
											  self.rect.bottom):
			return True
		return False
