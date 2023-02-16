#Display ‘This program calculates and displays travel expenses’
#Declare user_budget 
#input (int)
#		‘Enter budget:’
#Declare user_destination 
#input (int)
#‘Enter travel destination:’
#Declare user_gas 
#input (int)
#‘How much do you think you will spend on gas?’

#Declare user_hotel 
#Input (int)
#	‘Approximately, how much will you need for accommodation/ hotel?’
#Declare user_food
#	Input (int)
#		‘Last, how much do you need for food?’

#Insert printed page break

#Display individual output: 

#Location:
#Initial budget:
#Br
#Fuel: 
#Accommodation:
#Food:
#Br

#Calculate budgeted amount minus expected expenses

#Declare user_total = int(user_budget – user_food – user_gas – user_hotel)
#Display result	
#	‘Remaining balance:’
#---------------------------------------------------------------------------------------
#This program will enable you to plan your trip around your budget!!!
#20230213
#CTI-110 P1HW2-Travel Expense
#Lowery, Curtis
#

print('This program calculates and displays travel expenses')
user_budget = int(input('Enter budget:\n'))
#get user destination
user_destination = (input('Enter your travel destination:\n'))
#get approx gas expense
user_gas = int(input('How much do you think you will spend on gas?'))
#get approx lodging expense
user_hotel = int(input('Approximately, how much will you need for accomadation/hotel?\n'))
#get food expense
user_food = int(input('Last, how much do you need for food?\n'))
print('-----------------Travel Expenses----------------------')
#diplay all results from prior input in reciept format
print('Location:',user_destination)
print('Initial Budget:',user_budget)
#pg break
print('')
print('Fuel:',user_gas)
print('Accomodation:',user_hotel)
print('Food:',user_food)
#pg break
print('')
#calculate budgeted amount minus estimated expenses
user_total = int(user_budget - user_food - user_gas - user_hotel)
#display calculated result
print('Remaining balance:',user_total)