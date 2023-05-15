import json
log = input('Введите логин:')
passwd = input('Введите пароль:')  
data = {}
with open('2.json', 'r') as f:
	data = json.load(f)

def register(log, passwd):
	if log not in data.keys():
		data[log] = passwd
		with open('2.json', 'w') as f:
			json.dump(data, f)
register(log, passwd)
print ('Данные успешно приняты!')