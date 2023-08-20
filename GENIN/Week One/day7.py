#writing my day seven code below here
    #PY lists
import random
word_list = ["Razaq","Ogunmepon","Ajeku"]
computer_choice = random.choice(word_list)
display = []
for letter in range(len(computer_choice)):
    display += "_" 
print(display)
guesses = 3
playing = True
while playing:
    user_guess = input("guess a letter: ").lower()
    for position in range(len(computer_choice)):
        letter = computer_choice[position]
        if letter == user_guess:
            display[position] = letter
    if user_guess not in computer_choice:
        print("Not in word")
        guesses -= 1     
    print(display)
    if "_" not in display:
        print("You win")
        playing = False
    elif guesses == 0:
        print("You lose")
        playing = False
