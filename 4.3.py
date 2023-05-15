import json
data_in = {}
log = input('Введите логин:')
passwd = input('Введите пароль:')
def login_function(log, passwd):
	with open('2.json', 'r') as f:
		data_in = json.load(f)
		if log in data_in.keys():
			if data_in[log] == passwd:
				print('Вход выполнен!')
			else:
				print('Повторите попытку!')
login_function(log, passwd)