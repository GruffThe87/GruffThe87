import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

# Bot token from token.txt
with open("token.txt", "r") as token_file:
    TOKEN = token_file.read().strip()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

# Prefixes
def custom_prefix(bot, message):
    prefixes = ['!', '/']  # List of acceptable prefixes
    content = message.content.lower()  # Convert message content to lowercase
    for prefix in prefixes:
        if content.startswith(prefix):
            return prefix
    return None

bot = commands.Bot(command_prefix=custom_prefix, intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()  # Sync slash commands with Discord
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('BOT ONLINE!')

@bot.command(aliases=["Hi", "hi", "Hey", "hey", "Hello"])
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.mention}!")

# Good Morning
@bot.command(aliases=["GM", "gm", "Morning", "morning", "Goodmorning", "goodmorning"])
async def good_morning(ctx):
    await ctx.send(f"Good Morning, {ctx.author.mention}!")

# Command about my great friend, Chaca
@bot.command(aliases=["ChacaChaca13", "Chaca", "chaca", "Secret", "Chacachaca13"])
async def secret(ctx):
    await ctx.send(f"Hey man. I see you used my secret little command. This is just a little fun secret I put in here to express my gratitude towards my good friend ChacaChaca13,"
                   f" who has been awesome to me. Thank you! Love you bro")
    
# Command to send a link to Gruffs Twitch
@bot.command(aliases=["Twitch", "ttv", "TTV"])
async def twitch(ctx):
    embed = discord.Embed(title="Link to GruffThe87's twitch channel. Check it out!", description="Click [here](https://www.twitch.tv/gruffthe87) to visit Gruffs Twitch.", color=0x00ff00)
    await ctx.send(embed=embed)

# Command to the support server
@bot.command(aliases=["Support", "Server", "server", "SupportServer", "supportserver", "Supportserver"])
async def support(ctx):
    embed = discord.Embed(title="Link to the Bots Support Server. join here", description="Click [here](https://discord.gg/7gvZt85v5K) to join", color=0x00ff00)
    await ctx.send(embed=embed)

# Cat's meme command
@bot.command(aliases=["Cat", "Catmeme", "cat", "catmeme"])
async def send_gif(ctx):
    # Replace "https://example.com/your_gif.gif" with the URL of the GIF you want to send
    gif_url = "https://tenor.com/view/cat-frantic-the-voices-gif-4777666775328982944"
    await ctx.send(gif_url)

# Goldens command
USER_ID = 480223783890976779

@bot.command(aliases=["Golden"])
async def golden(ctx):
    user = ctx.message.author
    your_user = bot.get_user(480223783890976779)
    if your_user: 
        await your_user.send(f"{user.mention} Gruff is awesome!")

# SLASH COMMANDS

# Ping & Pong
@bot.hybrid_command(aliases=["Ping"])
async def ping(ctx: commands.Context):
    await ctx.send('pong')

# Sync
@bot.hybrid_command(aliases=["Sync", "SyncServer", "Syncserver", "syncserver"])
async def sync(ctx: commands.Context):
    await ctx.send('Syncing...')
    await bot.tree.sync()    

# Latency
@bot.hybrid_command(aliases=["Pingserver", "PingServer", "Serverping", "Pingbot", "PingBot", "serverping"])
async def pingbot(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f'Ping! Latency: {latency}ms')

# 8-Ball
responses = [ "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]

@bot.hybrid_command(aliases=["8-ball", "8-Ball", "ball", "Ball", "8ball", "8Ball", "8"])
async def eight_ball(ctx, *, question):
    response = random.choice(responses)
    await ctx.send(f"Question: {question}\nAnswer: {response}")

# List of jokes
jokes = ["Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you get when you cross a snowman with a vampire? Frostbite!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why couldn't the bicycle stand up by itself? Because it was two-tired!",
        "What do you call a bear with no teeth? A gummy bear!",
        "What do you call an alligator in a vest? An in-vest-igator!",
        "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the coffee file a police report? It got mugged!",
        "What do you call a fake noodle? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
        "What do you call a fish wearing a bowtie? Sofishticated!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why did the chicken join a band? Because it had the drumsticks!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why was the math book sad? Because it had too many problems!",
        "What did one plate say to the other plate? Dinner's on me!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "What do you call a belt made out of watches? A waist of time!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
        "What do you call a bear with no teeth? A gummy bear!",
        "Why couldn't the bicycle stand up by itself? Because it was two-tired!",
        "What do you call a pile of cats? A meowtain!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "What do you call a fake noodle? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "What do you call a belt made out of watches? A waist of time!",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
        "What do you call a pile of cats? A meowtain!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call a fake noodle? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "What do you call a belt made out of watches? A waist of time!",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
        "What do you call a pile of cats? A meowtain!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "What do you call a bear with no teeth? A gummy bear!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "What do you call a fake noodle? An impasta!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "What do you call a can opener that doesn't work? A can't opener!",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "What do you call a snowman with a six-pack? An abdominal snowman!",
        "What do you get when you cross a snowman and a dog? Frostbite!",
        "What do you call a belt made out of watches? A waist of time!",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
        "What do you call a pile of cats? A meowtain!"
    
]

# Command to tell a joke
@bot.hybrid_command(aliases=["Joke", "Jokes", "jokes"])
async def joke(ctx):
    # Select a random joke from the list
    joke = random.choice(jokes)
    await ctx.send(joke)


# Command to ban a user
@bot.command(aliases=["Ban"])
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned for: {reason}')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to use this command.")

# Command to kick a user
@bot.command(aliases=["Kick"])
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked for: {reason}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to use this command.")

# Command to mute a user
@bot.command(aliases=["Mute"])
@has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")

        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, speak=False, send_messages=False)

    await member.add_roles(muted_role, reason=reason)
    await ctx.send(f'{member.mention} has been muted for: {reason}')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to use this command.")

