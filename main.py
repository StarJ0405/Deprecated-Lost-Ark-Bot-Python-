import discord
from discord.ext import commands, tasks
import datetime as date
from datetime import timedelta
#from key import Token
import random
import os
import re
import time as tm

intents = discord.Intents.all()
intents.members = True
bot=commands.Bot(command_prefix='%',intents = intents)
jobs1 = {'Destroyer':[858024177097244692,906130095050194984],'WarLord':[858024416364855297,906130181066993686],'Berserker':[858024445038034944,906130245512466462],'HolyKnight':[858024470040412220,906130259374665728],'BattleMaster':[858024753180835891,906130412844232737],'infighter':[858024790383788063,906130449028501544],'SoulMater':[858025164129304607,906130482931068958],'LanceMaster':[858025187680976896,906130507476127764],'Striker':[858025214456496128,906130526870573056],'DevilHunter':[858025356111249408,906130842454212658],'Blaster':[858025430287515678,906130898729189406],'HawkEye':[858025451288395777,906130923999887410],'Scouter':[858025468393816074,906130946426818571],'GunSlinger':[858025481579659315,906130991754649621]}
jobs2 = {'Bard':[858025651956350996,906131139217997825],'Summoner':[858025696127221830,906131494353920030],'Arcana':[858025726552047646,906131534300463125],'Sorceress':[858025772413616150,906131568031055902],'Blade':[858025950793170984,906131680748769300],'Demonic':[858025848447434772,906131604886405120],'Reaper':[858026091452956722,906131723132235787],'Artist_':[921874293397262346,921874430450348073],'Meteorologist':[956053418491904061,956053753264488458]}
servers = {'1️⃣':858632883585810453,'2️⃣':882618750598279249,'3️⃣':858632832292487168,'4️⃣':868902014967488562,'5️⃣':858632859979612180,'6️⃣':858809645162561557,'7️⃣':878299316937191424,'8️⃣':878997499208151070}
parties1 = {'1️⃣':959104004225380412,'2️⃣':959104077147562034,'3️⃣':959104100841177178,'4️⃣':964865404369506344,'5️⃣':964865388133355551,'6️⃣':959104109988962324,'7️⃣':959104210379636756,'8️⃣':959104230671646740,'9️⃣':959104261579485214}
parties2 = {'1️⃣':976897200967778405,'2️⃣':979080604341649408,'3️⃣':979081660396105738,'4️⃣':979081660396105738,'5️⃣':983037342250061894,'6️⃣':983038209401438349}
timers = [] 

class info:
    def __init__(self,datetime,msg,text,repeat=False):
        self.__datetime = datetime
        self.__msg = msg
        self.__repeat = repeat
        self.__text=text
    def getdatetime(self):
        return self.__datetime
    def getmsg(self):
        return self.__msg
    def isrepeat(self):
        return self.__repeat
    def gettext(self):
        return self.__text
    def add(self,timedelta):
        self.__datetime += timedelta
    
@bot.event
async def on_ready():
    print('봇이 작동 시도중입니다.')
    print(f"봇={bot.user.name} 연결중")
    print('연결이 완료되었습니다.')
    task_loop.start()
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("어쩔티비 저쩔래미 무슨소리인지 모르겠는 명령어!")

@bot.event
async def on_member_join(member):
    guild = member.guild
    channel = None
    channel2 = None
    for tc in guild.text_channels:
        if tc.id == 932908858354044928:
            channel = tc
        elif tc.id == 959063025111937065:
            channel2 = tc
    if channel == None:
        return None
    if channel2 == None:
        return None
    await channel.send(f"{member.mention}서버에 입장하신것을 환영합니다. {channel2.mention} 부탁드립니다.")

@tasks.loop(seconds=1)
async def task_loop():
    dellist = []
    for timer in timers:
        now = date.datetime.now() + timedelta(hours=9)
        res = timer.getdatetime() 
        dif = res - now
        if res < now:
            dellist.append(timer)
        elif dif < timedelta(days=1) and dif > timedelta(hours=23,minutes=59,seconds=59):
            mention = ""
            msg = timer.getmsg()
            for cached in bot.cached_messages:
                if cached.id == msg.id:
                    msg = cached
            for reaction in msg.reactions:
                async for user in reaction.users():
                    if not user.bot:
                        mention += user.mention
                    mention += ""
            await msg.channel.send(mention +"\n오늘 레이드가 있는 날이에요! 안까먹었죠?\n"+timer.gettext())
        elif dif < timedelta(minutes=10) and dif > timedelta(minutes=9,seconds=59):
            mention = ""
            msg = timer.getmsg()
            for cached in bot.cached_messages:
                if cached.id == msg.id:
                    msg = cached
            for reaction in msg.reactions:
                async for user in reaction.users():
                    if not user.bot:
                        mention += user.mention
                    mention += ""
            await msg.channel.send(mention+"\n레이드 10분 전! 늦으면 머머리\n"+timer.gettext())
        elif dif < timedelta(seconds=1):
            if timer.isrepeat():
                timer.add(timedelta(days=7))
            else:
                dellist.append(timer)
            mention = ""
            msg = timer.getmsg()
            for cached in bot.cached_messages:
                if cached.id == msg.id:
                    msg = cached
            for reaction in msg.reactions:
                async for user in reaction.users():
                    if not user.bot:
                        mention += user.mention
                    mention += ""
            await msg.channel.send(mention +"\n레이드 시간입니다. 모두 모여주세요!\n"+timer.gettext())
    for dell in dellist:
        msg = dell.getmsg()
        if msg is not None:
            await msg.edit(content="종료된 알람")
        timers.remove(dell)
        print(f"{dell.getdatetime()} - {dell.gettext()} 이 삭제되었습니다.")

@bot.command(aliases=['helps'])
async def 도움말(ctx):
    embed = discord.Embed(title="명령어",color=0xFFD700)
    embed.add_field(name="도움말",value=f"%예약 목록\n%예약 추가 [년-월-일-시-분] [반복=True/1회용=False] \"예약메시지\"\n예시) %예약 추가 2022-04-15-00-57 False 혜일세이튼 척살조 구합니다.\n%예약 삭제 [번호] - 번호는 목록에서 참조",inline=True)
    await ctx.send(embed=embed)

