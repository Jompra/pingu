import os
import math
from crontab import CronTab

print("""                                                  
                                     ##           
                  (@@&&&&&.       &&@&@&.         
                @@( &&&&%%#//    &&@@@&&          
               %&@&&%&%%%&%@ (   @&%%%%%          
               #&&&%##(((/&&&%    &&#(##          
                  @@@@@@@&&&%      %&###          
               @@@@@@@@@@@%#(%     &&#%           
            *@@@&&&&&@&.     &@%&&&&%             
           &@@@&&&&&%..        %#                 
         (&@&&&&&&&/.                             
        .&&@@&&&@&/.                              
        &&&&&&&&@&.    . .                        
       &&&&@&&&@&.      ...                       
       &&@@@&%&@,.      .....                     
      /@@@@&&&@&,.     ........                   
     @@@@@&%&@@%..   . .........                  
   @@@@@@&&%%&@,,... ............                 
  &@&&&&/   %&&*..............,.                  
             //**,,......,,,,*/*           /***** 
           ##((    ,***.       /*         //***** 
          ((((((.               /*,*    ////////  
           (((////////***,.     (////////(        
                                                  """)
print('WELCOME TO PINGU, THE PREMIER PINGER FOR HEROKU')

dyno_hours = input('How many free Dyno Hours Do You Have? ')
websites = []
while 'done' not in websites:
  websites.append(input('Add Full URL of site to ping including http:// or https://.\nAdd as may as you like. Type done when finished: ').lower())

websites.remove('done')

hours_per_site = math.floor((float(dyno_hours) / len(websites)) / 31) 

start_time = input(f'Your sites will be kept live for {hours_per_site} hours per day,\nWhat time should I start? [Int between 0-23] ')

end_time = int(start_time) + hours_per_site

if end_time > 24:
  end_time = 24

site_file = open('site-to-ping.txt', 'w')

path = os.path.abspath(os.getcwd())

for site in websites:
  site_file.write(f'{site}\n')

cron = CronTab(user='root')
job = cron.new(command=f'python3 {path}/ping.py')
job.minute.during(start_time, end_time).every(10)
cron.write()
site_file.close()

print("""
  _   _    ____     ____    _______           _   _    ____     ____    _______ 
 | \ | |  / __ \   / __ \  |__   __|         | \ | |  / __ \   / __ \  |__   __|
 |  \| | | |  | | | |  | |    | |            |  \| | | |  | | | |  | |    | |   
 | . ` | | |  | | | |  | |    | |            | . ` | | |  | | | |  | |    | |   
 | |\  | | |__| | | |__| |    | |            | |\  | | |__| | | |__| |    | |   
 |_| \_|  \____/   \____/     |_|            |_| \_|  \____/   \____/     |_|   
                                                                                
""")
