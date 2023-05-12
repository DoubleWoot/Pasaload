import threading
import time
import random

load_balance = 0

if load_balance == 0:
    random_load = random.randint(1, 50)
    load_balance = random_load

def transaction(amount):
    global load_balance
    load_balance += amount
    print("\nProcessing...")
    time.sleep(3)
    print("\nYour balance is now: ", load_balance)


def add_load():
    x = True

    print("\nHow much do you want to add?")
    print("""
    1. P20
    2. P50
    3. P100""")

    while x == True:
        choice = input("Select amount or press 'e' to exit: ")
        if (choice == '1'):
            thread1 = threading.Thread(target=transaction, args=(20,))
            thread1.start()
            thread1.join()
        elif (choice == '2'):
            thread2 = threading.Thread(target=transaction, args=(50,))
            thread2.start()
            thread2.join()
        elif (choice == '3'):
            thread3 = threading.Thread(target=transaction, args=(100,))
            thread3.start()
            thread3.join()
        elif (choice == 'e'):
            x = False
            break



def main():
    global load_balance
    print("\n----Pasaload Service----")
    phoneNum = input("Enter your phone number: ")
    print("Checking your load balance...\n")
    time.sleep(3)
    print(phoneNum, "has a balance of:", load_balance)

    choice = input("Would you like to add load? (y/n): ")
    if choice.lower() == "y":
        add_load()
    elif choice.lower() == "n":
        print("Thank you for choosing us!")
    else:
        print("Please enter a valid choice.")
        main()

    pass

while True:
    main()
    choice = input("\nDo you want to run the program again? (y/n): ")
    if choice.lower() != "y":
        break