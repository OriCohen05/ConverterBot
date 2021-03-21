import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$', case_insensitive=True)


@client.event
async def on_ready():
    print('Logged as:\t', client.user.name)
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="$info, Im under construction"))



@client.command()
async def convert(ctx, *, msg, ):
    letters = {

        # Small letters:

        'a': ':regional_indicator_a:', 'b': ':regional_indicator_b:', 'c': ':regional_indicator_c:',
        'd': ':regional_indicator_d:', 'e': ':regional_indicator_e:', 'f': ':regional_indicator_f:',
        'g': ':regional_indicator_g:', 'h': ':regional_indicator_h:', 'i': ':regional_indicator_i:',
        'j': ':regional_indicator_j:', 'k': ':regional_indicator_k:', 'l': ':regional_indicator_l:',
        'm': ':regional_indicator_m:', 'n': ':regional_indicator_n:', 'o': ':regional_indicator_o:',
        'p': ':regional_indicator_p:', 'q': ':regional_indicator_q:', 'r': ':regional_indicator_r:',
        's': ':regional_indicator_s:', 't': ':regional_indicator_t:', 'u': ':regional_indicator_u:',
        'v': ':regional_indicator_v:', 'w': ':regional_indicator_w:', 'x': ':regional_indicator_x:',
        'y': ':regional_indicator_y:', 'z': ':regional_indicator_z:',

        # Numbers:

        '1': ':one:', '2': ':two:', '3': ':three:', '4': ':four:', '5': ':five:',
        '6': ':six:', '7': ':seven:', '8': ':eight:', '9': ':nine:', '10': ':keycap_ten:', '0': ':zero:',

        # Symbols:

        '/': '/', '.': '.', "'": "'", '"': '"', ' ': '  ', "#": '#', '@': '@', '*': '*',
        '-': '-', '_': '_', '(': '(', ')': ')', '=': '=', '+': '+', '!': '!', '?': '?',
        '<': '<', '>': '>', '{': '{', '[': '[', '}': '}', ']': ']', ';': ';', ':': ':'}
    await ctx.send(" ".join(letters[x] for x in msg.lower() if x in letters))


@client.command()
async def invite(ctx):
    await ctx.send("""Invite me: 
    \n https://discord.com/api/oauth2/authorize?client_id=822480756316045323&permissions=67136512&scope=bot""")


@client.command()
async def info(ctx):
    def check(m):
        return m.author.id == ctx.message.author.id and m.channel == ctx.channel

    await ctx.send(
        'Which info do you want to know?\n Type "about" to know some about me \n Type "bot" to know my commands.\n '
        'Type "both" to see both. ')
    myinfo = await client.wait_for('message', check=check)

    if myinfo.content == 'about':

        await ctx.send("""**__Info about me:__** \n
        Im **Converter** , All you need. \n
        Im taking regular and boring sentences and turn them into - **MAJESTIC** letters-emojis.\n
        you probably wonder-\n
        **__How did the developers make me?__**\n
        Im based on *Discod.py API*  and coded by-\n
        Ori Cohen,As known as: Ori | Gunt4R#0006 . \n
        Hope you will enjoy me! \t \n**Converter**.
        """)
    elif myinfo.content == 'bot':
        await ctx.send("""**__My commands:__**\n
        ```
            $convert { message } - Converting the message to letters emojis.
            $info - Shows this message (Only if you choose 'bot')
            $invite - Shows my invite link (Do it)
            ```
        """)
    elif myinfo.content == 'both':
        await ctx.send("""
        **__Info about me:__** \n
        Im **Converter** , All you need. \n
        Im taking regular and boring sentences and turn them into - **MAJESTIC** letters-emojis.\n
        you probably wonder-\n
        **__How did the developers make me?__**\n
        Im based on *Discod.py API* and coded by-\n
        Ori Cohen,As known as: Ori | Gunt4R#0006 . \n
        Hope you will enjoy me! \t \n**Converter**. \n
        -------------------------------------------
        **__My commands:__**\n
        ```
            $convert { message } - Converting the message to letters emojis.
            $info - Shows this message (Only if you choose 'bot')
            $invite - Shows my invite link (Do it)
            ```
        """)


client.run('ODIyNDgwNzU2MzE2MDQ1MzIz.YFS45Q.esgzNUIWlUkw9N09ImUdjM2Du1I')

print('all rights saved to Ori Cohen')
