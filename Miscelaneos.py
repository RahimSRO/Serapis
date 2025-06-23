# log((' '.join('{:02X}'.format(x) for x in data)))
from phBot import *
import struct
import QtBind
import threading
from threading import Timer
import phBotChat
import os
from time import sleep
import urllib.request
import random
import signal
import ssl
import subprocess
import sys
from math import pi, cos, sin
from random import random
import ctypes
import re
import json
from urllib.request import urlopen

ScrollUsado = False
CLIENTLESS_BOL = True
startAfterPick = ''
berserker = False

def zerk():
	global berserker
	return berserker

def rand(r=5):
	x1 = get_position()['x']
	y1 = get_position()['y']
	theta = random() * 2 * pi
	move_to(int(x1 + cos(theta) * r),int(y1 + sin(theta) * r),0)

def point(x1,y1):
	global NPC
	r = 2
	if NPC:
		theta = random() * 2 * pi
		move_to(int(x1 + cos(theta) * r),int(y1 + sin(theta) * r),0)
		Timer(0.2,point,[x1,y1]).start()

mobAtacked = []
myPlayers = ['Seven','Zoser','Trump','Cuantica','Amor','Paz','Yeico','Sol','Amanda','Rah','How']
itemList = ['advanced','sharpness','lottery','silk scroll','immortal','lucky','poro','sabakun','coin','blue stone','black stone','serapis','pop','reverse','global','gold','carnival']
itemListAzul = ['advanced','sharpness','lottery','silk scroll','immortal','lucky','poro','sabakun','coin','blue stone','black stone','serapis','carnival']
otrosItems = ['Reverse Reverse Return Scroll','Global chatting','Magic POP Card']
attackWolf = False
mercaPos = []

