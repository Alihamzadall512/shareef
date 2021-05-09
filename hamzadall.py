
import base64
exec(base64.b16decode('#!/usr/bin/python2
#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib
from multiprocessing.pool import ThreadPool
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('python2 dall.py')

from requests.exceptions import ConnectionError
from mechanize import Browser

#### browser ####
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####
B='\033[1;94m'
R='\033[1;91m'
G='\033[1;92m'
W='\033[1;97m'
S='\033[1;96m'
P='\033[1;95m'
Y='\033[1;93m'

#### exit ####
def exb():
	print (R + 'Exit')
	os.sys.exit()

#### clear ####
def cb():
    os.system('clear')

#### time sleep ####
def t():
    time.sleep(1)
def t1():
    time.sleep(0.01)

#### print std ####
def psb(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		t1()

#### token remove ####
def trb():
    os.system('rm -rf token.txt')

##### LOGO #####
logo='''
\033[1;94m ┈┈┈┈╱▔▔▔▔╲┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈╱▔▔▔▔╲┈┈┈┈
\033[1;94m ┈┈┈▕▕ DALL ▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕B4 M4▏▏┈┈┈
\033[1;94m ┈┈┈▕▕▂╱╲▂▏▏┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈▕▕▂╱╲▂▏▏┈┈┈
\033[1;94m ┈┈┈┈╲┊┊┊┊╱┈┈┈┈\033[1;94mShabirBaloch.\033[1;91m┈┈┈┈╲┊┊┊┊╱┈┈┈┈
\033[1;96m ┈┈┈┈▕╲▂▂╱▏┈┈┈┈☞☞☞☞☞☞\033[1;91m☜☜☜☜☜┈┈┈┈▕╲▂▂╱▏┈┈┈┈
\033[1;96m ╱▔▔▔▔┊┊┊┊▔▔▔▔╲☞☞☞☞☞☞\033[1;91m☜☜☜☜☜╱▔▔▔▔┊┊┊┊▔▔▔▔╲
\033[1;96m................\033[1;93mHamzaDall\033[1;91m...............
\033[1;96m................\033[1;93m✬✬\033[1;91m..............

\033[1;96m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

\033[1;91m☞ Auther     : ALI HAMZA 
\033[1;92m☞ WhatsApp   : 03057446523
\033[1;95m☞ Facebook  : Ali Hamza

\033[1;93m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                '''
