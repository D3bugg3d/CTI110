# CTI-110
   # P4HW2_Salary_LoweryCurtis
   # Curtis Lowery
   # 20230416
#First gather information on the employee
#use loop to ensure next iteration or exit when input = 'Done'
#employee name
#number of hours worked
#employee payrate
#has the employee worked overtime
    #hour_worked > 40 = overtime true
    #how much are they owed overtime = payrate * 2.5 (only for the amount of hours overtime)
    #ENSURE THAT YOU CAPTURE THE HOUR AMOUNT OVER 40 HOURS AND NOT 40 + OVERTIME!!!
    #
    #Display the information that they entered:
    #employee name
    #hours employee worked 
    #employee pay rate
#print out hours worked/ overtime/ overtime pay/ regular pay/ total pay

#This program will take an employee's input and calculate total pay and overtime pay
overtime = float(0.0)
reg_hour = float(0.0)
Employee_name = 'a'

#establish loop parameters for capturing multiple iterations of input
while True:
    Employee_name = input('Enter name of Employee\'s name or "Done" to terminate: ')

    if Employee_name == 'Done':
        break

    Hours_worked = float(input(f'How many hours did ' +Employee_name+ ' work:'))
    Hourly_wage = float(input('What is '+Employee_name+ ' pay rate?'))

    if Hours_worked > 40:
        overtime = (Hours_worked - 40)
        reg_hour = (Hours_worked - overtime)

    else: 
        overtime = 0
    #math corrected
    Ot_pay = float(((Hourly_wage * 2.5) - Hourly_wage) * overtime)
    reg_pay = float(reg_hour * Hourly_wage)
    tot_pay = float(reg_pay + Ot_pay)

    print('-----------------------------------------------------------------------------------------------')
    print('Employee Name: ', Employee_name)
    print('')
    print('Hours worked     Pay Rate        Overtime        OverTime Pay        RegHour Pay     Gross Pay')
    print('-----------------------------------------------------------------------------------------------')
    print(f"    {Hours_worked:.2f}         {Hourly_wage:.2f}            {overtime:.2f}              {Ot_pay:.2f}               {reg_pay:.2f}          {tot_pay:.2f}")




