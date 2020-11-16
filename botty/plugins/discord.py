import discord
from ..abc import plugin

class Discord(plugin.PluginBase):
	def __init__(self, token):
		self.token = token
		self.botty = None
		self.bot = discord.Client()

	async def on_message(self, message):
		await self.botty.event_received("message", message=message)

	async def run(self, botty):
		self.botty = botty
		await self.bot.connect()
		await self.bot.login(self.token)

	def send(self, messageable, content):
		await messageable.send(content)