def cancelAlchemy():
	inject_joymax(0x7150,b'\x01',True)
	Timer(1, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(2, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(3, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(4, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(5, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(6, inject_joymax,[0x7150, b'\x01', True]).start()
	Timer(7, inject_joymax,[0x7150, b'\x01', True]).start()
	quitarDressLucky()

traders = ['Cuantica','Trump','Zet','Dot','Fin']

def traderINtown(s=1):
	urllib.request.urlopen('https://api.telegram.org/bot6863881576:AAHQ34H1cMzGz8XsNf5SqiCkY2wQ-dpBBG4/sendMessage?chat_id=149273661&parse_mode=Markdown&text=TOWN%20%20`'+get_character_data()['name']+'`',context=ssl._create_unverified_context())
	return True

def disconnected():
	log('HAS SIDO DESCONECTADO TIO')
	return
	global dcName
	sendTelegram("DC "+get_character_data()['name'])
	if not get_client()['running'] and os.environ['COMPUTERNAME'] != 'PC-PATRIDA' and get_character_data()['name'] not in traders:
		os.kill(os.getpid(), 9)
	return True
	
pickAfterJoin = False
energy = False
thiefs = ['XxJhOnAtAnxX']
merca = False
partyAlert = True
USTR = False
UINT = False
dropg = False
gui = QtBind.init(__name__,'Miscelaneos')
ignore = ['[BOT]System','[BOT]Evento','[BOT]Evento1','[BOT]Evento2','Seven','Zoser']
uniques = ["Tiger Girl","Cerberus","Captain Ivy","Uruchi","Isyutaru","Lord Yarkan","Demon Shaitan","White Knight","Homocidal Santa","[GM] Serapis"]
NotificarCheck = QtBind.createCheckBox(gui,'Notificar','Notificar Chat',70,10)
partyAlertCheck = QtBind.createCheckBox(gui,'partyAlertChecker','Party Alert',90,40)
QtBind.setChecked(gui, NotificarCheck, True)
QtBind.setChecked(gui, partyAlertCheck, partyAlert)
TelegramBol = True
zones = ['Lost Lake','Samarkand','Jangan']
ignoreZones = ['Samarkand','Jangan','Königreich Hotan','Western-China-Donwhang','Constantinople']
jelp = False
partyNumber = 0
NPC = False
drop = True
dropItems		= QtBind.createButton(gui,'exitBandit','exitBandit',250,220)
partyList = QtBind.createList(gui,120,180,100,80)
btnRemove = QtBind.createButton(gui,'gobot',"     GO BOT     ",130,259)
btnFill = QtBind.createButton(gui,'llenarLista',"      REFRESH      ",130,160)
btnGoMerca = QtBind.createButton(gui,'goMerca',"     GO Merca     ",130,280)
pickAfterCheckBox = QtBind.createCheckBox(gui,'PickAfterFunction','Fick After Join',350,70)

def llenarLista():
	QtBind.clear(gui,partyList)
	Party = get_party()
	if Party:
		for memberID in Party:
			if Party[memberID]['name'] != get_character_data()['name']:
				QtBind.append(gui,partyList,Party[memberID]['name'])

def gobot():
	selectedItem = QtBind.text(gui,partyList)
	if selectedItem:
		Party = get_party()
		if Party:
			for memberID in Party:
				if selectedItem == Party[memberID]['name']:
					set_training_script('')
					Timer(1,set_training_position,[Party[memberID]['region'], Party[memberID]['x'], Party[memberID]['y'], 0.0]).start()
					Timer(1.5,start_bot).start()
	elif QtBind.text(gui,XY):
		x = QtBind.text(gui,XY).split(',')[0]
		y = QtBind.text(gui,XY).split(',')[1]
		move_to(float(x),float(y),0)

def talkToBandit():
	npcs = get_npcs()
	for id, npc in npcs.items():
		if "gestohlener Waren" in npc['name']:
			inject_joymax(0x7045, struct.pack('I',id), False)
			Timer(0.5, inject_silkroad,[0xB034, b'\x01\x06\x0D\x00\x00\x00\x00\xAB\x65\x00\x00\x01\x00', True]).start()
			Timer(1, inject_silkroad,[0xB074, b'\x02\x00', True]).start()
			# Timer(1.5,inject_joymax,[0x7046, struct.pack('I',id)+b'\x0C',True]).start()
			return True

def teleported():
	log(get_zone_name(get_character_data()['region']))
	global LastUniqueInRange
	global startAfterPick
	global attackWolf
	global energy
	global mercaPos
	global PICK
	global UINT
	if get_character_data()['name'] == 'Seven':
		if get_character_data()['region'] == 23603 and get_inventory()['items'][8]:
			log('23603')
			Timer(1,inject_joymax,[0x705A,bytes.fromhex('04 00 00 00 02 AE 00 00 00'),False]).start()
		LastUniqueInRange = False
		UINT = False
		startAfterPick = ''
		attackWolf = False
		PICK = False
		mercaPos = []
		energy = False
		ScrollUsado = False
		#inject_joymax(0xC003,bytearray(),False) #attendance
		quests = get_quests()
		for questID in quests:
			if quests[questID]['completed']:
				notice('Pending Quest!')
				break
		# if get_zone_name(get_character_data()['region']) == 'Diebesstadt':
		# 	Timer(2,phBotChat.Private,['Seven','Diebesstadt']).start()
		# 	stop_bot()
		# 	moveToBandit()
			# inject_joymax(0x7034, b'\x00\x6C\x6B\x01\x00',True)
			# Timer(4,inject_joymax,[0x7045,struct.pack('I',31),True]).start()
			# Timer(4,inject_joymax,[0x7034,b'\x00\x6C\x6B\x01\x00',True]).start()
			# Timer(4.5,inject_joymax,[0x7045,struct.pack('I',31),True]).start()
		Timer(5,inject_joymax,[0xA451, b'\x04', True]).start()
		return

def moveToBandit():
	x1 = 9113
	y1 = 876
	x2 = get_position()['x']
	y2 = get_position()['y']
	dis = ((x2-x1)**2+(y2-y1)**2)**1/2
	if dis > 30:	
		move_to(x1,y1,0)
		Timer(0.5,moveToBandit).start()
		return
	talkToBandit()

button1 = QtBind.createButton(gui, 'global_chat', 'Global', 530, 27)
text = QtBind.createLineEdit(gui,"",220,25,300,20)

def global_chat():
	phBotChat.Global(QtBind.text(gui,text))

def exitBandit():
	scrolls = 0
	for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Bandit Den Return Scroll':
					scrolls += x['quantity']
	if scrolls < 10:
		notice('BANDIT SCROLLS!')
		return
	Party = get_party()
	if Party:
		for memberID in Party:
			if get_zone_name(Party[memberID]['region']) == 'Diebesstadt' and get_character_data()['job_name'] != Party[memberID]['name']:
				return
	exit()

def exitBanditOLD():
	for i,x in enumerate(get_inventory()['items']):
		if x and i > 13:
			if x['name'] == 'Bandit Den Return Scroll':
				if x['quantity'] > 10:
					Party = get_party()
					if Party:
						if len(Party) == 2:
							for memberID in Party:
								if Party[memberID]['name'] != 'Mihar' and Party[memberID]['name'] != 'Rahim':
									return
								elif get_zone_name(Party[memberID]['region']) != 'Diebesstadt' and get_character_data()['job_name'] != Party[memberID]['name']:
									exit()
						else:
							return
					else:
						exit()
				else :
					notice('BANDIT SCROLLS!')
				return
def exit():
	npcs = get_npcs()
	for id, npc in npcs.items():
		if "Diebesstadt" in npc['name']:
			inject_joymax(0x705A, struct.pack('I',id)+b'\x01',True)

def script(arg):
	stop_bot()
	log(get_config_dir().replace('Config','Scripts')+arg[1]+'.txt')
	set_training_script(get_config_dir().replace('Config','Quests')+arg[1]+'.txt')
	start_bot()
	return
	
def droping():
	drops = get_drops()
	global dropg
	if len(drops) < 5:
		gold_available = get_character_data()['gold']
		gold = 100000000
		gold_minimo = 1000000
		if dropg:
			if gold_available > gold_minimo:
				droped = gold_available%gold
				if droped == 0:
					droped = gold
				Packet = b'\x0A'
				Packet += struct.pack('<I', droped)
				Packet += b'\x00\x00\x00\x00'
				inject_joymax(0x7034, Packet, False)
				Timer(0.5, droping).start()
			else:
				dropg = ~dropg
	else:
		Timer(0.5, droping).start()

def dropItem(name):
	global drop
	log('dropItem')
	for i,item in enumerate(get_inventory()['items']):
		if drop and item and i>12:
			log(item['name'])
			if name.upper() in item['name'].upper():
				log(item['servername'])
				Packet = bytearray()
				Packet.append(0x07)
				Packet.append(i)
				inject_joymax(0x7034, Packet, True)
				Timer(0.5,dropItem,[name]).start()
				return
	drop = False

eventos = ['Lucky','Bargain']
stats = True

def easyPick(k=0):
	drops = get_drops()
	if k == 0:
		pets = get_pets()
		if pets:
			for k, v in pets.items():
				if v['type'] == 'pick':
					break
	if drops:
		for dropID in drops:
			if k != 0 and 'adv' in drops[dropID]['name'].lower():
				inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'immortal' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if k != 0 and 'lottery' in drops[dropID]['name'].lower():
				inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'silk' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'pop' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if k != 0 and 'poro' in drops[dropID]['name'].lower():
				inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'arena' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'reverse' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'carnival' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'repair' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'stepflare' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log( drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'global' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.3,easyPick,[k]).start()
				return
		for dropID in drops:
			if 'gold' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
					log(drops[dropID]['name'])
					Timer(0.3,easyPick,[k]).start()
					return
				# inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				# log(drops[dropID]['name'])
				# Timer(0.3,easyPick,[k]).start()
				return

def easyPickOLD(k=0):
	temp = False
	drops = get_drops()
	if k == 0:
		pets = get_pets()
		if pets:
			for k, v in pets.items():
				if v['type'] == 'pick':
					break
	if drops:
		for dropID in drops:
			for item in itemList:
				if item in drops[dropID]['name'].lower():
					inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
					log(drops[dropID]['name'])
					if k != 0:
						inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
					Timer(0.3,easyPickOLD,[k]).start()
					return
		
def switchScroll():
	global ScrollUsado
	ScrollUsado = False		

def petrifyN(N):
	global petrify
	petrify = N

def equipShield():
	for i,item in enumerate(get_inventory()['items']):
		if drop and item and i>12:
			if '_SHIELD_' in item['servername']:
				log('Equiping shield')
				inject_joymax(0x7034, b'\x00'+ struct.pack('b', i) + b'\x07\x00\x00', True)
				return True


def petrify():
	global petrify
	if petrify == 5:
		return True
	else:
		return 0

def infiniteMove(x,y):
	azul('infiniteMove')
	if petrify != 0:
		# equipShield()
		x1 = get_position()['x']
		y1 = get_position()['y']
		dis = ((x-x1)**2+(y-y1)**2)**1/2
		move_to(x,y,0)
		Timer(0.2,infiniteMove,[x,y]).start()
		# if dis > 2:
		# # 	return
		# notice(str(dis))
		# notice('listo el infinito')



def alejare(distancia_objetivo):
	notice('alejare')
	global partyNumber
	if partyNumber != 0:
		stop_bot()
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['type'] == 24:
				A = get_character_data()
				B = mobs[mobID]
				# Calcular la distancia actual entre el personaje y el monstruo
				distancia_actual = math.sqrt((B['x'] - A['x'])**2 + (B['y'] - A['y'])**2)
				# notice('da: '+str(distancia_actual))
				# notice('do: '+str(distancia_objetivo))
				if distancia_actual > distancia_objetivo:
					azul('Listo')
					start_bot()
					return
				# Calcular la proporción para ajustar la distancia
				proporcion = distancia_objetivo / distancia_actual
				# Calcular las nuevas coordenadas
				nueva_x = A['x'] + (B['x'] - A['x']) * proporcion
				nueva_y = A['y'] + (B['y'] - A['y']) * proporcion
				move_to(nueva_x,nueva_y,0)
				# Timer(0.5,alejare,[A,B,distancia_objetivo])
				# Timer(0.2,alejare,[distancia_objetivo]).start()
				Timer(0.2,infiniteMove,[B,distancia_objetivo,0,0]).start()

skillsMedusa = []

def handle_joymax(opcode, data):
	global partyNumber
	global UniqueAlert
	global UINT
	global USTR
	global stats
	global itemList
	global mobAtacked
	global attackWolf
	global PICK
	global ScrollUsado
	global CLIENTLESS_BOL
	global energy
	global LastUniqueInRange
	global petrify
	global dcName
	if opcode == 0x3040 and len(data) == 23:
		verdemini(get_item(struct.unpack_from('i', data, 7)[0])['name'])
	elif opcode == 0x3041 and get_character_data()['player_id'] == struct.unpack_from('I',data,0)[0]:
		log('Poniendo capa...')
		# killClient()
	elif opcode == 0xB007: #capa no capa
		if dcName and CLIENTLESS_BOL:
			inject_joymax(0x7001, struct.pack('H', len(dcName)) + dcName.encode('ascii'), True)
		else:
			QtBind.setText(gui, text, struct.unpack_from('<' + str(data[7]) + 's',data,9)[0].decode('cp1252'))
		#QtBind.text(gui,text)
		log('CAPA NO CAPA: '+str(struct.unpack_from('<I', data, 83)[0]))
		return True
		#CHAR_NAME = struct.unpack_from('<' + str(data[7]) + 's',data,9)[0].decode('cp1252')
	# elif opcode == 0x38F5 and data[0] == 6 and data[5] == 2 and not data[6] and get_guild()[struct.unpack_from("<I", data, 1)[0]]['name'] == "Seven":
		# log((' '.join('{:02X}'.format(x) for x in data)))
		# log(str(get_guild()[struct.unpack_from("<I", data, 1)[0]]))
		# phBotChat.Private('Seven', 'Hello')
		# infoType = data[5]
		# memberID = struct.unpack_from("<I", data, 1)[0]
		# member = get_guild()[memberID]
		# data[6] == 0 es cuando se logea
		# return True
	elif opcode == 0x305C and get_character_data()['player_id'] == struct.unpack_from('I',data,0)[0]: #animacion cuando usa un scroll
		if struct.unpack_from('I',data,4)[0] == 2198:#and data == b'\x57\x74\x0E\x00\x96\x08\x00\x00':
			ScrollUsado = True
			morado('Scroll')
			Timer(2,switchScroll).start()
		elif struct.unpack_from('I',data,4)[0] == 2128:
			morado('Bandit Scroll')
	# if opcode == 0x706D: #party member joined
	# 	name = struct.unpack_from('<' + str(data[6]) + 's',data,8)[0].decode('cp1252')
	# 	notice('0x706D: ' + name)
	# 	phBotChat.Party('Hello ['+name+']')
	# 	mobs = get_monsters()
	# 	for mobID in mobs:
	# 		if mobs[mobID]['type'] == 24:
	# 			phBotChat.Party(name + ' Here! => ['+mobs[mobID]['name'] +']')
	# 			break
	elif opcode == 0x304E and data[0] == 4: #usar scroll cuando hay zerk
		if struct.unpack_from('b', data, 1)[0] == 5:
			if UINT and not LastUniqueInRange:
				useSpecialReturnScroll()
				stop_bot()
				morado('Zerk')
			if energy:
				energy = False
				notice('Energia Desactivada')
	elif opcode == 0x3864 and data: #party member joined
		if struct.unpack_from('<s', data, 0)[0] == b'\x02':
			name = struct.unpack_from('<' + str(data[6]) + 's',data,8)[0].decode('cp1252')
			mobs = get_monsters()
			for mobID in mobs:
				if mobs[mobID]['type'] == 24 and 'Balloon' not in mobs[mobID]['name']:
					phBotChat.Party(name + ' Here! => ['+mobs[mobID]['name'] +']')
					break
	elif opcode == 0xB070: #medusa
		mobs = get_monsters()
		for mobID in mobs:
			if len(data) > 3 and mobs[mobID]['type'] == 24:
				# green(str(struct.unpack_from('I', data, 3)[0]))
				if struct.unpack_from('I', data, 3)[0] == 12294:
					stop_bot()
					azulPerma("Petrificado")
					petrify = 1
					x1 = get_position()['x']
					y1 = get_position()['y']
					x2 = mobs[mobID]['x']
					y2 = mobs[mobID]['y']
					punto_mas_cercano(x1,y1,x2,y2,35)
					Timer(3,petrifyN,[5]).start()
					Timer(8,start_bot).start()
					Timer(10,petrifN,[0]).start()
					return True
		if get_character_data()['name'] == 'Dots' and struct.unpack_from('<I', data, 15)[0] == get_character_data()['player_id'] and data[1] == 2:
			azul('Me atacan...')
			# inject_joymax(0xC00C,b'\x06\x00\x61\x75\x74\x6F\x65\x71',False)
			return True
		if attackWolf: #MOB_ATTACKED
			pets = get_pets()
			if pets:
				for pet, v in pets.items():
					if v['type'] == 'wolf':
						victima = struct.unpack_from('<I', data, 15)[0]
						if victima == get_character_data()['player_id'] or victima == pet:
							mob = struct.unpack_from('<I', data, 7)[0]
							if mob not in mobAtacked and get_monsters()[mob]['type'] != 24:
								mobAtacked.append(mob)
							tempMob = 0
							for mob in mobAtacked:
								mobs = get_monsters()
								for mobID in mobs:
									if mobID == mob and mob > tempMob:
										tempMob = mob
										break
								mobAtacked.remove(mob)
							inject_joymax(0x70C5, struct.pack('i', pet) + b'\x02' + struct.pack('i', tempMob), False)
							log('Atacando a :' +str(tempMob))
							log(str(mobAtacked))
							return True
	elif opcode == 0xB034 and len(data) > 11:
		# if len(data) == 7:
		# 	log((' '.join('{:02X}'.format(x) for x in data)))
		if struct.unpack_from('h', data, 0)[0] == 3585:
			log('ITEM GANADOOOOO: '+get_item(struct.unpack_from('I', data, 8)[0])['name'])
			if struct.unpack_from('I', data, 8)[0] == 23357 or struct.unpack_from('I', data, 8)[0] == 5920:
				log('ITEM GANADOOOOO: '+get_item(struct.unpack_from('I', data, 8)[0])['name'])
				sort_inventory()
				log('HERINGER')
				return True
			elif struct.unpack_from('I', data, 8)[0] == 23356:
				useSpecialReturnScroll()
		dropType = struct.unpack_from('h', data, 0)[0]
		if dropType == 4353 or dropType == 7169:
			itemID = get_item(struct.unpack_from('I', data, 11)[0])
			itemName = itemID['name']
			# if struct.unpack_from('I', data, 11)[0] > 33892 and struct.unpack_from('I', data, 11)[0] < 33901:
			# 	azulPerma('item ['+itemName +'] gained.')
			if 'Poro' in itemID['name']:
				itemName = 'Poro Balloon'
			for item in itemListAzul:
				if item in itemName.lower():
					azulPerma('item ['+itemName +'] gained.')
					break
			if itemID['rare']:
				azulPerma('item ['+itemName +'] gained.')
			for item in otrosItems:
				if item == itemName:
					Union('item ['+itemName+'] gained')
		elif dropType == 1537:#1537
			itemID = get_item(struct.unpack_from('I', data, 7)[0])
			itemName = itemID['name']
			# if struct.unpack_from('I', data, 7)[0] > 33892 and struct.unpack_from('I', data, 7)[0] < 33901:
			# 	azulPerma('item ['+itemName +'] gained.')
			if 'Poro' in itemID['name']:
				itemName = 'Poro Balloon'
			for item in itemListAzul:
				if item in itemName.lower():
					azulPerma('item ['+itemName +'] gained.')
					break
			if itemID['rare']:
				azulPerma('item ['+itemName +'] gained.')
			for item in otrosItems:
				if item == itemName:
					Union('item ['+itemName+'] gained')
	elif opcode == 0x3068: #party item droped distributed
		itemName = get_item(struct.unpack_from('<I', data, 4)[0])['name']
		playerName = get_party()[struct.unpack_from('<I', data, 0)[0]]['name']
		# if struct.unpack_from('<I', data, 4)[0] > 33892 and struct.unpack_from('<I', data, 4)[0] < 33901:
		# 	red('item ['+itemName +']is distributed to ['+ playerName+']')
		if 'Poro' in itemName:
			itemName = 'Poro Balloon'
		for item in itemListAzul:
			if item in itemName.lower():
				red('item ['+itemName +']is distributed to ['+ playerName+']')
				# phBotChat.Party('item ['+itemName +']is distributed to ['+ playerName+']')
				break
		if get_item(struct.unpack_from('<I', data, 4)[0])['rare']:
			red('item ['+itemName +']is distributed to ['+ playerName+']')
		for item in otrosItems:
			if item == itemName:
				Union('item ['+itemName +']is distributed to ['+ playerName+']')
			# phBotChat.Party('item ['+itemName +']is distributed to ['+ playerName+']')
	elif stats and opcode == 0x3153:#silk sp serapis point
		Silk = str(struct.unpack_from('<I', data, 0)[0])
		SP = str(struct.unpack_from('<I', data, 4)[0])
		msg = get_character_data()['name'] + ' =>   SP: '+ SP + '     Silk: ' + Silk
		log(msg)
		threading.Thread(target=sendTelegram2, args=[msg],).start()
		stats = False
		return True
	elif opcode == 0x30CF: #Mensajes de eventos
		# if '[G' in str(data): 
			# log((' '.join('{:02X}'.format(x) for x in data)))
		if data == b'\x15\x02\x55\x00\x59\x6F\x75\x20\x6D\x75\x73\x74\x20\x63\x6F\x6D\x70\x6C\x65\x74\x65\x20\x74\x68\x65\x20\x63\x61\x70\x74\x63\x68\x61\x20\x76\x65\x72\x69\x66\x63\x61\x74\x69\x6F\x6E\x20\x74\x6F\x20\x70\x72\x6F\x63\x65\x65\x64\x20\x77\x69\x74\x68\x20\x62\x75\x79\x69\x6E\x67\x2F\x73\x65\x6C\x6C\x69\x6E\x67\x20\x74\x72\x61\x64\x65\x20\x67\x6F\x6F\x64\x73\x2E': # Trader Sell
			deleteClean()
		elif get_character_data()['name'] == 'Seven':
			msg = str(data[4:])[2:-1]
			if 'Specifications' not in msg:
				if ('Search & Destroy' in msg or 'Horse Race' in msg or 'Lucky Global' in msg) and 'Capture' not in msg:
					threading.Thread(target=sendTelegram, args=[msg],).start()
				elif 'Be the first' in msg:
					log(msg)
					msg = msg.replace('Be the first to find and kill "[GM] Serapis" around ','`')+'`'
					notice(msg.replace('`',''))
					threading.Thread(target=sendTelegram, args=[msg],).start()
				# elif 'safe trader' in msg.lower():
				# 	log(msg)
				# elif 'killed a balloon' in msg.lower():
				# 	pickCarnivalBox()
				elif 'balloons are now spawned' in msg.lower():
					azulPerma(msg)
					threading.Thread(target=sendTelegram, args=[msg],).start()
				elif 'balloons' in msg.lower():
					log(msg)
		return True
	elif opcode == 0xB069: #Party Form
		if data != b'\x02\x1D\x2C' and data != b'\x02\x1B\x2C':
			# log((' '.join('{:02X}'.format(x) for x in data)))
			log('party actualizado?')
			partyNumber = struct.unpack_from('I', data, 1)[0]
			notice(str(partyNumber))
		# if data[0] != 2:
		# 	log('xdxd')
		# 	# pt = str(struct.unpack_from('<I', data, 1)[0])
		# 	# log('Party number: ' + pt)
		# 	if partyNumber != '0' and int(pt) < int(partyNumber):
		# 		Packet = bytearray()
		# 		Packet += struct.pack('<I', struct.unpack_from('<I', data, 1)[0])
		# 		inject_joymax(0x706B, Packet, True)
		# 	else:
		# 		phBotChat.Guild('pe:0')
		# 		# phBotChat.Private('Cuantica', 'pt:'+pt)
		# 		if pt == partyNumber:
		# 			threading.Thread(target=sendTelegram, args=[get_character_data()['name'] + ' -> Ganador'],).start()
	elif opcode == 0x7074: #quest mob count
		log(str(struct.unpack_from('<I', data, 1)[0]))
	elif opcode == 0x300C:
		if data[0] == 5:# Unique Spawn
			uniqueName = get_monster(struct.unpack_from('<I', data, 2)[0])['name']
			log(uniqueName)
			if UniqueAlert and (uniqueName in uniques or 'STR' in uniqueName) and get_character_data()['name'] == 'Seven':
				play_wav('Sounds/Unique.wav')
				threading.Thread(target=sendTelegram, args=[uniqueName],).start()
				attackWolf = False
			if UINT:
				cancelAlchemy()
		elif data[0] == 6:
			if get_character_data()['region'] != 25037:
				easyPick()
			name = str(data[8:])[2:-1]
			log(name + ' Killed  -> '+ get_monster(struct.unpack_from('<I', data, 2)[0])['name'])
			if QtBind.text(gui,uniqueSTRname) != '' and QtBind.text(gui,uniqueSTRname).lower() in get_monster(struct.unpack_from('<I', data, 2)[0])['name'].lower():
				log('EJECUTANDO SCRIPT DE CAMBIO')
				Timer(10,afterUnique).start()
	elif opcode == 0x3080: #SERVER_GAME_PETITION_REQUEST exchange
		log('exchanginer')
		if data[0] == 1:
			inject_joymax(0x3080,b'\x01\x01',False)
	elif opcode == 0x30D5: #Kill quest Mob job
		return True
		if struct.unpack_from('<I', data, 6)[0] == 50401285:
			log('Priest: ' + str(struct.unpack_from('<I', data, 40)[0]))
			if struct.unpack_from('<I', data, 40)[0] == 250 and 'Harsa' not in get_training_area()['path']:
				changeTrainingArea('Harsa')
		elif struct.unpack_from('<I', data, 6)[0] == 33624069:
			log('Harsa: ' + str(struct.unpack_from('<I', data, 40)[0]))
			if struct.unpack_from('<I', data, 40)[0] == 200 and 'Keisas' not in get_training_area()['path']:
				changeTrainingArea('Keisas')
		elif struct.unpack_from('<I', data, 6)[0] == 16846853:
			log('Keisas: ' + str(struct.unpack_from('<I', data, 40)[0]))
			if struct.unpack_from('<I', data, 40)[0] == 200 and 'Priest' not in get_training_area()['path']:
				changeTrainingArea('Priest')
	elif opcode == 0x751A: #FGW
		log('me estas invitando?')
		return
		packet = data[:4] # Request ID
		packet += b'\x00\x00\x00\x00' # unknown ID
		packet += b'\x01' # Accept flag
		inject_joymax(0x751C,packet,False)
		log('Plugin: Forgotten World invitation accepted!')
	return True

def afterUnique():
	useSpecialReturnScroll()
	set_profile(QtBind.text(gui,configName))
	if QtBind.text(gui,configName) == 'Templo':
		j0b()
	else:
		start_bot()


def quest_complete():
	log('quest_complete')
	useSpecialReturnScroll()
	Timer(2,stop_bot).start()
	Timer(18, job).start()

def job():
	log('job')
	if get_inventory()['items'][8]:
		log('Hay capa')
		if get_position()['region'] == 26265: #Donwhang
			Dismount()
			inject_joymax(0x7061, bytearray(), False) #leave pt
			inject_joymax(0x7034, b'\x00\x08\x10\x00\x00', False) #quitar capa
			Timer(15, job).start()
	else:
		set_profile('Akeru')
		set_training_script(get_config_dir().replace('Config','Scripts')+'Akeru'+'.txt')
		log('No hay capa')
		npcs = get_npcs()
		Timer(0.5, move_to,[3548,2071,-106]).start()
		Timer(1, move_to,[3546,2086,-106]).start()
		for id, npc in npcs.items():
			if "Daily Quest Manager Shadi" in npc['name']:
				Timer(2,inject_joymax,[0x7045,struct.pack('I',id)+ b'\x00',False]).start() #Seleccionar NPC
				Timer(3,inject_joymax,[0x7046,struct.pack('I',id)+ b'5\x00\x02',False]).start() #Hablar con NPC
				Timer(4,inject_joymax,[0x30D4, b'\x08',False]).start() #Seleccionar Quest Templo
				Timer(5,inject_joymax,[0x30D4,b'\x05',False]).start() #Aceptar
				# Timer(6,phBotChat.All,['DWJG']).start()
				Timer(6, move_to,[3548,2071,-106]).start()
				Timer(7,start_bot).start()

def deleteClean():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'transport':
				for item in v['items']:
					if item != None:
						Timer(0.5,deleteClean).start()
						return
				break
	else:
		exitBandit()
	if v['type'] == 'pick' or v['type'] == 'wolf':
		exitBandit()
		return
	inject_joymax(0x70C6, struct.pack('I', k), False)
	Timer(1,deleteClean).start()


def TerminarTransporte():
	DismountTransport()
	p = get_position()
	pX = random.uniform(-2,2)
	pY = random.uniform(-2,2)
	pX = pX + p['x']
	pY = pY + p['y']
	threading.Thread(target=move, args=(pX,pY,p['z'])).start()
	log('Movido')
	Timer(2.0, TerminationTransport,).start()
	Timer(2.5, inject_joymax,[0x705A, b'\x01\x00\x00\x00\x01' , True]).start()

def delete_pet():
	verdemini('Quitando pets...')
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] != 'transport':
				data = struct.pack('i',petID) + b'\x00'
				inject_joymax(0x7116, data, True)
				Timer(0.5,delete_pet).start()
				return

def mihar():
	global partyNumber
	Party = get_party()
	if Party:
		for memberID in Party:
			if Party[memberID]['name'] == 'Mihar':
				inject_joymax(0x706B, struct.pack('I', int(partyNumber)), True)
				return
	if partyNumber != 0:
		phBotChat.Private('Zoser',str(partyNumber))
		Timer(3,mihar).start()
	if partyNumber == 0:
		if Party:
			inject_joymax(0x7069, b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03\x01\x87\x08\x00\x42\x75\x73\x63\x61\x6E\x64\x6F' , False)
		else:
			inject_joymax(0x7069, b'\x00\x00\x00\x00\x00\x00\x00\x00\x06\x03\x01\x6E\x08\x00\x42\x75\x73\x63\x61\x6E\x64\x6F' , False)
		Timer(1,mihar).start()

def spawnPickPet():
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'pick':
				return
	items = get_inventory()['items']
	for slot, item in enumerate(items):
		if item and 'Monkey' in item['name']:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xCC\x10', True)
			Timer(0.5,spawnPickPet).start()
			return
		elif item and 'Flinke' in item['name']:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xCD\x10', True)
			Timer(0.5,spawnPickPet).start()
			return

def spawnPets():
	verdemini('Spawmiando pets...')
	mono = False
	dragon = False
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'wolf':
				log('hay dragon')
				dragon = True
			elif pets[petID]['type'] == 'pick':
				log('hay mono')
				mono = True
	if dragon and mono:
		return
	items = get_inventory()['items']
	for slot, item in enumerate(items):
		if item and 'Red Dragon' in item['name'] and not dragon:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xCD\x08', True)
			Timer(0.5,spawnPets).start()
			return
		elif item and 'Monkey' in item['name'] and not mono:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xCC\x10', True)
			Timer(0.5,spawnPets).start()
			return
		elif item and 'Flinke' in item['name'] and not mono:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xCD\x10', True)
			Timer(0.5,spawnPets).start()
			return

def pickSpecialReturnScroll():
	verdemini('Agarrando Scroll')
	drops = get_drops()
	pet = False
	if drops:
		pets = get_pets()
		if pets:
			for n, v in pets.items():
				if v['type'] == 'pick':
					pet = True
					break
		for dropID in drops:
			if drops[dropID]['name'] == 'Special Return Scroll':
				if pet:
					inject_joymax(0x70C5, struct.pack('I', n) + b'\x08' + struct.pack('I', dropID), False) # pick with pet
				else:
					verde('no hay pet')
					inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False) # pick with pj
				Timer(0.5,pickSpecialReturnScroll).start()
				return
def mirror(f=0):
	npcs = get_npcs()
	for id, npc in npcs.items():
		if "SeaFarers Dimensional Gate" in npc['name']:
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\xCF\x00\x00\x00', False) #DWJG
			return
	return

def handle_silkroad(opcode,data):
	global PICK
	global partyNumber
	global targetBol
	global energy
	global mercaPos
	global merca
	if opcode == 0x2002 and checkParty() and ('Verbotene Ebene' == get_zone_name(get_character_data()['region']) or 'Tempel'  == get_zone_name(get_character_data()['region'])):
		pickWithPet()
		return True
	elif opcode == 0xA119: #HWID
		log('HWID')
		# log((' '.join('{:02X}'.format(x) for x in data)))
		return True
	elif opcode == 0x6102:
		log('6102')
		# killClient()
		return True
	# elif opcode == 0x7074:
	# 	return True
	# 	inject_joymax(0x7034,b'\x00\x0D\x06\x00\x00',False)
	elif opcode == 0xC00C and data == b'\x06\x00\x61\x75\x74\x6F\x65\x71':
		morado('Creo que es para actualizar el set')
		return True
		EquipUnequip()
	elif opcode == 0xC00C:

		#ESTE ERA PARA BUSCAR MERCA
		if merca:
			morado('STOP BOT')
			stop_bot()
			stop_trace()
		else:
			morado('START BOT')
			stop_bot()
			stop_trace()
			set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
			start_bot()
		merca = not merca
		return False
		mercaPos = []
		if merca:
			morado('OFF')
		else:
			morado('ON')
		buscarMerca()
	elif opcode == 0x7021 and mercaPos:
		#mide la distancia entre el pj y la merca
		x1 = get_position()['x']
		y1 = get_position()['y']
		dis = ((mercaPos[0]-x1)**2+(mercaPos[1]-y1)**2)**1/2
		morado(str(dis))
	elif opcode == 0x70C5: #attendance event
		return True
		azulPerma('atendance')
		if merca:
			morado('STOP BOT')
			stop_bot()
			stop_trace()
		else:
			morado('START BOT')
			stop_bot()
			stop_trace()
			set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
			start_bot()
		merca = not merca
		return False
		#mide la distancia entre el pj y la merca
		x1 = get_position()['x']
		y1 = get_position()['y']
		dis = ((mercaPos[0]-x1)**2+(mercaPos[1]-y1)**2)**1/2
		morado(str(dis))
	elif opcode == 0x7034: #put item equip wear
		#este opcode es para cuando se hace un cambio de item en el inventario o el se
		#anteriormente era para quitar los pets automaticamente cuando te ponias la capa, tambien te sacaba del pt en el que estabas
		return True
		morado('algo hace con la capa de thief')
		if data[0] == 0:
			if 'Thief ' in get_inventory()['items'][data[1]]['name']:
				inject_joymax(0x7061, bytearray(), False)
				return Dismount()
		# log(get_inventory()['items'][struct.unpack_from('>h', data, 0)[0]]['name'])
		# log(str(get_inventory()['items'][struct.unpack_from('>h', data, 0)[0]]))
	elif opcode == 0x706D:
		morado('joining party')
		partyNumber = struct.unpack_from('<I', data, 0)[0]
		notice(str(partyNumber))
	elif opcode == 0xA691:
		if data == b'\x2B\x23\x00\x00': #Unique Matching
			if merca:
				morado('STOP BOT')
				stop_bot()
				stop_trace()
			else:
				morado('START BOT')
				stop_bot()
				stop_trace()
				set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
				start_bot()
			merca = not merca
			return False
		elif data == b'\x36\x23\x00\x00':
			morado('joinParty')
			joinParty()
			return False
		elif data == b'\x3A\x23\x00\x00':
			return True
			morado('Target: General')
			targetBol = not targetBol
			targetGeneral()
		elif data == b'\x29\x23\x00\x00':
			#este era para invitar al otro thief al party y crear party match para robar juntos
			return False
			partyNumber = 0
			mihar()
		elif data == b'\x6E\x23\x00\x00': #socks
			return False
	elif opcode == 0x3091: #esencia1
		if data ==  b'\x00':
			#cambia a perfil grinding y se iba a scout a grindear
			morado('Grinding')
			set_profile('Grinding')
			Timer(0.5,changeTrainingArea,['Scout']).start()
			spawnPickPet()
			return False
			# trigerESSENCE()
		elif data == b'\x06':
			#cambia a perfil xBow y eliminaba los pets
			morado('2')
			mobs = get_monsters()
			for mobID in mobs:
				if mobs[mobID]['type'] == 24:
					dropScrollUnique()
					return False
			drops = get_drops()
			if drops:
				pickSpecialReturnScroll()
				return False
			UINT = True
			pets = get_pets()
			if pets:
				for petID in pets:
					if pets[petID]['type'] != 'transport':
						delete_pet()
						return False
			spawnPets()
			return False
			# trigerESSENCE2()
		elif data ==  b'\x01':
			morado('Mirror')
			stop_bot()
			stop_trace()
			set_profile('1')
			npcs = get_npcs()
			for id, npc in npcs.items():
				if "SeaFarers Dimensional Gate" in npc['name']:
					inject_joymax(0x705A, struct.pack('I',id)+b'\x02\xCF\x00\x00\x00', False) #DWJG
					break
			Timer(0.5,changeTrainingArea,['3mirror']).start()
			if get_character_data()['name'] == 'Seven':
				spawnPickPet()
			return False
			#Pick trade goods
			set_training_position(0,0,0,0)
			stop_trace()
			stop_bot()
			PICK = not PICK
			if PICK:
				notice('Pick activado')
			else:
				notice('Pick desactivado.')
			threading.Thread(target=pick_loop).start()
		elif data == b'\x05':
			PICK = not PICK
			morado('4')
			return False
		elif data ==  b'\x04':
			threading.Thread(target=picky).start()
			return False
		elif data ==  b'\x03':
			morado('pickWithPet?')
			pickWithPet()
			return False
			# followUnique()
		elif data ==  b'\x02':
			followUnique()
			return False
	elif opcode == 0x7402:
		energy = not energy
		if energy:
			notice('Energia Activada')
		else:
			notice('Energia Desactivada')
		useEnergy()
		return False
	return True

def useEnergy():
	global energy
	if energy:
		for slot, item in enumerate(get_inventory()['items']):
			if item:
				if 'Energy of Life' in item['name']:
					Packet = bytearray()
					Packet.append(slot)
					Packet.append(0xEC)
					Packet.append(0x76)
					inject_joymax(0x704C, Packet, True)
					inject_joymax(0x715F, b'\x89\x5D\x00\x00\x81\x5D\x00\x00', True)
					Timer(0.5,useEnergy).start()
					return

def targetHunter():
	mobs = get_monsters()
	for mobID in mobs:
		if 'Hunter' in mobs[mobID]['name'] and mobs[mobID]['hp'] != 0:
			Packet =  struct.pack('i', mobID)
			Packet += b'\x00'
			inject_joymax(0x7045, Packet, True)
			Timer(0.5,targetHunter).start()
			return


def notice(message):
	p = struct.pack('B',7)
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x3026,p,False)


UniqueAlert = False
UniqueStart = False
GMCheck = QtBind.createCheckBox(gui,'CheckGM','GM Notify',10,130)
UniqueCheck = QtBind.createCheckBox(gui,'UniqueCh','Unique',10,70)
UniqueStartSheck = QtBind.createCheckBox(gui,'UniqueStartSwitcher','Unique Start',70,70)
gSTR = QtBind.createCheckBox(gui,'UniqueSTR','STR',30,90)
gINT = QtBind.createCheckBox(gui,'UniqueINT','INT',30,110)
QtBind.setChecked(gui, UniqueCheck, UniqueAlert)
QtBind.setChecked(gui, UniqueStartSheck, UniqueStart)
QtBind.setChecked(gui, GMCheck, True)
GMDisconnect = QtBind.createCheckBox(gui,'GMDC','GM DC',10,150)
GM_Alert = True
GM_DC = False
QtBind.setChecked(gui, gSTR, USTR)

def UniqueStartSwitcher(checked):
	global UniqueStart
	UniqueStart = checked

def UniqueSTR(checked):
	global USTR
	USTR = checked

def UniqueINT(checked):
	global UINT
	UINT = checked

def UniqueCh(checked):
	global UniqueAlert
	UniqueAlert = checked


LastUniqueInRange = False

def handle_event(t, data):
	global UniqueAlert
	global GM_DC
	global partyAlert
	global UniqueStart
	global LastUniqueInRange
	global PICK
	global NPC
	if t == 9:
		log(data)
		if get_zone_name(get_character_data()['region']) not in ignoreZones:
			play_wav('Sounds/GM.wav')
			phBotChat.Party(dataf) #para eventos quitarle la f a data
			log(data)
			if GM_Alert:
				player = get_character_data()
				name = player['name']
				zona = ' | '+str(get_zone_name(get_position()['region']))
				xy = ' | ' +str(int(player['x']))+','+str(int(player['y']))
				play_wav('Sounds/GM.wav')
				if get_inventory()['items'][8]:
					threading.Thread(target=sendTelegram, args=[name + ' -> ' + data + zona + xy],).start()
	elif t == 7:
		log(data)
		if NPC:
			Timer(1, inject_joymax, [0x3053, b'\x01', True]).start()
		if get_character_data()['level'] < 11:
			Timer(1, inject_joymax, [0x3053, b'\x02', True]).start()
	elif t == 5:
		threading.Thread(target=sendTelegram, args=['*'+get_character_data()['name'] + '* -> `'+get_item(int(data))['name']+'`'],).start()
	elif t == 0 and UniqueAlert and '(INTs)' not in data and 'Apis' not in data and 'Priest of Luck' not in data and 'BeakYung' not in data:
		if get_character_data()['name'] != 'Seven':
			phBotChat.Private('Seven',data)
			UniqueStart = True
		LastUniqueInRange = data
		# targetUnique()
		useSpeed()
		play_wav('Sounds/Unique In Range.wav')
		notice(data)
		if partyAlert and data in uniques:
			phBotChat.Party('Here ---> ['+ data + ']')
		# cancelAlchemy()
		if 'Balloon' not in data:
			PICK = True
			goUnique()
	elif t == 8:
		threading.Thread(target=sendTelegram2, args=['Alchemy Finished']).start()
		# quitarDressLucky()

def petScroll(arg = 0):
	i = 0
	for x in get_inventory()['items']:
		if x:
			if x['name'] == 'Red Wolf Summon Scroll Skin Scroll':
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xEC)
				Packet.append(0x09)
				inject_joymax(0x704C, Packet, True)
				break
		i+=1
	return False

def CheckGM(checked):
	global GM_Alert
	GM_Alert = checked

def GMDC(checked):
	global GM_DC
	GM_DC = checked

def Notificar(checked):
	global TelegramBol
	TelegramBol = checked

def partyAlertChecker(checked):
	global partyAlert
	partyAlert = checked

def PickAfterFunction(checked):
	global pickAfterJoin
	pickAfterJoin = checked

btnReturn	= QtBind.createButton(gui,'SELL','SELL',250,65)
btnLast		= QtBind.createButton(gui,'Last','Last Recall Point',250,100)
DROP1GOLD	= QtBind.createButton(gui,'DROPXD','DROPGOLD',250,250)
clockBtn	= QtBind.createButton(gui,'resPet','CLOCK',600,210)
pickBTN		= QtBind.createButton(gui,'pick_function','PICK',600,240)
testing		= QtBind.createButton(gui,'testinger','TEST',250,280)
selectPJbtn	= QtBind.createButton(gui,'select','Select',600,290)
clientlessbtn	= QtBind.createButton(gui,'killClient','Clientless',650,290)
KillClientCheck = QtBind.createCheckBox(gui,'AutoClientless','Auto Clientless',560,260)
QtBind.setChecked(gui, KillClientCheck, True)

def testinger():
	update_plugin()
	return
	player_id = get_character_data()['player_id']
	log(f'{player_id}')
	message = 'Mensaje de prueba'
	green(message)

def alejare():
	stop_bot()
	x1 = get_position()['x']
	y1 = get_position()['y']
	x2 = mobs[mobID]['x']
	y2 = mobs[mobID]['y']
	R = 25
	dx = x1 - x2
	dy = y1 - y2
	distancia = math.sqrt(dx**2 + dy**2)
	dx /= distancia
	dy /= distancia
	x3 = x2 + dx * R
	y3 = y2 + dy * R
	infinito(x3,y3)

def infinito():
	azul('move_to_npc')
	x1 = get_position()['x']
	y1 = get_position()['y']
	dis = ((x-x1)**2+(y-y1)**2)**1/2
	move_to(x,y,0)
	Timer(0.2,move_to_npc,[x,y]).start()
	if dis > 2:
		set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
		start_bot()
		return
	notice(str(dis))


def move_to_npc(x,y):
	azul('move_to_npc')
	x1 = get_position()['x']
	y1 = get_position()['y']
	dis = ((x-x1)**2+(y-y1)**2)**1/2
	move_to(x,y,0)
	Timer(0.2,move_to_npc,[x,y]).start()
	if dis > 2:
		speak_npc()
		return
	notice(str(dis))

def call_one_for_one(slot):
	if slot < 8:
		Party = get_party()
		for i,memberID in enumerate(Party):
			if i == slot:
				inject_joymax(0x751A, struct.pack('I',memberID), False)
				Timer(0.5,call_one_for_one,[slot+1]).start()
				return

def speak_npc():
	npcs = get_npcs()
	for id, npc in npcs.items():
		if npc['name'] == 'Säule zum Rückruf der Gruppenmitglieder':
			inject_joymax(0x7045, struct.pack('L', id), False)
			log('Selecting NPC')
			Timer(1,inject_joymax,[0x7519, struct.pack('L', id), False]).start()
			Timer(1.5,log,['Starting to call members...'])
			Timer(2,call_one_for_one,[0]).start()
			return


def spawn_dimension():
	for slot, item in enumerate(get_inventory()['items']):
		if slot > 13 and item:
			if 'Hall of Worship (Level 1)' in item['name']:
				inject_joymax(0x704C, struct.pack('b', slot)+b'\x6C\x3E', True)
				log('Spawming dimension...')
				return

WTS = ['WTS PROTECTOR HANDS +8', 'WTS ARMOR HANDS +8', 'WTS GARMENT CHEST +7', 'WTS L.A HANDS +8', 'WTS PROTECTOR HEAD +7', 'WTS GARMENT CHEST +8', 'WTS PROTECTOR LEGS +8', 'WTS GARMENT FOOT +8']


def punto_mas_cercano(x1, y1, x2, y2, R):
    # Calcular el vector desde el centro de la circunferencia hasta el punto externo
    dx = x1 - x2
    dy = y1 - y2
    
    # Calcular la distancia desde el centro al punto externo
    distancia = math.sqrt(dx**2 + dy**2)
    
    # Normalizar el vector
    dx /= distancia
    dy /= distancia
    
    # Calcular el punto más cercano en el perímetro de la circunferencia
    x3 = x2 + dx * R
    y3 = y2 + dy * R
    
    infiniteMove(x3,y3)

def kick(slot=8):
	Party = get_party()
	for i,memberID in enumerate(Party):
		if i == slot:
			inject_joymax(0x7063, struct.pack('I',memberID), True)


def crystal():
	if get_quests()[371]['completed']:
		useSpecialReturnScroll()
	else:
		for slot, item in enumerate(get_inventory()['items']):
			if slot > 13 and item:
				if 'Shining Crystal' in item['name']:
					inject_joymax(0x704C, struct.pack('b', slot)+b'\xEC\x04', True)
					Timer(1,crystal).start()
					break


def AutoClientless(checked):
	global CLIENTLESS_BOL
	CLIENTLESS_BOL = checked

def select():
	inject_joymax(0x7001, struct.pack('H', len(QtBind.text(gui,text))) + QtBind.text(gui,text).encode('ascii'), True)
	# select_character(QtBind.text(gui,text))

def killClient():
	os.kill(get_client()['pid'], signal.SIGTERM)

def dropScrollUnique():
	verdemini('Tirando scrolls')
	mobs = get_monsters()
	for mobID in mobs:
		if mobs[mobID]['type'] == 24:
			Party = get_party()
			i = 0
			if Party:# and get_character_data()['name'] == 'Seven':
				for memberID in Party:
					if Party[memberID]['name'] == 'Seven':
						break
					elif Party[memberID]['region'] == get_character_data()['region']:
						i+=1
			verdemini(str(i))
			dropSpecialReturnScroll(i)
			break
	return True


# Definir las constantes y tipos necesarios de la API de Windows
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Definir el tipo de función GetWindowText
GetWindowText = user32.GetWindowTextW
GetWindowText.restype = ctypes.c_int
GetWindowText.argtypes = [ctypes.c_int, ctypes.c_wchar_p, ctypes.c_int]

# Función para obtener el nombre de la ventana
def obtener_nombre_ventana(window_id):
    # Crear un buffer para almacenar el título de la ventana
    buffer = ctypes.create_unicode_buffer(512)  # 512 caracteres es suficientemente grande
    length = GetWindowText(window_id, buffer, len(buffer))
    
    if length > 0:
        return buffer.value
    else:
        return f"La ventana con ID {window_id} no tiene un título o no es accesible."

def dropSpecialReturnScroll(n):
	if n > 0:
		for i,item in enumerate(get_inventory()['items']):
			if item and i>12 and item['name'] == 'Special Return Scroll' and item['quantity'] > 1:
				log(str(i))
				Packet = bytearray()
				Packet.append(0x00)
				Packet.append(i)
				for j,item2 in enumerate(get_inventory()['items']):
					if j>12 and item2 == None:
						Packet.append(j)
						Packet.append(0x01)
						Packet.append(0x00)
						inject_joymax(0x7034, Packet, True)
						Timer(0.5,dropSpecialReturnScroll,[n-1]).start()
						return
	elif n == 0:
		for i,item in enumerate(get_inventory()['items']):
			if item and i>12:
				if item['name'] == 'Special Return Scroll' and item['quantity'] == 1:
					Packet = bytearray()
					Packet.append(0x07)
					Packet.append(i)
					inject_joymax(0x7034, Packet, True)
					Timer(0.5,dropSpecialReturnScroll,[n]).start()
					return
		n = -1
	drops = get_drops()
	if n == -1:
		pets = get_pets()
		if pets:
			for n, v in pets.items():
				if v['type'] == 'pick':
					n = n*-1
					break
	if drops:
		for dropID in drops:
			if drops[dropID]['name'] == 'Special Return Scroll':
				inject_joymax(0x70C5, struct.pack('I', n*-1) + b'\x08' + struct.pack('I', dropID), False) # pick with pet
				# inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False) # pick with pj
				Timer(0.5,dropSpecialReturnScroll,[n]).start()
				return
	return

def red(message):
	name = 'Rahim'
	data = b'\x42'+struct.pack('H', len(name))
	for word in name:
		data += word.encode('ascii')
		data += b'\x00'
	data += struct.pack('H', len(message))
	for word in message:
		data += word.encode('ascii')
		data += b'\x00'
	data += b'\x00\x00\xFF\xFF\xEC\xEB\x10\x01\x00'
	inject_silkroad(0x30CF,data,False)

def green(message):
	name = 'Rahim'
	data = b'\x42'+struct.pack('H', len(name))
	for word in name:
		data += word.encode('ascii')
		data += b'\x00'
	data += struct.pack('H', len(message))
	for word in message:
		data += word.encode('ascii')
		data += b'\x00'
	data += b'\x00\xFF\x00\xFF\xF1\x2C\x30\x01\x00'
	inject_silkroad(0x30CF,data,False)


def Union(message):
	message = ') '+message
	p = b'\x0B'
	p += struct.pack('H', len('Serapis'))
	p += 'Serapis'.encode('ascii')
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x3026,p,False)

def tlp():
	inject_joymax(0x705B, bytearray(), False)
	npcs = get_npcs()
	for id, npc in npcs.items():
		log(npc['name'])
		if npc['name'] == 'Tunnelaufseher Salhap':#Tunel 1
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x1E\x00\x00\x00', False)
		elif npc['name'] == 'Tunnelaufseher Maryokuk':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x1B\x00\x00\x00', False)
		elif npc['name'] == 'Tunnelaufseher Topni': #Tunel 2
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x1D\x00\x00\x00', False)
		elif npc['name'] == 'Tunnelaufseher Asui':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x1A\x00\x00\x00', False)
		elif npc['name'] == 'Ferry Ticket Seller Hageuk': #Jangan West
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x09\x00\x00\x00', False)
		elif npc['name'] == 'Ferry Ticket Seller Chau':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x06\x00\x00\x00', False)
		elif npc['name'] == 'Ferry Ticket Seller Doji': #Jangan East
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x04\x00\x00\x00', False)
		elif npc['name'] == 'Ferry Ticket Seller Tayun':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x03\x00\x00\x00', False)
		elif npc['name'] == 'Boat Ticket Seller Rahan': #Hotan Ravine
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x0E\x00\x00\x00', False)
		elif npc['name'] == 'Boat Ticket Seller Salmai':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x0C\x00\x00\x00', False)
		elif npc['name'] == 'Boat Ticket Seller Asa': #Hotan Black Robber
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x0D\x00\x00\x00', False)
		elif npc['name'] == 'Boat Ticket Seller Asimo':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x0F\x00\x00\x00', False)
		elif npc['name'] == 'Flugkartenverkäuferin Shard': #Ivy
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x1F\x00\x00\x00', False)
		elif npc['name'] == 'Flugkartenverkäuferin Sangnia':
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x18\x00\x00\x00', False)
		elif npc['name'] == 'Harbor Manager Marwa' or npc['name'] == 'Pirate Morgun': #Alexandria
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x15\x00\x00\x00', False)
		elif npc['name'] == 'Harbor Manager Gale': #Dock
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x16\x00\x00\x00', False)
		elif npc['name'] == 'Pirate Blackbeard': #Sigia
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x15\x00\x00\x00', False)
		elif npc['name'] == 'Grab des Kaisers Qin-Shi Lv.4': #Medusa
			data = struct.pack('h',id)+b'\x00\x00\x03\x00'
			log((' '.join('{:02X}'.format(x) for x in data)))
			inject_joymax(0x705A, data, False)
		# elif npc['name'] == 'Dimensionslücke':
		# 	#54 FF 4D 05 03 00
		# 	data = struct.pack('I',id)+b'\x03\x00'
		# 	log((' '.join('{:02X}'.format(x) for x in data)))
		# 	inject_joymax(0x705A, data, False)
		# elif npc['name'] == '':
		# 	data = struct.pack('I',id)+b'\x03\x00'
		# 	log((' '.join('{:02X}'.format(x) for x in data)))
		# 	inject_joymax(0x705A, data, False)

def morado(message):
	p = struct.pack('B',7)
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x30CF,b'\x15'+p,False)

