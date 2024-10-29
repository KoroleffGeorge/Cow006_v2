# Cow006

#### Описание игры:

 - Каждому игроку выдается по 10 карт
 - В начале игры раскладка представляет собой 4 карты, расположенных в 4 рядах
 - Всего 104 карты

Когда приходит ваш черёд класть свою карту в ряд, вы должны следовать четырём правилам:
 - «По возрастанию». Карты в ряду должны идти по возрастанию (в слежке коровы
любят порядок!).
 - «Минимальная разница». Вы должны выбрать ряд, где разница между вашей
картой и последней в ряду – минимальна.
 - «Шестая корова». Если из-за первых двух правил, ваша корова оказалась 6-й в
своём ряду – увы, вам не повезло (мы предупреждали про шестую корову!). Вы
должны взять весь ряд себе, а свою корову положить первой в этом ряду. Забранные
карты коров кладите рубашкой вверх в стопочку перед собой – это ваша «база агентов-
неудачников». Эти карты в руки брать нельзя!
 - «Наименьшая карта». Если номер вашей карты такой маленький, что её нельзя
положить ни в один из рядов (по правилу №1), то вам придётся забрать один из рядов
«на базу». В этом случае вы сами решаете, какой именно ряд забрать. Ваша карта
становится первой в освободившемся ряду.

Очки определенных коров:
 - Агенты с номерами кратными 5 (5, 15, 25 и т.д.) имеют 2-й ранг.
 - Агенты с номерами кратными 10 (10, 20, 30 и т.д.) имеют 3-й ранг.
 - «Двойные агенты», у которых цифры в номере одинаковые (11, 22, 33 и т.д.) имеют 5-й
ранг.
 - Агент 55 – «суперагент», он имеет номер кратный 5, а также относится к «двойным
агентам», поэтому его ранг 7
 - У всех остальных агентов 1-й ранг.

#### Инструкция по установке: 

`git clone https://github.com/KoroleffGeorge/Cow006_v2.git`

`cd Cow006_v2` 
`python -m venv venv`
`source venv/Scripts/activate` - для windows
`source venv/bin/activate` - для linux
`pip install -r requirements.txt` 
`python manage.py runserver`
В адресной строке набрать `http://127.0.0.1:8000/`
