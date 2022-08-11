Stake_Amount = int(input("Please tell me the stake amount must be >= 50 : "))

if Stake_Amount >= 50 :
    print("Ok let me calculate!")
else :
    print("You can use Fee decreasing system but just for let you know ... ")
    
x = Stake_Amount/50*10
print(f"You can use fee decreasing system {x} times a day ; If you stake ${Stake_Amount}!")
