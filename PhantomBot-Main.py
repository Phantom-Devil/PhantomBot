# Imports all external functions
from Importer import *

# Globals uptime_start:
global uptime_start

# Sorts out start for the 'last' command:
global start
start = time.time()

# Confiqures starting process:
quotes = loadQuotes()
dev_users = loadDevs()
Elv_Servers = loadElv()
Token = loadToken()
Beta_Token = loadBetaToken()
bot_name = load_botname()

#intents = discord.Intents.default()
intents = discord.Intents.all()
intents.members = True

# Defines prefix + client + cogs:
prefix = loadPreix()
client = commands.Bot(command_prefix=(prefix), help_command=None, intents=intents)
slash = SlashCommand(client, override_type=True, sync_commands=True)
cogs = get_cogs()
ver = loadVer()
bot_type = loadBotType()

# Holds the status to be displayed:
status = prefix + "help"

# Trusted servers list:
trustedWorkoutServers = ['816722287939026944']
trustedAtlantisIndustriesServers = ['818509333544304640']

log('')
print("Connecting to discord...")
log("Connecting to discord...")

print()

for cog in cogs:  # Looks for the cogs,
    client.load_extension(cog)  # Loads the cogs.



# On a member joining
@client.event
async def on_member_join(member):
    if member.guild.id == 815893549337673750:
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        #await member.guild.create_role(name="Boo")
        role = discord.utils.get(member.guild.roles, id=815894346070622231)
        await member.add_roles(role)
        await channel.send("Hello {} welcome to Elvandar, use {}elv.help to see commands for the server!".format(member.mention,prefix))

    await member.send('Welcome to {}, my help command is {}help'.format(member.guild,prefix))

# Start up sequence
@client.event
async def on_ready():
    global uptime_start
    import time
    # Sorts out uptime_start for the 'uptime' command:
    uptime_start = time.time()

    print(f'{client.user.name} has connected to Discord!')
    print()

    # Logs the data
    log(f'{client.user.name} has connected to Discord!')
    log('')

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Starting...'))
    await asyncio.sleep(5)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
    return



# On a message sent
@client.event
async def on_message(message):
    # Defining all shorthand statements:
    msg = message

    # Defining all global varibles:
    global prefix
    global start

    # If the bot sends a message, it will ignore it's own message:
    if message.author == client.user:
        return

    # Checks if the message is a DM:
    if not message.guild:
        if message.content.startswith('yo'):
            await message.author.dm_channel.send('YOOOOOOO YO YOOO!!!')
        else:
            await message.author.create_dm()
            dm_response = ''
            dm_response = dm_response + "Commands are not supported in DMs, however they will be coming soon!\n\nHere is a random quote because why not:"
            quotes = loadQuotes()
            response = random.choice(quotes)
            dm_response = dm_response + "\n" + response
            await message.author.dm_channel.send(dm_response)

        # Logs the data
        data = "User: {" + str(message.author) + "} Command: {Unavailable} Channel: {" + str(message.channel) + "} Server: {Unavalible, message was sent in dm_channel]"
        log(data, True)

    # Finds hello there in staements
    if any(word in msg.content.lower() for word in ['hello there', 'hellothere']):
        await msg.channel.send("General Kenobi")
        await msg.channel.send('https://tenor.com/NMDa.gif')
        # Logs the data
        data = "Detected 'Hello There': User: {" + str(msg.author) + "} Channel: {" + str(msg.channel) + "} Server: {" + str(msg.channel.guild) + '}'
        log(data, True)
        start = time.time()

    # Finds am your father in staements
    if any(word in msg.content.lower() for word in
           ['i am your father', 'iamyourfather', 'i am your mother', 'iamyourmother']):
        await msg.channel.send('https://tenor.com/vnbU.gif')

        # Logs the data
        data = "Detected 'I Am Your Father': User: {" + str(msg.author) + "} Channel: {" + str(msg.channel) + "} Server: {" + str(msg.channel.guild) + '}'
        log(data, True)
        start = time.time()

    # if any(word in msg.content for word in ['SAMURAI','<@!821805839249702952>']):
    # await msg.channel.send('I am the samurai here!')

    # Allows program to listen for commands
    await client.process_commands(message)