def azul(message):
	p = b'\x15\x02'
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x30CF,p,False)

def azulPerma(message):
	p = b'\x15\x04'
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x30CF,p,False)

def verde(message):
	p = b'\x15\x01'
	p += struct.pack('H', len(message))
	p += message.encode('ascii')
	inject_silkroad(0x30CF,p,False)

def verdemini(message):
	p = b'\x15\x06'+struct.pack('H', len(message))+message.encode('ascii') + b'\x00\xFF\x27\x00\x00'
	inject_silkroad(0x30CF,p,False)

def purple(message):
	p = b'\x15\x06'+struct.pack('H', len(message))+message.encode('ascii') + b'\xEE\x88\xA7\x00\x01'
	inject_silkroad(0x30CF,p,False)

def aqua(message):
	inject_silkroad(0x30CF,b'\x15\x09'+struct.pack('H', len(message))+message.encode('ascii') + b'\xE0\xED\x2B\x00\x01',False)

def aquamini(message):
	data = b'\x15\x06'+struct.pack('H', len(message))+message.encode('ascii') + b'\xE0\xED\x2B\x00\x01'
	inject_silkroad(0x30CF,data,False)

def unequipar():
	if partyNumber != 0:
		items = get_inventory()['items']
		for i,item in enumerate(items):
			if item and i !=6 and i!=7 and 1!=8:
				log(item['name'])
				inject_joymax(0x7034, b'\x00'+ struct.pack('b', i) + b'\x14\x00\x00', True)
				Timer(0.3,unequipar).start()
				break
			if i>11:
				return

