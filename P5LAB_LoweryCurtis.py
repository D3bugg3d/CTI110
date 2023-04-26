# Define your function here.
def days_in_feb(user_year):
    
    if user_year % 4 == 0 and (user_year % 100 != 0 or user_year % 400 == 0):
        leap_year = 29
    else:
        leap_year = 28
        
    return leap_year
        
if __name__ == '__main__':
    year = int(input())
    print(year, 'has', days_in_feb(year), 'days in February.')
