score = 0
player_answers = []
true_answers = ["4", "4", "2", "3", "2", "1", "3", "1", "3", "3", ]
questions = [
    '''Вот твой первый вопрос:
Что народная мудрость советует отдать врагу?
1.завтрак
2.обед
3.полдник
4.ужин
''',
    """Вот твой второй вопрос:
Чему в Туле установлен памятник?
1.хлебу
2.кексу
3.бублику
4.прянику
""",
    """
    Вот твой третий вопрос:
Чего не ела героиня сказки «Гуси-лебеди», когда спасалась с братцем от погони?
1.пирожок
2.фуа-гра
3.кисель
4.яблоко
    """,
    """
    Вот твой четвертый вопрос:
Что обычно едят горячим?
1.окрошку
2.гаспачо
3.рассольник
4.свекольник
    """,
    """
    Вот твой пятый вопрос:
Что Китай недавно объявил своим национальным достоянием, вызвав возмущение граждан     
Южной Кореи?
1.онигири
2.кимчи
3.ушу
4.группу «BTS»
    """,
    """
    Вот твой шистой вопрос:
Какой ингредиент знаменитой пиццы «Маргарита» не символизирует ни один из цветов 
флага Италии?
1.оливковое масло
2.томаты
3.моцарелла
4.базилик
    """,
    """
    Вот твой седьмой вопрос:
В блюде немецкой кухни «Небо и земля» картофель — это земля. А что 
символизирует небеса?
1.грибы
2.петрушка
3.яблоки
4.клубника
    """,
    """
    Вот твой восьмой вопрос:
Какое блюдо создал французский повар Андре Дюпон, состоявший на службе у 
русского графа?
1.бефстроганов
2.цыпленок табака
3.шницель по-венски
4.ростбиф
    """,
    """
    Вот твой девятый вопрос:
Неправильное написание какого слова объясняется тем, что мода на блюдо 
пришла не из Японии, а из Европы?
1.тэмпура
2.рамэн
3.суши
4.гедза
    """,
    """
    Вот твой десятый вопрос:
Что стало популярным благодаря «Ресторану трех корон», 
обслуживавшему посетителей Всемирной выставки 1939 года?
1.коктейли
2.фастфуд
3.шведский стол
4.еда на вынос
    """,
]
name = input("Привет! Введи свое имя:")
print(f"""{name}, мы начинаем игру!
    Тебе будут заданы 10 вопросов. Каждый вопрос имеет 4 варианта ответа, но только один правильный. Как только ты дашь неправильный ответ, игра закончится. Но есть и приятные бонусы - несгораемые суммы.
    
    *После 3 вопроса твой несгораемый выигрыш составит 300000.
    *После 7 вопроса он увеличится до 700000.
    *Если же ты ответишь на все вопросы правильно, ты получишь 1000000!!! Желаю удачи!

""")

for num in range(len(questions)):
    print(questions[num])
    answer = input("твой ответ: ")
    player_answers.append(answer)

    if player_answers[num] == true_answers[num]:
        score += 1
    else:
        print(f"К сожалению, вы допустили ошибку на вопросе {num + 1}.")
        break
        
if score < 3:
    print("вы нечего не выйграли")
elif 3 <= score < 7:
    print("вы выйграли 300к")
elif 7 <= score < 10:
    print("вы выйграли 700к")
elif score == 10:
    print("вы выйграли 1000к")