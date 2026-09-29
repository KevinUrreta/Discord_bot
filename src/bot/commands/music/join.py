from discord.ext import commands

import wavelink


class Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="join")
    async def join(self, ctx):
        if ctx.voice_client is None:
            if not ctx.author.voice:
                return

            await ctx.author.voice.channel.connect(
                cls=wavelink.Player
            )
            return

        if ctx.voice_client.channel != ctx.author.voice.channel:
            await ctx.voice_client.move_to(
                ctx.author.voice.channel
            )