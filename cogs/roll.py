import asyncio
import random
import disnake
from disnake.ext import commands

class RollCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description="Rolls a specified number of dice numbered 1-6.")
    async def roll(self, inter: disnake.ApplicationCommandInteraction, amount: int):
        if (amount > 10 or amount < 1):
            await inter.response.send_message(
                ":game_die: Please enter a number of rolls from 1-10!"
            )
            return
        await inter.response.send_message(
            ":game_die: Rolling! . . ."
        )
        await asyncio.sleep(1)
        # calculations
        rolls = [0]*amount
        i = 0
        while i < amount:
            currentRoll = int(random.random()*6) + 1
            rolls[i] = currentRoll
            await asyncio.sleep(1)
            if (rolls[i] != 6):
                await inter.edit_original_message(
                    content=f":game_die: `{inter.author.name}`, you rolled a `{currentRoll}` (Roll `{i + 1}` out of `{amount}`)"
                )
            if (rolls[i] == 6):
                await inter.edit_original_message(
                    content=f":game_die: `{inter.author.name}`, you rolled a `{currentRoll}` (Roll `{i + 1}` out of `{amount}`) Wow, how lucky!"
                )
            i += 1
        
        await asyncio.sleep(1)
        sum = 0
        i = 0
        while i < amount:
            sum += rolls[i]
            i += 1
        
        if (sum != amount * 6):
            await inter.edit_original_message(
                content=f":game_die: `{inter.author.name}`, you rolled a total of `{sum}` with `{amount}` dice!"
            )
        if (sum == amount * 6):
            await inter.edit_original_message(
                content=f":game_die: `{inter.author.name}`, you rolled a total of `{sum}` with `{amount}` dice! WOW! You rolled all 6s! That's incredible luck!"
            )
        

def setup(bot: commands.Bot):
    bot.add_cog(RollCommand(bot))