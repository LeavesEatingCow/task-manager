import datetime
import pytz


tasks = {}

task_desc = input("What would you like to do? >> ")
task_day = int(input("What day do you want this event to take place? >> "))
task_hour = int(input("At which hour? >> "))

task = datetime.datetime(datetime.date.today().year,datetime.date.today().month, task_day,task_hour)

print(task)


