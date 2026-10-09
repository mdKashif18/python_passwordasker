with open ("passwrod","r") as f: #opens a file named passwrod.txt
    password=f.read().split() #reads and split lines, you can use splitlines() if there are strings with spaces like "senku ishigami" rest split() works for this type "senku"

print(password) #just a place holder to check the password output from file


for i in password:
    pass_input=input("Tell me the password or get shot: ")
    if pass_input in password:
        print("access granted")
        break
    else:
        print("access denied")
        continue
    