@bot.command(aliases=['reservation','res'])
async def 예약(ctx,types=None, datetime=None, repeat=False, *, text="빈 텍스트"):
    if "추가" in types:
        time = date.datetime.strptime(datetime,'%Y-%m-%d-%H-%M')
        if time is not None:
            embed = discord.Embed(title="레이드 예약",color=0xFFD700)
            embed.add_field(name=ctx.channel.name,value=f"{ctx.channel.mention}\n{time}시간에 레이드가 예약되었습니다.\n{text}\n매주 반복 : {repeat}",inline=True)
            msg = await ctx.send(embed=embed)
            if msg is not None:
                timers.append(info(time,msg,text,repeat))
        else:
            await ctx.send("%도움말")
            return None
    elif "목록" in types:
        num = 0
        msg = ""
        if len(timers) > 0:
            for time in timers:
                if msg != "":
                    msg +="\n"
                msg += str(num) + " : [" + str(time.getdatetime()) +"] - "+ time.gettext()
                num+=1
            await ctx.send(msg)
        else:
            await ctx.send("예약된 알람이 없습니다.")
            return None
    elif "제거" in types:
        if  datetime is not None and type(datetime) is str:
            datetime = int(datetime)
        if datetime >= 0 and datetime < len(timers):
            msg = timers[datetime].getmsg()
            if msg is not None:
                await msg.delete()
            del timers[datetime]
            await ctx.send(f"{dell.getdatetime()} - {dell.gettext()} 이 삭제되었습니다.")
        else:
            await ctx.send("%도움말")
            return None
    else:
        await ctx.send("%도움말")
    await ctx.message.delete()

@bot.command(aliases=['say'])
async def 말하기(ctx,*,text=None):
    if ctx.author.id == 262582555813871618:
        if text ==None:
            return None
        await ctx.message.delete()
        await ctx.send(text)
    else:
        await ctx.send("어허. 밑장빼기 금지 손모가지 날라간다!")
        return None

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

@bot.command(aliases=['party'])
async def 파티(ctx,text=None):
    if ctx.author.id == 262582555813871618:
        embed = discord.Embed(title="파티1",color=0xFFD700)
        embed.add_field(name="파티1",value=f":one: ①쿠크세이튼 1파티\n\n:two: ②쿠크세이튼 2파티\n\n:three: ③쿠크세이튼 3파티\n\n:four: ④쿠크세이튼 4파티\n\n:five: ⑤쿠크세이튼 5파티\n\n:six: ⑥쿠크세이튼 6파티\n\n:seven: ①아브렐슈드 12\n\n:eight: ①아브렐슈드 34\n\n:nine: ①아브렐슈드 56",inline=True)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
        await msg.add_reaction("7️⃣")
        await msg.add_reaction("8️⃣")
        await msg.add_reaction("9️⃣")
        embed = discord.Embed(title="파티2",color=0xFFD700)
        embed.add_field(name="파티2",value=f":one: ①하브렐슈드 12\n\n:two: ②하브렐슈드 34\n\n:three: ③하브렐슈드 56\n\n:four: ④카양겔 하드I 1파티\n\n:five: ⑤카양겔 하드II 1파티\n\n:six: ⑥카양겔 하드II 2파티",inline=True)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("1️⃣")
        await msg.add_reaction("2️⃣")
        await msg.add_reaction("3️⃣")
        await msg.add_reaction("4️⃣")
        await msg.add_reaction("5️⃣")
        await msg.add_reaction("6️⃣")
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
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name in str(jobs1):
                await msg.add_reaction(em)
        embed = discord.Embed(title="본캐 직업Ⅱ",color=0xFFD700)
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name == "Blade":
                a[0] = em
            elif em.name =="Demonic":
                a[1] = em
            elif em.name == "Reaper":
                a[2] = em
        embed.add_field(name="데런",value=f"{a[0]} 블레이드\n\n{a[1]} 데모닉\n\n{a[2]} 리퍼",inline=True)
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name == "Artist_":
                a[0] = em
            elif em.name =="Meteorologist":
                a[1] = em
        embed.add_field(name="요즈",value=f"{a[0]} 도화가\n\n{a[1]} 기상술사",inline=True)
        msg = await ctx.send(embed=embed)
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name in str(jobs2):
                await msg.add_reaction(em)
        embed = discord.Embed(title="부캐 직업Ⅰ",color=0xFFD700)
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
        embed.add_field(name="슈사이어",value=f"{a[0]} 디스트로이어\n\n{a[1]} 워로드\n\n{a[2]} 버서커\n\n{a[3]} 홀리나이트\n\n여버서커",inline=True)
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name in str(jobs1):
                await msg.add_reaction(em)
        embed = discord.Embed(title="부캐 직업Ⅱ",color=0xFFD700)
        a = [0 for col in range(5)]
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
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name == "Blade":
                a[0] = em
            elif em.name =="Demonic":
                a[1] = em
            elif em.name == "Reaper":
                a[2] = em
        Aembed.add_field(name="데런",value=f"{a[0]} 블레이드\n\n{a[1]} 데모닉\n\n{a[2]} 리퍼",inline=True)
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name == "Artist_":
                a[0] = em
            elif em.name =="Meteorologist":
                a[1] = em
        embed.add_field(name="요즈",value=f"{a[0]} 도화가\n\n{a[1]} 기상술사",inline=True)
        msg = await ctx.send(embed=embed)
        a = [0 for col in range(5)]
        for em in ctx.guild.emojis:
            if em.name in str(jobs2):
                await msg.add_reaction(em)
    else:
        return None

