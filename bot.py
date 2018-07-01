import requests

ID = ""
PASS = ""


url = "http://suna.e-sim.org/index.html"
login_url = "http://suna.e-sim.org/login.html"
training_url = "http://suna.e-sim.org/train/ajax"
working_url = "http://suna.e-sim.org/work/ajax?action=work"

r = requests.get(url)

login_params = {
        "login": ID,
        "password": PASS,
        "facebookAdId":""
    }

login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://suna.e-sim.org/index.html",
        "Content-Type": "application/x-www-form-urlencoded"
    }

train_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://suna.e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }


session = requests.session()
session.get(url, headers=login_headers)

cookies_b = {
        "md5": session.cookies['md5'],
        "JSESSIONID": session.cookies['JSESSIONID'],
        "showMission": "0",
        "registrationView": "REQUIRED_EMAIL"
        
    }
print(session.cookies['md5'])
print(session.cookies['JSESSIONID'])

#login
session.post(login_url, headers=login_headers, cookies=cookies_b, data=login_params)

#training
session.post(training_url, headers=train_headers, cookies=cookies_b)
#working
session.post(working_url, headers=train_headers, cookies=cookies_b)


session.close()



