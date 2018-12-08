import account as acc
import bot


def run(usr, passw, srv):
    sess = bot.login(usr, passw, srv)
    print("\nLog into "+usr+" , "+srv+" server")
    bot.train(sess,srv)
    print("\tTraining...")
    bot.work(sess,srv)
    print("\tWorking...")      
    sess.close()
    print("\tExit\n")  
    return



def runOne():
    user = input("Username: ")
    passw = input("Password: ")
    acc.printServers()
    srv = acc.servers.get(input("Server: "))
    run(user, passw, srv)
    
    return

def runEveryone():

    file = open("accounts.txt", "r")
    for line in file:
        user = line.split(",")[0]
        passw = line.split(",")[1]
        srv = line.split(",")[2]
        #print("Account " + user + " in " + srv + " server")
        run(user, passw, srv)       
        #print("Done")

    file.close()

    return



while 1:

    print("0 - Show accounts")
    print("1 - Add account")
    print("2 - Remove account")
    print("3 - Run for one")
    print("4 - Run for all")
    print("5 - Exit")

    ops = { '0': acc.showAccounts, '1': acc.addAccount, '2': acc.removeAccount,
            '3': runOne, '4': runEveryone, '5': exit
            }

    opt = input("Option: ")

    func = ops.get(opt, lambda: "Try another one")
    func()