@bot.command(aliases=['fighting'])
async def 영차영차(ctx,text=None):
    if ctx.author.id == 262582555813871618:
        await ctx.message.delete()
        msg = f"헤처모여! 영차영차~!"
        for a in range(25):
            msg += "\n영차"+str(a+1)
        msg += "\n영차영차s 집합 완료!"
        await ctx.send(msg)
        '''
        await ctx.send("헤처모여! 영차영차~!")
        for a in range(20):
            await ctx.send(f"영차{a+1}")
            tm.sleep(1)
        await ctx.send("영차영차s 집합 완료!")
        '''
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
    embed = None
    for em in msg.embeds:
        embed = em
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
    elif "파티1" in title:
        for party in parties1.keys() :
            if str(reaction.emoji.name) == party:
                for ro in roles:
                    if ro.id == parties1[party]:
                        await user.add_roles(ro)
    elif "파티2" in title:
        for party in parties2.keys() :
            if str(reaction.emoji.name) == party:
                for ro in roles:
                    if ro.id == parties2[party]:
                        await user.add_roles(ro)
    elif "돌 깍기" in title:
        await msg.remove_reaction(reaction.emoji,user)
        fields = embed.fields
        one, two, thr = [0]*10,[0]*10,[0]*10
        chance,one_i,two_i,thr_i =0,0,0,0
        for ind in range(len(fields)):
            field = fields[ind]
            if field.name == "증가 능력1":
                one_i = ind
                f_value = field.value
                for i in range(len(f_value)):
                    c = f_value[i]
                    if c == '□':
                        one[i] = 0
                    elif c == '▩':
                        one[i] = -1
                    elif c == '■':
                        one[i] = 1
            elif field.name == "증가 능력2":
                two_i = ind
                f_value = field.value
                for i in range(len(f_value)):
                    c = f_value[i]
                    if c == '□':
                        two[i] = 0
                    elif c == '▩':
                        two[i] = -1
                    elif c == '■':
                        two[i] = 1
            elif field.name == "감소 능력":
                thr_i = ind
                f_value = field.value
                for i in range(len(f_value)):
                    c = f_value[i]
                    if c == '□':
                        thr[i] = 0
                    elif c == '▩':
                        thr[i] = -1
                    elif c == '■':
                        thr[i] = 1
            elif field.name == "성공 확률":
                chance = int(re.sub("%","",field.value))
        now  = random.randrange(0,100)
        if str(reaction.emoji.name) == "1️⃣" and one[9] == 0:
            field = fields[one_i]
            value = ""
            act = False
            for slot in range(len(one)):
                v = one[slot]
                if not act and v == 0:
                    act = True
                    if now < chance:
                        v=1
                    else:
                        v=-1
                if v == 0:
                    value += '□'
                elif v == -1:
                    value += '▩'
                elif v == 1:
                    value += '■'
            embed.set_field_at(index=one_i,name=field.name,value=value,inline=field.inline)
            await msg.edit(embed=embed)
        elif str(reaction.emoji.name) == "2️⃣" and two[9] == 0:
            field = fields[two_i]
            value = ""
            act = False
            for slot in range(len(two)):
                v = two[slot]
                if not act and v == 0:
                    act = True
                    if now < chance:
                        v=1
                    else:
                        v=-1
                if v == 0:
                    value += '□'
                elif v == -1:
                    value += '▩'
                elif v == 1:
                    value += '■'
            embed.set_field_at(index=two_i,name=field.name,value=value,inline=field.inline)
            await msg.edit(embed=embed)
        elif str(reaction.emoji.name) == "3️⃣" and thr[9] == 0:
            field = fields[thr_i]
            value = ""
            act = False
            for slot in range(len(thr)):
                v = thr[slot]
                if not act and v == 0:
                    act = True
                    if now < chance:
                        v=1
                    else:
                        v=-1
                if v == 0:
                    value += '□'
                elif v == -1:
                    value += '▩'
                elif v == 1:
                    value += '■'
            embed.set_field_at(index=thr_i,name=field.name,value=value,inline=field.inline)
            await msg.edit(embed=embed)
        elif str(reaction.emoji.name) == "🔁":
            for i in range(len(fields)):
                field = fields[i]
                if field.name == "성공 확률":
                    embed.set_field_at(index=i,name=field.name,value="75%",inline=field.inline)
                else:
                    embed.set_field_at(index=i,name=field.name,value="□□□□□□□□□□",inline=field.inline)
            await msg.edit(embed=embed)

            
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
    elif "파티1" in title:
        for party in parties1.keys() :
            if str(reaction.emoji.name) == party:
                for ro in roles:
                    if ro.id == parties1[party]:
                        await user.remove_roles(ro)
    elif "파티2" in title:
        for party in parties2.keys() :
            if str(reaction.emoji.name) == party:
                for ro in roles:
                    if ro.id == parties2[party]:
                        await user.remove_roles(ro)