'''@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embed=embed)'''

'''new_user = True
    currency_data = loadCurrency()
    for i in range(len(currency_data)):
        if currency_data[i][1] == str(message.author.id):
            new_user = False
    if new_user == True:
        f = open('Currency_Data.txt', 'a')
        f.write('\n{},{},500'.format(message.author, message.author.id))
        f.close()'''

@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please make sure that you have the correct arguments (ERROR:MissingArguments).",delete_after=5)
    elif str(error) == 'Command raised an exception: Forbidden: 403 Forbidden (error code: 50013): Missing Permissions':
        await ctx.send("Please make sure that the bot has the correct perms (ERROR:MissingPermissions).",delete_after=5)
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command, use {}help to see avalible commands".format(prefix))
    else:
        print(error)

# Hello
@client.command(name="hello", aliases=['hi', 'ello', 'hiya'])
async def hello(ctx: commands.Context):
    await ctx.channel.send("Hello There")

    # Logs the data
    data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "hello} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
    log(data, True)

#Converts the time into days, hours, mins, seconds
def seconds_days(time_difference_seconds):
    #Finds the number of mins
    time_difference_minutes = time_difference_seconds // 60
    #Finds the excess number of seconds
    seconds = (time_difference_seconds - (time_difference_minutes * 60))
    #Finds the number of hours
    time_difference_hours = time_difference_minutes // 60
    #Finds the excess number of mins
    mins = (time_difference_minutes - (time_difference_hours * 60))
    #Finds the number of days
    time_difference_days = time_difference_hours // 24
    #Finds the excess number of hours
    hours = (time_difference_hours - (time_difference_days * 24))

    #Finds the excess number of days
    days = time_difference_days

    return seconds,mins,hours,days

# Uptime(Utility) - must be in main
@client.command(name="uptime", aliases=['up', 'runtime'])
async def uptime(ctx: commands.Context):
    import time
    uptime_end = time.time()
    time_difference = round((uptime_end - uptime_start), 0)
    seconds, mins, hours, days = seconds_days(time_difference)

    embed = discord.Embed(title="PhantomBot uptime!", color=0x9A2D22)
    embed.add_field(name=("Days:"), value=str(int(days)), inline=False)
    embed.add_field(name=("Hours:"), value=str(int(hours)), inline=False)
    embed.add_field(name=("Minutes:"), value=str(int(mins)), inline=False)
    embed.add_field(name=("Seconds:"), value=str(int(seconds)), inline=False)
    embed.set_footer(text='{} {}'.format(bot_name,ver), icon_url='https://i.imgur.com/E05aPoD.png?1')
    await ctx.channel.send(embed=embed)

    # Logs the data
    data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "uptime} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
    log(data, True)


# Last
@client.command(name="last")
async def quote(ctx: commands.Context, ):
    # end = time.time()
    # global start

    await ctx.channel.send("Command not in use...", delete_after=3)
    # Logs the data
    data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "last} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
    log(data, True)

    # await ctx.channel.send("{:.2f} seconds since last response from this bot!".format(end - start))
    # start = time.time()

