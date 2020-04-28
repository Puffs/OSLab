import re
import sqlite3

def output_table(name):
	"""Функция выводит статьи определенного автора"""
	con = sqlite3.connect(r'C:\Games\bibliotek\test.db')
	c = con.cursor()   #подключаем 'курсор' для взаимодействия с бд
	author = ["%"+name+"%",] #
	c.execute("SELECT * FROM articles WHERE Autor LIKE ?", author) #SQL запрос
	print(c.fetchall())
	con.close()



con = sqlite3.connect(r'C:\Games\bibliotek\test.db')
cur = con.cursor() #подключаем 'курсор' для взаимодействия с бд
cur.execute("""CREATE TABLE IF NOT EXISTS articles (Autor,Journal,Title, Year)""")

""" Открываем файл с данными и с помощью регулярных выражений заносим в iterat"""
file = open(r'C:\Games\bibliotek\biblio.bib', mode = 'r', encoding = 'utf-8')
data = file.read()
reg1 = re.compile(r'@(?P<type>\w+){(?P<tag>.+?),(?P<body>.+?)}\s*}', re.DOTALL)
reg2 = re.compile(r'(\w+)\s*=\s*{(.+?)}')
iterat = reg1.finditer(data)
d_list = []
for i in iterat:
	body_orig = i.group('body')+'}'          # находим нужную часть и
	body_list = reg2.findall(body_orig)      # записываем ее в список
	d = {
	'type': i.group('type'),
	'tag' : i.group('tag')
	}
	for i in body_list:
		d[i[0]] = i[1]
	d_list.append(d) #создаем список словарей
dats = ['Author', 'Journal','Title', 'Year']
tmp = {}
for i in d_list:
	for j in dats:
		if j in i:
			tmp[j] = i.get(j)
		else:
			tmp[j] = ''
	tmp['Author'] = tmp['Author'].replace(' and ', ',')   #заменяем and на ', '

        """Заносим данные из файла в базу"""
	purchases = [(tmp.get('Author'),tmp.get('Journal'),tmp.get('Title'),tmp.get('Year'))]
	cur.executemany("INSERT INTO articles VALUES(?,?,?,?)",purchases)
	con.commit()
con.close()
print ('Введите имя автора')
name = input()
output_table(name)
