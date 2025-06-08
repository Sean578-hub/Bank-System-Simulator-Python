import random
bank_account = []
balance = 1000
count = 0
increase = 0
pin = ""
def create_acount():
    global pin
    name = input("Enter your name ")
    LastName = input("Enter your last name ")
    DateOfBirth = input("Enter your date of birth ")
    age = int(input("How old are you ? "))
    list = [name, LastName, DateOfBirth, age, pin]
    if age < 18:
        print("You are not old anaf to create a bank account ")
    else:
        first = random.randint(1, 100000)
        second = random.randint(1, 100000)
        third = random.randint(1, 100000)
        forth = random.randint(1, 100000)

        first = str(first)
        second = str(second)
        third = str(third)
        forth = str(forth)
        pin = first + second + third + forth

        print(f"Coungrats {name}, you have created a bank account ")
        list.append(bank_account)

def add_money():
    global balance
    money = int(input("How much would you like to add money to your bank account ? "))
    balance += money
    print(f"Succesfuly add {money} to your balance ")

def withdrow():
    global balance
    remove = int(input("How much money would you like to withdraw ? "))
    while remove > balance:
        print("Over limit ")
        remove = int(input("How much money would you like to withdraw ? "))
    if remove <= balance:
        balance -= remove
        print(f"Succesfuly removed {remove} from yor bank account ")

def income():
    global balance
    global count
    global increase
    ammount = int(input("Enter the amount of money that you want to put for income "))
    years = int(input("Enter the amount of years you want your money to income "))
    while ammount > balance:
        print("over limit")
        ammount = int(input("Enter the amount of money that you want to put for income "))
        years = int(input("Enter the amount of years you want your money to income "))
    if ammount <= balance:
        balance -= ammount
        while count != years:
            increase = ammount * 0.1
            ammount = ammount + increase
            count +=1
        print(f"Your new balance after income is {ammount} ")

while True:
    print("1. create a bank account")
    print("2. add money")
    print("3. withdrow")
    print("4. income")
    print("5. exit")
    choice = int(input("Enter a your choice form 1 to 5 only "))
    if choice == 1:
        create_acount()
    elif choice == 2:
        add_money()
    elif choice == 3:
        withdrow()
    elif choice == 4:
        income()
    elif choice == 5:
        print("Have a good rest of your day ")
        break












