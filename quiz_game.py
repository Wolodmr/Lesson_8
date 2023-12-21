
# Preparation of the quiz questions:
def quiz_preparation():   
    
# Getting the themes and the quiz questions from the 'data_themes.json' and 'data_questions.json':    
    import json
    
    if cont != 'a':
        quest =[]
        with open("data_questions.json") as read_file:
            data = json.load(read_file)
            quest.append(data)
        with open("data_themes.json") as read_file1:
            themes = json.load(read_file1)               
        quest = quest[0]        
        return quest, themes
    
# Adding the themes and the quiz questions to the 'data_themes.json' and 'data_questions.json':   
    if cont == 'a':

    # Opening existing data for the quiz from the files:   
        with open("data_questions.json") as read_file:
                    quest = json.load(read_file)      
        with open("data_themes.json") as read_file1:
                    themes = json.load(read_file1) 

# Adding the new theme name, then new questions and answers options within the theme:
    # You can use this sample to add new data if your new theme is philosophy:
                    
                # theme_add = 'philosophy'
                    
                # dict_questions = [
                #                'Who wrote "Critique of Pure Reason"?',
                #                'Who was Socrates student?',
                #                'Who was a tutor of  Alexander the Great?',
                #                'Who is a founder of logical system?'
                #               ]
                
                # dict_opt[0] = ['Hegel','Kant', 'Kant'] 
                # dict_opt[1] = ['Xenophon','Plato', 'Plato']
                # dict_opt[2] = ['Pythagoras','Aristotl', 'Aristotl'] 
                # dict_opt[3] = ['Aristotl','Socrates', 'Aristotl'] 

        # Inputing the new theme:                    
        theme_add = input('A name of the new theme is: ')
        if theme_add not in themes:
            themes.append(theme_add)

        # Inputing the questions within the new theme:
        quest_add = [{}]*size
        dict_questions = ['']*size     
        
        for i in range(size):
            dict_questions[i] = input(f'Question number {i+1} from {size}: ')
        
        # Inputing the answers options for the questions:
        dict_options = [{}]*size            
        dict_opt = [['']*ans_opt]*size
             
        for i in range(size):
            print(f'Answer options for the question number {i+1} from {size}')
            for j in range(ans_opt):
                dict_opt[i][j] = input(f'{j+1} option from {ans_opt} ')
        
        # Formatting the new data as a list of dictionaries and concatenating the list with the existing one:
        for i in range(size):  
            for j in range(ans_opt):
                dict_options[i][str(j)] = dict_opt[i][j] 
        for i in range(size):
            quest_add[i] = {theme_add:{dict_questions[i]:dict_options[i]}}
        print(quest_add)
        quest +=quest_add
        
        # Saving all the data in the proper files:
        with open("data_themes.json", 'w') as write_file2:
                    json.dump(themes, write_file2)
        with open("data_questions.json", 'w') as write_file2:
                    json.dump(quest, write_file2)  
#--------------------------------------------------------------------------------------------------------------- 
#  START! START START START START START START START START START START START START START START START START START!                                 

# QUIZ STARTS! Answering questions begins:
def quiz_game(size, ans_opt, funct):
     
    if cont == 'y': 
        
        quest, themes = funct 
           
        que = []        
        theme = {}
        questions = []
        questions_theme = []
        que = []
        options = []
        
    # Displaying themes of questions for player and getting player's choice:        
        print()
        print('Themes of quiz:')
        size_themes = len(themes) 
        
        for i in range(size_themes):
            
            theme[i] = themes[i] 
            print(i, '. ', theme[i])
        print()
    
    # Choosing the theme:
        range_theme = None
        while not range_theme:
            t = int(input('Your theme number:  '))
            if t>=0 and t<size_themes:
                range_theme = 'ok'

    # Displaying questions for player and getting player's choice:                    
        for i in range(size_themes):
            for j in range(size_themes*size):
                if themes[i] in quest[j]:
                    questions.append(quest[j][themes[i]])

        # Distincting questions, which matches the chosen theme:            
        for j in range(size_themes*size):
            if themes[t] in quest[j]:
                questions_theme.append(quest[j][themes[t]])
        print()
        print(f'There are questions for the theme "{themes[t]}":')
        print()        

    # Displaying answer options for player and getting player's choice:        
        for i in range(size):
            for key, value in questions_theme[i].items():
                que.append(key)
                options.append(value)
        
        for i in range(size):
            print(i, '.  ', que[i])

        print()
        range_question = None
        while not range_question:
            q = int(input('Your question number:  '))
            if q>=0 and q<size:
                range_question = 'ok'
        
        print()
        print('So, your chosen question is: ')
        print(que[q])
        print()
        print('Choose answer: ')       
        print()

        for i in range(ans_opt-1):            
            print(i,'. ', options[q][str(i)])
        print()

        range_option = None
        while not range_option:
            ans_num = int(input('Number of your option  '))
            if ans_num>=0 and ans_num<ans_opt:
                range_option = 'ok'
        
        # Comparasing the answer with the right option:
        right = 0
        if options[q][str(ans_num)] == options[q][str(ans_opt-1)]:
            right = 1
            print('Congratulations! You are right')            
            archive_correct.append([t, q, ans_num])           
        else:
            if right == 0:
                print('Wrong answer')   
                archive_incorrect.append([t, q, ans_num])

    return archive_correct, archive_incorrect

