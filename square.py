def ask():
    name = True
    while name:
        try:
            n = int(input("enter a number"))
            print(n)
        except:
            print("it is not valid\n")
            continue
        else:
            name = False
    print("squared number is: ")
    print(n**2)
ask()

