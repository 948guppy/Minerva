import discord
from discord.ext import commands

import textwrap


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        """サーバー参加時にメッセージを送信します"""

        async def send_disclaimer_of_liability(Guild):
            e = discord.Embed()
            e.title = "Minervaを招待していただきありがとうございます！"
            e.description = textwrap.dedent(
                f"""
                このボットはDiscord上で大会を簡単に実施できるようにした
                ⇩ ⇩ 各種リンク ⇩ ⇩
                [・公式ホームページ(作成中)]()
                [・招待URL](https://discord.com/api/oauth2/authorize?client_id=734416043266670703&permissions=335011152&scope=bot)
                """
            )
            e.colour = 0x99FFFF
            if Guild.system_channel:
                await Guild.system_channel.send(embed=e)
            else:
                channel = Guild.text_channels[0]
                await channel.send(embed=e)

        await send_disclaimer_of_liability(guild)

    @commands.command()
    async def _hoge(self, ctx):
        return


def setup(bot):
    bot.add_cog(Server(bot))
