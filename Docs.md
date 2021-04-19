#PhantomBot Docs:
PhantomBot is a multi purpose open source discord bot 
to bring fun, games, moderation tools to your server.

###Info:

**Langauge:** Python 3

**Packages:** Discord, Random, Time, Csv, Asyncio, Sys, Traceback, Requests, Logging, Glob, Shutil, Zipfile, Pytz

**Framework:** The code is split up into a few parts, first there is 'PhantomBot-Main.py' which is the core of the bot. The other commands and functions are pulled into this file before being ran. The cogs directory is seperated into multiple category which each represent a seperate function. These are all pulled into the main file through the getcogs() function which can be ran from Get_Cogs.py.

###The Code:
```python
intents = discord.Intents.all()
intents.members = True

# Defines prefix + client + cogs:
prefix = loadPreix()
client = commands.Bot(command_prefix=(prefix), help_command=None, intents=intents)
slash = SlashCommand(client, override_type=True, sync_commands=True)
cogs = get_cogs()
ver = loadVer()
``` 
This is the defining factor of the bot, it loads the 
bot data from the external config file and the activates
the bit with the 'commands.Bot()' command this bot instance
is then ran with the...

```python
client.run(Token)
```
which turns the bot online with the token from the config file.

###Commands:

**Ban:** p!ban [user] [reason]

Bans a user from the server!
![alt text](https://i.imgur.com/qttkhvK.png)

**Unban:** p!unban [user]

Unbans a user from the server!
![alt text](https://i.imgur.com/6Ost56F.png)

**Clear:** p!clear [amount]

Clears a 'x' amount of messages
![alt text](https://i.imgur.com/4sZEDmO.png)

**Kick:** p!kick [user]

Kicks the specified user from the server
![alt text](https://i.imgur.com/r9rtY2B.png)

**Vote:** p!vote [vote-content]

Makes a vote
![alt text](https://i.imgur.com/QFhPoqz.png)
