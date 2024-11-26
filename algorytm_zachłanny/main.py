def change():

    # User input
    try:
        Change = int(input("Enter change: "))
        n = int(input("Amount of different coins: "))
        Coins = []
        for a in range(n):
            Coins.append(int(input(f"Value of coin {a + 1}: ")))
    except:
        print("Something went wrong, make sure you used correct values and try again")
        input("press enter to exit")  # used so console doesn't close instantly
        exit(1)

    Coins.sort(reverse=True) #making sure we got our values in correct order to avoid issues

    i = 0
    counter = 0

    if(Coins[0]>Change):
        print("Coins values are greater than change, giving change is impossible")
        input("press enter to exit")  # used so console doesn't close instantly
        exit(1)
    while Change > 0: #counting coins
        while Change >= Coins[i]:
            Change -= Coins[i]
            counter+=1
        i += 1

    print(f"Required amount of coins:{counter}") #result

if __name__ == '__main__':
    change()
    input("press enter to exit") #used so console doesn't close instantly