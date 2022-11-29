from code import interact
import discord
from discord import app_commands, guild
from discord.ext import *
from discord.utils import *
import os
import asyncio
import datetime
import time
import requests
import datetime
import time

currentdate_epoch = time.time()
currentdate_epoch = int(currentdate_epoch)
currentdate = datetime.datetime.fromtimestamp(currentdate_epoch)

print(f"""Started running:
{currentdate}
{currentdate_epoch}""")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

with open("token.txt") as fp: TOKEN = fp.read().strip()

phrases = ['how to join', 'join server', 'join rp', 'how i join', 'want to join rp', 'join rp','how can i join','how do i join','how to get in rp','get rp','into rp','in rp','get in rp','join rp',]
phrases_generic = ['on ','','on my ','with ','with my ','using ',]
consoles_xbox = ['xbox','xbox series x','xbox series s','xbox one','xbox 1','xbox 1 s','xbox one s', 'xbox 1 x','xbox one x',]
consoles_ps4 = ['ps4','playstation 4','playstation four',]
consoles_ps5 = ['ps5','playstation 5','playstaton five']
consoles_fivem = ['fivem','five-m','five m','5 m','5m']

phrases_ps4 = []
phrases_ps5 = []
phrases_xbox = []
for x in phrases_generic:
    for y in consoles_xbox:
        add = f"{x}{y}"
        phrases_xbox.append(add)
    for y in consoles_ps4:
        add = f"{x}{y}"
        phrases_ps4.append(add)
    for y in consoles_ps5:
        addd = f"{x}{y}"
        phrases_ps5.append(add)
phrases_ps45 = phrases_ps4 + phrases_ps5

channel_howtojoin = 1030296552218050736
channel_xboxserver = 1041007190850420779
channel_playstationserver = 1041007141185650719

channel_sessionannoucements = 1036399898943303740
channel_2 = 1046823014056079380

me = 458657458995462154
bot = 1046576383662501998

greensquare = "\U0001f7e9"
greencircle = "\U0001f7e2"
bluesquare = "\U0001f7e6"
bluecircle = '\U0001f535'
orangesquare = "\U0001f7e7"
orangecircle = "\U0001f7e0"
whitesquare = "\U00002b1c"
whitecircle = "\U000026aa"

clock_late = '<a:clock_:1046808379357659216>'
check_ontime = '<a:check_:1046808377373769810>'
x_notcoming = '<a:X_:1046808381266067547>'

admins = [me,]

nomessage = True

now = datetime.datetime.now()
cyear = int(now.year)
cmonth = int(now.month)
cmonth2 = str(cmonth)
cday = int(now.day)
chour = int(now.hour)
cminute = int(now.minute)
csecond = int(now.second)

class Confirmbutton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()

class PersistentView1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is green.', ephemeral=True)

    @discord.ui.button(label='Red', style=discord.ButtonStyle.red, custom_id='persistent_view:red')
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is red.', ephemeral=True)

    @discord.ui.button(label='Grey', style=discord.ButtonStyle.grey, custom_id='persistent_view:grey')
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('This is grey.', ephemeral=True)

