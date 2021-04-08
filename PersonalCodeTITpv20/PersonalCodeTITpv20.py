valid_codes = []
invalid_codes = []
sex = ""
date = ""
birth_location = ""
def parse_location(loc):
	parsing = loc[0:10]
	num = loc[-4:-1]
	num = num.zfill(3)
	n = 1
	summ = 0
	for i in parsing:
		summ += n * int(i)
		n += 1
		n %= 10
		if n == 0:
			n = 1
	c = summ / 11
	c = int(c)
	c *= 11
	control_num = summ - c
	if control_num != int(loc[-1]):
		print("ОШИБКА! В личном коде не совпадает контрольная сумма!")
		return 0/0 # Вызов исключения, в случае неверной суммы контроля
	inm = int(num)
	if inm >= 1 and inm <= 10:
		return "Kuressaare Haigla"
	elif inm >= 11 and inm <= 19:
		return "Tartu Ülikooli Naistekliinik, Tartumaa, Tartu"
	elif inm >= 21 and inm <= 220:
		return "Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla)"
	elif inm >= 221 and inm <= 270:
		return "Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)"
	elif inm >= 271 and inm <= 370:
		return "Narva Haigla"
	elif inm >= 371 and inm <= 420:
		return "Pärnu Haigla"
	elif inm >= 421 and inm <= 490:
		"Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla"
	elif inm >= 491 and inm <= 520:
		return "Järvamaa Haigla (Paide)"
	elif inm >= 521 and inm <= 570:
		return "Rakvere, Tapa haigla"
	elif inm >= 571 and inm <= 600:
		return "Valga Haigla"
	elif inm >= 601 and inm <= 650:
		return "Viljandi Haigla"
	elif inm >= 651 and inm <= 700:
		return "Lõuna-Eesti Haigla (Võru), Põlva Haigla"
	else:
		print("Неизвестно что за род. дом!")
		return 0/0

	


def get_sex(sx):
	male = "Мужчина"
	female = "Женщина"
	unk = "Неопределён"
	if sx == 1 or sx == 3 or sx == 5:
		return male
	elif sx == 2 or sx == 4 or sx == 6:
		return female
	else:
		return unk
		
def format_date(dat, sx):
	ERROR = "Невалидная дата рождения"
	year = int(dat[0] + dat[1])
	month = int(dat[2] + dat[3])
	day = int(dat[4] + dat[5])

	fmonth = ["Января", "Фефраля", "Марта", "Апреля", "Мая", "Июня", "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"]
	
	if sx <= 4:
		year += 1900
	else:
		year += 2000



	if month > 12:
		return ERROR
	elif day > 31:
		return ERROR
	elif month == 2 and day > 29:
		return ERROR
	elif month % 2 == 1 and day > 30:
		return ERROR

	return f"{year}-м году, {day}-го {fmonth[month-1]}"

def getDate(code):
	return code[1:7]


def check_code(code): # Функция возвращает Истина, если код валидный, иначе ложь
	try:
		first = int(code[0]) # Пол
		dat = getDate(code) # дата рождения
		if (first >= 1 and first <= 6) and len(code) == 11:
			global date
			global sex
			global birth_location # объявляем глобально переменные, чтобы можно было менять их значение в любой области видимости
			date = format_date(dat,first)
			sex = get_sex(first)
			birth_location = parse_location(code)
			return True
		else:
			print("Невалидный код. Попробуйте ещё раз!")
			return False

	except:
		print("Failed")
		return False
def get_info(sx,dat,loc):
	return f"Это {sx}. Родился в {dat}, в род доме {loc}"
while len(valid_codes) + len(invalid_codes) < 10:
	pers_code = input(f"Введите личный код (Осталось попыток: {10 - (len(valid_codes) + len(invalid_codes))}) => ")
	if check_code(pers_code):
		print(get_info(sex,date,birth_location))
		valid_codes.append(pers_code)
	else:
		invalid_codes.append(pers_code)

print("Правильные коды: \n", valid_codes)
print("Неправильные коды: \n", invalid_codes)