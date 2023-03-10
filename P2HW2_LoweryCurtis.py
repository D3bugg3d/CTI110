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
   # P2HW2 - List
   # Curtis Lowery
   # 20230309
   #

#get all inputs for the modules 1-6

module_1 = float(input('Enter your grade for module 1: '))
module_2 = float(input('Enter your grade for module 2: '))
module_3 = float(input('Enter your grade for module 3: '))
module_4 = float(input('Enter your grade for module 4: '))
module_5 = float(input('Enter your grade for module 5: '))
module_6 = float(input('Enter your grade for module 6: '))
print('')
sum = float(module_1 + module_2 + module_3 + module_4 + module_5 + module_6)
avg = float(module_1 + module_2 + module_3 + module_4 + module_5 + module_6)/6

#print pg break
print('------------ RESULTS ------------') 
#print out the lowest entry
low_num = [module_1, module_2, module_3, module_4, module_5, module_6]
print('Lowest grade:       ',min (low_num))
#print out the hightest entry
high_num = [module_1, module_2, module_3, module_4, module_5, module_6]
print('Highest grade:      ',max(high_num))
#print out the sum of the entries
print(f"Sum of grades:       {sum:.1f}")
#print out the average of the enteries
print(f"Average of grades:   {avg:.2f}")
#inser lower pg break
print('---------------------------------')

print(f'Lowest grade: {min(low_num):.0f}')