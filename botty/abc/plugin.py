import abc
from . import base

class PluginBase(base, abc.ABC):
	@abc.abstractmethod
	def run(self, botty):
		raise NotImplementedError("Setting up the plugin must be implemented")

	@abc.abstractmethod
	def send(self, messageable, content):
		raise NotImplementedError("Sending messages must be implemented")
