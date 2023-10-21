

def dollarizer(word):
    if 's' in word:
        return word.replace('s', '$')
    else:
        return word
  
print(f'Dollarizer: {dollarizer("lexus")}')
        
def eurizer(word):
    if 'e' in word:
        return word.replace('e', '€')
    else:
        return word
  
print(f'Eurizer: {eurizer("lex")}')

def replacer(word, symbol1, symbol2):
    if symbol1 in word:
        return word.replace(symbol1, symbol2)
    else:
        return word
  
print(f"Replacer: {replacer('lex', 'x', 't')}")

def wonky_text(word, symbols, functions):
                                                                                
    
    return functions[0](functions[1](functions[2](word, symbols[0],symbols[1])))       
      
print(f"Wonky text: {wonky_text('interstellar',['l','£'], [dollarizer, eurizer, replacer] )}")

def celsius_to_fahrenheit(celsius):
    return celsius*9/5 + 32
print(f'Celsius to Fahrenheit: {celsius_to_fahrenheit(-70)}f')

def age_in_days(age_in_years):
    return age_in_years*365
print(f'Age in Days: {age_in_days(350)}')

def simple_interest(principal, rate_of_interest, time_in_years):
    return principal*rate_of_interest*time_in_years

print(f'Simple interest: {simple_interest(1000, 0.05, 3)}')

def plan_finance(amounts, rate_of_interest, time_in_years):
    amount_principal = amounts[0]
    amount_desired = amounts[1]
    amount_after_interest = amount_principal*(rate_of_interest*time_in_years + 1)
    return amount_desired < amount_after_interest
print(plan_finance([4_500_000, 5_000_000], 0.03, 4))











