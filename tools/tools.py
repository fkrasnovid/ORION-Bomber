# Инструменты для разных обработок

from termcolor import colored
from datetime import datetime
import requests as r, os, time, random
from sys import platform
from tools import proxy
from tools import headers

def FormattingNumber(number, country):
	numb = str(number)
	if country == "ru": # Для России
		if numb[0:1] == "+" and numb[1:2] == "7": # +71234567890
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = "8"+numb[2:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "7":  # 71234567890
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = "8"+numb[1:]
			numb = "+"+numb
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
		elif numb[0:1] == "8":  # 81234567890
			numb_1 = "+7"+numb[1:]
			numb_2 = "7"+numb[1:]
			numb_3 = numb
			numb = "+7"+numb[1:]
			numb_4 = numb[:2] + " (" + numb[2:5] + ") " + numb[5:8] + "-" + numb[8:10] + "-" + numb[10:]
	elif country == "by": # Для Балуруси
		if numb[0:1] == "+": # +123456789012
			numb_1 = numb
			numb_2 = numb[1:]
			numb_3 = numb[4:]
		elif numb[0:1] == "3" or numb[0:3] == "375": # 123456789012
			numb_1 = "+"+numb
			numb_2 = numb
			numb_3 = numb[3:]

	if country == "by":
		return numb_1, numb_2, numb_3
	elif country == "ru":
		return numb_1, numb_2, numb_3, numb_4

def clear():
	if platform == "linux" or platform == "linux2":
	    os.system("clear")
	elif platform == "win32":
	    os.system("cls")

def banner():
	a = open("tools\\version.txt", "r")
	ver = a.read()
	a.close()

	banner = colored("""

	 ▒█████   ██▀███   ██▓ ▒█████   ███▄    █ 
	▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██▒  ██▒ ██ ▀█   █ 
	▒██░  ██▒▓██ ░▄█ ▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
	▒██   ██░▒██▀▀█▄  ░██░▒██   ██░▓██▒  ▐▌██▒
	░ ████▓▒░░██▓ ▒██▒░██░░ ████▓▒░▒██░   ▓██░
	░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
	  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
	░ ░ ░ ▒    ░░   ░  ▒ ░░ ░ ░ ▒     ░   ░ ░ 
	    ░ ░     ░      ░      ░ ░           ░ 
	               Sms Bomber                            
	\n""", "red")

	info = " "*13+colored("[", "blue")+"Developers :"+colored("Lucky", "green")+" and "+colored("LostIk", "red")+"\n"
	info_2 = " "*13+colored("[", "blue")+"Version    :"+colored(ver, "red")+"\n"

	print(banner+info+info_2)

def banner_tools():
	print(colored("[1]", "red"), colored("Начать спам", "green"))
	print(colored("[99]", "red"), colored("Информация", "cyan"))
	print(colored("\n[0] Выход", "red"))

def banner_info():
	print(colored("\nТелеграм", "cyan"))
	print("├"+colored("Lucky", "green")+":", colored("https://t.me/Lucky1376", "cyan"))
	print("├"+colored("LostIk", "red")+":", colored("https://t.me/LostIk31", "cyan"))
	print("└"+colored("Канал", "cyan")+":", colored("https://t.me/orion_bomber", "cyan"))
	print("\nНажмите Enter чтобы вернуться назад")
	input()

def start_input():
	country_code = {"1": "+380",
					"2": "+7"}
	country_code_2 = {"1": "by",
					  "2": "ru"}
	while True:
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		print(colored("[1]", "red"), colored("Беларусь +380", "blue"))
		print(colored("[2]", "red"), colored("Россия +7", "cyan"))
		print("")
		ct = input(colored("Выберите страну: ", "green"))
		if ct in ["1", "2"]:
			break
		elif ct == "99":
			return 0, 0, 0
	while True:
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		numb = input(colored("Введите номер без кода страны "+country_code[ct]+" ", "green"))
		if ct == "1" and len(numb) == 9 or ct == "2" and len(numb) == 10:
			break
		elif numb == "99":
			return 0, 0, 0
	while True:
		print("")
		print(colored("[99] Отмена", "red"))
		print("")
		print(colored("[1]", "red"), colored("Да", "green"))
		print(colored("[2]", "red"), colored("Нет", "red"))
		print("")
		pr = input(colored("Использовать прокси?: ", "green"))
		if pr in ["1", "2"]:
			if pr == "1":
				pr = country_code_2[ct]
			else:
				pr = None
			break
		elif pr == "99":
			return 0, 0, 0
	if pr != None:
		while True:
			print("")
			print(colored("[99] Отмена", "red"))
			print("")
			print(colored("[1]", "red"), colored("Общедоступный прокси", "yellow"))
			print("└"+colored("Общедоступный прокси используют все пользователи ORION-Bomber", "cyan"))
			print("")
			print(colored("[2]", "red"), colored("Свой прокси", "green"))
			print("└"+colored("Ваш прокси обязательно должен иметь протокол HTTP или HTTPS с поддержкой ipv4 и страну вашего номера", "cyan"))
			print("")
			who_pr = input("Вариант: ")
			if who_pr in ["1", "2"]:
				if who_pr == "2":
					print("")
					print(colored("[99] Отмена", "red"))
					print("")
					print(colored("Введите Ip и Port и логин и пароль если прокси частный", "green"))
					print("└"+colored("Пример:\n├123.45.678.910:8080\n└123.45.678.910:8080:LOGIN:PASSWORD", "cyan"))
					print("")
					new_pr = input(colored("~# ", "red"))
					
					if len(new_pr.split(":")) < 3:
						# Проверка общего прокси
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = result
							print(colored("Прокси работает!", "green"))
							time.sleep(2)
							break
					elif len(new_pr.split(":")) > 2:
						# Проверка частного прокси
						result = proxy.SPC(new_pr.split(":")[0], new_pr.split(":")[1], login=new_pr.split(":")[2], password=new_pr.split(":")[3])
						if result == False:
							print(colored("Ваш прокси не работает!", "red"))
						else:
							pr = result
							print(colored("Прокси работает!", "green"))
							time.sleep(2)
							break

				else:
					break
			elif who_pr == "99":
				return 0, 0, 0

	return country_code[ct]+numb, country_code_2[ct], pr


def ICC():
	try:
		print(colored("Проверка интернет соединения...", "green"))
		time.sleep(1)
		r.get("https://google.com")
		clear()
	except Exception as es:
		clear()
		print(colored("[!]", "red"), colored("Ваше устройство не подключено к интернету!", "magenta"))
		exit()

def FormattingResponse(status_code, service):
	date = datetime.now()
	if status_code == 200:
		print(colored())

def start(number, country, proxy_=None):
	print("")
	print(colored("Остановка спама", "yellow"))
	print("├"+colored("Termux", "magenta")+":", colored("На встроенной клавиатуре от Termux выбрать CTRL затем Z", "cyan"))
	print("└"+colored("Windows", "blue")+":", colored("Комбинация клавишь Ctrl+C или Ctrl+Z", "cyan"))
	an=["10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
	for i in an:
		print(colored("Спам начнется через ", "red")+colored(i, "green")+" ",sep=' ',end='\r')
		time.sleep(1)
	clear()

	# Форматы номера
	number = FormattingNumber(number, country)

	print(number)
	print(country)
	print(proxy_)

	time.sleep(30)

	# Запуск Бомбера
	