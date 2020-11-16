import abc

class Base(abc.ABC):
	def __init__(self, identifier, plugin):
		self.identifier = identifier
		self.plugin = plugin

	@property
	def id(self):
		return self.identifier

	@id.setter
	def id(self, value):
		self.identifier = value
