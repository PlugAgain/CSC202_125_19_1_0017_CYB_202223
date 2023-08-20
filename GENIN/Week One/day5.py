#writing my day five code below here
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits) 

    #Average Height
student_heights = input("Input a list of student heights\n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)
average_height = round(total_height / number_of_students)
print(average_height)

    #High Score 
stud_scores = input("input a list of students scores").split()
for n in range(0, len(stud_scores)):
      stud_scores[n] = int(stud_scores[n])
      print(stud_scores)
highscore = 0
for score in stud_scores:
     if score > highscore:
      highscore = score
print(f"The high score is {highscore}")

    #Adding even numbers
total = 0
for number in range (0, 101):
    if number % 2 == 0:
        total += number
        print(total)
    
    #FizzBuzz game
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
    #Password generator
import random
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', ' 3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']
print("Welcome to the Password Generator")
nb_alphabets = int(input("How many letters would you like in your password? \n"))
nb_numbers = int(input("How  many numbers would you like? \n"))
nb_symbols = int(input("How many symbols would you like? \n"))
password = ""
for chr in range(1, nb_alphabets + 1):
    password += random.choice(alphabets)
for chr in range(1, nb_numbers + 1):
    password += random.choice(numbers)
for chr in range(1, nb_symbols + 1):
    password += random.choice(symbols)
print(password)
password_list = []
for chr in range(1, nb_alphabets + 1):
    password_list.append(random.choice(alphabets))
for chr in range(1, nb_numbers + 1):
    password_list += random.choice(numbers)
for chr in range(1, nb_symbols + 1):
    password_list += random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(str(password_list))
password = ""
for chr in password_list:
    password += chr
print(password)
