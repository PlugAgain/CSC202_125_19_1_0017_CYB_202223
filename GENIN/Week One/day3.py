#writing my day three code below here
    #Can u ride in Costa Rica
print("Welcome to the roller-costa-rica!")
height = int(input("What is your height in centimeter? "))
if height >= 120:
    print("You can ride the roller-costa-rica")
else:
    print("Sorry Mr/Mrs Dwarf, you have to grow taller before you can ride.")

    #Modulo Operation 
number = int(input("Which number you wan check?"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#BMI 2.0
bmi = 28
if bmi < 18.5:
    print(f"Your BMI is {bmi},you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi < 40:
    print(f"Your BMI is {bmi}, you are ROBERTO CALORIES.")
else:
    print(f"Your BMI is {bmi}, you are clinically Obese.")

    #check a leap year
year = int(input("Which year do you want to check?"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year.")

    #Order a Pizza
size = input("What size pizza do you want? S, M, L or XL ?")
pepperoni = input("Do you want to add pepperoni? Y or N? ")
cheese = input("Do you want to add extra cheese? Y or N? ")
price = 0
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    price += 30

if pepperoni == "Y":
    if size == "S":
        price += 5
    else:
        price += 10
if cheese == "Y":
    price += 5
print(f"Your final bill is ${price}")

    #Love Calculator
print("Welcome to the love calculator")
name1 = input("What is your name? \n")
name2 = input ("What is your partner's name? \n")
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()
lowercase_name1_count1 = lowercase_name1.count("t") + lowercase_name2.count("t")
lowercase_name1_count2 = lowercase_name1.count("r") + lowercase_name2.count("r")
lowercase_name1_count3 = lowercase_name1.count("u") + lowercase_name2.count("u")
lowercase_name1_count4 = lowercase_name1.count("e") + lowercase_name2.count("e")
true_sum = lowercase_name1_count1 + lowercase_name1_count2 + lowercase_name1_count3 + lowercase_name1_count4
lowercase_name2_count1 = lowercase_name1.count("l") + lowercase_name2.count("l")
lowercase_name2_count2 = lowercase_name1.count("o") + lowercase_name2.count("o")
lowercase_name2_count3 = lowercase_name1.count("v") + lowercase_name2.count("v")
lowercase_name2_count4 = lowercase_name1.count("e") + lowercase_name2.count("e")
love_sum = lowercase_name2_count1 + lowercase_name2_count2 + lowercase_name2_count3 + lowercase_name2_count4
love_percentage = int(str(true_sum) + str(love_sum))
print(f"Your love percentage is {love_percentage}%")
if (love_percentage) < 10 or (love_percentage > 90):
    print(f"Your score is {love_percentage}, you go together like coke and mentos.")
elif (love_percentage >= 40) and (love_percentage <= 50):
    print(f"Your score is {love_percentage}, you are alright together. Love Birds")
else:
    print(f"Your score is {love_percentage}.")

    #Treasure Game
print("Welcome to Treasure Land Game!\nYour mission is to find the treasure!")
path = input("Choose a path between left and right. Type 'left' or 'right' to choose a path \n").lower()
if path == "left":
    choice1 = input("You are at a lake. There is an island at the middle of the lake.\nType 'swim' to swim across or type 'wait' to wait for a boat \n").lower()
    if choice1 == "wait":
        choice2 = input("The boat has arrived and it has three doors colored red, blue and yellow.\nType 'red' to enter through the red door or 'blue' to enter through the blue door \nor type 'yellow' to go through the yellow door  \n").lower()
        if choice2 == "red":
            print("Oops! Game over")
        elif choice2 == "blue":
            print("Oops! Wrong choice. Game over")
        else:
            print("Congratulations! You found the treasure")
    else:
        print("Oops, Game Over! The lake is too vast. You'll die if you choose to swim across")
else:
    print("Game over! You fell into a hole")
