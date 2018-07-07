import requests

def login(user, passw, server):
    url = "http://" + server + ".e-sim.org/index.html"
    login_url = "http://" + server + ".e-sim.org/login.html"
    login_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/index.html",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    login_params = {
        "login": user,
        "password": passw,
        "facebookAdId":""
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
    session.post(login_url, headers=login_headers, cookies=cookies_b, data=login_params)
    return session



def train(session, server):
    training_url = "http://" + server + ".e-sim.org/train/ajax"
    train_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }

    session.post(training_url, headers=train_headers)
    return 0



def work(session, server):
    train_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }
    working_url = "http://" + server + ".e-sim.org/work/ajax?action=work"
    session.post(working_url, headers=train_headers)



def gift(sess, server):
    gift_url = "http://" + server + ".e-sim.org/gift.html?quality=1"
    gift_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }
    sess.post(gift_url, headers=gift_headers)
    return 0

def eat(sess, server):
    eating_url = "http://" + server + ".e-sim.org/eat.html?quality=1"
    eat_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }
    sess.post(eating_url, headers=eat_headers)
    return 0

def fight(sess, server):
    fighting_url = "http://" + server + ".e-sim.org/fight.html"
    fight_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "*/*",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "https://" + server + ".e-sim.org/train.html",
        "X-Requested-With": "XMLHttpRequest"
    }
    fight_params = {
        "weaponQuality":"1",
        "battleRoundId": "941536",
        "side": "attacker",
        "value": "undefined"
        }
    sess.post(fighting_url, headers=fight_headers, data=fight_params)
    return 0
