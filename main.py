import discord
from discord.ext import commands
#from key import Token
import random

intents = discord.Intents.default()
intents.members = True
bot=commands.Bot(command_prefix='./',intents = intents)
jobs1 = {'Destroyer':[958786150863089704,958959054456225882],'WarLord':[0,0],'Berserker':[0,0],'HolyKnight':[0,0],'BattleMaster':[0,0],'infighter':[0,0],'SoulMater':[0,0],'LanceMaster':[0,0],'Striker':[0,0],'DevilHunter':[0,0],'Blaster':[0,0],'HawkEye':[0,0],'Scouter':[0,0],'GunSlinger':[0,0]}
jobs2 = {'Bard':[0,0],'Summoner':[0,0],'Arcana':[0,0],'Sorceress':[0,0],'Blade':[0,0],'Demonic':[0,0],'Reaper':[0,0],'Artist':[0,0]}
servers = {'1️⃣':959010842416906250,'2️⃣':0,'3️⃣':0,'4️⃣':0,'5️⃣':0,'6️⃣':0,'7️⃣':0,'8️⃣':0}

@bot.event
async def on_ready():
    print('봇이 작동 시도중입니다.')
    print(f"봇={bot.user.name} 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("어쩔티비 저쩔래미 무슨소리인지 모르겠는 명령어!")

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = None
    for tc in guild.text_channels:
        if tc.id == 959012156332974083:
            channel = tc
    if channel == None:
        return None
    await channel.send(f"{member.mention}서버에 입장하신것을 환영합니다. {channel.mention} 부탁드립니다.")

@bot.command(aliases=['server'])
async def 서버(ctx,text=None):
    if ctx.author.id == 262582555813871618:
        embed = discord.Embed(title="서버",color=0xFFD700)
        embed.add_field(name="서버",value=f":one: 카단\n\n:two:카제로스\n\n:three:실리안\n\n:four:아브렐슈드\n\n:five:아만\n\n:six:루페온\n\n:seven:니나브\n\n:eight:카마인",inline=True)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("8️⃣")
    else:
        return None

@bot.command(aliases=['character'])
async def 캐릭터(ctx,text=None):
    if ctx.author.id == 262582555813871618:
        embed = discord.Embed(title="본캐 직업Ⅰ",color=0xFFD700)
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name == "Destroyer":
                a[0] = em
            elif em.name =="WarLord":
                a[1] = em
            elif em.name == "Berserker":
                a[2] = em
            elif em.name =="HolyKnight":
                a[3] = em
        embed.add_field(name="슈사이어",value=f"{a[0]} 디스트로이어\n\n{a[1]} 워로드\n\n{a[2]} 버서커\n\n{a[3]} 홀리나이트",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "BattleMaster":
                a[0] = em
            elif em.name =="infighter":
                a[1] = em
            elif em.name == "SoulMater":
                a[2] = em
            elif em.name =="LanceMaster":
                a[3] = em
            elif em.name =="Striker":
                a[4] = em
        embed.add_field(name="애니츠",value=f"{a[0]} 배틀마스터\n\n{a[1]} 인파이터\n\n{a[2]} 기공사\n\n{a[3]} 창술사\n\n{a[4]} 스트라이커",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "DevilHunter":
                a[0] = em
            elif em.name =="Blaster":
                a[1] = em
            elif em.name == "HawkEye":
                a[2] = em
            elif em.name =="Scouter":
                a[3] = em
            elif em.name =="GunSlinger":
                a[4] = em
        embed.add_field(name="아르덴타인",value=f"{a[0]} 데빌헌터\n\n{a[1]} 블래스터\n\n{a[2]} 호크아이\n\n{a[3]} 스카우터\n\n{a[4]} 건슬링어",inline=True)
        msg = await ctx.send(embed=embed)
        for em in ctx.guild.emojis:
            if em.name in str(jobs1):
                await msg.add_reaction(em)
        embed = discord.Embed(title="본캐 직업Ⅱ",color=0xFFD700)
        for em in ctx.guild.emojis:
            if em.name == "Bard":
                a[0] = em
            elif em.name =="Summoner":
                a[1] = em
            elif em.name == "Arcana":
                a[2] = em
            elif em.name =="Sorceress":
                a[3] = em
        embed.add_field(name="실린",value=f"{a[0]} 바드\n\n{a[1]} 서머너\n\n{a[2]} 아르카나\n\n{a[3]} 소서리스",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "Blade":
                a[0] = em
            elif em.name =="Demonic":
                a[1] = em
            elif em.name == "Reaper":
                a[2] = em
        embed.add_field(name="데런",value=f"{a[0]} 블레이드\n\n{a[1]} 데모닉\n\n{a[2]} 리퍼",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "Artist":
                a[0] = em
        embed.add_field(name="요즈",value=f"{a[0]} 도화가",inline=True)
        msg = await ctx.send(embed=embed)
        for em in ctx.guild.emojis:
            if em.name in str(jobs2):
                await msg.add_reaction(em)
        embed = discord.Embed(title="부캐 직업Ⅰ",color=0xFFD700)
        for em in ctx.guild.emojis:
            if em.name == "Destroyer":
                a[0] = em
            elif em.name =="WarLord":
                a[1] = em
            elif em.name == "Berserker":
                a[2] = em
            elif em.name =="HolyKnight":
                a[3] = em
        embed.add_field(name="슈사이어",value=f"{a[0]} 디스트로이어\n\n{a[1]} 워로드\n\n{a[2]} 버서커\n\n{a[3]} 홀리나이트\n\n여버서커",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "BattleMaster":
                a[0] = em
            elif em.name =="infighter":
                a[1] = em
            elif em.name == "SoulMater":
                a[2] = em
            elif em.name =="LanceMaster":
                a[3] = em
            elif em.name =="Striker":
                a[4] = em
        embed.add_field(name="애니츠",value=f"{a[0]} 배틀마스터\n\n{a[1]} 인파이터\n\n{a[2]} 기공사\n\n{a[3]} 창술사\n\n{a[4]} 스트라이커",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "DevilHunter":
                a[0] = em
            elif em.name =="Blaster":
                a[1] = em
            elif em.name == "HawkEye":
                a[2] = em
            elif em.name =="Scouter":
                a[3] = em
            elif em.name =="GunSlinger":
                a[4] = em
        embed.add_field(name="아르덴타인",value=f"{a[0]} 데빌헌터\n\n{a[1]} 블래스터\n\n{a[2]} 호크아이\n\n{a[3]} 스카우터\n\n{a[4]} 건슬링어",inline=True)
        msg = await ctx.send(embed=embed)
        for em in ctx.guild.emojis:
            if em.name in str(jobs1):
                await msg.add_reaction(em)
        embed = discord.Embed(title="부캐 직업Ⅱ",color=0xFFD700)
        for em in ctx.guild.emojis:
            if em.name == "Bard":
                a[0] = em
            elif em.name =="Summoner":
                a[1] = em
            elif em.name == "Arcana":
                a[2] = em
            elif em.name =="Sorceress":
                a[3] = em
        embed.add_field(name="실린",value=f"{a[0]} 바드\n\n{a[1]} 서머너\n\n{a[2]} 아르카나\n\n{a[3]} 소서리스",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "Blade":
                a[0] = em
            elif em.name =="Demonic":
                a[1] = em
            elif em.name == "Reaper":
                a[2] = em
        embed.add_field(name="데런",value=f"{a[0]} 블레이드\n\n{a[1]} 데모닉\n\n{a[2]} 리퍼",inline=True)
        for em in ctx.guild.emojis:
            if em.name == "Artist":
                a[0] = em
        embed.add_field(name="요즈",value=f"{a[0]} 도화가",inline=True)
        msg = await ctx.send(embed=embed)
        for em in ctx.guild.emojis:
            if em.name in str(jobs2):
                await msg.add_reaction(em)
    else:
        return None
    
@bot.event
async def on_raw_reaction_add(reaction):
    user = reaction.member
    if user.bot == 1:
        return None
    guild = user.guild
    emojis = guild.emojis
    roles = guild.roles
    channel = None
    for tc in guild.text_channels:
        if tc.id == reaction.channel_id:
            channel = tc
    if channel == None:
        return None
    msg = await channel.fetch_message(reaction.message_id)
    title = None
    for em in msg.embeds:
        title = em.title
    if title == None:
        return None
    if "본캐" in title:
        for job in jobs1.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs1[job][0]:
                        await user.add_roles(ro)
        for job in jobs2.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs2[job][0]:
                        await user.add_roles(ro)
    elif "부캐" in title:
        for job in jobs1.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs1[job][1]:
                        await user.add_roles(ro)
        for job in jobs2.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs2[job][1]:
                        await user.add_roles(ro)
    elif "서버" in title:
        for server in servers.keys() :
            if str(reaction.emoji.name) == server:
                for ro in roles:
                    if ro.id == servers[server]:
                        await user.add_roles(ro)

@bot.event
async def on_raw_reaction_remove(reaction):
    for g in bot.guilds:
        if g.id == reaction.guild_id:
            guild = g
    if guild == None:
        return None
    for u in await guild.query_members(user_ids=reaction.user_id):
        user = u
    if user.bot == 1:
        return None
    emojis = user.guild.emojis
    roles = user.guild.roles
    channel = None
    for tc in guild.text_channels:
        if tc.id == reaction.channel_id:
            channel = tc
    if channel == None:
        return None
    msg = await channel.fetch_message(reaction.message_id)
    title = None
    for em in msg.embeds:
        title = em.title
    if title == None:
        return None
    if "본캐" in title:
        for job in jobs1.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs1[job][0]:
                        await user.remove_roles(ro)
        for job in jobs2.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs2[job][0]:
                        await user.remove_roles(ro)
    elif "부캐" in title:
        for job in jobs1.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs1[job][1]:
                        await user.remove_roles(ro)
        for job in jobs2.keys():
            if str(reaction.emoji.name) == job:
                for ro in roles:
                    if ro.id == jobs2[job][1]:
                        await user.remove_roles(ro)
    elif "서버" in title:
        for server in servers.keys() :
            if str(reaction.emoji.name) == server:
                for ro in roles:
                    if ro.id == servers[server]:
                        await user.remove_roles(ro)
bot.run(Token)
