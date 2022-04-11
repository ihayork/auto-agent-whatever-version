import asyncio
import random
import disnake
from disnake.ext import commands

class SlotsCommand(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.slash_command(description="Responds with the values of each slot image.")
    async def slots_help(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(
            ":slot_machine: Slots guide:\n"
            ":stars::stars::stars: : Bet x 20\n"
            ":star::star::star: : Bet x 15\n"
            ":sunflower::sunflower::sunflower: : Bet x 10\n"
            ":mushroom::mushroom::mushroom: : Bet x 10\n"
            ":feather::feather::feather: : Bet x 5\n"
            ":egg::egg::egg: : Bet x 5\n"
            ":stars::stars::grey_question: : Bet x 4\n"
            ":stars::grey_question::grey_question: : Bet x 2\n"
        )

    @commands.slash_command(description="Runs a variation of 3-reel-slots. Add a bet from 1-100 coins.")
    async def slots(self, inter: disnake.ApplicationCommandInteraction, bet: int):
        if (bet > 100 or bet < 1):
            await inter.response.send_message(
                ":slot_machine: Please enter a valid bet from 1-100!"
            )
            return
        rolls = [":stars:", ":star:", ":sunflower:", ":mushroom:", ":feather:", ":egg:"]
        roll1 = int(random.random()*6)
        roll2 = int(random.random()*6)
        roll3 = int(random.random()*6)
        await inter.response.send_message(
            f":slot_machine: Rolling!\n:grey_question:|:grey_question:|:grey_question:"
        )
        
        await asyncio.sleep(1)
        await inter.edit_original_message(
            content=f":slot_machine: Rolling! . \n{rolls[roll1]}|:grey_question:|:grey_question:"
        )
        await asyncio.sleep(1)
        await inter.edit_original_message(
            content=f":slot_machine: Rolling! . . \n{rolls[roll1]}|{rolls[roll2]}|:grey_question:"
        )
        await asyncio.sleep(1)
        await inter.edit_original_message(
            content=f":slot_machine: Rolling! . . .\n{rolls[roll1]}|{rolls[roll2]}|{rolls[roll3]}"
        )
        
        results = "Sorry... You lost your bet!"
        reward = 0
        if (roll1 == 0 or roll2 == 0 or roll3 == 0):
            results = "Congrats! Bet x 2!"
            reward = bet * 2
            if ((roll1 == 0 and roll2 == 0) or (roll2 == 0 and roll3 == 0) or (roll3 == 0 and roll1 == 0)):
                results = "Congrats! Bet x 4!"
                reward = bet * 4
                if (roll1 == roll2 == roll3):
                    if(roll1 == 0):
                        results = "WOW! Bet x 20!"
                        reward = bet * 20
                    if(roll1 == 1):
                        results = "WOW! Bet x 15!"
                        reward = bet * 15
                    if(roll1 == 2):
                        results = "WOW! Bet x 10!"
                        reward = bet * 10
                    if(roll1 == 3):
                        results = "WOW! Bet x 10!"
                        reward = bet * 10
                    if(roll1 == 4):
                        results = "WOW! Bet x 5!"
                        reward = bet * 5
                    if(roll1 == 5):
                        results = "WOW! Bet x 5!"
                        reward = bet * 5
        
        await asyncio.sleep(1)
        await inter.edit_original_message(
            content=f":slot_machine: {results} {reward}:coin: gained.\n{rolls[roll1]}|{rolls[roll2]}|{rolls[roll3]}"
        )

def setup(bot: commands.Bot):
    bot.add_cog(SlotsCommand(bot))