@bot.event
async def on_message(msg):
    if msg.content.startswith("%"):
        await bot.process_commands(msg)
    elif msg.author.id != 958224347116494918:
        if bot.user in msg.mentions:
            if "뭐해" in msg.content:
                return await msg.channel.send("알아서 뭐하게")
            elif "할줄" in msg.content:
                return await msg.channel.send(f"얼마 [가격], [가디언이름], \'마법의 별\' ㅇㅇㅇ?, 돌 깍기")
            elif "얼마" in msg.content:
                numbers = int(re.sub('958224347116494918','',re.sub(r'[^0-9]','',msg.content)))
                return await msg.channel.send(f"4인 기준 : {int(numbers*0.66)}원\n8인 기준 : {int(numbers*0.77)}원")
            elif "마법의 별" in msg.content or "마법의별" in msg.content :
                answers = ["언젠가는","가만있어요.","다 안 돼요.","그것도 안 돼요.","좋아요.","다시 한 번 물어봐요.","괜찮아요","안 돼요.","돼요"]
                c = random.randrange(0,len(answers))
                return await msg.channel.send(answers[c])
            elif "먕누나" in msg.content or "먕난나" in msg.content:
                for em in msg.guild.emojis:
                    if em.name == "mo_noona":
                        a = em
                return await msg.channel.send(f"{a}")
            elif "돌 깍기" in msg.content or "돌깍기" in msg.content :
                embed = discord.Embed(title="돌 깍기 시뮬레이터",color=0xFF0000)
                embed.add_field(name="성공 확률",value="75%",inline=False)
                embed.add_field(name="증가 능력1",value=f"□□□□□□□□□□",inline=False)
                embed.add_field(name="증가 능력2",value=f"□□□□□□□□□□",inline=False)
                embed.add_field(name="감소 능력",value=f"□□□□□□□□□□",inline=False)
                embed.set_author(name=msg.author.name)
                msg = await msg.channel.send(embed=embed)
                await msg.add_reaction("1️⃣")
                await msg.add_reaction("2️⃣")
                await msg.add_reaction("3️⃣")
                return await msg.add_reaction("🔁")

            elif "우르닐" in msg.content:
                embed = discord.Embed(title="우르닐",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 1단계 첫번째 가디언",value=f"아이템 레벨 : 302\n레이드 지역 : 붉은 모래 사막\n단단한 갑옷을 두른 우르닐은, 분노에 찬 앞발로 눈앞의 적을 유린한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"기본적으로 패턴이 후방 공격이 없다.\n\n단, 광폭화하여 불이 붙으면 후방을 공격하는 강력한 패턴이 존재하므로 주의가 필요하다.\n\n우르닐+의 경우 옆구르기와 뒤로 넘어지기 패턴이 추가되어 후방과 측면에서 전투시 추가적인 주의가 필요하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "루메루스" in msg.content:
                embed = discord.Embed(title="루메루스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 1단계 두번째 가디언",value=f"아이템 레벨 : 340\n레이드 지역 : 짙은 안개 능선\n짙은 안개 속에서 머무는 가디언 루메루스는, 자신의 앞에 나타난 모험가들을 광휘의 빛으로 시험한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 신호탄\n약점 속성 : 암속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"모든 패턴이 느리지만 공격 범위가 굉장히 크다.\n\n후방을 공격하는 기술이 거의 없기 때문에 꼬리에 위치하여 있으면 대부분의 패턴에 피격당하지 않는다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "빙결의 레기오로스" in msg.content or "빙결의레기오로스" in msg.content or "빙레기" in msg.content:
                embed = discord.Embed(title="빙결의 레기오로스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 1단계 세번째 가디언",value=f"아이템 레벨 : 380\n레이드 지역 : 혹한의 안식처\n빙결의 레기오로스는 거대한 몸집으로부터 냉기를 발생시켜 적들을 꽁꽁 묶은 뒤 파괴시킨다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 아군 정화 직업\n배틀 아이템 : 회복약, 성스러운 부적, 신호탄\n약점 속성 : 화속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"거리를 벌리는 패턴이 매우 많아 이동기를 쓸때 주의를 해야한다.\n\n브레스는 동결을 걸기 때문에 주의가 필요하며, 후반에는 브레스를 2번 연속으로 쓴다.\n\n무력화 이후 몸이 하얗게 빛나면 몸 주위로 얼음 파편 공격을 하므로, 무력화 후 딜을 넣다가 일어나기 전에는 멀리 떨어져야한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "베르투스" in msg.content:
                embed = discord.Embed(title="베르투스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 1단계 네번째 가디언",value=f"아이템 레벨 : 420\n레이드 지역 : 혹한의 안식처\n혹한의 지배자라 불리고 있는 괴수 베르투스는 곁에 가까이 있는 것만으로도 몸을 얼리는 매서운 추위가 온 몸을 파고 든다고 한다. 베르투스의 차가운 숨결과 강력한 꼬리를 조심해야 한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 페로몬 폭탄, 신호탄\n약점 속성 : 뇌속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"거리를 벌리는 패턴이 매우 많아 이동기를 쓸때 주의를 해야하며, 브레스는 동결을 걸기 때문에 주의가 필요하며, 후반에는 브레스를 2번 연속으로 쓴다.\n\n주의 사항으로 무력화 이후 몸이 하얗게 빛나면 몸 주위로 얼음 파편 공격을 하므로, 무력화 후 딜을 넣다가 일어나기 전에는 멀리 떨어져야한다.\n\n총 3페이지로 이루어져있으며, 2페이즈 부터는 납치하는 패턴을 사용하며, 무력화를 통해 구출할 수 있다.\n\n얼음 밑으로 숨은 뒤 대상을 추적하다 튀어나와 강력한 피해를 주는데, 서리가 휘날리는 것을 통해 움직이는 방향을 추측할 수 있으며, 한방향으로 계속 달리면 거의 맞지 않는다." ,inline=False)
                return await msg.channel.send(embed=embed)

            elif "크로마니움" in msg.content and not "용암 크로마니움" in msg.content:
                embed = discord.Embed(title="크로마니움",color=0xFFD700)
                embed.add_field(name="아이템 레벨 : 460\n레이드 지역 : 메마른 절규의 땅\n에버그레이스의 시험 2단계 첫번째 가디언",value=f"단단한 등껍질을 가진 이 폭군은 그저 크고 단단한 괴수가 아니다. 크로마니움의 포효 속에서 뿜어지는 브레스와 등껍질에서 튀어나오는 마법의 구체를 조심해야 한다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 부위 파괴 직업\n배틀 아이템 : 회복약, 파괴폭탄, 신호탄\n약점 속성 : 뇌속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"등껍질을 파괴해야 방어력이 감소하고, 첫 무력화 이후에 아군 피해량이 증폭된다.\n\n첫 무력화 이전과 이후로 패턴이 나눠지며 체력 30%이하 광폭화시 몇가지 패턴이 강화되고 무력화 전/후 패턴을 전부 사용한다.\n\n대부분의 패턴이 느려서 피하기 어렵지 않으나 강력하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "나크라세나" in msg.content and not "중갑" in msg.content:
                embed = discord.Embed(title="나크라세나",color=0xFFD700)
                embed.add_field(name="아이템 레벨 : 500\n레이드 지역 : 메마른 절규의 땅\n에버그레이스의 시험 2단계 두번째 가디언",value=f"거대한 몸집, 단단하고 강력한 집게와 거대 가시를 지닌 사막의 별 나크라세나는 보는 사람들을 압도할 만한 위용을 자랑한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 페로몬 폭탄, 파괴폭탄, 신호탄\n약점 속성 : 토속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"나크라세나가 무력화 되었을때 꼬리에 파괴표시가 뜨며, 총 16의 파괴를 넣으면 꼬리가 절단된다.\n\n단, 체력이 30% 이하가되면 이동하며 꼬리가 재생한다.\n\n꼬리가 잘리지 않은 상태에서 전기를 충전하며, 적중시 감전 상태 이상에 걸린다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "홍염의 요호" in msg.content or "홍염의요호" in msg.content:
                embed = discord.Embed(title="홍염의 요호",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 2단계 세번째 가디언",value=f"아이템 레벨 : 540\n레이드 지역 : 짙은 검붉은 대지의 상흔\n홍염의 요호가 뿜어내는 불길의 숨결은, 상대와 함께 주변을 모조리 화염으로 불살라 버리며 숨통을 죄어올 것이다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"\"구슬 회전\", \"브레스\", \"화염구 퍼뜨리기\"에 피격 당하면 \'불타는 영혼\'버프가 걸리며, 공격력 2000이상 공격 속도가 20% 증가한다.\n\n도주 할때마다 페이즈가 넘어가며 총 2번 도주하여 3페이즈까지 존재한다.\n\n여담으로 전멸시 여성형태로 변신하여 유유히 걸어간다고한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "타이탈로스" in msg.content:
                embed = discord.Embed(title="타이탈로스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 2단계 네번째 가디언",value=f"아이템 레벨 : 580\n레이드 지역 : 붉은 모래 사막\n흉포하고 거대한 사암의 발톱, 타이탈로스는 사막의 모래와 함께 나타나 상대의 전의를 상실하게 만든다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 만능물약, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"전투를 시작하고 일정 시간이 지나면 모래 회오리 2개를 소환하며, 이 회오리는 목표 대상을 따라간다.\n\n회오리 안에 있으면 이동속도 감소 상태 이상에 걸리며 3회 중첩시 5초간 \'모래의 저주\'라는 석화에 걸려 행동 불가 상태가 되며, 동시에 무적 상태가 된다.\n\n모래의 저주가 풀린 이후에는 30초간 모래의 저주에 면역된다.\n\n지진 패턴 이후 3번의 공격 뒤 전멸기를 사용한다." ,inline=False)
                return await msg.channel.send(embed=embed)

            elif "어둠의 레기오로스" in msg.content or "어둠의레기오로스" in msg.content or "어레기" in msg.content:
                embed = discord.Embed(title="어둠의 레기오로스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 3단계 첫번째 가디언",value=f"아이템 레벨 : 802\n레이드 지역 : 짙은 안개 능선\n어둠의 레기오로스는 거대한 몸집으로부터 어둠을 끌어내어 적의 눈을 멀게 한 뒤 공격하는 것이 특징이다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 아군 정화 직업, 정화룬\n배틀 아이템 : 회복약, 신호탄\n약점 속성 : 성속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"레기오로스의 마법 공격에 피격되면 암흑에 걸린다.\n\n공격 범위가 넓어 빠르게 이동기로 따라 붙는게 중요하며 특히 벡스텝을 주로 하므로 주의해야한다.\n\n브레스가 메인 패턴이자 가장 강력한 패턴이다.\n\n하늘로 포효한후 어둠의 비를 내리는데, 꼬리쪽에 있으면 안전하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "헬가이아" in msg.content and not "혹한의" in msg.content:
                embed = discord.Embed(title="헬가이아",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 3단계 두번째 가디언",value=f"아이템 레벨 : 840\n레이드 지역 : 붉은 모래 사막\n헬가이아는 화려한 깃털을 가진 거대한 새로 싸움이 시작되면 깃털이 점차 불꽃으로 덮여가며 더욱 강력해진다. 헬가이아는 불 속에서 되살아나는 신령한 새라는 전설이 있다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 회오리 수류탄, 만능 물약, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"피격시 화상 상태로 인해 45초간 피해를 받으며 4중첩까지 쌓인다.\n\n50초 마다 진화를 시도하며, 성공시 다음 페이지로 넘어가므로 무력화를 해줘야한다.\n진화에 실패할 때마다 무력화 수치가 올라가며 매 진화단계마다 보통 3회에서 최대 5번정도까지 가능하다.\n\n3단계에서 무력화시 다시 1단계로 내려간다.\n\n대부분의 패턴이 꼬리에 바짝붙어있으면 맞지 않지만, 패턴이 빨라 고개를 많이 돌릴 수 있으므로, 어그로를 끌고 있는 사람은 머리를 가능한 고정시키는 것이 좋다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "칼벤투스" in msg.content:
                embed = discord.Embed(title="칼벤투스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 3단계 세번째 가디언",value=f"아이템 레벨 : 880\n레이드 지역 : 혹한의 안식처\n암흑을 부리는 칼벤투스의 매서운 광풍은, 자신을 제외한 모든 존재를 부정하며 일대를 뒤덮는다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 아군 정화 직업, 정화룬\n배틀 아이템 : 회복약, 만능 물약, 신호탄\n약점 속성 : 성속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"칼벤투스의 마법 공격에 피격 당할 때마다 \'광풍의 낙인\'이 걸리며, 중첩될 때마다 마법 피해가 10% 증가한다.\n\n전투 시작 후 5분 후 2페이즈에 돌입하며, 30초마다 \'광풍옥\'을 소환한다.\n\n\'광풍옥\'은 칼벤투스를 항해 천천히 다가와 흡수되며, 4개가 흡수되면 광폭화 상태가 된다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "아카테스" in msg.content:
                embed = discord.Embed(title="아카테스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 3단계 네번째 가디언",value=f"아이템 레벨 : 920\n레이드 지역 : 붉은 모래 사막\n아카테스는 풍성한 은빛 갈기와 눈부시게 빛나는 날개를 가지고 신성한 빛을 수호하는 성스러운 가디언입니다. 사슬 전쟁이 끝난 후, 구름 너머의 고요한 땅에 잠들어 있었던 아카테스는 최근 아크라시아 대륙에 울려 퍼지고 있는 차원의 진동을 느끼고 다시 깨어나 어디에선가 조용히 중간계 아크라시아의 흐름을 지켜보고 있습니다. 축복의 빛을 두르고 있는 거대한 몸집도 위협적이지만, 성스러운 포효 속에서 터져 나오는 빛의 불꽃은 감히 범접할 수 없는 존재임을 확인시켜 줄 것입니다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄, 신호탄\n약점 속성 : 암속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"초록/노랑/파랑/몸색을 정해야하며, 잠깐 무적 상태가 되어 구역 중앙으로 이동 후 석상을 소환하는데, 석상을 부수면 3개 색깔의 돌조각을 떨군다.\n아카테스의 몸색깔과 같은 색깔의 돌을 2개 던져한다.\n패턴에 성공하면 날개에 부위 파괴를 해야한다. 패턴에 실패하면 3페이즈로 넘어가며 즉사기를 발동한다.\n\n아가테스가 적들을 자신으로 빨아들이며, 일정 범위를 벗어나지 않으면 즉사급 데미지를 받는다.\n\n불꽃 패턴을 맞으면 성화 스택이 쌓이는데, 4스택이 쌓이면 주위에 지속적으로 피해를 주며 스택을 옮기므로 주의가 필요하다.\n\n전투 시작후 30초가 지나면 기를 모으며, 이후 일정 시간이 지나면 2페이즈로 넘어가는데, 기를 모으는 동안 극딜 타이밍이다.\n\n체력이 35%미만이 되면 수시로 랜덤 2명에게 \'빛의 저주\'를 걸며, 서로 접촉해야 해제가 가능하다.\n\n여기까지 도달한 플레이어가 없기를 바라며, 3페이즈는 30초마다 즉사기를 사용하며, 즉사기 이후 \'압도\' 디버프를 걸며, 디버프에 걸린 대상은 공격력이 50% 감소된다." ,inline=False)
                return await msg.channel.send(embed=embed)

            elif "혹한의 헬가이아" in msg.content or "혹한의헬가이아" in msg.content:
                embed = discord.Embed(title="혹한의 헬가이아",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 4단계 첫번째 가디언",value=f"아이템 레벨 : 960\n레이드 지역 : 혹한의 안식처\n온 몸이 이글거리는 냉염으로 뒤덮여있는 혹한의 헬가이아는 강력한 얼음과 냉기 브레스를 사용하여 생명이 있는 모든 것을 얼려버린다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 아군 정화 직업, 정화룬\n배틀 아이템 : 회복약, 만능 물약, 신호탄\n약점 속성 : 뇌속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"피격시 \'빙결\' 상태이상이 걸려 이동속도가 감소되며, 10중첩시 동결에 걸린다.\n\n헬가이아와 마찬가지로 1-3페이지로 진화하며, 무력화로 저지가능하다.\n단, 혹한의 헬가이아는 일정 피해를 받으면 강제 2페이지로 진화하며, 2페이지는 2번의 무력화만 가능하며, 3번째 무력화는 불가능하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "용암 크로마니움" in msg.content or "용암크로마니움" in msg.content:
                embed = discord.Embed(title="용암 크로마니움",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 4단계 두번째 가디언",value=f"아이템 레벨 : 1000\n레이드 지역 : 검붉은 대지의 상흔\n용암 크로마니움의 뜨거운 등엔 뜨거운 용암이 흐르는 균열이 존재한다. 그 균열을 중심으로 만들어진 틈에서는 연신 연기와 불길이 새어 나오고 있다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 부식 폭탄, 회오리 폭탄, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"등껍질이 파괴되기 전까지 일정 주기로 운석을 떨어 뜨린다.\n\n일정 시간 안에 무력화를 하지 못하면 다른 구역으로 이동하며, 등껍질이 복구된다.\n\n4개의 분화구를 소환하며, 분화구를 오랜 시간 제거하지 않으면 폭발하여 큰 피해를 입힌다.\n4개의 분화구를 전부 파괴하는 것보단 안전 구역을 확보하는 쪽이 좋다.\n\n체력이 20% 미만이 되면 광폭화하여 일정 주기로 주변에 광역 화염파를 방출한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "레바노스" in msg.content:
                embed = discord.Embed(title="레바노스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 4단계 세번째 가디언",value=f"아이템 레벨 : 1040\n레이드 지역 : 짙은 안개 능선\n오래된 존재인 정령왕 레바노스는 강력한 갑주를 두른 것이 특징이다. 힘의 근원인 코어를 공격하기 위해선 그가 두르고 있는 갑주부터 제거해야 할 것이다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 부식 폭탄, 신호탄\n약점 속성 : 화속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"부위 파괴를 하기 전까지는 피해량이 안들어간다.\n\n땅에 팔을 꽂고 있으면 갑옷을 재생하는데 무력화를 통해 저지할 수 있다.\n\n다른 구역으로 이동하거나, 광폭화 상태가 되면 갑옷이 자동으로 재생된다.\n\n주기적으로 \'레바노스 코어\'를 소환하며, 코어가 존재하는 동안 본체는 무적이고, 일정 시간마다 순간이동하며 일부 패턴을 따라한다.\n또한 3번째 코어를 소환하며 다른 구역으로 이동하는데, 3번째 코어를 빠르게 제거하면 다른 구역으로 이동하지 않는다.\n\n체력이 25% 미만이 되면 광폭화한다.\n\n전방을 주로 공격하며 소용돌이로 주변이 피해를 주며 돌진하는 패턴이 매우 위험하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "엘버하스틱" in msg.content:
                embed = discord.Embed(title="엘버하스틱",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 4단계 네번째 가디언",value=f"아이템 레벨 : 1080\n레이드 지역 : 메마른 절규의 땅\n사슬전쟁 이후 선택을 기다리던 가디언 엘버하스틱은, 번뇌의 창을 그러쥔 채 아크라시아에 그 장엄한 모습을 드러냈다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 회오리 폭탄, 페로몬 폭탄, 신호탄\n약점 속성 : 없음" ,inline=False)
                embed.add_field(name="특이사항",value=f"기본형인 창으로 시작하여 일정 체력이 달면 날개 혹은 클로 형태로 폼을 체인지하며 이동시 클로로 시작한다.\n\n변환 이후 열기 구슬이 등장하며, 파괴하고 푸른 구슬을 먹으면 피해의 90%를 1회 감소시켜준다.\n단, 엘버하스틱이 흡수하면 엘버스하스틱이 강해진다.\n\n엘버하스틱 몸에 푸른 아우라가 흘러 나오면 무력화를 해야하며 실패시 전멸기를 발동한다.\n\n날개 상태에서 엘버하스틱 주변에 푸른 소용돌이가 발생하고 수초 후 착지해서 피해를 입히는데, 공중에 떠오를때 소용돌이를 타서 회피해야한다.\n\n클로 상태에서 엘버하스틱이 지면에 색깔을 일으키면 해당 문양의 색과 반대되는 색깔을 흡수해야한다." ,inline=False)
                return await msg.channel.send(embed=embed)

            elif "중갑 나크라세나" in msg.content or "중갑나크라세나" in msg.content:
                embed = discord.Embed(title="중갑 나크라세나",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 5단계 첫번째 가디언",value=f"아이템 레벨 : 1302\n레이드 지역 : 붉은 모래 사막\n중갑 나크라세나는 약점이었던 꼬리를 철퇴 형태로 변형시켜 공격에 사용한다. 강화된 꼬리는 순식간에 주변 모든 것을 파괴할 정도의 위력을 지니고 있다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 페로몬 폭탄, 신호탄\n약점 속성 : 토속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"두번째 무력화 이후부터 부위 파괴를 통해 꼬리를 절단할 수 있다.\n\n꼬리가 절단되지 않은 나크라세나는 일정 시간마다 몸을 웅크리고 전기 충전을 시도하는데 무력화로 끊을 수 있고 꼬리 쪽에 딱 붙어있으면 피격 당하지 않는다.\n\n절단 후 일정 시간이 지나면 다른 구역으로 이동한다.\n\n번개 패턴은 맞으면 전부 감전당한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "이그렉시온" in msg.content:
                embed = discord.Embed(title="이그렉시온",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 5단계 두번째 가디언",value=f"아이템 레벨 : 1325\n레이드 지역 : 검붉은 대지의 상흔\n사슬전쟁 때 대지를 붉게 물들인 파멸의 포식자 이그렉시온. 거친 포효와 함께 검붉은 대지를 뚫고 나온 그는, 적으로 인식된 모든 것을 파멸시키기 위해 움직이기 시작했다.",inline=False)
                embed.add_field(name="권장사항",value=f"권장사항 : 아군 정화 직업, 정화룬\n배틀 아이템 : 회복약, 페로몬 폭탄, 만능 물약, 신호탄\n약점 속성 : 화속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"3가지 페이즈로 나눠지며, 페이즈를 넘어가거나 자기장 충전시 1/100만 피해 감소 효과가 있으며, 자기장 충전은 1분만다 발동한다.\n\n몸을 웅크려 에너지를 모으면 반격을 패턴이다.\n\n2페이즈에는 자기장 범위 내에 있거나 패턴에 적중 시 이동속도 감소 디버프가 쌓인다.\n\n체력이 30%이하가 되면 3페이즈로 변하며 이동하는데, 이때부터는 중첩당 데미지 400정도가 들어온다.\n\n3페이지의 바닥을 찍고 베이컨 형태의 장판기는 주의가 필요하다.\n\n무력화 상태가 되면 노랑-파랑-노랑 순으로 이펙트가 퍼지는데 파란색 범위가 안전하다.\n3페이즈는 빨강-파랑-빨강인데 파랑에서 첫타를 피하고 빨강으로 두번째 공격을 피해야한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "흑야의 요호" in msg.content or "흑야의요호" in msg.content:
                embed = discord.Embed(title="흑야의 요호",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 5단계 세번째 가디언",value=f"아이템 레벨 : 1355\n레이드 지역 : 메마른 절규의 땅\n빛을 두른 꼬리로부터 나오는 신비한 빛. 흑야의 요호가 가진 아름다움에 현혹된다면, 그 안에 숨어 있는 냉혹한 발톱에 공격 당할 것이다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 페로몬 폭탄, 신호탄\n약점 속성 : 성속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"1페이즈때는 인간형 요호를 2마리씩 소환하며, 해치우면 방어 에테를 획득 가능하다.\n원을 그리는데 원이 사라지기 전에 원 밖으로 도망 못치면 인간형 요호로 변신하게되며 변하게되면 행동이 제한된다.\n\n2페이즈에는 구슬을 날리는데 슬로우가 걸리며 3중첩시 인간형 요호로 변하게된다.\n\n3페이즈에는 기를 모으는 채널링을 시전하며 무력화 실패시 파티원 전원이 인간형 요호로 변하게된다.\n\n4페이즈에는 주기적으로 무력화가 가증하며, 무력화시 꼬리를 최대 3번까지 파괴할 수 있다.\n부위파괴 이전에는 데미지 감소가 적용된다.\n플레이어의 시야가 좁아지며 이동속도 감소가 디버프가 걸리고 요호를 기준으로 무작위로 회오리를 날리는데 이에 닿으면 감금당한다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "벨가누스" in msg.content:
                embed = discord.Embed(title="벨가누스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 5단계 네번째 가디언",value=f"아이템 레벨 : 1385\n레이드 지역 : 짙은 안개 능선\n빛과 어둠의 힘을 다루는 벨가누스는, 끓어오르는 분노를 표출하며 적을 심판한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 페로몬 폭탄, 신호탄\n약점 속성 : 성속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"조우 20초 이후 흑화상태에 들어가며 피해감소 상태가 되며 \'빛의 권능\'버프를 받지 않으면 데미지가 들어가지않는다.\n검은 패턴을 맞을 경우 \'빛의 권능\'이 하나씩 줄어들고 \'암흑의 권능\'이 걸리며 받는 피해가 증가한다.\n\n100%~70% 1페이즈, 70%~40% 2페이즈, 40%~30% 3페이즈, 30%~광폭화\n\n대부분의 패턴은 옆구리에서 피할 수 있다.\n\n벨가누스 조우 1분 후 시전하는 빛속성 무력화 패턴으로, 바닥에 화려한 문양이 생겨나는데 무력화를 해야한다.\n무력화 이후 1분이 지나면 제물패턴을 하는데, 아군 4명 머리 위에 빛속성 표시가 뜨다가 한명이 암속성으로 바뀌는데 그 사람이 머리쪽 장판에 들어가야한다." ,inline=False)
                return await msg.channel.send(embed=embed)

            elif "데스칼루다" in msg.content :
                embed = discord.Embed(title="데스칼루다",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 6단계 첫번째 가디언",value=f"아이템 레벨 : 1415\n레이드 지역 : 메마른 절규의 땅\n죽음을 쫓는 멸화의 집행자 데스칼루다는 맹렬한 화염으로 지상의 모든 생명을 소멸시킨다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄, 신호탄\n약점 속성 : 수속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"카운터를 자주 하므로 알아두면 좋다.\n\n데스칼루다가 공중으로 사라지고 빠자녀갈 수 없는 원형진이 생기는데 이때 최대 2명에게 십자선이 그려지므로 위치를 아군에게 맞추지않도록 잡아야한다.\n경직 면역 이상 스킬이나 이동기를 사용하며 원 밖으로 나갈 수는 있으나, 거리가 짧으면 다시 들어가진다.\n\n일렬로 마법진이 생기고 레이저를 발사하는데, 하늘색이 안전지역이다.\n\n4분마다 공습 패턴을 사용하는데 6번은 분신이고 7번째가 본체이며, 카운터가 가능하다.\n카운터에 실패하면 이동하며, 이전에 부위파괴를 못했으면 카운터가 안된다.\n\n부위 파괴는 몸에 불이 들어 온 이후 부터 몸에 부위 파괴가 가능하다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "쿤겔라니움" in msg.content:
                embed = discord.Embed(title="쿤겔라니움",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 6단계 두번째 가디언",value=f"아이템 레벨 : 1460\n레이드 지역 : 혹한의 안식처\n사슬전쟁 시기, 전장을 얼려버렸던 빙하의 포식자 쿤겔라니움. 혼돈의 영향으로 깨어난 그가 냉혹한 서리바람과 함께 돌아왔다...!",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 페로몬 폭탄, 신호탄\n약점 속성 : 뇌속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"시작부터 등껍질을 가지고 있어 파괴가 필요하다.\n\n총 2번 이동하므로, 페로몬 폭탄이 2개 필요하다.\n페로몬 타이밍은 첫 파괴, 첫번째 전멸기 때이다.\n\n전멸기는 체력이 일정이하로 떨어지면, 동서남북에 간헐천을 생성하며 눈보라를 일으키는데, 간헐천에 다가가 빙결되면 사망하지 않는다.\n\n브레스 및 동결 구체로 인해 동결이 걸리며, 그 외에도 이동속도 감소 버프가 중첩으로 걸린다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "칼엘리고스" in msg.content:
                embed = discord.Embed(title="칼엘리고스",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 6단계 세번째 가디언",value=f"아이템 레벨 : 1490\n레이드 지역 : 혹한의 안식처\n번개의 주인인 칼엘리고스는 푸른 뇌전을 다루는 고대의 존재로, 뇌전의 힘을 몸에 깃들여 모든 생물을 압도한다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 페로몬 폭탄, 신호탄\n약점 속성 : 토속성" ,inline=False)
                embed.add_field(name="특이사항",value=f"주변에 결계가 생기며, 번개치며 기를 모으는 행동을 하면 반격상태이므로 주의가 필요하다.\n\n손을 크게 들고 기를 모으고 있다면, 무력화 상태이며 실패시 주위에 큰 데미지를 준다.\n무력화에 성공하면 부위파괴가 뜨며, 이때 부위파괴에 성공하면 주위에 구체가 5개씩 뜬다.\n이 구체를 부수면 뇌룡의 힘 버프가 걸리며, 1중첩당 공격력 10%와 재사용 대기시간이 10% 감소한다.\n단, 지속적인 피해를 받으며 5개를 초과하는 경우 엄청난 도트 데미지가 들어오므로 주의가 필요하다.\n또한, 뇌룡옥을 파괴하면 뇌전 보호막 버프를 얻게되며, 이를 얻게되면 뇌룡의 힘을 얻을 수 없다.\n3페이즈에서 큰 쿠게체 등장하는데, 빠르게 부수지 않으면 저주의 데미지가 점점 강해집니다.\n\n일정 체력으로 내려가면 주위에 광역으로 번개를 떨어뜨리며 페이즈가 넘어가며 이동합니다." ,inline=False)
                return await msg.channel.send(embed=embed)
            elif "하누마탄" in msg.content:
                embed = discord.Embed(title="하누마탄",color=0xFFD700)
                embed.add_field(name="에버그레이스의 시험 6단계 네번째 가디언",value=f"아이템 레벨 : 1540\n레이드 지역 : 어그러진 안개의 숲\n사슬전쟁 시기, 빛의 진영에서 적들을 궤멸시켰던 가디언 하누마탄. 오랜 잠에서 깨어난 그는, 강력한 파괴력으로 별을 혼탁하게 만든 자들을 벌하기 시작했다.",inline=False)
                embed.add_field(name="권장사항",value=f"배틀 아이템 : 회복약, 파괴 폭탄 or 페로몬 폭탄, 신호탄\n약점 속성 : 없음" ,inline=False)
                embed.add_field(name="특이사항",value=f"갑주를 가지고 시작하며, 3번 부술수 있으며 이 부위파괴가 전부 이루어지지 못할 경우 페이즈 변환시 주위에 큰 데미지를 가한다.\n부위 파괴가 3번 뜨지 못할정도로 강력한 파티의 경우 무조건 보게되는 패턴이다.\n또한, 부위 파괴시 마다 버프가 생기며 중첩당 이동속도가 5% 재사용 대기시간 3.5% 공격속도가 3.5% 증가한다.\n\n하누마탄을 공격할 경우 디버프 창에 \'약점 포착\'이라는 디버프가 중첩되며, 해당 디버프는 치명타 적중률이 중첩당 1%씩 올라가는 대신 하누마탄에게 받는 데미지가 1.25%(1페이즈) / 2%(2페이즈)씩 올라간다.\n총 치명타 적중률 40%가 증가하고 받는 피해량은 50% (1페이즈) / 80% (2페이즈) 증가한다.\n10중첩이 되면 \'전투 의지\'라는 버프를 얻게되며, 공격력이 10% (1페이즈) / 15% (2페이즈) 증가하고, 재사용 대기시간이 5% (1페이즈) / 10% (2페이즈) 감소한다.\n공격력 40회 중첩되면 \'전투 각성\'으로 변형되며, 공격력이 30% 증가하고 재사용 대기시간이 30% 감소한다.\n단, 2페이즈는 40스택을 쌓을 경우 버프가 사라져 아무 효과를 받을 수 없다." ,inline=False)
                return await msg.channel.send(embed=embed)
            
            elif msg.author.id== 487906112020938763:
                replies = ["😍","😝","무슨일이야 누나","부르셨나요 공주님","먕난나!먕난나!","머야 누가 괴롭혀?","얘들아 누님이 부른다 연장 챙겨라"]
                c = random.randrange(0,len(replies))
                return await msg.channel.send(replies[c])
            replies = ["🤬","☠","🤘🤘 니코니코니~","왜 불러","불만있냐 자세를 고쳐 앉아"]
            c = random.randrange(0,len(replies))
            await msg.channel.send(replies[c])
bot.run(os.environ.get('Token'))
