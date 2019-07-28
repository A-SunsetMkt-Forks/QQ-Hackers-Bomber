import ctypes
import os
import random
import requests
import string
import time
from faker import Faker

if __name__ == '__main__':
    # url = 'http://nuiyyz.cn/save.php'
    url = input()
    if len(url) < 11:
        quit()
    fake = Faker()
    ctypes.windll.kernel32.SetConsoleTitleW("别惹你爸，听见没")
    count = 0
    locale = ['ar_AA', 'ar_EG', 'ar_JO', 'ar_PS', 'ar_SA', 'bg_BG', 'bs_BA', 'cs_CZ', 'de', 'de_AT', 'de_CH', 'de_DE', 'dk_DK', 'el_CY', 'el_GR', 'en', 'en_AU', 'en_CA', 'en_GB', 'en_IE', 'en_NZ', 'en_TH', 'en_US', 'es', 'es_CA', 'es_ES', 'es_MX', 'et_EE', 'fa_IR', 'fi_FI', 'fr_CH', 'fr_FR', 'he_IL', 'hi_IN', 'hr_HR', 'hu_HU', 'hy_AM', 'id_ID', 'it_IT', 'ja_JP', 'ka_GE', 'ko_KR', 'la', 'lb_LU', 'lt_LT', 'lv_LV', 'mt_MT', 'ne_NP', 'nl_BE', 'nl_NL', 'no_NO', 'pl_PL', 'pt_BR', 'pt_PT', 'ro_RO', 'ru_RU', 'sk_SK', 'sl_SI', 'sv_SE', 'th_TH', 'tr_TR', 'tw_GH', 'uk_UA', 'zh_CN', 'zh_TW']

    while(True): 
        username = ''
        password = ''
        length = random.randint(6, 10)
        curr = 0

        # Generate a user ID as if it were truly exists. 
        # The user IDs that Python randomly generated are more likely to regress to the mean. 
        # So I write this. 
        while curr < length:
            rd = random.randint(0, 9)
            if (curr > 3 or rd > 0):
                username += str(rd)
            if (curr == 9 and int(username[0:1]) > 3):
                username = username[0:9]
            curr += 1
        
        if len(username) < 5:
            continue
        elif len(username) < 7 and random.random() > 0.3:
            continue
        
        # Generate passwords that are as real as possible. 
        # Most people won't use random characters as passwords, they prefer meaningful words or phrases instead. 
        # Based on my everyday experience, I assume that one of twenty people use fully randomized string. 
        # This is a very rough estimate. 
        # Also, I assume that one of ten people use random letters or numbers respectively. 
        # The remaining passwords are more like human language. 
        # As you can see, I take FAKER package to generate a user name, which looks like a real password. 
        # In addition, I think more people prefer lower case instead of mixed case. 
        if (20 * random.random() < 1):
            chars = string.ascii_letters + string.digits
        elif (19 * random.random() < 2):
            chars = string.ascii_letters
        elif (17 * random.random() < 2):
            chars = string.digits
        else:
            # Randomly generate the locale of user
            fake = Faker(locale[random.randint(0, 64)])
            while True:
                password += fake.user_name()
                if len(password) > 15:
                    password = ''
                elif len(password) > 9:
                    break
        if len(password) == 0:
            password = ''.join([random.choice(chars) for i in range(random.randint(8, 14))])
        if random.random() < 0.5:
            password = password.lower()
        
        # Who TM knows why it take such a FUCKING variable name
        # EDIT HERE
        upload_value = {'hrUW3PG7mp3RLd3dJu': username, 'LxMzAX2jog9Bpjs07jP': password}

        r = requests.post(url, data = upload_value, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        s = random.randint(500, 9500) / 1000.0      # Upload interval

        if count % 250 == 0:
            os.system('cls')
        
        count += 1
        if r.text == '':
            print('#' + str(count) + ' QQ:' + username + ', password: ' + password + '. Next in ' + str(s) + 's')
        else:
            print(r.text)
        time.sleep(s)
