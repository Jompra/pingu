import os
from crontab import CronTab

site = input('Website address: ')
minutes = input('Interval in minutes: ')
start_time = input('Starting at (integer between 1 and 24): ')
end_time = input('Ending at (integer between 1 and 24): ')

site_file = open('site-to-ping.txt', 'w')

site_file.write(site)

path = os.path.abspath(os.getcwd())

cron = CronTab(user='root')

job = cron.new(command=f'python3 {path}/ping.py', comment=f'Keeping {site} alive')

job.minute.during(start_time, end_time).every(minutes)

cron.write()