# Help
@client.command(name="help")
async def help(ctx: commands.Context):
    # Loads in the elv servers + dev users
    Elv_Servers = loadElv()
    dev_users = loadDevs()

    # Tests if the user specifies a certain help page to veiw
    try:
        # This is for if they specify a certain help page to veiw
        help_type = (ctx.message.content.split(prefix + "help ", 1)[1]).lower()

        if help_type == 'fun':
            embed = discord.Embed(title=f"{bot_name} 'Fun' Help Page!", description="Commands are below:",color=0x9A2D22)
            embed.add_field(name=(prefix + "quote"),value="Feeling down and moody, this command will boost your day with a great quote",inline=False)
            embed.add_field(name=(prefix + "repeat [message to repeat here]"),value="Fun Fact: This bot is a parrot, Squark Squark", inline=False)
            embed.add_field(name=(prefix + "hug"), value="Need a hug, well here one is!", inline=False)
            embed.add_field(name=(prefix + "cry"), value="Feeling sad, the bot will cry for you", inline=False)
            embed.add_field(name=(prefix + "pp"), value="You know what this does", inline=False)
            embed.add_field(name=(prefix + "empire"), value="The empire is pretty chill!", inline=False)
            embed.add_field(name=(prefix + "bored"), value="Are you bored, the bot will give you something to do!", inline=False)
            embed.add_field(name=(prefix + "ghostping"), value="Admins can use this to 'ghostping' people",inline=False)
            embed.set_footer(text=f'{bot_name} {ver}', icon_url='https://i.imgur.com/E05aPoD.png?1')
            await ctx.channel.send(embed=embed)

        if help_type == 'utility':
            embed = discord.Embed(title=f"{bot_name} 'Utility' Help Page!", description="Commands are below:",color=0x9A2D22)
            embed.add_field(name=(prefix + "help"), value="Help page for me!", inline=False)
            embed.add_field(name=(prefix + "patch"), value="See the patch notes of PhantomBot", inline=False)
            embed.add_field(name=(prefix + "up"),value="Shows the bot uptime(how long it has been running for since last restart)",inline=False)
            embed.add_field(name=(prefix + "ver"), value="Use this command to see what version the bot is running",inline=False)
            embed.add_field(name=(prefix + "info"), value="Shows info about me!", inline=False)
            embed.add_field(name=(prefix + "addbot"), value="Provides link to add me to your server", inline=False)
            embed.add_field(name=(prefix + "joinserver"), value="Come join the PhantomBot development server, where you can ask questions and chat about the bot", inline=False)
            embed.set_footer(text=f'{bot_name} {ver}', icon_url='https://i.imgur.com/E05aPoD.png?1')
            await ctx.channel.send(embed=embed)

        if help_type == 'tools':
            embed = discord.Embed(title=f"{bot_name} 'Tools' Help Page!", description="Commands are below:",color=0x9A2D22)
            embed.add_field(name=(prefix + "vote [vote]"), value="Use this to make a vote", inline=False)
            embed.add_field(name=(prefix + "suggest [suggestion]"), value="Suggest something to your server",inline=False)
            embed.add_field(name=(prefix + "roll [num of sides]"), value="Roll an 'x' sided dice", inline=False)
            embed.add_field(name=(prefix + "flip"), value="Heads or Tails? The bot will decide", inline=False)
            embed.add_field(name=(prefix + "art [message to convert]"), value="Turns a message into ASCII art",inline=False)
            embed.add_field(name=(prefix + "time"), value="See the times from all over the world!", inline=False)
            embed.set_footer(text=f'{bot_name} {ver}'.format(ver), icon_url='https://i.imgur.com/E05aPoD.png?1')
            await ctx.channel.send(embed=embed)

        if help_type == 'misc':
            embed = discord.Embed(title=f"{bot_name} 'Misc' Help Page!", description="Commands are below:",color=0x9A2D22)
            embed.add_field(name=("We currently have no 'misc' commands"), value="Turns a message into ASCII art",inline=False)
            embed.set_footer(text=f'{bot_name} {ver}', icon_url='https://i.imgur.com/E05aPoD.png?1')
            await ctx.channel.send(embed=embed)

        if help_type == 'mod' or help_type == 'moderation':
            embed = discord.Embed(title=f"{bot_name}'Moderation' Help Page!", description="Commands are below:",color=0x9A2D22)

            #If can manage messages
            if ctx.message.author.guild_permissions.manage_messages or (any(word in str(ctx.author.id) for word in dev_users)):
                embed.add_field(name=(prefix + "clear [num of messages to clear]"),value="Use this command to batch clear messages. Max messages to clear in one go is 100",inline=False)

            #If can ban members
            if ctx.message.author.guild_permissions.ban_members or (any(word in str(ctx.author.id) for word in dev_users)):
                embed.add_field(name=(prefix + "ban @[user] [reason]"), value="Use this to ban a user", inline=False)
                embed.add_field(name=(prefix + "unban [user_id]"), value="Use this to unban a user", inline=False)

            #If can manage roles
            if ctx.message.author.guild_permissions.manage_roles or (any(word in str(ctx.author.id) for word in dev_users)):
                embed.add_field(name=(prefix + "role add/rem @user @role"), value="Add/Remove roles from users", inline=False)

            #If admin
            if ctx.message.author.guild_permissions.administrator or (any(word in str(ctx.author.id) for word in dev_users)):
                embed.add_field(name=(prefix + "record start/stop [time] [time_format (s/m/h)]"), value="This can be used to 'record' a channel! Great for evidence against people who are abusing the rules", inline=False)
            embed.set_footer(text=f'{bot_name} {ver}', icon_url='https://i.imgur.com/E05aPoD.png?1')
            await ctx.channel.send(embed=embed)

    except Exception:
        # Starts a embed
        embed = discord.Embed(title=f"{bot_name} Help Page!", description="Welcome to PhantomBot, commands are below:",color=0x9A2D22)
        embed.add_field(name=(prefix + "patch"), value="See the patch notes of PhantomBot {}".format(ver), inline=False)
        # embed.add_field(name=(prefix + "last"), value="Curious to see how long since the last message was sent, if so this command is for you", inline=False)
        embed.add_field(name=(prefix + "help fun"), value="Help page for the 'fun' commands", inline=False)
        embed.add_field(name=(prefix + "help utility"), value="Help page for the 'utility' commands", inline=False)
        embed.add_field(name=(prefix + "help tools"), value="Help page for the 'tools' commands", inline=False)
        embed.add_field(name=(prefix + "help mod"), value="Help page for the 'moderation' commands", inline=False)
        # Checks if the server can use Elvandar commands
        if any(word in str(ctx.guild.id) for word in Elv_Servers):
            embed.add_field(name=(prefix + "elv.help"), value="This is the help page for the Kingdom Of Elvandar",inline=False)
        # Checks if the server can use Atlantis Industries commands
        if any(word in str(ctx.guild.id) for word in trustedAtlantisIndustriesServers):
            embed.add_field(name=(prefix + "ai.help"), value="This is the help page for Atlantis Industries",inline=False)
        # Checks if the user is a Dev
        if any(word in str(ctx.author.id) for word in dev_users):embed.add_field(name=(prefix + "dev.help"), value="This is the help page for Devs", inline=False)
        embed.set_footer(text=f'{bot_name} {ver}', icon_url='https://i.imgur.com/E05aPoD.png?1')
        await ctx.channel.send(embed=embed)

        # Logs the data
        data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "help} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
        log(data, True)