class SessionButton1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label=f'Attending', style=discord.ButtonStyle.green, custom_id='persistent_view:green',emoji=check_ontime)
    async def green(self, interaction: discord.Interaction, button: discord.ui.Button):
        e,f,g = session_attending(interaction.user,1)
        if e:
            # no need to run function again as they have been added already
            await interaction.response.send_message(f'Listed you as **Attending**. {check_ontime}', ephemeral=True)
        elif e == False:
            if f != True:
                if g == 1:
                    remove_session_attending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending**. {check_ontime}', ephemeral=True)
                if g == 2:
                    remove_session_attendinglate(interaction.user,1)
                    session_attending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending Late** {clock_late} and listed you as **Attending**. {check_ontime}', ephemeral=True)
                if g == 3:
                    remove_session_notattending(interaction.user,1)
                    session_attending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Not Attending**. {x_notcoming} and listed you as **Attending**. {check_ontime}', ephemeral=True)




    @discord.ui.button(label=f'Attending Late', style=discord.ButtonStyle.gray, custom_id='persistent_view:gray',emoji=clock_late)
    async def red(self, interaction: discord.Interaction, button: discord.ui.Button):
        e,f,g = session_attendinglate(interaction.user,1)
        if e:
            # no need to run function again as they have been added already
            await interaction.response.send_message(f'Listed you as **Attending Late**. {clock_late}', ephemeral=True)
        elif e == False:
            if f != True:
                if g == 1:
                    remove_session_attending(interaction.user,1)
                    session_attendinglate(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending** {check_ontime} and listed you as **Attending Late**. {clock_late}', ephemeral=True)
                if g == 2:
                    remove_session_attendinglate(interaction.user,1)
                    session_attendinglate(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending Late** {clock_late}', ephemeral=True)
                if g == 3:
                    remove_session_notattending(interaction.user,1)
                    session_attendinglate(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Not Attending**. {x_notcoming} and listed you as **Attending Late**. {clock_late}', ephemeral=True)



    @discord.ui.button(label=f'Not Attending', style=discord.ButtonStyle.red, custom_id='persistent_view:red',emoji=x_notcoming)
    async def grey(self, interaction: discord.Interaction, button: discord.ui.Button):
        #await interaction.response.send_message('This is grey.', ephemeral=True)
        e,f,g = session_notattending(interaction.user,1)
        if e:
            # no need to run function again as they have been added already
            await interaction.response.send_message(f'Listed you as **Not Attending**. {x_notcoming}', ephemeral=True)
        elif e == False:
            if f != True:
                if g == 1:
                    remove_session_attending(interaction.user,1)
                    session_notattending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending** {check_ontime} and listed you as **Not Attending**. {x_notcoming}', ephemeral=True)
                if g == 2:
                    remove_session_attendinglate(interaction.user,1)
                    session_notattending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Attending Late** {clock_late} and listed you as **Not Attending**. {x_notcoming}', ephemeral=True)
                if g == 3:
                    remove_session_notattending(interaction.user,1)
                    await interaction.response.send_message(f'Unlisted you as **Not Attending**. {x_notcoming}', ephemeral=True)

class startbot(discord.Client):
    def __init__(self):
        super().__init__(timeout=None)

    def setupbuttons(self):
        self.add_view(PersistentView1())

    def setupbuttons2(self):
        self.add_view(SessionButton1())

def gotosession(sessionnum):
    sessionnum = str(sessionnum)
    os.chdir('sessions')
    try:
        os.chdir(sessionnum)
    except:
        os.mkdir(sessionnum)
        os.chdir(sessionnum)
    
def remove_line(fileName,lineToSkip):
    # Removes a given line from a file
    with open(fileName,'r') as read_file:
        lines = read_file.readlines()

    currentLine = 1
    with open(fileName,'w') as write_file:
        for line in lines:
            if currentLine == lineToSkip:
                pass
            else:
                write_file.write(line)
            currentLine += 1

def checkuser(user):
    with open('attending.txt','r') as f:
        lines = f.readlines()
        found = False, 0, False
        timesran = 0
        for line in lines:
            timesran += 1
            if f"{user.name} ({user.id})\n" == line:
                found = True, timesran, 1
    with open('attending_late.txt','r') as f:
        lines = f.readlines()
        timesran = 0
        for line in lines:
            timesran += 1
            if f"{user.name} ({user.id})\n" == line:
                found = True, timesran, 2
    with open('not_attending.txt','r') as f:
        lines = f.readlines()
        timesran = 0
        for line in lines:
            timesran += 1
            if f"{user.name} ({user.id})\n" == line:
                found = True, timesran, 3
    return found

def session_attending(user,sessionnum):
    if str(os.getcwd())[:-1] != "/Users/johnmulligan/Documents/automation/socialmedia-automation/discord-automation/newuser-automation/sessions/":
        gotosession(sessionnum)
    founduser, line, num = checkuser(user)
    if founduser == False:
        with open('attending.txt','a+') as f:
            f.write(f"{user.name} ({user.id})\n")
            return True, True, True
    else:
        return False, line, num

def session_attendinglate(user,sessionnum):
    if str(os.getcwd())[:-1] != "/Users/johnmulligan/Documents/automation/socialmedia-automation/discord-automation/newuser-automation/sessions/":
        gotosession(sessionnum)
    founduser, line, num = checkuser(user)
    if founduser == False:
        with open('attending_late.txt','a+') as f:
            f.write(f"{user.name} ({user.id})\n")
            return True, True, True
    else:
        return False, line, num

def session_notattending(user,sessionnum):
    if str(os.getcwd())[:-1] != "/Users/johnmulligan/Documents/automation/socialmedia-automation/discord-automation/newuser-automation/sessions/":
        gotosession(sessionnum)
    founduser, line, num = checkuser(user)
    if founduser == False:
        with open('not_attending.txt','a+') as f:
            f.write(f"{user.name} ({user.id})\n")
            return True, True, True
    else:
        return False, line, num

def remove_session_attending(user,sessionnum):
    e,f,g = checkuser(user)
    remove_line('attending.txt',g)

def remove_session_attendinglate(user,sessionnum):
    e,f,g = checkuser(user)
    remove_line('attending_late.txt',g)

def remove_session_notattending(user,sessionnum):
    e,f,g = checkuser(user)
    remove_line('not_attending.txt',g)

def getjoinmessage(authorid,requestedby):
    return f"""Hello <@{authorid}>!

I see you would like to join the server. If this is the case follow the steps below:

<:xbox:1046582352794636370> If you are on **Xbox**, see this channel for more info: <#{channel_xboxserver}>

<:ps4:1046582534940672091> If you are on **PS4/5**, see this channel for more info: <#{channel_playstationserver}>

<:fivem:1046602426796486766> If you are on **FiveM**, please talk to the Head of FiveM Operations for more info.

Please note we only RP on the **last gen** version of GTA 5.

In addition, make sure to read <#{channel_howtojoin}>.

*Requested by:* <@{requestedby}>"""

def getjoinmessage_xbox(authorid,requestedby):
    return f"""Hello <@{authorid}>!

I see you would like to join our xbox server. If this is the case follow the steps below:

<:xbox:1046582352794636370> If you are on **Xbox**, see this channel for more info: <#{channel_xboxserver}>

Please note we only RP on the **last gen** version of GTA 5.

In addition, make sure to read <#{channel_howtojoin}>.

*Requested by:* <@{requestedby}>"""

def getjoinmessage_ps45(authorid,requestedby):
    return f"""Hello <@{authorid}>!

I see you would like to join our PS4/5 server. If this is the case follow the steps below:

<:ps4:1046582534940672091> If you are on **PS4/5**, see this channel for more info: <#{channel_playstationserver}>

Please note we only RP on the **last gen** version of GTA 5.

In addition, make sure to read <#{channel_howtojoin}>.

*Requested by:* <@{requestedby}>"""

def getjoinmessage_fivem(authorid,requestedby):
    return f"""Hello <@{authorid}>!

I see you would like to join our FiveM server. If this is the case follow the steps below:

<:fivem:1046602426796486766> If you are on **FiveM**, please talk to the Head of FiveM Operations for more info.

In addition, make sure to read <#{channel_howtojoin}>.

*Requested by:* <@{requestedby}>"""

@tree.command(name = "commandname", description = "My first application Command",) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

@tree.command(name='ban',description='bans and logs reason')
async def ban(interaction,user: str,reason: str):
    if interaction.user.id in admins:
        if user.isnumeric():
            # user id
            user = client.get_user(user)
        else:
            try:
                user = discord.utils.get(interaction.guild.members,name=user)
            except:
                interaction.response.send_message("Could not find user",ephemeral=True)
                user=None

        if user != None:
            try:
                await user.ban(reason=f"{interaction.user.id} ({interaction.user.name}): {reason}")
                banned = True
            except:
                interaction.response.send_message("Don't have perms",ephemeral=True)
            if banned:
                channelid = 1034468707554041866
                channel = client.get_channel(channelid)
                now = datetime.datetime.now()
                now = datetime.datetime.timestamp(now)
                channel.send(f"<@{interaction.user.id}> banned user <@{user.id}> at <t:{now}:F>. Reason: {reason}")
    else:
        now = datetime.datetime.now()
        now = datetime.datetime.timestamp(now)
        with open('idiots.txt','a+') as f:
            f.write(f"{interaction.user.id} ({interaction.author.name}): {datetime.datetime.fromtimestamp(now)} ({now})\n")
        interaction.response.send_message("Nice try buddy. Logged to idiot log.",)#ephemeral=True)        

@client.event
async def on_raw_reaction_add(payload):
    channelid = payload.channel_id
    emoji = payload.emoji
    messageid = payload.message_id
    userid = payload.user_id
    guildid = payload.guild_id

    channel = client.get_channel(channelid)
    guild = client.get_guild(guildid)
    user = client.get_user(userid)
    message = await channel.fetch_message(messageid)

    if channelid == channel_2:
        #channel = await bot.fetch_channel(payload.channel_id)
        #message = await channel.fetch_message(payload.message_id)
        # iterating through each reaction in the message
        for r in message.reactions:
            # checks the reactant isn't a bot and the emoji isn't the one they just reacted with
            userlist = [user async for user in r.users()]
            if payload.member in userlist and not payload.member.bot and str(r) != str(payload.emoji):
                # removes the reaction
                await message.remove_reaction(r.emoji, payload.member)
    #print(emoji)
    #print(greensquare)
    #print(type(emoji))
    #print(type(greensquare))
    #print(message.reactions)
    emoji_str = str(emoji)
    if userid == me:
        if emoji_str == greensquare:
            print('ran')
            await message.clear_reaction(greensquare)
            await message.reply(f"""<@{message.author.id}> Please do not advertise any servers or services with monetary gain or "free money" involved.""")
        # How to join
        if emoji_str == whitecircle:
            await message.clear_reaction(whitecircle)
            await message.reply(getjoinmessage(message.author.id,bot))
        if emoji_str == orangecircle:
            await message.clear_reaction(orangecircle)
            await message.reply(getjoinmessage_fivem(message.author.id,bot))
        if emoji_str == bluecircle:
            await message.clear_reaction(bluecircle)
            await message.reply(getjoinmessage_ps45(message.author.id,bot))
        if emoji_str == greencircle:
            await message.clear_reaction(greencircle)
            await message.reply(getjoinmessage_xbox(message.author.id,bot))

@tree.command(name='button1',description='makes button1')
async def button(interaction):
    if interaction.user.id == me:
        """Asks the user a question to confirm something."""
        # We create the view and assign it to a variable so we can wait for it later.
        view = Confirmbutton()
        await interaction.response.send_message('Do you want to continue?', view=view)
        # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
            print('Timed out...')
        elif view.value:
            print('Confirmed...')
        else:
            print('Cancelled...')

        async def setup_hook(client):
            client.add_view(PersistentView1())

@tree.command(name='staticbutton',description='makes static button')
async def staticbutton(interaction,content: str):
    if interaction.user.id == me:
        view = PersistentView1()
        try:
            await interaction.channel.send(content,view=view)
            await interaction.response.send_message(f"{check_ontime} Sucessfully made the button.",ephemeral=True)
        except:
            await interaction.response.send_message(f"{x_notcoming} Could not make the button.",ephemeral=True)

@tree.command(name='postsessionannoucement',description='post session annoucement. Only availible if you are a session host. Note times are in CST.')
@app_commands.describe(month='Months in the year')
@app_commands.choices(month=[
    app_commands.Choice(name='January', value=1),
    app_commands.Choice(name='Febuary', value=2),
    app_commands.Choice(name='March', value=3),
    app_commands.Choice(name="April",value=4),
    app_commands.Choice(name="May",value=5),
    app_commands.Choice(name="June",value=6),
    app_commands.Choice(name="July",value=7),
    app_commands.Choice(name="August",value=8),
    app_commands.Choice(name="September",value=9),
    app_commands.Choice(name="October",value=10),
    app_commands.Choice(name="November",value=11),
    app_commands.Choice(name="December",value=12),
    app_commands.Choice(name='Current',value=13)])

@app_commands.describe(ampm="Select whether time given is AM or PM.")
@app_commands.choices(ampm=[
    app_commands.Choice(name='AM',value=''),
    app_commands.Choice(name='PM',value='pm'),])
#async def postsession(interaction,hostgamertag: str,aop: str,year: int=cyear,month: str=cmonth2,day: int=cday,hour: int=chour,minute: int=cminute,second: int=csecond,ampm: str="",channelid: str='1036399898943303740'):
#async def postsession(interaction,hostgamertag: str,aop: str,year: int=cyear,month: Choice[int],day: int=cday,hour: int=chour,minute: int=cminute,second: int=csecond,ampm: str="",channelid: str='1036399898943303740'):
async def postsession(interaction,hostgamertag: str,aop: str,year: int=None,month: app_commands.Choice[int]=None,day: int=None,hour: int=None,minute: int=None,second: int=None,ampm: str="",channelid: str='1036399898943303740',usebutton: bool=True):
    if ampm != "":
        if ampm.lower() == 'pm':
            hour += 12
    
    now = datetime.datetime.now()
    if year is None:
        year = int(now.year)
    if month in [None,"Current",13,0]:
        month = int(now.month)
    if day is None:
        day = int(now.day)
    if hour is None:
        hour = int(now.hour)
    if minute is None:
        minute = int(now.minute)
    if second == None:
        second = int(now.second)
    
    #await interaction.response.send_message(thinking = True)
    await interaction.response.defer(thinking=True,ephemeral=True)

    #if month.isnumeric():
    #    month = int(month)
    #    ran1 = True
    #else:
    #    ran1 = True
    #    m = month.lower()
    #    if m == 'january':
    #        month = 1
    #    elif m == 'febuary':
    #        month = 2
    #    elif m == 'march':
    #       month = 3
    #    elif m == 'april':
    #        month = 4
    #    elif m == 'may':
    #        month = 5
    #    elif m == 'june':
    #        month = 6
    #    elif m == 'july':
    #        month = 7
    #    elif m == 'august':
    #        month = 8
    #    elif m == 'september':
    #        month = 9
    #    elif m == 'october':
    #        month = 10
    #    elif m == 'november':
    #        month = 11
    #    elif m == 'december':
    #        month = 12
    #    else:
    #        interaction.response.send_message("invalid month")
    #        ran1 = False
    
    try:
        channelid = int(channelid)
        ran = True
    except:
        await interaction.response.send_message("Channel must be an `int`")
        ran = False
    #if ran1 and ran2:
    #if ran2:
    #    ran = True
    #else:
    #    ran = False

    if ran:
        sessionpingrole = 1031737503281053748
        #channelid = 1036399898943303740
        channel = client.get_channel(channelid)

        if channel is None:
            print("nonetype")

        clock_late = '<a:clock_:1046808379357659216>'
        check_ontime = '<a:check_:1046808377373769810>'
        x_notcoming = '<a:X_:1046808381266067547>'

        #month = int(month.value)
        #print(month)
        #print(type(month))

        datetimeobj = datetime.datetime(year,int(month),day,hour,minute,second,0,None)
        time = int(datetime.datetime.timestamp(datetimeobj))

        content = f"""════════════════════════════════════════════════════

<@{sessionpingrole}>

════════════════════════════════════════════════════

・Main Information

・Name of host: <@{interaction.user.id}>
・Host gamertag: {hostgamertag}
・Time: <t:{time}:F> (Adapts to your timezone)
・AOP: {aop}

════════════════════════════════════════════════════

・Additional Information

・Invites will be announced with a gamer tag attached, shortly after the awaiting invite announcement goes out.
・Have your mics muted upon entering Awaiting Invite. if any questions, issues or concerns arise state the term PTS (Permission To Speak). Once granted permission you are free to ask your question.
・Always make sure to message the Xbox tag assigned, NOT anyone else!

════════════════════════════════════════════════════

{check_ontime} - Attending
{x_notcoming} - Not Attending
{clock_late} - Attending Late

════════════════════════════════════════════════════

Timezones: Above timestamp adjusts to your timezone, however a map is below:"""

        file = discord.File("images/timezones.jpeg", filename="timezones.jpeg")
        embedimage = discord.Embed()
        embedimage.set_image(url="attachment://timezones.jpeg")
        
        #message = await channel.send(content,file=file,embed=embedimage)

        if usebutton:
            view = SessionButton1()
            message = await channel.send(content,file=file,embed=embedimage,view=view)
        if usebutton == False:
            message = await channel.send(content,file=file,embed=embedimage)
            await message.add_reaction(check_ontime)
            await message.add_reaction(clock_late)
            await message.add_reaction(x_notcoming)
        await interaction.followup.send(f"{check_ontime} Sucessfully posted session annoucement in <#{channel.id}>.",ephemeral=True)

@tree.command(name='updatecommands',description='Owner only. Updates command tree.')
async def updatecommands(interaction):
    if interaction.user.id == me:
        await tree.sync()
        #startbot.setupbuttons(client)
        await interaction.response.send_message("Updated command tree.",ephemeral=True)
    else:
        await interaction.response.send_message('no.',ephemeral=True)

# ephemeral
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user.mention in message.content.split():
        if message.author.id != me:
            await message.reply("No more pings.")
    
    if message.reference != None and not message.is_system :
        ref = await message.channel.fetch_message(message.reference.message_id)
        if ref.author == 1046576383662501998:
            await message.reply("No. (well unless you are <@694187304910192650> then yes)") #reply to a specific message with its id
    
    if "ban" in message.content.lower():
        if client.user.mention in message.content.split():
            await message.add_reaction('\U0001f631') # 0_0
        else:
            await message.add_reaction('\U0001f633') # scream
    e = message.content.lower()
    if ("hi" in e) or ("hello" in e):
        wave = '\U0001f44b'
        await message.add_reaction(wave)

    for x in consoles_xbox:
        if x in message.content.lower():
            if "cool" in message.content.lower():
                await message.add_reaction("<:xbox2:1046582503445643274>")
                break
            else:
                await message.add_reaction("<:xbox:1046582352794636370>")
                break
    for x in consoles_ps4:
        if x in message.content.lower():
            await message.add_reaction("<:ps4:1046582534940672091>")
            break
    for x in consoles_ps5:
        if x in message.content.lower():
            await message.add_reaction("<:ps4:1046582534940672091>")
            break
    for x in consoles_fivem:
        if x in message.content.lower():
            await message.add_reaction("<:fivem:1046602426796486766>")

    for x in phrases:
        if x in message.content.lower():
            nomessage = True
            for y in phrases_xbox:
                if y in message.content.lower():
                    await message.reply(getjoinmessage_xbox(message.author.id,bot),mention_author=True)
                    await message.add_reaction("<:xbox:1046582352794636370>")
                    nomessage = False
                    break
            for y in phrases_ps45:
                if y in message.content.lower():
                    await message.reply(getjoinmessage_ps45(message.author.id,bot),mention_author=True)
                    await message.add_reaction("<:ps4:1046582534940672091>")
                    nomessage = False
                    break
            
            if nomessage:
                await message.reply(getjoinmessage(message.author.id,bot),mention_author=True)
                nomessage = False

async def pings():
    ch = client.get_channel(1030296552603926610)
    await ch.send("<@964374152712704051> I don't like being pinged.")

guild = 1030296550846505020

@client.event
async def on_ready():
    startbot.setupbuttons(client)
    #await tree.sync()
    print("Ready!")
    #await pings()
    #await funny()

print(TOKEN)
#bot = PersistentViewBot()
#bot.run(TOKEN)
client.run(TOKEN)
