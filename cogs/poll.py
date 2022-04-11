import disnake
from disnake.ext import commands
import asyncio

class PollCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    letters = [
        "🇦",
        "🇧",
        "🇨",
        "🇩",
        "🇪",
        "🇫"
    ]
        
    def getOptions(self, message, options): #recursive function
        first = message.find('[') + 1
        last = message.find(']')
        if(first == 0 or last == -1):
            return options
        options.append(message[first:last])
        print(message[first:last])
        message = message[last + 1:]
        return self.getOptions(message, options)
    
    @commands.slash_command(description="Options format: [option][option][option][option][option] for max 6 options")
    async def poll(self, inter: disnake.ApplicationCommandInteraction, title: str, options: str):
        
        optionList = self.getOptions(options, [])
        
        if(len(optionList) > 6):
            await inter.response.send_message(
                f"Please enter a maximum of 6 options"
            )
        
        content = "**" + title + "**\n\n"
        i = 0
        while i < len(optionList):
            content = content + self.letters[i] + " " + optionList[i] + "\n"
            print(content)
            i = i + 1
        
        content = content + "\nReact with the following emoji to vote!"
        
        message = await inter.response.send_message(
            content
        )
        print(message)
        
        i = 0
        while i < len(optionList):
            await message.add_reaction(self.letters[i])
            i = i + 1


def setup(bot: commands.Bot):
    bot.add_cog(PollCommand(bot))