# Command to prune messages from a user
@bot.command(aliases=["Prune", "P"])
@has_permissions(manage_messages=True)
async def prune(ctx, member: discord.Member, limit: int = 100):
    def check(msg):
        return msg.author == member

    deleted = await ctx.channel.purge(limit=limit, check=check)
    await ctx.send(f'Deleted {len(deleted)} messages from {member.mention}')

@prune.error
async def prune_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to use this command.")

# Command to echo a message
@bot.command(aliases=["ECHO", "Echo"])
async def echo(ctx, *, message):
    await ctx.message.delete()  # Delete the original command message
    await ctx.send(message)

# Command to warn a user
@bot.command(aliases=["Warn", "WARN", "Warning", "warning"])
@has_permissions(manage_messages=True)
async def warn(ctx, member: discord.Member, *, reason=None):
    if reason is None:
        await ctx.send(f'{ctx.author.mention}, please provide a reason for the warning.')
    else:
        await ctx.send(f'{member.mention}, you have been warned for: {reason}')

@warn.error
async def warn_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You don't have permission to use this command.")

# Rock, Paper, Scissors command
@bot.command(aliases=["RPS"])
async def rps(ctx, user_choice: str):
    user_choice = user_choice.lower()  # Convert user's input to lowercase
    choices = ['rock', 'paper', 'scissors']
    if user_choice not in choices:
        await ctx.send("Invalid choice! Please choose rock, paper, or scissors.")
        return

    bot_choice = random.choice(choices)
    result = ""
    if user_choice == bot_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        result = f'You win! You chose {user_choice} and I chose {bot_choice}.'
    else:
        result = f'I win! You chose {user_choice} and I chose {bot_choice}.'

    await ctx.send(result)

# Commands
@bot.command(aliases=["Commands", "CMD", "cmd", "Command", "command"])
async def commands(ctx):
    embed = discord.Embed(title="All the commands", description="List of available commands:", color=0x00ff00)
    embed.add_field(name="!Hello", value="Responds with 'Hello!'", inline=False)
    embed.add_field(name="!Goodmorning", value="Responds with 'Says Goodmorning to a member'", inline=False)
    embed.add_field(name="!Ban [member] [reason]", value="Bans a member with an optional reason. Requires ban permissions.", inline=False)
    embed.add_field(name="!Kick [member] [reason]", value="Kicks a member with an optional reason. Requires kick permissions.", inline=False)
    embed.add_field(name="!Mute [member] [reason]", value="Mutes a member with an optional reason. Requires manage roles permissions.", inline=False)
    embed.add_field(name="!Prune [member] [limit]", value="Deletes up to the specified limit of messages from a member. Requires manage messages permissions.", inline=False)
    embed.add_field(name="!Echo [message]", value="Echoes the message after deleting the original command message.", inline=False)
    embed.add_field(name="!Warn [member] [reason]", value="Warns a member with a specified reason. Requires manage messages permissions.", inline=False)
    embed.add_field(name="!rps [choice]", value="Plays Rock, Paper, Scissors. Choose rock, paper, or scissors.", inline=False)
    embed.add_field(name="!Cat", value="Responds with sending a cat meme", inline=False)
    embed.add_field(name="!Twitch", value="Responds with sending the link to Gruffs Twitch", inline=False)
    embed.add_field(name="!Support", value="Responds with sending the link to this bots support server invite", inline=False)
    embed.add_field(name="/8Ball", value="Ask a question and recieve an answer from the magic 8-Ball", inline=False)
    embed.add_field(name="/Ping", value="Responds with Pong", inline=False)
    embed.add_field(name="/Pingbot", value="Pings the bot to the server to see it's latency", inline=False)
    embed.add_field(name="/Sync", value="Responds with Syncing...", inline=False)
    embed.add_field(name="/Joke", value="Tells you a random joke from the database", inline=False)
    await ctx.send(embed=embed)
    
bot.run(TOKEN)
