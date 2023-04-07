#Create multiple var module_1 - 6 to collect data for list/ equations
#create list for min var
#create list for max var
#
#ensure that all items are declared as FLOAT!!!
#
#create var for sum/ mod_1 + mod_2 etc...
#create var for avg/ sum of mod/ by amount input = 6
#
#print statements requesting input to the 6 module grades
#
#br
#
#display lowest grade: space evenly and ensure that :.1f to display input number .0
#
#display highest grade: space evenly and ensure that :.1f to display input number .0
#
#display sum of grade: space evenly and ensure that :.1f to display input number .0
#
#display avg of grade: space evenly and ensure that :.2f to display input number .0
#
#
    # CTI-110

   # P4HW1 - Score List
   # Curtis Lowery
   # 20230406 
   #

#get all inputs for the modules 1-6

#get how many grades user would like to enter
num_scores = (int(input('How many scores do you want to enter?')))
scores = []


for i in range(num_scores):
    score = float(input('Enter score number #{}: '.format(i+1)))
    scores.append(score)

    if score < 0 or score > 100:
        print('INVALID score entered!!!! \nScore should be between 0 and 100')
        i-= 1
    else: 
        scores.append(score)


print('')
if scores: #ensure list is not empty
    sum = sum(scores)
    avg = sum / num_scores

    print('------------ RESULTS ------------')
    print('Lowest grade:       ', min(scores))
    print('Highest grade:      ', max(scores))
    print(f'Sum of grades:      ', sum)
    print(f'Average of grades:  ', format(avg, '.2f'))
    print('---------------------------------')
else: 
    print('No valid scores entered')