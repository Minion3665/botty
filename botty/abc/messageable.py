from . import base

zclass Messageable(base):
	def __init__(self, plugin, identifier, name,):
		self.plugin = plugin
		self.identifier = identifier
		self.name = name
		self.encrypted = self.plugin.encrypted(self)

	def send(self, content):
		self.plugin.send(self, content)
