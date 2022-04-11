import disnake
from disnake.ext import commands

date_format = "%a, %b %d, %Y"

class InfoCommands(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Responds with your user info.")
    async def user(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            f"User `{inter.author}`\nYour ID: `{inter.author.id}`\nDate of server join: `{inter.author.joined_at.strftime(date_format)}`\nDate of registration: `{inter.author.created_at.strftime(date_format)}`"
        )
        
    @commands.slash_command(description="Responds with the server's info.")
    async def server(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            f"Server `{inter.guild.name}`\nServer ID: `{inter.guild.id}`\nMember count: `{inter.guild.member_count}`\n  Date of creation: `{inter.guild.created_at.strftime(date_format)}`"
        )


def setup(bot: commands.Bot):
    bot.add_cog(InfoCommands(bot))
    