def emptySlot():
	items = get_inventory()['items']
	for i,item in enumerate(items):
		if i < 13 and i !=6 and i !=7 and i !=8:
			if item == None:
				return i
		elif i > 12:
			return i

accesories = ['ITEM_EU_EARRING_11_A_RARE','ITEM_EU_NECKLACE_11_A_RARE','ITEM_EU_RING_11_A_RARE','ITEM_EU_RING_11_A_RARE']

def equipar():
	if partyNumber != 0:
		items = get_inventory()['items']
		for i,item in enumerate(items):
			if item and i > 12:
				slot = emptySlot()
				if slot > 12:
					return
				if 'ITEM_EU_M_LIGHT_11_' in item['servername'] or item['servername'] in accesories:
					log(str(slot))
					data = b'\x00'+ struct.pack('b', i) + struct.pack('b', slot)+ b'\x00\x00'
					inject_joymax(0x7034, b'\x00'+ struct.pack('b', i) + struct.pack('b', slot)+ b'\x00\x00', True)
					Timer(0.3,equipar).start()
					break

def EquipUnequip():
	if get_inventory()['items'][0]: #hay que unequipar
		unequipar()
	else:
		equipar()

def vaciarPickPet():
	global partyNumber
	if partyNumber != 0:
		pets = get_pets()
		if pets:
			for k, v in pets.items():
				if v['type'] == 'pick':
					i = 0
					for item in v['items']:
						if item and '_11_A' in item['servername'] and 'RARE'not in item['servername']:
							log(item['name'])
							data = b'\x1A'+struct.pack('i', k) + struct.pack('b', i)
							items = enumerate(get_inventory()['items'])
							for slot, item in items:
								if slot > 12 and item == None:
									data = b'\x1A'+struct.pack('i', k) + struct.pack('b', i) + struct.pack('b', slot)
									inject_joymax(0x7034,data,False)
									return
						i+=1
def cancelscroll(s):
	useSpecialReturnScroll()
	Timer(0.5,cancelReturnScroll).start()
	return True

def checkParty():
	Party = get_party()
	if Party and get_character_data()['name'] == 'Seven':
		for memberID in Party:
			if Party[memberID]['region'] == get_character_data()['region'] and Party[memberID]['name'] != 'Seven':
				return False
	return True

def pickCarnivalBox(k=0):
	log('pickCarnivalBox')
	drops = get_drops()
	if k == 0:
		pets = get_pets()
		if pets:
			for k, v in pets.items():
				if v['type'] == 'pick':
					break
	if drops:
		for dropID in drops:
			if 'carnival' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
					Timer(0.2,pickCarnivalBox,[k]).start()
					log(drops[dropID]['name'])
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				Timer(0.2,pickCarnivalBox,[k]).start()
				log(drops[dropID]['name'])
				return
		for dropID in drops:
			if '_RARE' in drops[dropID]['servername']:
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
				inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				log(drops[dropID]['name'])
				Timer(0.2,pickCarnivalBox,[k]).start()
				return
		for dropID in drops:
			if 'gold' in drops[dropID]['name'].lower():
				if k != 0:
					inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
					Timer(0.2,pickCarnivalBox,[k]).start()
					log(drops[dropID]['name'])
					return
				# inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID), False)
				return


def pickWithPet():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'pick':
				drops = get_drops()
				if drops:
					for dropID in drops:
						inject_joymax(0x70C5, struct.pack('I', k) + b'\x08' + struct.pack('I', dropID), False)
						Timer(0.5,pickWithPet).start()
						return


def quitarInvisible():
	global PICK
	return PICK
			

def pick_function():
	log('pick_function')
	global PICK
	PICK = not PICK
	pick_loop()

targetBol = False

def targetUnique():
	global LastUniqueInRange
	global uniques
	if LastUniqueInRange:
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['type'] == 24 and (mobs[mobID]['name'] in uniques or 'STR' in mobs[mobID]['name']):
				inject_joymax(0x7045, struct.pack('L', mobID), False)
				break
		Timer(0.5,targetUnique).start()



def targetGeneral():
	global targetBol
	if targetBol:
		log('targeting generaling')
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['type'] == 0 and mobs[mobID]['hp'] != 0:
				x1 = get_position()['x']
				y1 = get_position()['y']
				max_distance = 0
				for mobID in mobs:
					if mobs[mobID]['type'] < 2 and mobs[mobID]['hp'] != 0:
						x2 = mobs[mobID]['x']
						y2 = mobs[mobID]['y']
						dis = ((x2-x1)**2+(y2-y1)**2)**1/2
						if max_distance == 0:
							max_distance = dis
							mobID_MAS_CERCANO = mobID
						elif dis < max_distance:
							max_distance = dis
							mobID_MAS_CERCANO = mobID
				inject_joymax(0x7045, b''+ struct.pack('<I', mobID_MAS_CERCANO), False)
				Timer(0.1,targetGeneral).start()
				return

def quitarDressLucky():
	return
	global partyNumber
	if get_character_data()['name'] == 'Seven':
		if partyNumber != 0:
			ya_no_tengo_dress_lucky = False
			slut = 0
			for slot, item in enumerate(get_inventory()['items']):
				if item:
					if item['name'] == 'Boss Kelbim Female Dress (F)':
						log(item['name'])
						ya_no_tengo_dress_lucky = True
					elif item['name'] == 'Arabian - Black Edition Dress (F)':
						log(item['name'])
						slut = slot
						if ya_no_tengo_dress_lucky:
							break
			if not ya_no_tengo_dress_lucky:
				inject_joymax(0x7034, b'\x23\x00\x16', False) #quitar dress
				Timer(0.5,quitarDressLucky).start()
				return
			elif slut != 0:
				# log(str(slot))
				# log(str(get_inventory()['items'][slot]))
				inject_joymax(0x7034, b'\x24' + struct.pack('I', slut) + b'\x00', False) #quipar dress
				Timer(0.5,quitarDressLucky).start()
				return
			for slot, item in enumerate(get_inventory()['items']):
				if item:
					if item['name'] == 'Arabian - Black Edition Accessory (F)':
						log(item['name'])
						inject_joymax(0x7034, b'\x24' + struct.pack('I', slot) + b'\x01', False)
						Timer(0.5,quitarDressLucky).start()
						return
			if get_inventory()['items'][13]:
				if get_inventory()['items'][13]['name'] == 'Global chatting':
					start_bot()
					for slot, item in enumerate(get_inventory()['items']):
						if slot > 13:
							if item == None:
								inject_joymax(0x7034, b'\x00'+ struct.pack('b', 13) + struct.pack('b', slot) + struct.pack('b', get_inventory()['items'][13]['quantity'])+b'\x00', True)
								return
	return





