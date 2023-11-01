def potion(potions):
    print()
    

    print('The potions you can choose are: ')
    potions_list = potions.keys()
    print()

    for item in potions_list:
        print(item)
    print()
    
    enter = 1
    while enter:
        choose = input('Choose the potion for you: ')
        if choose in potions_list:
            enter = 0
        else:
            print('Wrong name. Try to enter proper name of potion')
    print()
    print('You need to buy the following ingredients for the potion. You can buy them now: ')
    print()

    ingredients = potions[choose]
    for item in ingredients:
        print(item)
    print()

 
    bought = []
    for item in ingredients:
        buy = input(f"If you want to buy {item.upper()}, press 'y', otherwise press 'n' or any other but not 'y' ")
        if buy == 'y':
            bought.append(item)
            print(f"You've bought {item.upper()} ")
        #else: 
            #continue
    print()   
    print("You've bought these ingeredients:")
    print()
    for item in bought:
        print(item)
    print()

potion_dict = { "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"], "Flying Potion": 
           ["Phoenix feather", "Troll tooth", "Mermaid scale"], "HealingPotion": ["Unicorn horn", "Elf hair", "Golden apple"] }

shopping = 1
while shopping:
    print()
    print('Welcome to the Magic Potion Shop!')
    potion(potion_dict)
    shopping = int(input('If you want shopping to go on, enter number "1". To stop shopping enter number "0"  '))
