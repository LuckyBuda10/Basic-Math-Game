import random
#Player Chooses mode, and makes sure their number is a number
game_mode = input('Easy, Medium, or Hard? ')
player_number = input('Enter A Whole Number Greater Then 10! ')
if player_number.isdigit() and int(player_number)>10:
    player_number = int(player_number)
else:
    print('Please Learn To Read, Then Play Again!')
    quit()

correct_answers = 0
incorrect_answers = 0

while True:
    #Assigns the sign numgber and number range values based on the mode selected by the player
    if game_mode == 'Easy':
        x = 1
        y = 2
        a = 10
        b = 100
    elif game_mode == "Medium":
        x = 3
        y = 4
        a = 2
        b = 10
    else:
        if game_mode == "Hard":
            x = 3
            y = 5
            a = 2
            b = 4
    sign_number = random.randint(x, y)
    num_range = random.randint(a, b)
    #Assigning the 1-5 sign_number to represent a math symbol
    if sign_number == 1:
        after_sign_number = int(player_number) + num_range
    elif sign_number == 2:
        after_sign_number = int(player_number) - num_range
    elif sign_number == 3:
        after_sign_number = int(player_number) * num_range
    elif sign_number == 4:
        after_sign_number = int(player_number) / num_range
    else:
        if sign_number == 5:
            after_sign_number = int(player_number) ** num_range
    #If Player chooses easy
    if game_mode == 'Easy':
        print(player_number, '->',after_sign_number)
        #making sure users answer is either a number or Exit
        user_guess = input('Guess What Number Was Added Or Subtracted To Get The Answer! Or, Type "Exit" To Quit! ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
        elif user_guess == 'Exit':
            print('Correct Answers: ', correct_answers)
            print('Incorrect Answers: ', incorrect_answers)
            quit()
        else:
            print('Please Insert A Number Next Time!')
            continue
        #Checking to see if they got the answer correct or not
        if user_guess == num_range:
            correct_answers +=1
            print('Congradulations! You Now Have', correct_answers, 'Correct Answer(s)!')
        elif user_guess != num_range:
            incorrect_answers +=1
            print('Ya Kinda Missed It... Try Again!')
            print('Incorrect Answers:', incorrect_answers)
            continue
    #If Player chooses medium
    if game_mode == "Medium":
        #checks if users guess is a number or exit command
        print(player_number, '->',after_sign_number)
        user_guess = input('Guess What Number Was +, -, *, or / To Get The Answer! Or, Type "Exit" To Quit! ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
        elif user_guess == 'Exit':
            print('Correct Answers: ', correct_answers)
            print('Incorrect Answers: ', incorrect_answers)
            quit()
        else:
            print('Please Insert A Number Next Time!')
            continue
        #checks if they got it right, and awards correct and incorrect answer points
        if user_guess == num_range:
            correct_answers +=1
            print('Congradulations! You Now Have', correct_answers, 'Correct Answer(s)!')
        elif user_guess != num_range:
            incorrect_answers +=1
            print('Ya Kinda Missed It... Try Again!')
            print('Incorrect Answers:', incorrect_answers)
    #If player selects hard
    if game_mode == "Hard":
        print(player_number, '->',after_sign_number)
        #checks if it is valid number or command
        user_guess = input('Guess What Number Was +, -, *, or / To Get The Answer! Or, Type "Exit" To Quit! ')
        if user_guess.isdigit():
            user_guess = int(user_guess)
        elif user_guess == 'Exit':
            print('Correct Answers: ', correct_answers)
            print('Incorrect Answers: ', incorrect_answers)
            quit()
        else:
            print('Please Insert A Number Next Time!')
            continue
        #checks if they got it right, and awards correct and incorrect answer points
        if user_guess == num_range:
            correct_answers +=1
            print('Congradulations! You Now Have', correct_answers, 'Correct Answer(s)!')
        elif user_guess != num_range:
            incorrect_answers +=1
            print('Ya Kinda Missed It... Try Again!')
            print('Incorrect Answers:', incorrect_answers)
            