import telethon
from telethon import events
from telethon.sync import functions
from telethon import TelegramClient
import telethon
import random
from random import choices
import time ;import os
from telethon.tl.functions.messages import GetPeerDialogsRequest
from telethon.sessions import StringSession
from config import *

auction = []

band = []

auction.append("vipjz\n")

@StrPython.on(
events.NewMessage(
outgoing=True, pattern=r"صيد"))
async def StrPychecker(event):
        clicks = 1
        msg = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
        
        type = str(msg[0])
      
        username = await rando(type)
        await event.reply(f"تم البدأ على النوع  - {type}")

        while True:
                clicks += 1
                try:
                	os.remove("clicks.txt")
                except :
                	open("clicks.txt","a").write(str(clicks)+"\n")
                else:
                	open("clicks.txt","a").write(str(clicks)+"\n")
                try:
             	   await StrPython(GetPeerDialogsRequest(peers=[username]))
                except Exception as err:
                    if "No user has" in str(err):
                        try:
                        	await StrPython(functions.account.UpdateUsernameRequest(username=username))           
                        
                        	await StrPython.send_file("@isandreew", "https://t.me/illl0o/3",caption=f'''
Good evening 🗽
⌯ New Caught by Andrew 💸
⌯ User ⤷ @{username}
⌯ Save ⤷ Account
⌯ Clicks ⤷ {clicks}
⌯ Program the bot : @illl0''')
                        	os.remove("clicks.txt")
                        	break
                        except Exception as USFL:
                        	await StrPython.send_message(event.chat_id,f"User is error : @{username}\nError: {USLF}")
                    else:
                        continue                    
                        
                except telethon.errors.rpcerrorlist.UsernameInvalidError:
                    	await StrPython.send_message(event.chat_id,f"User is band 🥴 : {username}")
                    	band.append(username)
                    	
                except telethon.errors.rpcerrorlist.UsernameOccupiedError:
                    	time.sleep(1);continue
                    	
                except telethon.errors.rpcerrorlist.FloodWaitError as ses:
                    	await StrPython.send_message(event.chat.id,f"Flood & {ses.seconds}")
                    	
                    	break
                except telethon.errors.rpcerrorlist.UsernamePurchaseAvailableError: 
                    	
                    	auction.append(username+"\n")
                    	
              
                except Exception as Error:
                   await StrPython.send_message(event.chat.id,f"Error in the check : {Error}\nUser is Err : @{username}") 
                   break
                   
       
#  تخمط دليل فشلك 🤨
#تيم ستار بايثون 🗽

ban = open("band.txt","r").read().split()
band.append(ban)

abcd = "qwertyuiopassdfghjklzxcvbnm"
number = "1234567890"
xx = "qwertyuiopassdfghjklzxcvbnm1234567890"
async def rando(type):
	if type == "خماسيات-3":
		q = random.choices(abcd)
		w = random.choices(abcd)
		user = ["vip",q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات":
		q = random.choices(abcd)
		w = random.choices(xx)
		user = [q[0],q[0],q[0],q[0],w[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "ثلاثيات":
		q = random.choices(abcd)
		w = random.choices(abcd)
		b = random.choices(xx)
		user = [q[0],"_",b[0],"_",w[0]]
		username = "".join(user)
		
		
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "سداسيات":
		q = random.choices(abcd)
		w = random.choices(xx)
		user = [q[0],w[0],w[0],w[0],w[0],w[0]]
		username = "".join(user)
		return username
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "تيست":
		q = random.choice(abcd)
		w = random.choice(abcd)
		user = [q[0],"b",q[0],"66",q[0],q[0],w[0]]
		username = "".join(user)
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "خماسيات-2":
		q = random.choice(abcd)
		w = random.choice(abcd)
		nu = random.choices(number)
		num = random.choices(number)
		user = [q[0],w[0],nu[0],nu[0],nu[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "بوتات":
		q = random.choices(abcd)
		w = random.choices(xx)
		b = random.choices(xx)
		user = [q[0],w[0],b[0]]
		username = "".join(user)
		username = username+"bot"
		
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
	if type == "حرفين":
		q = random.choices(abcd)
		w = random.choices(xx)
		user = [q[0],w[0],q[0],q[0],w[0]]
		username = "".join(user)
		if username in band[0]:
			pass
		else:
			pass
		if username in auction[0] :
			pass
		else:pass
		return username
		
@StrPython.on(events.NewMessage(outgoing=True, pattern=r"تشغيل الصيد"))
async def Shhtah(event):
	await event.reply(""" 
اهلا بك ، لتشغيل الصيد قم بتحديد النوع اولا 🤡
لصيد ثلاثي بوت : صيد بوتات
لصيد خماسي حرفين : صيد حرفين
لصيد خماسي rm111 : صيد خماسيات-2
لصيد خماسي : صيد خماسيات
لصيد سداسي :  صيد سداسيات
لصيد ثلاثي : صيد ثلاثيات
لصيد vip : صيد خماسيات-3
للتجربه : صيد تيست

""")

@StrPython.on(events.NewMessage(outgoing=True, pattern=r"الضغطات"))
async def Shhtah(event):
	try:
		n = open("clicks.txt","r").read()
		
	except:
		await event.reply("طافي حب 🗽")
	else:
		
		await event.reply(f"عدد الضغطات حاليا : {n}")
	
	
	
	
	

for x in StrPython.iter_dialogs():
		if x.is_user and not x.entity.bot:
			
				too = x.id
				msg = """
Welcome to Channel Programmers (MAX)
It is in this channel : Sources, bots
to join : t.me/illl0
-------------------------------------------
مرحباً بك في القناة البرمجيه (ماكس)
يوجد في هذه القناة : ملفات سورسات، بوتات 🗽
للأنضمام : t.me/Max985"""
				try:
					StrPython.send_message(too, msg)
				except BaseException:continue
StrPython.send_file("me","https://t.me/illl0o/6",caption=f"""**مرحبا بك في سورس تشيكر !
تابع لـ[MAX](t.me/MAX985) .
اليك الاوامر ادناة .
الأمر الاول : ايقاف الصيد
الأمر الثاني : تشغيل الصيد 
الأمر الثالث : الضغطات**
""")

		     #
		
		    		     		     
		    		     		     		     
		    		     		     		     		     
		    		     		     		     		     		     
		    		     		     		     		     		     		     
		    		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     			     
		    		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     	
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   
		    		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		     		   

@StrPython.on(events.NewMessage(outgoing=True, pattern=r"ايقاف الصيد"))
async def Shhtah(event):
	await StrPython.send_message(event.chat_id,"جارِ ...")
	
	await StrPython.disconnect()
	time.sleep(5)
	
	await StrPython.start()
	await event.reply("تم")
print("Run")
StrPython.run_until_disconnected()