def quitarDressLuckyOLD():
	return 
	if get_character_data()['name'] == 'Seven':
		HayDress1 = True
		HayDress2 = True
		slut = 0
		items = enumerate(get_inventory()['items'])
		for slot, item in items:
			if item:
				if item['name'] == 'Arabian - Black Edition Dress (M)':
					log(item['name'])
					slut = slot
				elif item['name'] == 'Boss Kelbim Female Dress (F)':
					HayDress1 = False
				elif item['name'] == 'Samurai Dress (M)':
					HayDress2 = False
		if HayDress1 or HayDress2:
			inject_joymax(0x7034, b'\x23\x00\x16', False) #quitar dress
		if slut != 0:
			inject_joymax(0x7034, b'\x24' + struct.pack('I', slut) + b'\x00', False)
			Timer(0.5,quitarDressLucky).start()
			return
		items = enumerate(get_inventory()['items'])
		for slot, item in items:
			if item:
				if item['name'] == 'Arabian - Black Edition Accessory (F)':
					log(item['name'])
					inject_joymax(0x7034, b'\x24' + struct.pack('I', slot) + b'\x01', False)
					Timer(0.5,quitarDressLucky).start()
					return
		if get_inventory()['items'][13]:
			if get_inventory()['items'][13]['name'] == 'Global chatting':
				start_bot()
				for slot, item in enumerate(get_inventory()['items']):
					if slot > 13:
						if item == None:
							inject_joymax(0x7034, b'\x00'+ struct.pack('b', 13) + struct.pack('b', slot) + struct.pack('b', get_inventory()['items'][13]['quantity'])+b'\x00', True)
							return
	return

def questHWT():
	quests = get_quests()
	for questID in quests:
		if quests[questID]['name'] == 'Collecting Pharaoh Tomb Heart (Beginner)':
			if quests[questID]['objectives'][0]['progress'] == 4:
				log('casi')
			break

def picky():
	drops = get_drops()
	if drops:
		for dropID in drops:
			x1 = get_position()['x']
			y1 = get_position()['y']
			max_distance = 0
			for dropID in drops:
				x2 = drops[dropID]['x']
				y2 = drops[dropID]['y']
				dis = ((x2-x1)**2+(y2-y1)**2)**1/2
				if max_distance == 0:
					max_distance = dis
					dropID_MAS_CERCANO = dropID
				elif dis < max_distance:
					max_distance = dis
					dropID_MAS_CERCANO = dropID
			inject_joymax(0x7074, b'\x01\x02\x01' + struct.pack('I', dropID_MAS_CERCANO), False)
			log('Agarrando Drop...')
			Timer(0.5,picky).start()
			return
	


def resPet():
	for i, item in enumerate(get_inventory()['items']):
		if item and i > 13:
			if 'Clock of Reincarnation' in item['name']:
				Packet = bytearray()
				Packet.append(i)
				Packet+= b'\xED\x66'
				for i, item in enumerate(get_inventory()['items']):
					if item and i > 13:
						if 'Flinke' in item['name'] or 'Monkey Summon Scroll' in item['name']:
							Packet.append(i)
							inject_joymax(0x704C, Packet, True)
							Timer(0.5,resPet).start()
							return



def uniqueHP():
	log('uniqueHP')
	mobs = get_monsters()
	for mobID in mobs:
		if mobs[mobID]['type'] != 24:
			# log(str(mobs[mobID]['hp']))
			log(str(mobs[mobID]['max_hp']))
			# log(str(round(mobs[mobID]['hp']/mobs[mobID]['max_hp'],2)))
			# phBotChat.Party('HP: '+str(round(mobs[mobID]['hp']/mobs[mobID]['max_hp'],2)*100)+'%')
			return

def getlog():
	log("\n+++"+str(get_log())+'+++')



def SELL():
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'transport':
				for i, item in enumerate(pets[petID]['items']):
					if item != None:
						# Packet = bytearray(b'\x14\xF1\x4A\xED\x00')
						Packet = bytearray(b'\x14\x90\x0E\x14\x00')
						Packet.append(i)
						Packet += b'\x90\x01\x1B\x00\x00\x00'
						inject_joymax(0x5624, Packet, True)
						log(str(get_character_data()['gold']))
						sleep(0.5)
						threading.Thread(target=SELL).start()
						break

def goUnique():
	UniqueDown = ['Cerberus','Tiger Girl','Captain Ivy']
	log('goUnique')
	global UniqueStart
	global uniques
	global PICK
	if PICK:
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['type'] == 24:
				if (mobs[mobID]['name'] in uniques or 'STR' in mobs[mobID]['name']):
					x1 = mobs[mobID]['x']
					y1 = mobs[mobID]['y']
					move_to(x1,y1,0)
					if UniqueStart:
						stop_bot()
						stop_trace()
						set_training_position(0,x1,y1,0)
						log('iniciando bot por Unique')
						start_bot()
					x2 = get_position()['x']
					y2 = get_position()['y']
					dis = ((x2-x1)**2+(y2-y1)**2)**1/2
					if mobs[mobID]['name'] in UniqueDown:
						dis = dis-600
						pets = get_pets()
						if pets:
							for petID, v in pets.items():
								if v['type'] == 'wolf':
									inject_joymax(0x70C5, struct.pack('i', petID) +b'\x02' +struct.pack('i', mobID), False)
									break
					if dis < 100:
						DismountHorse()
						return
				else:
					return
		Timer(0.1,goUnique).start()

def getWolf():
	pets = get_pets()
	if pets:
		for pet, v in pets.items():
			if v['type'] == 'wolf':
				return pet	

def followUnique():
	global UINT
	mobs = get_monsters()
	for mobID in mobs:
		if mobs[mobID]['type'] == 24:
			move_to(mobs[mobID]['x'],mobs[mobID]['y'],0)
			Timer(1,followUnique).start()
			return
	UINT = True

DROP = False

def DROPXD():
	global DROP
	DROP = ~DROP
	if DROP:
		DROP1()

def DROP1():
	global DROP
	if DROP:
		Packet = b'\x0A'
		Packet += struct.pack('<I', 1)
		Packet += b'\x00\x00\x00\x00'
		inject_joymax(0x7034, Packet, False)
		Timer(0.5,DROP1).start()

def ReturnScroll():
	Packet = b'\x7F\xAA\x00\x00\xB9\x0E\x00\x00'
	inject_joymax(0x715F, Packet, True)

def Last():
	Packet = b'\x7F\xAA\x00\x00\xD3\x0E\x00\x00\x02'
	inject_joymax(0x715F, Packet, True)
	
invisible = False
btn1 = QtBind.createButton(gui,'Dismount','DISMOUNT',600,40)
btn1 = QtBind.createButton(gui,'DismountHorse','DISMOUNT HORSE',600,10)
btn2 = QtBind.createButton(gui,'MountTransport','MOUNT',600,70)
btn3 = QtBind.createButton(gui,'TerminationTransport','TERMINATE',600,100)
btn4 = QtBind.createButton(gui,'summonTradeHorse','SUMMON TRADER',600,130)
btn5 = QtBind.createButton(gui,'cancelReturnScroll','Cancelar Scroll',100,120)
# btn6 = QtBind.createButton(gui,'Disconected','DISCONECT',100,155)
btn7 = QtBind.createButton(gui,'useBanditScroll','Bandit Scroll',10,40)
btn8 = QtBind.createButton(gui,'DC','DC',10,170)
btn08 = QtBind.createButton(gui,'disco','disconnect',10,190)
btn9 = QtBind.createButton(gui,'unequipJob','Unequip Job',250,160)
btn9 = QtBind.createButton(gui,'equipJob','Equip Job',250,190)
btn10 = QtBind.createButton(gui,'petScroll','Pet Scroll',600,160)
termbtm	= QtBind.createButton(gui,'TerminarTransporte','term',250,130)
termbtm1 = QtBind.createButton(gui,'spawnHorse','HORSE',600,190)
buscarMercabtn = QtBind.createButton(gui,'buscarMerca','buscarMerca',20,290)
Essences = QtBind.createButton(gui,'trigerESSENCE','ESSENCE',20,260)

def disco():
	inject_joymax(0x7061, bytearray(), False)

def DC():
	inject_joymax(0x704C, bytearray(), False)
	killClient()
	log('DC')
	return False

superEssence = False
superEssence2 = False
balloon = False
def event_loop():
	global PICK
	global uniques
	if PICK:
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['type'] == 24 and (mobs[mobID]['name'] in uniques or 'STR' in mobs[mobID]['name']):
				inject_joymax(0x7045, struct.pack('L', mobID), False)
				break
	global superEssence
	global superEssence2
	if superEssence:
		pets = get_pets()
		if pets:
			for petID in pets:
				if pets[petID]['name'] == 'Red Dragon':
					Strength = False
					Physical = False
					skills = get_active_skills()
					for skillID in skills:
						if skills[skillID]['name'] == 'Speed Essence':
							log('Eliminando Speed Essence')
							inject_joymax(0x7074, b'\x01\x05\x08\x85\x00\x00\x00', True)
						if skills[skillID]['name'] == 'Strength Essence':
							Strength = True
						elif skills[skillID]['name'] == 'Physical Damage Essence':
							Physical = True
					if not Strength:		
						inject_joymax(0xA691, b'\x33\x23\x00\x00', False)
					if not Physical:
						inject_joymax(0xA691, b'\x37\x23\x00\x00', False)
					break
	if superEssence2:
		pets = get_pets()
		if pets:
			for petID in pets:
				if pets[petID]['name'] == 'Red Dragon':
					Strength = False
					Speed = False
					skills = get_active_skills()
					for skillID in skills:
						if skills[skillID]['name'] == 'Physical Damage Essence':
							log('Eliminando Physical Damage Essence')
							inject_joymax(0x7074, b'\x01\x05\x06\x85\x00\x00\x00', True)
						if skills[skillID]['name'] == 'Speed Essence':
							Speed = True
						elif skills[skillID]['name'] == 'Strength Essence':
							Strength = True
					if not Speed:
						inject_joymax(0xA691, b'\x39\x23\x00\x00', False)
					if not Strength:		
						inject_joymax(0xA691, b'\x33\x23\x00\x00', False)
					break

def trigerESSENCE(n=0):
	global superEssence
	global superEssence2
	superEssence2 = False
	superEssence = not superEssence
	if superEssence:
		notice('Esencia Activada')
	else:
		notice('Esencia Desactivada')
	return True

def trigerESSENCE2(n=0):
	global superEssence2
	global superEssence
	superEssence = False
	superEssence2 = not superEssence2
	if superEssence2:
		notice('Esencia Activada')
	else:
		notice('Esencia Desactivada')

def ESSENCE():
	global superEssence
	if superEssence:
		pets = get_pets()
		if pets:
			for petID in pets:
				if pets[petID]['name'] == 'Red Dragon':
					Strength = False
					Physical = False
					skills = get_active_skills()
					for skillID in skills:
						if skills[skillID]['name'] == 'Strength Essence':
							Strength = True
						elif skills[skillID]['name'] == 'Physical Damage Essence':
							Physical = True
					if not Physical:
						inject_joymax(0xA691, b'\x37\x23\x00\x00', False)
					if not Strength:		
						inject_joymax(0xA691, b'\x33\x23\x00\x00', False)
					break
		Timer(1,ESSENCE).start()

def AtackPet():
	log('atacando')
	if atackSUNGSUNG:
		mobs = get_monsters()
		for mobID in mobs:
			if mobs[mobID]['name'] == 'Ghost SungSung':
				p =  struct.pack('i', getWolf())
				p += b'\x02'
				p += struct.pack('i', mobID)
				inject_joymax(0x70C5, p, False)
				break
		Timer(1,AtackPet).start()


def getWolf():
	pets = get_pets()
	if pets:
		for pet, v in pets.items():
			if v['type'] == 'wolf':
				# log(str(v))
				break
	return pet

def buscarMerca():
	global merca
	merca = not merca
	soundMerca()

def soundMerca():
	log('Buscando...')
	global merca
	global mercaPos
	global PICK
	if merca:
		drops = get_drops()
		if drops:
			for dropID in drops:
				if 'TRADE' in drops[dropID]['servername']:
					log(drops[dropID]['servername'])
					mercaPos.append(drops[dropID]['x'])
					mercaPos.append(drops[dropID]['y'])
					stop_bot()
					merca = False
					play_wav('Sounds/MercaEncontrada.wav')
					if PICK:
						pick_loop()
					break
		Timer(1,soundMerca).start()

def goMerca():
	global mercaPos
	move_to(mercaPos[0],mercaPos[1],0)
	return

def puntoV():
	log('puntoV')
	global PICK
	drops = get_drops()
	if drops:
		for dropID in drops:
			if 'TRADE' in drops[dropID]['servername']:
				log(drops[dropID]['servername'])
				inject_joymax(0x705B, bytearray(), False)
				PICK = True
				buscarMerca()
				return
	Timer(1,puntoV).start()

def j0b():
	# if get_zone_name(get_position()['region']) == 'Western-China-Donwhang':
	if get_zone_name(get_position()['region']) == 'Samarkand':
		set_profile('Templo')
		set_training_script(get_config_dir().replace('Config','Scripts')+'Priest.txt')
		inject_joymax(0x7061, bytearray(), False) #leave
		Timer(2, DismountTransporte).start()
		Timer(3, equipJob).start()
		if get_inventory()['items'][8]:
			start_bot()
		else:
			Timer(15, j0b).start()	
	else:
		Timer(1, j0b).start()

def unequipJob():
	global stats
	stats = True
	Dismount()
	inject_joymax(0x7061, bytearray(), False)
	Packet = bytearray()
	Packet.append(0x00)
	Packet.append(0x08)
	Packet.append(0x10)
	Packet.append(0x00)
	Packet.append(0x00)
	inject_joymax(0x7034, Packet, False)
	log('Quitando capa')

def equipJob():
	global partyNumber
	SAFE_ZONES = [26265,23687,27244,26959,25000,23603,23088]
	if get_character_data()['region'] in SAFE_ZONES:
		stop_bot()
		delete_pet()
		if get_inventory()['items'][8]:
			return
		else:
			stats = True
			Dismount()
			if get_party():
				inject_joymax(0x706B,struct.pack('I',partyNumber),False)
				inject_joymax(0x7061, bytearray(), False)
				Timer(0.3,equipJob).start()
				return
			else:
				for k, item in enumerate(get_inventory()['items']):
					if item and k > 12 and ('Thief ' in item['name'] or '_TRADE' in item['servername']):
						# Timer(5,killClient).start()
						log(item['name'])
						data = struct.pack('>H',k)+b'\x08\x00\x00'
						log((' '.join('{:02X}'.format(x) for x in data)))
						inject_joymax(0x7034, data,False)
						return
	else:
		useSpecialReturnScroll()
		Timer(1,equipJob).start()



def equipJobOLD():
	global partyNumber
	stop_bot()
	global stats
	set_profile('Thief')
	inject_joymax(0x706B,struct.pack('I',partyNumber),False)
	delete_pet()
	stats = True
	#ITEM_MALL_W_SERAPIS_THIEF
	#Thief King suit (F)
	Dismount()
	inject_joymax(0x7061, bytearray(), False)
	inventory = get_inventory()['items']
	for k, item in enumerate(inventory):
		if item and k > 12 and ('Thief ' in item['name'] or '_TRADE' in item['servername']):
			Timer(5,killClient).start()
			log(item['name'])
			Packet = bytearray()
			Packet.append(0x00)
			Packet.append(k)
			Packet.append(0x08)
			Packet.append(0x00)
			Packet.append(0x00)
			inject_joymax(0x7034, Packet, False)
			log('Poniendo capa')
			break

def useBanditScroll(a=0):
	for i,item in enumerate(get_inventory()['items']):
		if item and i > 12:
			if item['name'] == 'Bandit Den Return Scroll':
				inject_joymax(0x704C, struct.pack('b',i)+b'\xEC\x09', True)
				log('Bandit Den Return Scroll')
				return True
	log('No hay bandit scrolls')
	if get_inventory()['items'][8]:
		if get_inventory()['items'][8]['name'] == 'Mental Bronze Bag' or 'White Flag' in get_inventory()['items'][8]['name']:
			start_bot()
			return
	return True

def chatpt(msg):
	phBotChat.Party(str(msg[1]))
	return False

def chat(msg):
	phBotChat.All(str(msg[1]))
	return False

def setTraining(script):
	log('Setting training script: ' + script[1])
	set_training_script('C:/Users/User/AppData/Local/Programs/phBot Testing/'+ str(script[1]) +'.txt')
	return False

def MountTransport():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'wolf' or v['type'] == 'transport':
				p = b'\x01'
				p += struct.pack('I', k)
				inject_joymax(0x70CB, p, False)
				log('mounted')
				return True
	return False

def DismountTransporte():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['mounted'] and v['type'] == 'wolf':
				log(v['type'])
				p = b'\x00'
				p += struct.pack('I', k)
				inject_joymax(0x70CB, p, False)
				log('dismounted')
				return True
	return False

