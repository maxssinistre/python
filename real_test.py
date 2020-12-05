#!/usr/bin/python

 

 

from datetime import datetime, timedelta, date

import time

 

#N = 37

 

#date_N_days_ago = datetime.now() - timedelta(days=N)

 

#print datetime.now()

#print date_N_days_ago.strftime("/""%Y""/""%m""/""%d")

 

DATES = []

MAIN_URL = []

 

BACKUP_LIST = [ 1, 2, 3, 4, 5, 6, 7 ]

 

               

               

for OFFSET in BACKUP_LIST :

 

                #print OFFSET

               

                date_N_days_ago = datetime.now() - timedelta(days=OFFSET)

                               

                DATES.append(date_N_days_ago.strftime("/""%Y""/""%m""/""%d"))

                               

                               

#print DATES

                               

                                 

RADIO1 = "https://www.bbc.co.uk/schedules/p00fzl86"

RADIO2 = "https://www.bbc.co.uk/schedules/p00fzl8v"

RADIO3 = "https://www.bbc.co.uk/schedules/p00fzl8t"

ONEXTRA = "https://www.bbc.co.uk/schedules/p00fzl64"

RADIO4 = "https://www.bbc.co.uk/schedules/p00fzl7l"

RADIO5 = "https://www.bbc.co.uk/schedules/p00fzl7g"

RADIO5LIVE = "https://www.bbc.co.uk/schedules/p00fzl7h"

RADIO6 = "https://www.bbc.co.uk/schedules/p00fzl65"

ASIANNETWORK = "https://www.bbc.co.uk/schedules/p00fzl68"

WORLDSERVICE = "https://www.bbc.co.uk/schedules/p00fzl9p"

 

 

CHANNELS = [ RADIO1, RADIO2, RADIO3, ONEXTRA, RADIO4, RADIO5, RADIO5LIVE, RADIO6, ASIANNETWORK, WORLDSERVICE ]

 

 

for STATION in CHANNELS :

 

                for DATE_PARAM in DATES :

 

                                MAIN_URL.append(STATION+DATE_PARAM)

                                               

                               

 

for GETME in MAIN_URL :

 

                print GETME