# |-------------------------------- Workout  --------------------------------|
# Workout help
@client.command(name="workout.help")
async def dev_change_quotes(ctx: commands.Context):
    if any(word in str(ctx.guild.id) for word in trustedWorkoutServers):
        embed = discord.Embed(title='Workout Help Page!',
                              description="Welcome to Workout help page, commands are below:", color=0xED7136)
        embed.add_field(name=(prefix + "workout.big [num of rounds] [num of exercises per round]"),
                        value="Makes a large workout for you to do", inline=False)
        embed.set_footer(text=f'{bot_name} Owner', icon_url='https://i.imgur.com/E05aPoD.png?1')
        await ctx.channel.send(embed=embed)

        # Logs the data
        data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "workout.help} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
        log(data, True)
    else:
        await ctx.channel.send("Cannot run that command here")


# Workout Big
@client.command(name="workout.big")
async def dev_change_quotes(ctx, x, y):
    if any(word in str(ctx.guild.id) for word in trustedWorkoutServers):
        try:
            x = int(x)
            y = int(y)
            workout = big_workout(x, y)
            msg = ""
            for i in workout:
                msg = msg + ("\n" + i)

            await ctx.channel.send(msg)
        except ValueError:
            await ctx.channel.send(f'SyntaxError at {prefix}workout.big [!] [!], use p!help or p!workout.help for more info')

        # Logs the data
        data = "User: {" + str(ctx.author) + "} Command: {" + prefix + "workout.big} Channel: {" + str(ctx.channel) + "} Server: {" + str(ctx.channel.guild) + '}'
        log(data, True)

    else:
        await ctx.channel.send("Cannot run that command here")

    global start
    start = time.time()


# Run with token - Make sure this is PhantomBot's before putting up

if bot_type.lower() == 'beta':
    # PhantomBot (Beta)
    client.run(Beta_Token)
else:
    # PhantomBot
    client.run(Token)
