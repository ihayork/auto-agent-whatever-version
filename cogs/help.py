import disnake
from disnake.ext import commands

class HelpCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Responds with a list of commands.")
    async def help(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            ":grey_question: **Auto Agent 3000 Help**\n"
            "`/ping`: Responds with current ping.\n"
            "`/user`: Responds with your user info.\n"
            "`/server`: Responds with the server's info.\n"
            "`/roll <number>`: Rolls a specified number of dice numbered 1-6.\n"
            "`/slots <number>`: Runs a variation of 3-reel-slots. Add a bet from 1-100 coins.\n"
            "`/slots_help`: Responds with the values of each slot image.\n"
        )


def setup(bot: commands.Bot):
    bot.add_cog(HelpCommand(bot))