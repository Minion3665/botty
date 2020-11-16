from . import base

class Callable(base):
	def __init__(self, plugin, identifier, name,):
		self.plugin = plugin
		self.identifier = identifier
		self.name = name

	def call_start(self):
		self.plugin.call_start(self)

	def call_join(self):
		self.plugin.call_join(self)
