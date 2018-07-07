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

def flyToWork(session, server, regionId, countryId, quality):
    fly_url = "http://" + server + ".e-sim.org/travel.html"
    travel_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://" + server + ".e-sim.org/region.html?id="+regionId  
    }
    travel_params = {
        "countryId":countryId,
        "regionId":regionId,
        "ticketQuality":quality
        }
    session.post(fly_url,headers=travel_headers,data=travel_params)
    return


session = login("n0nam3","esimsuna23","suna")
flyToWork(session,"suna","368","62","5")
print("Done")

session.close()












    
    
