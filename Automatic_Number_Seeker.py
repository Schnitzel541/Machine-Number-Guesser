import random

low = 0

search_for = int(input("Please input a number to search for: "))
high = int(input("Please input a roof number: "))


if high < search_for:
    print(f"{high} is lower than {search_for}, can't proceed.")
else:

    list_numbers = []

    guess_counter = 0
    x = random.randint(low, high)
    while x != search_for:
        x = random.randint(low, high)
        guess_counter = guess_counter + 1
        list_numbers.append(x)
        print(x)
        
    print(f'It took the machine {guess_counter} guesses!')
    print_list = input("Would you like to see a list of the numbers attempted? (Y/N?): ")
    if print_list == "Y":
        print(list_numbers)
    elif print_list == "y":
        print(list_numbers)
    else:
        print("Okay, bye")