# Keeping track of score and archiving correct and incorrect answers:
def main(function, funct):
    
    archive_correct = funct[0]
    archive_incorrect = funct[1]
    
    if cont == 'n':
# Calculating the score:           
        print()
        count = len(archive_correct + archive_incorrect)
        tru = len(archive_correct)
        print('#'*100)
        print()
        print("The score is: ", tru, '/', count)
# Archiving/displaying the data of correct answers:

# Archiving/displaying the themes of correct answers:             
        print()
        print('Correct answers you gave to these questions are: ')
        print()
        if len(archive_correct) == 0:
            print("Sorry, you have no correct answers.")
        themes_correct = []
        quest_correct = []
        ans_correct_options = []
        for i in range(len(archive_correct)):
            
            function_index = archive_correct[i][0] * size + archive_correct[i][1]
      
          
            for key, value in function[0][function_index].items():
                print('Theme is: ', key)
                themes_correct.append(key)

# Archiving/displaying the questions, for which player gave correct answers:
                for key_in, value_in in value.items():
                    quest_correct.append(key_in)
                    print(key_in)
                     
# Archiving/displaying the correct options:
                    ans_correct_options.append(value_in)  
                    print('Your option is: ', value_in[str(archive_correct[i][2])])                    
                    print()  

        
# Archiving/displaying the data of incorrect answers:  

# Archiving/displaying the themes of incorrect answers:        
        print()
        print('Questions, for which you gave wrong answers and proper correct answers: ')
        print()
        if len(archive_incorrect) == 0:
            print("You have no wrong answers.")
        themes_incorrect = []
        quest_incorrect = []
        ans_incorrect_options = []
        for i in range(len(archive_incorrect)):
            
            function_index = archive_incorrect[i][0] * size + archive_incorrect[i][1]
            for key, value in function[0][function_index].items():
                print('Theme is: ', key)
                themes_incorrect.append(key)

# Archiving/displaying the questions, for which player gave incorrect answers:
            for key_in, value_in in value.items():
                quest_incorrect.append(key_in)
                print(key_in)

# Archiving/displaying given by player incorrect answers:
                ans_incorrect_options.append(value_in)                     
                print('Your option is: ', value_in[str(archive_incorrect[i][2])])
# Archiving/displaying the correct options:
                correct_option = value_in['2']         
                print('Correct option is:', correct_option)
                print() 
        finish = True

# START START START START START START START START START START START START START START START START START START
        
# Start of the game.
# Source data, besides the questions and answers options, which are stored in 'data_file.json' file.
# The number of answer options for each question in 'data_file.json' file. (Real number is less by one than given here,
# because one option, declared by game authors among the options is etalon and it is in the last position of the options list):
        
from datetime import datetime

# current date and time
now = datetime.now()
timestamp_start = datetime.timestamp(now)
ans_opt = 3
size = 4

archive_correct = []
archive_incorrect = []    
finish = None
cont = 0 

# Loop for multiple running the program, according to player's wishes: 
cont = input('To play press "y", to add a question press "a" ')
if cont != 'a':
    while cont != 'n' or not finish:
        
        main(quiz_preparation(), quiz_game(size, ans_opt, quiz_preparation() ))  
        if cont == 'n': 

            # Time spent for the game:
            now = datetime.now()
            timestamp_stop = datetime.timestamp(now)
            print() 
            print(f'Time spent for the game is {(timestamp_stop - timestamp_start)//60} min, {(timestamp_stop - timestamp_start)//10*10} s')        
            break

        cont = input('If you want to continue, press "Enter", if no, press "n" ')    
       
else:
    quiz_preparation()
    
    
           
    

    


    
   
    



