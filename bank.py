class Bank:
	def __init__(self):
		self.clients = []

	def add_client(self, client):
		self.clients.append(client)

	def del_client(self, client):
		for i in range(len(self.clients)):
			if self.clients[i].id == client.id:
				self.clients.pop(i)
				break

	def all_cash(self):
		res = 0
		for client in self.clients
			res += client.money

		return res

	def get_client(self, id):
		for i in range(len(self.clients)):
			if self.clients[i].id == id:
				return client[i]



