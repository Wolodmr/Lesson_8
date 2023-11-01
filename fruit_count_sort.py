#Counting times, fruit is called by user
dict = {}

answer = 1
while answer != '0':  
    answer = input('Enter name of a fruit or enter "0" ')
    
    if answer not in dict:
        if answer != '0':
            dict[answer] = 1  
        else: break 
    else:
        dict[answer] +=1  

print()
print('Items, Counts')

d1 = sorted(dict.items(), key=lambda item: item[1])   

for i in range(len(d1)-1, -1, -1):
    print(d1[i][0], ': ', d1[i][1])



