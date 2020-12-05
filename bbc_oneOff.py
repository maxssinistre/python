#!/usr/bin/python
#------------------------------------------------------
# Script Name: function_test.py
# Script Version: 1.0
# Date: Thur Oct  10 13:14:50 EDT 2018
# Author: ahamil10
# Description: bbc stream downloader
# Revision history:
#------------------------------------------------------

from datetime import datetime, timedelta, date
import time
import os
import optparse
import sys
import re
import subprocess
import commands

DATES = []
MAIN_URL = []
MAIN_URL_OUTPUT = []
GETME_ARRAY = []
#DL_LIST = []
FINAL_LIST = []


BACKUP_LIST = [ 1, 2, 3, 4, 5, 6, 7 ]

#==============================================================================================================

WGET_COMMAND = "wget -O - -q "

HOMEDIR = os.getcwd()

WORKINGDIR =  HOMEDIR + "/" + "BBC_1XTRA_" + time.strftime("%a%b%d%g")

os.system( "mkdir " + WORKINGDIR )

os.chdir( WORKINGDIR )

RAW_HTML = "bbc_html." + time.strftime("%m.%d.%y.%H.%M") + ".txt"
OUTPUT_URL = open( RAW_HTML, 'a+' )

MATCHED_LINK = "bbc_matched." + time.strftime("%m.%d.%y.%H.%M") + ".txt"
MATCHED_OUTPUT = open( MATCHED_LINK, 'a+' )
	 
#==============================================================================================================
		 
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



#CHANNELS = [ RADIO1, RADIO2 ]


ARTIST_LIST = [
"Hospital Records",
"UKF"
]

#==============================================================================================================

def flatten(l, ltypes=(list, tuple)):
    ltype = type(l)
    l = list(l)
    i = 0
    while i < len(l):
        while isinstance(l[i], ltypes):
            if not l[i]:
                l.pop(i)
                i -= 1
                break
            else:
                l[i:i + 1] = l[i]
        i += 1
    return ltype(l)
	
# Python code to remove duplicate elements 
def removedup(duplicate): 
    final = [] 
    for num in duplicate: 
        if num not in final: 
            final.append(num) 
    return final 
	
def youtubedl(LINK):

	#print( "youtube-dl --extract-audio --audio-format mp3 -v -t " + LINK + " &" )

	YOUTUBEDL_COMMAND = os.system( "youtube-dl --continue --add-metadata --extract-audio --audio-format mp3 -v -t " + LINK  + " &" )
	
def AWK1(MATCHING,INPUTFILE,OUTFILE):

	#print( "cat " + INPUTFILE + " | awk -F \'\"\' \'BEGIN{IGNORECASE = 1 }  /" + MATCHING + "/ { print $4 }\' >> " + OUTFILE )

	AWK1_COMMAND = os.system( "cat " + INPUTFILE + " | awk -F \'\"\' \'BEGIN{IGNORECASE = 1 }  /" + MATCHING + "/ { print $4 }\' >> " + OUTFILE )

def CONTROL(PARR):

	PROCESS_NUMBER = PARR+5
	
	while PROCESS_NUMBER > PARR :
	
		PROCESS_LISTING = os.popen( "ps -ef | grep you[t]ube-dl" ).read().strip().split('\n')
		PROCESS_NUMBER = len(PROCESS_LISTING)
		#print PROCESS_NUMBER
		#print PARR
		#print ( "sleeping till processes finish." )
		time.sleep(30)
		

#==============================================================================================================

for OFFSET in BACKUP_LIST :

	date_N_days_ago = datetime.now() - timedelta(days=OFFSET)
		
	DATES.append(date_N_days_ago.strftime("/""%Y""/""%m""/""%d"))
	

for STATION in CHANNELS :

	for DATE_PARAM in DATES :

		MAIN_URL.append(STATION+DATE_PARAM)
			

for GETME in MAIN_URL :