def dismount2():
	pets = get_pets()
	if pets:
		for slot, pet in pets.items():
			if pet['type'] == 'horse':
				p = b'\x00'
				p += struct.pack('I', slot)
				inject_joymax(0x70CB, p, False)
				Timer(0.5,dismount).start()
				break
	return

def DismountHorse():
	pets = get_pets()
	if pets:
		for slot, pet in pets.items():
			if pet['type'] == 'wolf':
				if pet['mounted']:
					log('is mounted')
					p = b'\x00'
					p += struct.pack('I', slot)
					inject_joymax(0x70CB, p, False)
					log('dismounted')
					Timer(1,DismountHorse).start()
					break
	return

def Dismount():
	pets = get_pets()
	for k, v in pets.items():
		if v['mounted']:
			inject_joymax(0x70CB, b'\x00'+struct.pack('I', k), False)
			return True
	return True

def TerminatePet():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'wolf':
				p = struct.pack('I', k)
				p += b'\x03'
				inject_joymax(0x7116, p, False)
				log('terminamos')
				return True
	return False

def TerminationTransport():
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'transport':
				p = struct.pack('I', k)
				inject_joymax(0x70C6, p, False)
				log('terminamos')
				return True
	return False

def spawnThiefPet():
	inventory = get_inventory()
	items = inventory['items']
	for slot, item in enumerate(items):
		if item:
			if 'Goldclad Trade Horse' in item['name'] and len(get_drops()) < 10:
				log('Summoning: '+ item['name'])
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xEC)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xED)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				return
			elif len(get_drops()) > 9 and (item['name'] == 'Donkey' or 'elephant' in item['name'].lower()):
				log('Summoning: '+ item['name'])
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xEC)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xED)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				return
	for slot, item in enumerate(items):
		if item:
			if 'Goldclad Trade Horse' in item['name']:
				log('Summoning: '+ item['name'])
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xEC)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xED)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				return
	return False



def summonTradeHorse():
	inventory = get_inventory()
	items = inventory['items']
	for slot, item in enumerate(items):
		if item:
			if item['name'] == 'Donkey' or 'elephant' in item['name'].lower() or 'Goldclad Trade Horse' in item['name']:
				log('Summoning: '+ item['name'])
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xEC)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				Packet = bytearray()
				Packet.append(slot)
				Packet.append(0xED)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				break
	return False

def mount(s):
	pets = get_pets()
	if pets:
		for k, v in pets.items():
			if v['type'] == 'wolf':
				p = b'\x01'
				p += struct.pack('I', k)
				inject_joymax(0x70CB, p, False)
				log('MOUNTED')
				return True
	return False

def SAM(s):
	inject_joymax(0x7059, b'\x07\x00\x00\x00', False)
	return False

def AN(s):
	inject_joymax(0x7059, b'\x06\x00\x00\x00', False)
	return False

def Disconected(k=1):
	Packet = bytearray()
	# inject_joymax(0x704C, Packet, False)
	log('Disconected')
	# Timer(1.0, os.kill, (os.getpid(), 9)).start()
	return False

def cancelReturnScroll():
	inject_joymax(0x705B, bytearray(), False)
	log('Scroll cancelado')

# def equipJob(a=0):
# 	inventory = get_inventory()['items']
# 	for k, item in enumerate(inventory):
# 		if item and item['servername'].find('_THIEF_') > 0:
# 			log(item['name'])
# 			Packet = bytearray()
# 			Packet.append(0x00)
# 			Packet.append(k)
# 			Packet.append(0x08)
# 			Packet.append(0x00)
# 			Packet.append(0x00)
# 			inject_joymax(0x7034, Packet, False)
# 			Timer(2,log,('Equipando capa de thief'))
# 			break
# 	return False

token = urlopen('https://raw.githubusercontent.com/RahimSRO/Serapis/refs/heads/main/test.txt').read().decode("utf-8")[:-1]
token2 = urlopen('https://raw.githubusercontent.com/RahimSRO/Serapis/refs/heads/main/test2.txt').read().decode("utf-8")[:-1]

def sendTelegram(data='quest'):
	if data[0] == 'sendTelegram':
		data = 'quest'
	url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=149273661&parse_mode=Markdown&text='
	if '_' in data:
		url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=149273661&text='
	url = url + urllib.parse.quote(data)
	urllib.request.urlopen(url,context=ssl._create_unverified_context())
	return True

def sendTelegram2(data='quest'):
	url = f'https://api.telegram.org/bot{token2}/sendMessage?chat_id=149273661&parse_mode=Markdown&text='
	if '_' in data:
		url = f'https://api.telegram.org/bot{token2}/sendMessage?chat_id=149273661&text='
	url = url + urllib.parse.quote(data)
	urllib.request.urlopen(url,context=ssl._create_unverified_context())
	return True

def move(x,y,z):
	Timer(1.0, move_to,[x,y,z]).start()

def openStall(pid):
	inject_joymax(0x70B3, int(pid).to_bytes(4, 'little'), False)

# pid = QtBind.createLineEdit(gui,"",250,220,50,20)
# btn11 = QtBind.createButton(gui,'openStall','Open Stall',250,250)

def buyAll(i):
	if i < 10:
		log('Buying:' + str(i))
		Packet = bytearray()
		Packet.append(i)
		inject_joymax(0x70B4, Packet, False)
		Timer(1,buyAll,[i+1]).start()

def resurection(n):
	Packet = bytearray()
	Packet.append(n)
	Packet.append(0x00)
	Packet.append(0x00)
	Packet.append(0x00)
	inject_joymax(0x7059, Packet, False)

