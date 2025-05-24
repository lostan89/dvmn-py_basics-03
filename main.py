import smtplib

import os

from dotenv import load_dotenv

load_dotenv()

website = 'https://dvmn.org/profession-ref-program/lostan/QmhKD'

friend_name = 'Петруша'

my_name = 'Иваныч'

sender = 'ewankarbasov@yandex.ru'

recipient = 'superkeeper@mail.ru'

letter = '''\
From: {sender}
To: {recipient}
Subject: Devman3
Content-Type: text/plain; charset="UTF-8";

Привет, {friend_name}! {my_name} приглашает тебя на сайт {website}!

{website} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {website}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {website}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(sender = sender, recipient = recipient, friend_name=friend_name, my_name=my_name, website=website)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(os.environ['LOGIN'], os.environ['TOKEN'])
server.sendmail(sender, recipient, letter)
server.quit()
