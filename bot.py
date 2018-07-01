import requests

servers = { '1': "primera", '2': "secura", '3': "suna",
            '4': "nebula", '5': "xix", '6': "xaria" }


def printServers():
    print("1 - Primera\n2 - Secura\n3 - Suna\n4 - Nebula\n5 - XIX\n6 - Xaria")
    return


def showAccounts():
    try:
        file = open("accounts.txt", "r")
        for line in file:
            print(line.split(",")[2] + ", " + line.split(",")[0])

        file.close()
    except:
        print("Can't open file")
        
    return

def addAccount():
    user = input("Username: ")
    passw = input("Password: ")
    printServers()
    srv = input("Server Nº: ")

    file = open("accounts.txt", "a")
    file.write(user+","+passw+","+servers.get(srv)+",")
    
    return


def removeAccount():
    user = input("Username to delete: ")
    printServers()
    srv = input("Server: ")

    file = open("accounts.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("accounts.txt", "w")
    for line in lines:
        if (line.split(",")[0]!=user) and (line.split(",")[2] != servers.get(srv)) :
            file.write(line)
        else:
            print("Deleting " + line.split(",")[0] + " from " +line.split(",")[2]+" server")

    file.close()          
    return

def bot(user, passw, server):
    url = "http://" + server + ".e-sim.org/index.html"
    login_url = "http://" + server + ".e-sim.org/login.html"
    training_url = "http://" + server + ".e-sim.org/train/ajax"
    working_url = "http://" + server + ".e-sim.org/work/ajax?action=work"


    login_params = {
            "login": user,
            "password": passw,
            "facebookAdId":""
        }

    login_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://" + server + ".e-sim.org/index.html",
            "Content-Type": "application/x-www-form-urlencoded"
        }

    train_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
            "Accept": "*/*",
            "Accept-Language": "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://" + server + ".e-sim.org/train.html",
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
    return


def runOne():
    user = input("Username: ")
    passw = input("Password: ")
    printServers()
    srv = servers.get(input("Server: "))
    bot(user, passw, srv)
    
    return

def runEveryone():

    file = open("accounts.txt", "r")
    for line in file:
        user = line.split(",")[0]
        passw = line.split(",")[1]
        srv = line.split(",")[2]
        print("Account " + user + " in " + srv + " server")
        bot(user, passw, srv)
        print("Done")

    file.close()

    return



while 1:

    print("0 - Show accounts")
    print("1 - Add account")
    print("2 - Remove account")
    print("3 - Run for one")
    print("4 - Run for all")
    print("5 - Exit")

    ops = { '0': showAccounts, '1': addAccount, '2': removeAccount,
            '3': runOne, '4': runEveryone, '5': exit
            }

    opt = input("Option: ")

    func = ops.get(opt, lambda: "Try another one")
    func()


    


