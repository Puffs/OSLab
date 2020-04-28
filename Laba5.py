import re

""" Функция преобразующая полученный текст в гост формат"""
def gost(art):
    ls =['Author','Title', 'Journal','Year','Pages', 'Numpages', 'Volume', 'Language']

    """Создаем словари для русского и английского языков"""
    prefx_eng = {
        'Pages':'.-P. ',
        'Volume':'.-Vol. ',
        'Year': '.-',
    }
    prefx_rus = {
        'Pages':'-С, ',
        'Volume':',-Вып ',
        'Year':'.-'
    }

    art_temp = {} #создаем пустой словарь

    if art.get('Language') == 'russian':
        prefx = prefx_rus
    else:
        prefx = prefx_eng

        """ Проходим по массиву ls и записываем в словарь данные полученные функцией"""
    for x in ls:
        if x in art:
            art_temp[x]= prefx.get(x,'') + art.get(x,'')
        else:
            art_temp[x] = ''

    art_temp['Author'] = art_temp['Author'].replace(' and ', ', ') #заменяем у авторов все 'and' на ', '

    # Создаем словарь для статей и книг
    temp_dict = {
        'Article': '{Author} {Title} // {Journal}{Year}{Pages}',
        'Book': '{Author} {Title}{Year} {Numpages}'}

    # Выводим данные в зависимости от того книга это или статья
    if art['type'] in temp_dict.keys():
        return temp_dict[art['type']].format(**art_temp)
    else:
        return temp_dict['Article'].format(**art_temp)


file = open(r'C:\Games\bibliotek\biblio.bib', mode = 'r', encoding = 'utf-8')
data = file.read()
"""преобразовываем данные из файла в нужных формат с помощью регулярных выражений"""
reg1 = re.compile(r'@(?P<type>\w+){(?P<tag>.+?),(?P<body>.+?)}\s*}', re.DOTALL)
reg2 = re.compile(r'(\w+)\s*=\s*{(.+?)}')
iterat = reg1.finditer(data)
d_list = []
for i in iterat:
	body_orig = i.group('body')+'}'
	body_list = reg2.findall(body_orig) #Получаем список строк описанных регулярным выражением
	d = {
	'type': i.group('type'),
	'tag' : i.group('tag')
	}
	for i in body_list:
		d[i[0]] = i[1]
	d_list.append(d) #Преобразуем в массив строк
for d in d_list:
    print(gost(d)) #вывод в гост формате