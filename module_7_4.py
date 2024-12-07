#!/home/igor/PycharmProjects/module_7/.venv/bin/python
# -*- coding: utf-8 -*-

team1_num = 5 # Мастера Кода
team2_num = 6 # Волшебники Данных
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time1_avg = team1_time / score1
time2_avg = team2_time / score2
time_avg = (team1_time + team2_time) /tasks_total

if time1_avg > time2_avg:
    challenge_result = 'Победа команды Мастера Кода!'
elif time1_avg < time2_avg:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print("В команде Мастера кода участников: %s" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Команда Волшебники данных решила задач: {}!".format(score2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print(f"Команды решили {score1} и {score2} задач.")
print(f"Результат битвы: {challenge_result}!")
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')