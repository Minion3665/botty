import asyncio

from . import abc

__all__ = (
	abc.messageable.Messageable,
	abc.callable.Callable,
)

class Bot:
	def __init__(self, plugins=(), loop=asyncio.new_event_loop(),):
		self.loop = loop

		for plugin in plugins:
			self.load(plugin)

		self.event_callbacks = {}

	def load(self, plugin):
		return self.loop.create_task(plugin.run(self))

	def on_event(self, event, callback):
		self.event_callbacks[event] = self.event_callbacks.get(event, [])
		self.event_callbacks[event].append(callback)

	async def event_received(self, event, **event_data):
		for callback in self.event_callbacks.get(event, []):
			yield self.loop.create_task(callback(**event_data))
