from . import messageable
from . import callable

class User(messageable, callable):
	def __init__(self, plugin, identifier, name,):
		self.plugin = plugin
		self.identifier = identifier
		self.name = name

