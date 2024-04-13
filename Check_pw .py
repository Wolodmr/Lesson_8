# This program checks if entered password is correct, e.i. matches specified requirements, shown below
    # User can also check a series of passwords at once

# The function to input passwords:
def input_pw():

    # The requirements for password:
    print()
    print('STRONG PASSWORD is to match the following requirements:')
    print('-------------------------------------------------------')
    print()
    length_min = 7
    print(f'Length: {length_min} at least')
    special_char = ['@','#','$','%', '^', '&', '*']
    special_quantity = 1
    print(f'Special characters quantity of that {special_char}: {special_quantity} characters at least')
    numbers_quantity = 1
    print(f'Numbers quantity: {numbers_quantity}  ')
    uppercase_quantity = 1
    letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Uppercase letters quantity: {uppercase_quantity}  ')
    lowercase_quantity = 1
    letters_lower = 'abcdefghijklmnopqrstuvwxyz'
    print(f'Lowercase letters quantity: {lowercase_quantity}  ')
    print()
    print('VERY STRONG PASSWORD is to have the following additional quality:')
    print('-----------------------------------------------------------------')
    print()
    length_min_verystrong = 15
    print(f'Length - at least 15 characters {length_min_verystrong}')
    special_quantity_verystrong = 3
    print(f'Special characters quantity of that: {special_char}, at least {special_quantity_verystrong}')
    numbers_quantity_verystrong = 5
    print(f'Numbers - at least {numbers_quantity_verystrong}')

    # Input password:
    pw_series = []
    finish = False
    
    while not finish:
        pw = input('Enter your password: ')
        pw_series.append(pw)
        series = input('Press "Enter", if you want to check just that you have yet entered. If you want to check one more password, press "m" to continue ')
        if series != 'm':    
            finish = True

    return pw_series, length_min, special_quantity, numbers_quantity, uppercase_quantity, lowercase_quantity, length_min_verystrong, special_quantity_verystrong, numbers_quantity_verystrong, special_char, letters_upper, letters_lower

# The function to check quality of passwords:
def check_pw(data):
    pw_series, length_min, special_quantity, numbers_quantity, uppercase_quantity, lowercase_quantity, length_min_verystrong, special_quantity_verystrong, numbers_quantity_verystrong, special_char, letters_upper, letters_lower = data
    pw_quantity = len(pw_series)
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    passwords = []
    for i in range(pw_quantity):
        passwords.append({})
    
    # Initialization the passwords checking:
    for i in range(pw_quantity):        
        passwords[i]['Your password'] = pw_series[i]
        passwords[i]['Length of your password'] = len(pw_series[i])

        # Counting the special characters in password:        
        count = 0
        passwords[i]['Special characters in your password'] = str(0)
        for j in range(len(special_char)):
            for k in range(len(pw_series[i])):
                if special_char[j] == pw_series[i][k]:
                    count += 1
                passwords[i]['Special characters in your password'] = str(count)

    
        # Counting numbers in password:
        count = 0
        passwords[i]['Numbers quantity in password'] = str(0)
        for j in range(len(numbers)):
            for k in range(len(pw_series[i])):
                if numbers[j] == pw_series[i][k]:
                    count += 1
                passwords[i]['Numbers quantity in password'] = str(count)
        
        # Check if password contains uppercase characters:
        count = 0
        for k in range(len(passwords[i]['Your password'])):
            passwords[i]['Uppercase letters number in your password'] = str(0)
            if passwords[i]['Your password'][k] in letters_upper:
                count +=1
                passwords[i]['Uppercase letters number in your password'] = str(count)
                break

        # Check if password contains uppercase characters:
        count = 0
        for k in range(len(passwords[i]['Your password'])):
            passwords[i]['Lowercase letters number in your password'] = str(0)
            if passwords[i]['Your password'][k] in letters_lower:
                count += 1
                passwords[i]['Lowercase letters number in your password'] = str(count)
                break
    
    # Checking if the password is very strong:
    pw = ''    
    report = ['']*len(pw_series)
    for i in range(len(pw_series)):
        report[i] = {}
        report[i]['Your password'] = pw_series[i]
        report[i]['Your password strength'] = None
        if int(passwords[i]['Lowercase letters number in your password']):
            if int(passwords[i]['Uppercase letters number in your password']):                
                if int(passwords[i]['Special characters in your password']) >= special_quantity_verystrong:                    
                    if int(passwords[i]['Numbers quantity in password']) >= numbers_quantity_verystrong:                      
                        if int(passwords[i]['Length of your password']) >= length_min_verystrong:
                            pw = 'verystrong'
                            report[i]['Your password strength'] = 'very strong'
                
                # Checking if the password is strong:
                if int(passwords[i]['Special characters in your password']) >= special_quantity:
                    if int(passwords[i]['Numbers quantity in password']) >= numbers_quantity:
                        if int(passwords[i]['Length of your password']) >= length_min:
                            
                            if not pw:
                                report[i]['Your password strength'] = 'strong'
                            pw = ''

        # Detecting lack of specific characters in the password:           
            else:
                report[i]['Uppercase letters number in your password']= f"Add uppercase letters at least up to {uppercase_quantity}"           
        else:
            report[i]['Lowercase letters number in your password']= f"Add uppercase letters at least up to {lowercase_quantity}"
                  
        if int(passwords[i]['Special characters in your password']) < special_quantity:
            report[i]['Special characters in your password'] = f'Add special characters at least up to {special_quantity}'
        if int(passwords[i]['Numbers quantity in password']) < numbers_quantity:
            report[i]['Numbers quantity in password'] = f'Add numbers at least up to {numbers_quantity}'
        if int(passwords[i]['Length of your password']) < length_min:
            report[i]['Length of your password'] = f'Add characters at least up to {length_min}'
        if int(passwords[i]['Lowercase letters number in your password']) < lowercase_quantity:
            report[i]['Lowercase letters number in your password'] = f'Add Lowercase letters at least up to {lowercase_quantity}'
        if int(passwords[i]['Uppercase letters number in your password']) < uppercase_quantity:
            report[i]['Uppercase letters number in your password'] = f'Add uppercase letters at least up to {uppercase_quantity}'

    # Output the report about passwords quality:
    for i in range(len(pw_series)):
        print()
        print('NEW PASSWORD:')
        print('-------------')
        for k, v in report[i].items():
            print()
            print(k, ':', v)
        print()

max_try = 3
repeat = 0
count = 0
while repeat != 'n' and count < max_try:
    count += 1
    repeat = input('If you want to enter new password or series of passwords, enter "Enter", if not, enter "n"  ')
    if repeat != 'n':
        check_pw(input_pw())
if count == max_try:
    print('Sorry, you have reached the maximum number of tries')
    print()