def help():
	global jelp
	if jelp:
		phBotChat.All('PARTY @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
		Timer(10,help).start()

def joinParty():
	global partyNumber
	if not get_party() and partyNumber != 0:
		Packet = bytearray()
		Packet += struct.pack('<I', partyNumber)
		inject_joymax(0x706D, Packet, False)
		Timer(1,joinParty).start()

def unequip(j,k):
	for i,item in enumerate(get_inventory()['items']):
		if item == None and i > j and k < 8:
			# log(str(i))
			# log(str(i)+': '+item['name'])
			Packet = bytearray()
			Packet.append(0x00)
			Packet.append(k)
			Packet.append(i)
			Packet.append(0x00)
			Packet.append(0x00)
			inject_joymax(0x7034, Packet, True)
			Timer(1,unequip,[i,k+1]).start()
			break

def equipItem(itemName):
	for i,item in enumerate(get_inventory()['items']):
		if item and i > 12:
			if itemName in item['name'].lower():
				log(item['name'])
				Packet = bytearray()
				Packet.append(0x00)
				Packet.append(i)
				Packet.append(0x06)
				Packet.append(0x00)
				Packet.append(0x00)
				inject_joymax(0x7034, Packet, True)
				break

def hunterAlarm():
	global NPC
	if NPC:
		pets = get_pets()
		if pets:
			for petID in pets:
				if pets[petID]['type'] == 'transport' and pets[petID]['items'][0] != None:
					mobs = get_monsters()
					for mobID in mobs:
						if mobs[mobID]['name'] == 'The Hunter':
							play_wav('Sounds/NPC.wav')
							Timer(40,hunterAlarm).start()
							return
					Timer(1,hunterAlarm).start()
					return
	NPC = ~NPC

def createParty():
	global partyNumber
	# log('createParty')
	# log(partyNumber)
	if partyNumber != '0':
		if get_inventory()['items'][8] == None:
			inject_joymax(0x7069, b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x01\x6E\x01\x00\x31' , True)
		else:
			inject_joymax(0x7069, b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03\x01\x87\x08\x00\x42\x75\x73\x63\x61\x6E\x64\x6F' , True)
		Timer(5.1,createParty).start()

PICK = False

def spawn(name):
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'transport':
				return
	items = get_inventory()['items']
	for slot, item in enumerate(items):
		if item and item['name'] == name:
			log('Summoning: '+ item['name'])
			inject_joymax(0x704C, struct.pack('b',slot)+b'\xEC\x11', True)
			Timer(0.5,spawn,[name]).start()
def ujob():
	global ignoreZones
	if get_zone_name(get_character_data()['region']) in ignoreZones:
		Dismount()
		inject_joymax(0x7061, bytearray(), False)
		unequipJob()
		return
	Timer(1,ujob).start()

def zerkoff():
	global berserker
	berserker = False

invite = False
tracebuff = False

def update_plugin():
    try:
        urllib.request.urlretrieve('https://raw.githubusercontent.com/RahimSRO/Serapis/refs/heads/main/Miscelaneos.py', 'Plugins/Miscelaneos.py')
        log(f"Archivo guardado como: Miscelaneos.py")
    except Exception as e:
        log(f"Error al descargar el archivo: {e}")

def update_town(name):
	name = name+'.txt'
	try:
		urllib.request.urlretrieve(f'https://raw.githubusercontent.com/RahimSRO/Serapis/refs/heads/main/{name}', f'Town/{name}')
		log(f"Archivo guardado como: {name}")
	except Exception as e:
		log(f"Error al descargar el archivo: {e}")

def handle_chat(t,player,msg):
	#1 All
	#2 Private
	#4 Party
	#5 Guild
	#6 Global
	#7 Notice
	#9 Stall
	global TelegramBol
	global partyNumber
	global NPC
	global drop
	global dropg
	global superEssence
	global PICK
	global attackWolf
	global startAfterPick
	global energy
	global merca
	global berserker
	global targetBol
	global invite
	global tracebuff
	if msg == '.c':
		inject_joymax(0x705B, bytearray(), False)
	elif '/p' in msg:
		splited = msg.split()
		phBotChat.Private(splited[1],splited[2])
	elif msg[:5] == 'down!' and get_character_data()['name'] == player:
		update_plugin(msg[5:])
	elif msg == 'town!' and get_character_data()['name'] == player:
		update_town()
	elif msg == 'eshield':
		equipShield()
	elif msg == 'punto':
		move_to(3549,2069,0)
	elif msg == 'id':
		log(str(get_character_data()['player_id']))
	elif msg == 'npc':
		npcs = get_npcs()
		for id, npc in npcs.items():
			log(str(id)+': '+npc['name'])
	elif msg == 'pos':
		log(str(get_position()))
	elif msg[:4].lower() == 'kick' and msg[4:].isnumeric():
		kick(int(msg[4:]))
	elif msg.lower() == 'lvl' and t == 2:
		phBotChat.Private(player,str(get_character_data()['level']))
	elif msg.lower() == 'exp' and t ==2:
		phBotChat.Private(player,str(round(get_character_data()['current_exp']/get_character_data()['max_exp']*100,2)))
	elif msg == 'stops' and player != get_character_data()['name']:
		useSpecialReturnScroll()
		stop_bot()
	elif msg.lower() == 'invite':
		invite = not invite
		if invite:
			ChangeBotOption(['none',True,'Party','AutoInviteParty'],True)
		else:
			ChangeBotOption(['none',False,'Party','AutoInviteParty'],True)
	elif msg.lower() == 'tb':
		tracebuff = not tracebuff
		if tracebuff:
			ChangeBotOption(['none',True,'Trace','Buffs'],True)
			Timer(1,ChangeBotOption,[['none',True,'Trace','Party Buffs']],True).start()
		else:
			ChangeBotOption(['none',False,'Trace','Buffs'],True)
			Timer(1,ChangeBotOption,[['none',False,'Trace','Party Buffs']],True).start()
	elif msg[:4].lower() == 'rand' and msg[4:].isnumeric():
		stop_trace()
		stop_bot()
		log('Random ' + msg[4:])
		rand(int(msg[4:]))
	elif msg[:5].lower() == 'rands' and msg[5:].isnumeric():
		stop_trace()
		stop_bot()
		log('Randoms ' + msg[5:])
		rand(int(msg[5:]))
		set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
		start_bot()
	elif msg[len(msg)-1] == '/':
		args = msg.replace('/','').split(',')
		args.insert(0,'none')
		for i,value in enumerate(args):
			if value.lower() == 'true':
				args[i] = True
			elif value.lower() == 'false':
				args[i] = False
		log(str(args))
		ChangeBotOption(args,True)
	elif msg == 'chek':
		log('atendance')
		inject_joymax(0xC003,bytearray(),False)
	elif msg.lower() == 'instant' and (player == 'Sever' or get_character_data()['name'] == player):
		for slot,item in enumerate(get_inventory()['items']):
			if drop and item and slot>12:
				if item['name'] == 'Instant Return Scroll':
					inject_joymax(0x704C, struct.pack('b',slot)+b'\xED\x09', True)
					return True
	elif msg == 'targ' and get_character_data()['name'] == player:
		targetBol = not targetBol
		targetGeneral()
	elif msg == 'r/1231231231515164' and get_character_data()['name'] != player:
		for slot, item in enumerate(get_inventory()['items']):
			if slot > 13 and item:
				if item['name'] == 'Special Reverse Return':
					data = struct.pack('H', len(player)) + player.encode('ascii') + struct.pack('b', slot)
					log((' '.join('{:02X}'.format(x) for x in data)))
					inject_joymax(0xA459,data,True)
					return True
	elif msg == '.dc' and get_character_data()['name'] == player:
		inject_joymax(0x704C, bytearray(), False)
		killClient()
	elif msg == 'true' and get_character_data()['name'] != player:
		ChangeBotOption(['none',True,'Berserk','Unique'],True)
		return
		berserker = True
		if berserker:
			stop_bot()
			Timer(1,start_bot).start()
			Timer(1,zerkoff).start()
	elif msg == 'false' and get_character_data()['name'] != player:
		ChangeBotOption(['none',False,'Berserk','Unique'],True)
		return
	elif t == 2 and msg.lower() == 'str':
		questSTR()
	elif msg == 'crystal' and get_character_data()['name'] == player:
		crystal()
	elif msg == 'sort':
		sort_inventory()
	elif msg == 'go':
		Party = get_party()
		if Party:
			for memberID in Party:
				if Party[memberID]['name'] == 'Seven' or Party[memberID]['name'] == 'Rahim':
					stop_bot()
					set_training_script('')
					Timer(1,set_training_position,[Party[memberID]['region'], Party[memberID]['x'], Party[memberID]['y'], 0.0]).start()
					Timer(1.5,start_bot).start()
	elif msg[0] == 'p' and get_character_data()['name'] == player and msg[1:].isnumeric():
		dropSpecialReturnScroll(int(msg[1]))
	elif msg == 'pets':
		pets = get_pets()
		if pets:
			for petID in pets:
				log('petID: '+str(petID)+' '+str(pets[petID]))
	elif msg == 'bandit':
		useBanditScroll()
	elif msg == 'zerc' and get_character_data()['name'] != player:
		energy = not energy
		if energy:
			notice('Energia Activada')
		else:
			notice('Energia Desactivada')
		useEnergy()
	elif msg == 'donkey':
		PICK = True
		spawn('Donkey')
	elif msg == 'trada':
		PICK = True
		spawn('Goldclad Trade Horse')
	elif msg == 'tlp':
		tlp()
	elif msg == '.b':
		inject_joymax(0x705B, bytearray(), False)
		stop_trace()
		PICK = True
		buscarMerca()
	elif msg == '.v':
		puntoV()
	elif msg == 'exit':
		exit()
	elif msg == 'ejob':
		equipJob()
	elif msg == 'ujob':
		Dismount()
		inject_joymax(0x7061, bytearray(), False)
		unequipJob()
	elif msg == '.a' and player == get_character_data()['name']:
		attackWolf = not attackWolf
		if attackWolf:
			morado('Wolf activado')
		else:
			morado('Wolf desactivado')
	if t == 2:
		foo = msg.split()
		for word in foo:
			if word.isnumeric():
				notice(word)
				partyNumber = int(word)
				break
	if msg == 'dress' and get_character_data()['name'] == player:
		quitarDressLucky()
	if msg == 'clock' and get_character_data()['name'] == player:
		resPet()
	if msg == 'inter' and player == 'Seven':
		inject_joymax(0x705A, b'\x02\x00\x00\x00\x02\xA6\x00\x00\x00', False) #intermediate
	if msg == 'adv' and player == 'Seven':
		inject_joymax(0x705A, b'\x02\x00\x00\x00\x02\xA7\x00\x00\x00', False) #intermediate
	# if player == 'Seven' and ' (STR)]' in msg and get_character_data()['name'] == 'Zoser':
	# 	stop_bot()
	# 	Timer(3,go_Seven).start()
	if t == 6 and '[G' in player and get_character_data()['name'] == 'Seven':
		threading.Thread(target=sendTelegram, args=['`'+player+'`' + " -> " + msg],).start()
	if t == 2:
		play_wav('Sounds/PrivateMessage2.wav')
	if msg.isnumeric():
		notice(msg)
		partyNumber = int(msg)
		if t == 2 and player == 'Seven':
			joinParty()
	char = get_character_data()
	if t == 5 and msg[0:2] == '..' and get_character_data()['name'] != 'Trump' and get_character_data()['name'] != 'Seven':
		phBotChat.Global(msg[2:])
	elif msg.lower() == '.pk' and player == get_character_data()['name']:
		NPC = not NPC
		point(get_position()['x'],get_position()['y'])
		if NPC:
			ChangeBotOption(['none',False,'AutoPotions','UseHP'],True)
			Timer(1,ChangeBotOption,[['none',False,'AutoPotions','UseVigorHP'],True]).start()
			return
		ChangeBotOption(['none',True,'AutoPotions','UseHP'],True)
		Timer(1,ChangeBotOption,[['none',True,'AutoPotions','UseVigorHP'],True]).start()
	elif t == 2 and player == 'Seven' and msg.lower() == 'pet':
		inject_joymax(0x7034, b'\x18\x1B\x04\x04\x04\x0C\x19\x00\x50\x41\x43\x4B\x41\x47\x45\x5F\x49\x54\x45\x4D\x5F\x43\x4F\x53\x5F\x54\x5F\x44\x4F\x4E\x4B\x45\x59\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\xF4\x09\x00\x00', True)
	elif t == 2 and player == 'Seven' and msg.lower() == '50s':
		inject_joymax(0x7034, b'\x18\x1B\x04\x02\x00\x0D\x20\x00\x50\x41\x43\x4B\x41\x47\x45\x5F\x49\x54\x45\x4D\x5F\x4D\x41\x4C\x4C\x5F\x53\x43\x52\x4F\x4C\x4C\x5F\x53\x49\x4C\x4B\x5F\x35\x30\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x86\x06\x00\x00', True)
	elif msg == 'sh':
		spawnHorse()
	elif msg == 'zona' and t == 2:
		phBotChat.Private(player, get_zone_name(get_character_data()['region']))
	elif msg == 'region' and t == 2:
		phBotChat.Private(player, str(get_character_data()['region']))
	if t == 7:
		log('Noticia: '+msg)
	elif msg == 'last' and (get_character_data()['name'] == player or player == 'Seven'):
		reverse_return(0,'')
	elif msg == 'death' and (get_character_data()['name'] == player or player == 'Seven'):
		reverse_return(1,'')
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tomb':
		stop_trace()
		stop_bot()
		reverse_return(3, "Seenwald")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tptg':
		stop_trace()
		stop_bot()
		reverse_return(3, "Bandit-Bergfestung")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpdemon':
		stop_trace()
		stop_bot()
		reverse_return(3, "Heart Peak")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpuru1':
		stop_trace()
		stop_bot()
		reverse_return(3, "Black-Robber-Lager")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpuru2':
		stop_trace()
		stop_bot()
		reverse_return(3, "Tarimbecken")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tplord1':
		stop_trace()
		stop_bot()
		reverse_return(3, "Niya-Ruine")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tplord2':
		stop_trace()
		stop_bot()
		reverse_return(3, "Fruchtbarkeitstempel")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpisy1':
		stop_trace()
		stop_bot()
		for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Reverse Reverse Return Scroll':
					inject_joymax(0x704C, struct.pack('b',i)+b'\xED\x19\x07\x14\x00\x00\x00', False)
					inject_joymax(0x704C, struct.pack('b',i)+b'\xEC\x19\x07\x14\x00\x00\x00', False)
					return
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpisy2':
		stop_trace()
		stop_bot()
		for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Reverse Reverse Return Scroll':
					inject_joymax(0x704C, struct.pack('b',i)+b'\xED\x19\x07\x15\x00\x00\x00', False)
					inject_joymax(0x704C, struct.pack('b',i)+b'\xEC\x19\x07\x15\x00\x00\x00', False)
					return
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpisy3':
		stop_trace()
		stop_bot()
		for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Reverse Reverse Return Scroll':
					inject_joymax(0x704C, struct.pack('b',i)+b'\xED\x19\x07\x13\x00\x00\x00', False)
					return
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tproc':
		stop_trace()
		stop_bot()
		reverse_return(3, "Herzgipfel") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tproc2':
		stop_trace()
		stop_bot()
		reverse_return(3, "Windstadt") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpivy':
		stop_trace()
		stop_bot()
		reverse_return(3, "Cleopatra-Tor") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpivy2':
		stop_trace()
		stop_bot()
		reverse_return(3, "Teich-Ruinen") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tphwt':
		stop_trace()
		stop_bot()
		reverse_return(3, "Roter Boden") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpcerb':
		stop_trace()
		stop_bot()
		reverse_return(3, "Göttergarten") #Wind Town
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpred':
		stop_trace()
		stop_bot()
		for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Reverse Reverse Return Scroll':
					inject_joymax(0x704C, struct.pack('b',i)+b'\xED\x19\x07\x29\x00\x00\x00', False)
					return
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpforest':
		stop_trace()
		stop_bot()
		reverse_return(3, "Kummerwald")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpsalt':
		stop_trace()
		stop_bot()
		reverse_return(3, "Salz-Posten")
	elif ((t == 2 and player == 'Seven') or player == get_character_data()['name']) and msg.lower() == 'tpb4':
		stop_trace()
		stop_bot()
		for i,x in enumerate(get_inventory()['items']):
			if x and i > 13:
				if x['name'] == 'Reverse Reverse Return Scroll':
					inject_joymax(0x704C, struct.pack('b',i)+b'\xED\x19\x07\x26\x00\x00\x00', False)
					return
	if (t == 4 or t == 2 or t == 1) and ',' in msg and msg.replace(',','').replace('-','').isnumeric():
		log('aca hay comas')
		stop_trace()
		stop_bot()
		set_training_script('')
		region = msg.split(',')[0]
		x = msg.split(',')[1]
		y = msg.split(',')[2]
		set_training_position(int(region), int(x), int(y), 0)
		if get_training_area()['radius'] == 0:
			set_training_radius(20)
		start_bot()
	elif msg.lower() == 'quest':
		log(str(get_quests()))
	elif msg[:3] == 'pe:':
		partyNumber = msg[3:]
		createParty()
	elif msg == '.dp' and player != char['name']:
		stop_bot()
		dropg = ~dropg
		Timer(0.5, droping).start()
	elif msg[:6] == "drop: " and char['name'] != player and char['job_name'] != player:
		log('xdasdasd')
		drop = True
		dropItem(msg[6:])
	elif msg.lower() == '.h':
		NPC = True
		hunterAlarm()
	elif msg.lower() == 'unequip':
		unequip(12,6)
	elif msg[:6] == 'equip:':
		equipItem(msg[7:])
	elif msg.lower() == 'dwht':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Donwhang" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x05\x00\x00\x00', False) #DWHT
		return
		spawnHorse()
		script = '''walk,3549,2071,-106
walk,3549,2084,-106
teleport,Donwhang,Hotan
wait,500
walk,114,19,244
stop'''
		start_script(script)
		return
		Timer(0.5, move_to,[3548,2071,-106]).start()
		Timer(1, move_to,[3546,2086,-106]).start()
		def dwht():
			npcs = get_npcs()
			for id, npc in npcs.items():
				if "Donwhang" in npc['name']:
					inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x05\x00\x00\x00', False) #DWHT
					break
		Timer(2.5,dwht).start()
	elif msg.lower() == 'dwjg':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Donwhang" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x01\x00\x00\x00', False) #DWJG
				break
		return
		Timer(0.5, move_to,[3548,2071,-106]).start()
		Timer(1, move_to,[3546,2086,-106]).start()
		def dwjg():
			npcs = get_npcs()
			for id, npc in npcs.items():
				if "Donwhang" in npc['name']:
					inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x01\x00\x00\x00', False) #DWJG
					break
		Timer(2.5,dwjg).start()
	elif msg.lower() == 'mir':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "SeaFarers Dimensional Gate" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\xCF\x00\x00\x00', False) #DWJG
				break
		return
		#0x705A (Data) 65 02 00 00 02 CF 00 00 00
	elif msg.lower() == 'htdw':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Hotan" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x02\x00\x00\x00', False) #HTDW
				break
	elif msg.lower() == 'htsk':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Hotan" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x19\x00\x00\x00', False) #HTDW
				break
	elif msg.lower() == 'htjg':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Hotan" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x01\x00\x00\x00', False) #HTDW
				break
	elif msg.lower() == 'htco':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Hotan" in npc['name']:
				data = struct.pack('I',id)+b'\x02\x14\x00\x00\x00'
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x14\x00\x00\x00', False) #HTDW
				break
	elif msg.lower() == 'jgdw':
		npcs = get_npcs()
		for id, npc in npcs.items():
			if "Jangan" in npc['name']:
				inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x02\x00\x00\x00', False) #JGDW
				break
	elif msg[:3].lower() =='pt:':
		inject_joymax(0x7061, bytearray(), False)
		partyNumber = int(msg[3:])
		Timer(1,joinParty).start()
	elif (t == 5 or t == 2) and msg[:2] == '=>':
		set_profile(msg[2:])
		Timer(1,set_training_position,[0, get_character_data()['x'], get_character_data()['y'], 0]).start()
		Timer(1.5,start_bot).start()
	elif msg[:2] == ':>':
		log('Profile?: '+msg[2:])
		set_profile(msg[2:])
	elif msg == ".90":
		inject_joymax(0x705A, b'\x1A\x00\x00\x00\x02\x0E\x01\x00\x00', True)
	elif msg == '.PT':
		global jelp
		jelp = ~jelp
		help()
	elif msg == '.p':
		partyNumber = 0
		inject_joymax(0x7069, b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x03\x01\x87\x08\x00\x42\x75\x73\x63\x61\x6E\x64\x6F' , True)
	elif msg == '.die':
		# inject_joymax(0x704B, b'\x97\x02\x00\x00', True)
		inject_joymax(0x705A, b'\x97\x02\x00\x00\x05\x03', True)
		# inject_joymax(0x705A, b'\x1A\x97\x02\x00\x00\x05\x03', True)
	elif msg.lower() == 'training':
		stop_trace()
		stop_bot()
		phBotChat.Party(str(set_training_script(get_training_area()['path'])))
		start_bot()
	elif msg[:2] == ': ':
		itemName = msg[2:]
		items = get_inventory()['items']
		for item in items:
			if item and itemName.upper() in item['name'].upper():
				phBotChat.Guild(item['name'] + ' [' + str(item['quantity']) + ']')
	elif msg.lower() == 'g':
		log('[Gold] '+str(get_character_data()['gold']))
	elif msg.lower() == '-g':
		log('[Gold] '+str(get_character_data()['gold']-1000000))
	elif (t == 1 or t == 2 or t == 4 or t == 5) and msg[0:2] == '::' and msg[3] != ' ':
		changeTrainingArea(msg[2:])
	elif msg[0:3] == '>>>' and player != get_character_data()['name']:
		changeTrainingArea(msg[3:])
	elif msg[0:2] == '>>' and (player == get_character_data()['name'] or t == 2) and msg[2] != '>':
		changeTrainingArea(msg[2:])
	elif msg[0:1] == '>' and (player == get_character_data()['name'] or t == 2):
		startAfterPick = msg[1:]
	elif msg.lower() == 'chatoff':
		global TelegramBol
		TelegramBol = False
		QtBind.setChecked(gui, NotificarCheck, False)
	elif msg == 'gmon':
		global GM_DC
		GM_DC = True
		QtBind.setChecked(gui, GMDisconnect, True)
	elif msg == 'gmoff':
		GM_DC = False
		QtBind.setChecked(gui, GMDisconnect, False)
	elif msg.lower() == 'getinv':
		items = get_inventory()['items']
		for i,item in enumerate(items):
			if item:
				log(item['name'] + ' :' +str(i))
	elif msg.lower() == 'getinv*':
		items = get_inventory()['items']
		for item in items:
			if item:
				log(item['servername'])
	# elif msg == '--':
	# 	i = 0
	# 	for x in get_inventory()['items']:
	# 		if x:
	# 			if 'Event Spotted Rabbit' in x['name']:
	# 				moveItem(i,1,'Event Spotted Rabbit')
	# 			elif 'Yellow Sparkle Ostrich Summon Scroll' in x['name']:
	# 				moveItem(i,2,'Yellow Sparkle Ostrich Summon Scroll')
	# 			elif 'HP Recovery Potion (XX-Large)' in x['name']:
	# 				moveItem(i,3,'HP Recovery Potion (XX-Large)')
	# 			elif 'MP Recovery Potion (XX-Large)' in x['name']:
	# 				moveItem(i,4,'MP Recovery Potion (XX-Large)')
	# 			elif 'Special Return Scroll' in x['name']:
	# 				moveItem(i,5,'Special Return Scroll')
	# 			elif 'Grass of life' in x['name']:
	# 				moveItem(i,6,'Grass of life')
	# 			elif 'HGP recovery potion' in x['name']:
	# 				moveItem(i,7,'HGP recovery potion')
	# 			elif 'Recovery kit (xx-large)' in x['name']:
	# 				moveItem(i,8,'Recovery kit (xx-large)')
	# 		i+=1
	elif msg == 'AS':
		resurection(2)
	elif msg == 'AN':
		resurection(3)
	elif msg == 'DW' or msg == 'HT':
		resurection(5)
	elif msg == 'CONS':
		# resurection(6)
		resurection(5)
	elif msg == 'SAM':
		resurection(7)
	elif msg == 'JG':
		resurection(13)
	elif msg.lower() == 'back':
		inject_joymax(0x3053, b'\x01', False)
	elif msg.lower() == 'zona':
		log(get_zone_name(get_position()['region']))
	elif msg.lower() == 'region':
		log('la region es: '+str(get_position()['region']))
	elif msg.lower() == 'petoff':
		TerminatePet()
	elif msg.lower() == 'speed':
		useSpeed()
	# elif (t == 4 or t == 1 or t == 5) and msg == 'OFF':
	# 	Packet = bytearray()
	# 	Packet.append(0x03)
	# 	Packet.append(0x01)
	# 	inject_joymax(0x34BF, Packet, False)
	# 	log("EXP OFF")
	# elif (t == 4 or t == 1 or t == 5) and msg == 'ON':
	# 	Packet = bytearray()
	# 	Packet.append(0x03)
	# 	Packet.append(0x00)
	# 	inject_joymax(0x34BF, Packet, False)
	# 	log("EXP ON")
	# elif t == 9:
	# 	global Leaders
	# 	phBotChat.Private(player, 'Escribeme por WhatsApp a traves de este link https://wa.me/584123748436')
	# 	phBotChat.Private(player, 'Este es mi telefono +58 412 374 8436')
	if TelegramBol and player not in ignore and (t == 2 or t == 9):
		if player != char['name']:
			threading.Thread(target=sendTelegram, args=[player + " -> " + char['name'] + ' -> ' + msg],).start()
	if (t == 4 or t == 2) and msg.lower() == 'coo' and (char['name'] == player or char['job_name'] == player):
		log('dijo coo en party')
		region = str(get_position()['region'])
		x = str(int(get_position()['x']))
		y = str(int(get_position()['y']))
		phBotChat.Party(region+','+x+','+y)
	elif (t == 1 or t == 2 or t == 4 or t == 5) and msg.lower() == 'stop':
		stop_trace()
		stop_bot()
		superEssence = False
		NPC = False
		drop = False
		dropg = False
		PICK = False
		merca = False
	elif msg.lower() == 'here':
		log('dijo here en all')
		stop_bot()
		stop_trace()
		set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
		start_bot()
	elif msg == 's' and char['name'] == player:
		stop_trace()
		start_bot()
	elif msg == 'd' and char['name'] == player:
		stop_bot()
		stop_trace()
	elif msg == 'set':
		set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
	elif msg == 'sets':
		set_training_position(0, get_character_data()['x'], get_character_data()['y'], 0)
		start_bot()
	elif msg == 'town':
		TownSpawn()
	elif msg.lower() == 'pet':
		spawnPet()
	elif msg.lower() == 'spawn' and get_inventory()['items'][8]:
		spawnThiefPet()()
	elif msg.lower() == 'leave':
		inject_joymax(0x7061, bytearray(), False)
	elif msg == '100%':
		manito100()
	elif msg == '60%':
		manito60()
	elif msg.lower() == 'scroll':
		useSpecialReturnScroll()
	elif msg == 'term':
		pets = get_pets()
		if pets:
			for k, v in pets.items():
				if v['type'] == 'transport':
					inject_joymax(0x70C6, struct.pack('I', k), False)
					return True
	elif msg == 'cless' and (char['name'] == player or char['job_name'] == player) and get_client()['pid']:
		os.kill(get_client()['pid'], signal.SIGTERM)
		log('Client-less')
	elif msg == 'clientless' and char['name'] != player and char['job_name'] != player and get_client()['pid']:
		os.kill(get_client()['pid'], signal.SIGTERM)
		log('Client-less')
	elif t != 6 and msg == '2':
		Dismount()
	elif t != 6 and msg == '1':
		MountTransport()
	elif t != 6 and msg == 'start':
		stop_trace()
		start_bot()
	elif t != 6 and msg == 'f':
		stop_bot()
		stop_trace()
		if t == 2 and player == 'Seven':
			if get_inventory()['items'][8]:
				start_trace('Rahim')
				return
			else:
				start_trace(player)
				return
		if char['name'] != player:
			start_trace(player)
	elif (t == 4 or t == 1 or t == 5 or t == 2) and msg[0] == 'r' and msg[1:].isnumeric() and len(msg[1:]) < 4:
		r = int(msg[1:len(msg)])
		set_training_radius(r)
		ChangeBotOption(['none',r,'Loop','Script','1','Radius'],False)
	elif msg == 'usedevil':
		devil()
	elif msg == 'equipdevil':
		equipdevil()
	elif t == 2 and msg == 'pick':
		inject_joymax(0x705B, bytearray(), False)
		set_training_position(0,0,0,0)
		stop_trace()
		stop_bot()
		PICK = True
		pick_loop()
	elif char['name'] == player or char['job_name'] == player:
		if msg == '.os':
			phBotChat.All('s:'+ str(get_character_data()['player_id']))
	elif 's:' in msg[:2]:
		openStall(msg[2:])
	elif msg == '.buy':
		buyAll(0)
	if msg == ';;;':
		log('superDC')
		inject_joymax(0x704C, bytearray(), False)
		os.kill(os.getpid(), 9)
	elif msg == ';;':
		log('superDC')
		inject_joymax(0x704C, bytearray(), False)

def go_Seven():
	log('go_Seven')
	Party = get_party()
	if Party:
		for memberID in Party:
			if 'Seven' == Party[memberID]['name']:
				set_training_position(Party[memberID]['region'], Party[memberID]['x'], Party[memberID]['y'], 0.0)
				log('training area settle')
				start_bot()
				return

def moveItem(i,k,name):
	# log(str(i))
	# log(str(len(get_inventory()['items'])-k))
	# log(get_inventory()['items'][i]['name'])
	# log(get_inventory()['items'][len(get_inventory()['items'])-k]['name'])
	# if not get_inventory()['items'][len(get_inventory()['items'])-k] or get_inventory()['items'][len(get_inventory()['items'])-k]['name'] != name:
	# if not get_inventory()['items'][len(get_inventory()['items'])-k] or get_inventory()['items'][i]['name'] == name:
	if i != len(get_inventory()['items'])-k:
		log('Moving: ' + name)
		Packet = bytearray()
		Packet.append(0x00)
		Packet.append(i)
		Packet.append(len(get_inventory()['items'])-k)
		Packet.append(get_inventory()['items'][i]['quantity'])
		Packet.append(0x00)
		inject_joymax(0x7034, Packet, True)
		Timer(2, moveItem,[i,k,name]).start()

def teleportacion(source,destination):
	t = get_teleport_data(source, destination)
	if t:
		npcs = get_npcs()
		for key, npc in npcs.items():
			if npc['name'] == source:
				inject_joymax(0x705A,struct.pack('<IBI', key, 2, t[1]),False)

def useSpecialReturnScroll():
	global ScrollUsado
	if not ScrollUsado:
		log('Usando scroll')
		i = 0
		for x in get_inventory()['items']:
			if x:
				if x['name'] == 'Special Return Scroll' or x['name'] == 'Beginner Return Scroll':
					log(x['name'])
					Packet = bytearray()
					Packet.append(i)
					Packet.append(0xEC)
					Packet.append(0x09)
					inject_joymax(0x704C, Packet, True)
					return
			i+=1
		Timer(0.5,useSpecialReturnScroll).start()
	ScrollUsado = False

def spawnPet():
	i = 0
	for x in get_inventory()['items']:
		if x:
			if 'Dragon' in x['name']:
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xCD)
				Packet.append(0x08)
				inject_joymax(0x704C, Packet, True)
				Timer(1,inject_joymax,[0xA691, b'\x33\x23\x00\x00', True]).start()
				break
		i+=1

def useSpeed():
	i = 0
	for x in get_inventory()['items']:
		if x:
			if 'Drug' in x['name'] or x['name'] == 'Super Scroll (Schnelligkeit 100%)':
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xEC)
				Packet.append(0x0E)
				inject_joymax(0x704C, Packet, True)
				break
		i+=1

def manito60():
	i = 0
	for x in get_inventory()['items']:
		if x:
			if '60%' in x['name']:
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xEC)
				Packet.append(0x26)
				inject_joymax(0x704C, Packet, True)
				break
		i+=1

def manito100():
	i = 0
	for x in get_inventory()['items']:
		if x:
			if '100%' in x['name']:
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xEC)
				Packet.append(0x26)
				inject_joymax(0x704C, Packet, True)
				break
		i+=1

