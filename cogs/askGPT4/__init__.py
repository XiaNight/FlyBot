from nextcord.ext import commands
from utils import embed_success
import utils.ChatGPTHandler as ChatGPTHandler

'''
gpt-4-1106-preview
gpt-3.5-turbo-1106
'''

class ChatGPT(commands.Cog, name="AskGPT4"):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command(name="ask")
	async def ask(self, ctx: commands.Context):
		returnText = None
		try:
			response = ChatGPTHandler.CreateResponse("gpt-4-1106-preview", "You are helpful, answering question in detail", ctx.message.content)
			response = ChatGPTHandler.GetResponse(response)
			returnText = response
		except Exception as e:
			returnText = str(e)
		await ctx.send(embed=embed_success(returnText))

# This function will be called when this extension is loaded.
# It is necessary to add these functions to the bot.
def setup(bot: commands.Bot):
	bot.add_cog(ChatGPT(bot))
