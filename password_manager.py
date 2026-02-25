pwd = input("what is the master password? ")

def view():
    with open("passwords.txt","r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            user,passw = line.split("|")
            print("User:",user,"| Password:",passw)

def add():
    name = input("Account name: ")
    password = input("Password: ")
    f = open("passwords.txt","a")
    f.write(name+"|"+password+"\n")
    f.close()
    print("saved...")

while True:

    mode = input("add or view? press q to quit : ")

    if mode.lower() == "q":
        print("bye")
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("wrong option try again")