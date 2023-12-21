size = 4
ans_opt = 4
themes_source = 'math,physics,history,geography'
quest = [
['What is prime number?,0,Natural number divisible only by itself and 1,Natural number divisible only by itself and 1',
'What is linear equation?,The one with variables in power to 1,The one with the only variable,The one with variables in power to 1',
'What is 5/0 equal to?,0,No result,No result',
'What is a divisibility rule for 2?,Number is to end with 2,Number is to end with 0 or 2 or 4 or 6 or 8,Number is to end with 0 or 2 or 4 or 6 or 8'],
['In what case an Archimedes force is greater for the same submarine: when it is lying on the dirt bottom or on the sand bottom of the sea in the same depth?,Doesn"t matter,On the sand,On the sand',
'If a Gravitational force is greater for the same body when it is lying or when it is in a free flight in the same point of the space?,No,Yes,No',
'What is the speed of a book lying on the table in the school?,Depends on the choice of frame of reference,0,Depends on the choice of frame of reference',
'What is an acceleration module of the car with engine trust of 1000 Newtons if the car mass is 1000 kg?,1mps**2,10mps**2,1mps**2'],
['What country king was Leonidas in an Ancient Greece?,Sparta,Thebes,Sparta',
'Who was the first Emperor of Rome?,Gaius Julius Caesar,Marcus Junius Brutus,Gaius Julius Caesar',
'Whose army have defeated army of Spartakus?,Marcus Licinius Crassus,Gnaeus Pompeius Magnus,Marcus Licinius Crassus',
'Who was a leader of the peasant war in Germany?,Thomas Muntzer,Martin Luther,Thomas Muntzer'],
['What is the southern cape of the Southern America?,Cape Horn,Cape of Good Hope,Cape Horn',
'What is the most western country of the European continent?,United Kingdom,Portugal,Portugal',
'What is a capital of New Zealand?,Wellington,Auckland,Wellington',
'In what country is Brisbane town?,New Zealand,Australia,Australia']]
themes = themes_source.split(',')
for i in range(size):
    for j in range(size):
        quest[i][j] = quest[i][j].split(',')
        
import json

quiz = []
questi = {}
ans = {}
ansi = {}

#Write the data to the file

for i in range(size):
    ansi[i] = {}
    ans[i] = {}
    questi[i] = {}
    for j in range(size):
        ansi[i][j] = {}
        ans[i][j] = {}
        questi[i][j] = {}
        
for i in range(size):
    for j in range(size):
        
        questi[i][j][themes[i]] = ansi[i][j]
        
        
for i in range(size):
    for j in range(size):
        ansi[i][j][quest[i][j][0]] = ans[i][j]
        #print(quest[i][j])
for i in range(size):
    for j in range(size):
        for k in range(1, ans_opt):
            ans[i][j][k-1] = quest[i][j][k]
       
        quiz.append(questi[i][j])
print(quiz)
            
with open("data_questions.json", "w") as write_file:
    json.dump(quiz, write_file)
    
with open("data_themes.json", "w") as write_file1:
    json.dump(themes, write_file1)


              
    

    
    

    


    
   
    



