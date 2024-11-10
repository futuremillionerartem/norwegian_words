import random

dict = {'adjektiv': "прилагательное", #1
        'advokat': "адвокат",
        'andre': "второй",
        'angrep':  "атака",
        'appelsin': "апельсин",
        'april': "апрель",
        'arm':  "рука",
        'atten': "18",
        'avis':  "газета",
        'baby': "грудной ребенок",
        'bad': "ванная", #2
        'bag': "сумка",
        'bak': "сзади",
        'bakke': "холм",
        'ball': "мяч",
        'band': "музыкальная группа",
        'banan': "банан",
        'bank': "банк",
        'bar': "бар",
        'barn': "ребенок",
        'be': "просить",
        'bekk': "речка",
        'ben': "нога",
        'bensin': "бензин",
        'berømt': "известный",
        'besteforelder': "прародитель", #3
        'bestefar': "дедушка",
        'bestemor': "бабушка",
        'farfar': "папин папа",
        'farmor': "папина мама",
        'morfar': "мамин папа",
        'mormor': "мамина мама",
        'mor': "мама",
        'far': "папа",
        'betale': "платить",
        'bibliotek': "библеотека",
        'biff': "стейк",
        'bil': "машина",
        'bilde': "изображение",
        'billett': "билет",
        'billig': "дешевый",
        'blad': "лист",
        'blind': "слепой",
        'blod': "кровь",
        'blomst': "цветок",
        'blyant': "карандаш",
        'blå': "голубой", #4
        'lyseblå': "светло голубой",
        'mørkeblå': "темно синий",
        'bok': "книга",
        'boks': "коробка",
        'bokstav': "буква",
        'bord': "стол",
        'bot': "штраф",
        'bred': "широкий",
        'brekke': "сломать",
        'bro': "мост",
        'bror': "брат",
        'brun': "коричневый",
        'bryllup': "свадьба",
        'brød': "хлеб",
        'bukse': "штаны",
        'bunn': "дно", #5
        'buss': "автобус",
        'butikk': "бутик",
        'by': "город",
        'bygge': "строить",
        'bygning': "здание",
        'bære': "нести",
        'bølge': "волна",
        'bøye': "сгибать",
        'båt': "лодка",
        'centimeter' : "сантиметр",
        'dag': "день", #6 
        'dal': "долина",
        'dance': "танцевать",
        'datamaskin': "компьютер",
        'dato': "дата",
        'datter': "дочь",
        'de': "они",
        'dek': "шина",
        'desember': "декабрь",
        'det/dette': "это",
        'diamant': "алмаз",
        'doktor': "доктор",
        'domstol': "суд", #7
        'dra': "путешествовать",
        'drepe': "убить",
        'dress': "костюм",
        'drikke': "пить",
        'drikkevare': "напиток",
        'dronning': "",
        'drøm': "сон",
        'du': "ты",
        'dyp': "глубокий",
        'dyr': "дорогой",
        'dytte': "толкнуть",
        'død': "смерть",
        'dør ': "дверь", #8
        'døv': "глухой",
        'dårlig': "плохой",
        'egg': "яйцо",
        'eksplodere': "взрывать",
        'ektefelle': "супруг",
        'elektronikk': "электроника",
        'elleve': "11",
        'elske': "любить",
        'elv': "река",
        'en': "1",
        'energi': "энергия",
        'eple': "яблоко",
        'ettermiddag': "полдень",
        'falle': "падать"
        }
        






list = ['adjektiv', 'advokat', 'andre', 'angrep', 'appelsin', 'april',
        'arm', 'atten', 'avis', 'baby', 'bad', 'bag', 'bak', 'bakke',
        'ball', 'banan', 'band', 'bank', 'bar', 'barn', 'be', 'bekk', 'ben', 'bensin',
        'berømt', 'besteforelder', 'bestefar', 'bestemor', 'farfar', 'farmor', 'morfar',
        'mormor', 'far', 'mor',  'betale', 'bibliotek', 'biff', 'bil', 'bilde', 'billett',
        'billig', 'blad', 'blind', 'blod', 'blomst', 'blyant', 'blå', 'lyseblå', 'mørkeblå',
        'bok', 'boks', 'bokstav', 'bord', 'bot', 'bred', 'brekke', 'bro', 'bror', 'brun', 'bryllup',
        'brød', 'bukse', 'bunn', 'buss', 'butikk', 'by', 'bygge', 'bygning', 'bære', 'bølge',
        'bøye', 'båt', 'centimeter', 'dag', 'dal', 'dance', 'datamaskin', 'dato', 'datter',
        'de', 'dek', 'desember', 'det/dette', 'diamant', 'doktor', 'domstol', 'dra', 'drepe',
        'dress', 'drikke', 'drikkevare', 'dronning', 'drøm', 'du', 'dyp', 'dyr','dytte', 'død',
        'dør ', 'døv', 'dårlig', 'egg', 'eksplodere', 'ektefelle', 'elektronikk', 'elleve', 'elske',
        'elv', 'en', 'energi', 'eple', 'ettermiddag', 'falle']

print(len(list), len(dict))

random.shuffle(list)
count = 0

for i in range(len(list)):
    print(list[i])
    string = input().lower()
    
    if dict[list[i]] == string:
        count += 1
    else:
        print(f"Вы написали {string}, а нужно {dict[list[i]]}")

if count == 85:
    print('Ты перевёл все слова правильно, ЛЕГЕНДА')
