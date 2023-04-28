#print welcome message
#print menu option
#get user input for the menu option
#create while loop for iteration
#create if loop for each selection choice
#within ea. if loop conduct the proper math with random ints(can input range if you want)
#IF the user calculates and inputs the correct number output congratulations
#ensure count is displayed of 1 for how many guesses to get it correct
#IF user does not get it correct 
    #count +1
    #print the answer is incorrect try again
    #have a continue statment to re-iterate THEIR INPUT
    #***DO NOT RE-ITERATE BACK TO THE MATH PROBLEM!!!!***
    #when the right answer is input after others 
        #print congratulation it took you ## guesses
#when complete retrun to main menu 
#if '3' is input exit the program
#else continue program
# 27APRIL2023

   # CTI-110 P5HW - Math Quiz

   # Curtis Lowery
import random

loop_count = True


print('Welcome to the Math Quiz!!!')
while loop_count:
    
    print('MAIN MENU \n' +
        '-------------------\n' +
        '1) Adding random number \n' +
        '2) Subtracting random number \n' +
        '3) Exit')  
    print('')
    print('Please choose one of the menu options:')
    
    user_input = int(input())
    counter = 0

    if user_input == 1:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        quiz_answer = num1+num2
        print(f"  {num1} \n"
              f"+ {num2}")
        user_guess = int(input())
        print('')
        if user_guess == quiz_answer:
            counter += 1
            
        elif user_guess != quiz_answer:    
            while user_guess != quiz_answer:
                counter += 1
                if user_guess < quiz_answer:
                    print('Sorry, guess is to low.')
                elif user_guess > quiz_answer:
                    print('Sorry, gues is to high.')
                    print('')
                user_guess = int(input('Try again: '))
                counter += 1

        print('Congratulations!!! Your answer is correct. \n'
                    'Number of guesses:', counter)
        print('')
    elif user_input == 2:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        quiz_answer = num1-num2
        print(f"  {num1} \n"
              f"- {num2}")
        user_guess = int(input())
        print('')
        if user_guess == quiz_answer:
            counter += 1
            
        elif user_guess != quiz_answer:    
            while user_guess != quiz_answer:
                counter += 1
                if user_guess < quiz_answer:
                    print('Sorry, guess is to low.')
                elif user_guess > quiz_answer:
                    print('Sorry, guess is to high.')
                    print('')
                user_guess = int(input('Try again: '))

                counter += 1
        print('Congratulations!!! Your answer is correct. \n'
                    'Number of guesses:', counter)
        print('')
    elif user_input == 3:
        loop_count = False
        print('Thanks for playing....')
        print('Bye!!')
    else:
        print('Invalid input try again')
        
        

 


