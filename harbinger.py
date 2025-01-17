from datetime import datetime
from os import listdir

import discord
from discord.ext import commands

from config.read_configs import ReadConfigs as configs

TOKEN = configs.token()

class Harbinger:
    """Class for the main bot functions."""

    # config_path = "config/config.ini"
    # config = ConfigParser()
    # config.read(config_path)
    # email_address = Configure.reveal(config["Email"]["address"])
    # email_pass = Configure.reveal(config["Email"]["password"])
    # server_dir = Configure.reveal(config["Server"]["server_dir"])
    # startup_script = Configure.reveal(config["Server"]["startup_script"])
    # server_public_ip = Configure.reveal(config["Server"]["server_public_ip"])
    # moderator_role_id = int(Configure.reveal(config["Roles"]["moderator"]))
    # developer_role_id = int(Configure.reveal(config["Roles"]["developer"]))
    # d_time = int(config["Bot"]["delete_after"])
    # rgb = config["Custom Color"]["rgb"]
    # r, g, b = map(int, rgb.split())
    # custom_color = discord.Color.from_rgb(int(r), int(g), int(b))

    start_time = datetime.now()

    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)
    bot.remove_command("help")

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def setup_hook() -> None:
        """Sequentially load cogs."""
        print(f"Loading cogs...")
        for cog in listdir("cogs"):
            if cog.endswith(".py") == True:
                try:
                    await bot.load_extension(f"cogs.{cog[:-3]}")
                    print(f"Loaded {cog}")
                except Exception as exc:
                    print(f"An error has occured: {exc}.")

    def get_ver() -> str:
        """Check CHANGELOG.md for version info, return version string.

        Returns:
            str: Software version
        """
        with open("docs/CHANGELOG.md", "r") as f:
            changelog = f.readlines()
            version_line = changelog[6]
            version = version_line[4:9]
            return version

    def timestamp(user, cmd, cmd_msg) -> None:
        """Print timestamp and end-of-command separator."""
        current_time = datetime.now()
        print(f"++++\n{current_time}\nUSR| {user}\nCMD| {cmd}\nMSG| {cmd_msg}")

    def start() -> None:
        """Start the bot."""
        bot.run(TOKEN)

    async def send_dm(ctx, member: discord.Member, *, content) -> None:
        """Create a Direct Message channel with a given member."""
        channel = await member.create_dm()
        await channel.send(content)


bot = Harbinger.bot


def main():
    Harbinger.start()


if __name__ == "__main__":
    main()
