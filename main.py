

with open (r"\passwrod.txt","r") as f: #opens a file named passwrod.txt
    password=f.read().split() #reads and split lines, you can use splitlines() if there are strings with spaces like "senku ishigami" rest split() works for this type "senku"

print(password) #just a place holder to check the password output from file


for i in password:
    pass_input=input("Tell me the password or get shot or type 'add' to add a password: ")
    if pass_input in password:
        print("access granted")
        break
    elif pass_input == "add":
        add_pass = input("type your password you want to add: ")
        with open(r"\passwrod.txt","a") as f:
            f.write(add_pass+"\n")
            print(f"'{add_pass}' succesfully added")
    else:
        print("access denied")
        continue
    