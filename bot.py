import traceback
import discord
from discord.ext import commands
from config import DiscordBot

intent = discord.Intents.all()


class Minerva(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix=commands.when_mentioned_or('t/'), intents=intent, **kwargs, pm_help=None,
                         help_attrs=dict(hidden=True))
        for cog in DiscordBot.cogs:
            try:
                self.load_extension(cog)
            except Exception as exc:
                print('Could not load extension {0} due to {1.__class__.__name__}: {1}'.format(
                    cog, exc))

    async def on_ready(self):
        print('Logged on as {0} (ID: {0.id})'.format(self.user))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            return

        orig_error = getattr(error, "original", error)
        error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
        error_msg = "```py\n" + error_msg + "\n```"
        await ctx.send(error_msg)


bot = Minerva()

# write general commands here

bot.run(DiscordBot.token)