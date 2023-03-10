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
print(f"Sum of grades:       {sum:.0f}")
#print out the average of the enteries
print(f"Average of grades:   {avg:.0f}")
#inser lower pg break
print('---------------------------------')