#	os.system(WGET_COMMAND + GETME + " | grep programme__titles >>" + RAW_HTML ) 
# 	9/9/2019 - updated parse for new code on websites - this joins two lines together
#        os.system(WGET_COMMAND + GETME + " | egrep \"(programme__titles|programmeobjectlink=title)\" | paste -d, - - >>" + RAW_HTML )
        os.system(WGET_COMMAND + GETME + " | egrep \"(programme__titles|programmeobjectlink=title|aria-label=)\" | paste -d, - - >>" + RAW_HTML )
	
	
for MATCH in ARTIST_LIST :

	AWK1(MATCH,RAW_HTML,MATCHED_LINK)

	
for PROG in MATCHED_OUTPUT:

		PROG = PROG.rstrip("\r\n")
	
		FINAL_LIST.append(PROG)
		
		
for URL in removedup(FINAL_LIST):

	 youtubedl(URL)
	 
	 CONTROL(4)
	 

	


	

	
	
	

	
#youtube-dl --extract-audio --audio-format mp3 -y -t

#os.system( AWK1(MATCH,RAW_HTML) + " >> " + MATCHED_LINK )
#os.system('awk -F "\"" "/MATCH/ { print $4 }" ' + RAW_HTML + ">> " + MATCHED_LINK )
#os.system( + MATCH + "/ { print $4 }" + RAW_HTML + ">> " + MATCHED_LINK )
#MATCHED_LINK = "bbc_matched." + time.strftime("%m.%d.%y.%H.%M")
#MATCHED_OUTPUT = open( MATCHED_LINK, 'a+' )
	
# awk -F '"' 'BEGIN{IGNORECASE = 1 } /programme__titles/  && /annie/ { print $4 }' bbc_html.10.25.18.18.37
#OUTPUT1.close(),

ARTIST_LIST1 = [
"soundscapes",
"workout.wednesday",
"across.the.line",
"residency",
"ravenscroft",
"playlists",
"nile.rodgers",
"Levi",
"Huey",
"Cullum",
"cerys",
"reggae",
"Rodigan",
"Live.Lounge",
"Best.of.the.Week",
"Nihal",
"Essential.Mix",
"Annie.Mac",
"Crissy.Criss",
"Grooverider",
"Gilles.Peterson",
"New.DJs",
"Kissy.Sell.Out",
"Judge.Jules",
"Pete.Tong",
"The.1Xtra.Showcase",
"Bailey",
"Benji.B",
"BBC.Radio.1.s.Stories",
"My.Top.Ten",
"MistaJam",
"DJ.Target",
"The.Official.Chart",
"Charlie.Sloth",
"CJ.Beatz",
"Young.Lion",
"Robbo.Ranx",
"DJ.Edu",
"Anthem",
"Dancefloor",
"Friction",
"Skream",
"Diplo",
"Gilles",
"Traits",
"6.Mix",
"Mixtape",
"Live.Hour",
"Old.Skool",
"Panjabi",
"Kan.D.Man",
"Ladyland",
"Tiesto",
"Fred.V",
"Funk",
"Live.Lounge",
"Best.of.the.Week",
"Essential.Mix",
"Annie.Mac",
"Crissy.Criss",
"Gilles.Peterson",
"New.DJs",
"Kissy.Sell.Out",
"Judge.Jules",
"Pete.Tong",
"The.1Xtra.Showcase",
"Benji.B",
"BBC_Radio.1.s.Stories",
"My.Top.Ten",
"DJ.Target",
"The.Official.Chart",
#"Charlie.Sloth",
"CJ.Beatz",
"Young.Lion",
"Robbo.Ranx",
"DJ.Edu",
"6.Mix",
"Live.Hour",
"Old.Skool",
"Kan.D.Man",
"Fred.V",
"Letts",
"Jazz",
"Ajmal",
"Pandya",
"Omkar",
"disco",
"Drum",
"Friction",
"Rene",
"Sounds.Of.The.70s",
"Johnnie.Walker"
]