def devil():
	Packet = bytearray()
	Packet.append(0x01)
	Packet.append(0x04)
	Packet.append(0xA5)
	Packet.append(0x79)
	Packet.append(0x00)
	Packet.append(0x00)
	Packet.append(0x00)
	inject_joymax(0x7074, Packet, False)

def equipdevil():
	i = 0
	for x in get_inventory()['items']:
		if x:
			if 'Devil' in x['name']:
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0x2D)
				Packet.append(0X0F)
				inject_joymax(0x704C, Packet, True)
				Packet = bytearray()
				Packet.append(0x24)
				Packet.append(i)
				Packet.append(0X04)
				inject_joymax(0x7034, Packet, True)
				break
		i+=1

def invisible():
	global invi
	return invi

def spawnHorse(a=0):
	i = 0
	for x in get_inventory()['items']:
		if x:
			if '_C_DHORSE' in x['servername']:
				log(x['name'])
				Packet = bytearray()
				Packet.append(i)
				Packet.append(0xEC)
				Packet.append(0x11)
				inject_joymax(0x704C, Packet, True)
				break
		i+=1
	return True

labelName = QtBind.createLabel(gui,'Nombre:',370,180)
scriptName = QtBind.createLineEdit(gui,"Scripts/",425,176,150,20)
labelXY = QtBind.createLabel(gui,'x,y',363,147)
XY = QtBind.createLineEdit(gui,"3548,2085",380,145,120,20)
MakeScript = QtBind.createButton(gui,'ScriptMaker',"MakeScript",410,220)
GetPosition = QtBind.createButton(gui,'GetPosition',"GetPosition",510,220)

uniqueSTRname = QtBind.createLineEdit(gui,"",325,276,80,20)
configName = QtBind.createLineEdit(gui,"Akeru",420,276,80,20)

def GetPosition():
	QtBind.setText(gui, XY, str(int(get_position()['x']))+','+str(int(get_position()['y'])))

def ScriptMaker():
	msg = QtBind.text(gui,XY)
	x = float(msg[:msg.find(',')])
	y = float(msg[msg.find(',')+1:])
	path = generate_path(x,y)
	file = open(QtBind.text(gui,scriptName)+'.txt','w')
	for k in path:
		s = 'walk,'+str(k[0])+','+str(k[1])+",0\n"
		file.write(s)
	file.close()
	log('Listo el script')

def changeTrainingArea(area):
	stop_trace()
	stop_bot()
	set_training_script('')
	path = get_config_dir().replace('Config','Scripts')+area+'.txt'
	ChangeBotOption(['none',path,'Loop','Script','1','Path'],False)
	log(get_config_dir().replace('Config','Scripts')+area+'.txt')
	Timer(1,set_training_script,[path]).start()
	Timer(2,start_bot).start()


def killAfterJoined(dcName):
	global CLIENTLESS_BOL
	ignore_dc_names = ['Seven','Zoser','Norte','Gana','Clear','Trump']
	if CLIENTLESS_BOL and dcName not in ignore_dc_names:
		log('not in dc name')
		killClient()
	if CLIENTLESS_BOL and os.environ['COMPUTERNAME'] == 'LAPTOP':
		killClient()

dcName = ''

def joined_game():
	global dcName
	global UniqueAlert
	global pickAfterJoin
	global PICK
	dcName = get_character_data()['name']
	if get_character_data()['name'] == 'Seven':
		UniqueAlert = True
		QtBind.setChecked(gui, UniqueCheck, UniqueAlert)
	else:
		if os.environ['COMPUTERNAME'] == 'LAPTOP':
			Timer(50,killAfterJoined,[dcName]).start()
		else:
			Timer(20,killAfterJoined,[dcName]).start()
	if pickAfterJoin:
		PICK = True
		pick_function()

def joint():
	global UniqueAlert
	if get_zone_name(get_character_data()['region']) != 'Rot Eggre':
		UniqueAlert = True
		QtBind.setChecked(gui, UniqueCheck, UniqueAlert)

if get_character_data()['name'] == 'Seven':
	UniqueAlert = True
	QtBind.setChecked(gui, UniqueCheck, UniqueAlert)

def pick_loop():
	stop_trace()
	global startAfterPick
	global PICK
	if PICK:
		drops = get_drops()
		pets = get_pets()
		if drops:
			for dropID in drops:
				if 'TRADE' in drops[dropID]['servername']:
					if pets:
						for slot, pet in pets.items():
							if pet['type'] == 'horse':
								inject_joymax(0x70CB, b'\x00'+struct.pack('I', slot), False) #dismount horse
							elif  pet['type'] == 'transport':
								x1 = get_position()['x']
								y1 = get_position()['y']
								max_distance = 0
								for dropID in drops:
									if 'TRADE' in drops[dropID]['servername']:
										x2 = drops[dropID]['x']
										y2 = drops[dropID]['y']
										dis = ((x2-x1)**2+(y2-y1)**2)**1/2
										if max_distance == 0:
											max_distance = dis
											dropID_MAS_CERCANO = dropID
										elif dis < max_distance:
											max_distance = dis
											dropID_MAS_CERCANO = dropID
								packet = b'\x01\x02\x01' + struct.pack('I', dropID_MAS_CERCANO)
								inject_joymax(0x7074, packet, False)
								log('Agarrando...')
								for item in pet['items']:
									if item == None:
										Timer(0.5, pick_loop).start()
										return
								PICK = False
								if startAfterPick:
									set_training_script(get_config_dir().replace('Config','Scripts')+startAfterPick+'.txt')
									start_bot()
								useBanditScroll()
						spawnThiefPet()
						Timer(0.5, pick_loop).start()
						return
					else:
						spawnThiefPet()
						Timer(0.5, pick_loop).start()
						return
					break
		else:
			if pets:
				for slot, pet in pets.items():
					if pet['type'] == 'transport':
						PICK = False
						if startAfterPick:
							set_training_script(get_config_dir().replace('Config','Scripts')+startAfterPick+'.txt')
							start_bot()
						useBanditScroll()

def notFull():
	response = False
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'transport':
				for item in pets[petID]['items']:
					if item == None:
						response = True
						break
	return response

def thereIsATransport():
	bol = False
	pets = get_pets()
	if pets:
		for petID in pets:
			if pets[petID]['type'] == 'transport':
				bol = True
			elif pets[petID]['type'] == 'horse':
				dismount()
	return bol

def HayMerca(drops):
	response = False
	if drops:
		for dropID in drops:
			if 'TRADE' in drops[dropID]['servername']:
				return True
	return False

def TownSpawn(s=0):
	log(str(s))
	towns = ['Jangan','Donwhang','Hotan','Samarkand','Constantinople','Alexandria (Nord)','Alexandria (Süd)']
	npcs = get_npcs()
	for id, npc in npcs.items():
		if s == 0 or len(s) == 1:
			if npc['name'] in towns:
				log('TownSpawn:   ' +npc['name'])
				inject_joymax(0x7059, struct.pack('I',id), False) #DWHT
				return True
			continue
		if npc['name'] == s[1]:
			log('TownSpawn:   ' +s[1])
			inject_joymax(0x7059, struct.pack('I',id), False) #DWHT
			return True
	return True

# quests = get_quests()
# for questID in quests:
# 	if quests[questID]['name'] == 'Thief-Job Temple Quest':
def afterTemplo():
	log('afterTemplo')
	npcs = get_npcs()
	for id, npc in npcs.items():
		# if 'Samarkand' in npc['name']:
		if 'Donwhang' in npc['name']:
			inject_joymax(0x705A, struct.pack('I',id)+b'\x02\x05\x00\x00\x00', False) #SKHT
			Timer(6,start_bot).start()
			return
	Timer(1,afterTemplo).start()


def templo(s):
	npcs = get_npcs()
	for id, npc in npcs.items():
		if npc['name'] == 'Daily Quest Manager Shadi':
			Timer(0, inject_joymax,[0x7045, struct.pack('I',id), False]).start() #Seleccionar NPC
			Timer(0.5, inject_joymax,[0x7046, struct.pack('I',id) + b'\x02', False]).start() #Hablar con NPC
			Timer(1, inject_joymax,[0x30D4, b'\x08', False]).start() #Seleccionar Quest Templo
			Timer(1.5, inject_joymax,[0x30D4, b'\x05', False]).start() #Aceptar
			log('quest templo acceptando')
			Timer(3,afterTemplo).start()
			return True

def questSTR(s=0):
	if get_zone_name(get_position()['region']) == 'Samarkand':
		move_to(-5179,2857,180)
	elif get_zone_name(get_position()['region']) == 'Western-China-Donwhang':
		move_to(3549,2068,-106)
		Timer(0.5,move_to,[3543,2088,-106]).start()
	npcs = get_npcs()
	for id, npc in npcs.items():
		if npc['name'] == 'Daily Quest Manager Shadi':
			Timer(2, inject_joymax,[0x7045, struct.pack('I',id), False]).start() #Seleccionar NPC
			Timer(2.5, inject_joymax,[0x7046, struct.pack('I',id) + b'\x02', False]).start() #Hablar con NPC
			Timer(3, inject_joymax,[0x30D4, b'\x08', False]).start() #Seleccionar Quest Templo
			Timer(3.5, inject_joymax,[0x30D4, b'\x05', False]).start() #Aceptar

def scrptChat(scriptName):
	stop_bot()
	useSpecialReturnScroll()
	set_training_script(get_config_dir().replace('Config','Scripts')+str(scriptName[1])+'.txt')
	Timer(1,start_bot).start()
	Timer(1,cancelReturnScroll).start()
	return True

def ChangeBotOption(args,reload):
	if len(args) <= 3 or len(args) >= 7:
		log(f"Plugin: Incorrect Format, cant change setting.")
		return 0
	value = args[1]
	path = get_config_dir()
	CharData = get_character_data()
	ConfigFile = f"{CharData['server']}_{CharData['name']}.{get_profile()}.json" if len(get_profile()) > 0 else f"{CharData['server']}_{CharData['name']}.json"
	if os.path.exists(path + ConfigFile):
		with open(path + ConfigFile,"r") as f:
			Configdata = json.load(f)
			if len(args) == 4:
				try:
					data = Configdata[args[2]][args[3]]
				except:
					log('Plugin: Incorrect json key, cant change setting')
					return 0					
				if type(data) == list:
					Configdata[args[2]][args[3]].append(value)
				else:
					Configdata[args[2]][args[3]] = value
				
			if len(args) == 5:
				try:
					data = Configdata[args[2]][args[3]][args[4]]
				except:
					log('Plugin: Incorrect json key, cant change setting')
					return 0
				if type(data) == list:
					Configdata[args[2]][args[3]][args[4]].append(value)
				else:
					Configdata[args[2]][args[3]][args[4]] = value
					
			if len(args) == 6:
				try:
					data = Configdata[args[2]][args[3]][args[4]][args[5]]
				except:
					log('Plugin: Incorrect json key, cant change setting')
					return 0
				if type(data) == list:
					Configdata[args[2]][args[3]][args[4]][args[5]].append(value)
				else:
					Configdata[args[2]][args[3]][args[4]][args[5]] = value
				
			with open(path + ConfigFile ,"w") as f:
				f.write(json.dumps(Configdata, indent=4))
				log('Plugin: Settings Successfully Changed')
				if reload:
					reload_profile()
				return 0

log('[%s] Loaded' % __name__)
