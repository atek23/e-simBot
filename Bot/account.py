servers = { '1': "primera", '2': "secura", '3': "suna",
            '4': "nebula", '5': "xix", '6': "xaria", '7':"alpha" }


def printServers():
    print("1 - Primera\n2 - Secura\n3 - Suna\n4 - Nebula\n5 - XIX\n6 - Xaria\n7 - Alpha")
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
    file.write(user+","+passw+","+servers.get(srv)+",\n")
    
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
        if ((line.split(",")[0]!=user) and (line.split(",")[2] != servers.get(srv))) :
            file.write(line)
        else:
            print("Deleting " + line.split(",")[0] + " from " +line.split(",")[2]+" server")

    file.close()          
    return

