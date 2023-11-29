class Client:
	cur_id = 1

	def __init__(self, name, money):
		self.name = name 
		self.money = money
		self.id = cur_id
		cur_id += 1

	def signature(self):
		print("Да")