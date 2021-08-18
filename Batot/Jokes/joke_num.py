from sounds.speak_ import speak_ar
import requests
from bs4 import BeautifulSoup
import re
import random
from mtranslate import translate

#************************ search for user input  **********************#
def joke_num(joke_type,lang):
    
    Found = False
    file_variable = open('C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt')
    all_lines = file_variable.readlines()

    #***** handling Data base if search in database & random *************#
    search = joke_type
    line_num = 0
    search_rand = ""
    if(search == 'random'):
        options = []
        file_variable = open('C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_list.txt')
        read_jokes_list = file_variable.readlines()
        for l in read_jokes_list:
            words = l.rstrip("\n")
            options.append(words)
            
        rand = random.randint(0,len(options)-1)
        search_rand = options[rand]
        if(lang=='en'):
            print(f"I choose {search_rand} jokes for you")
        else:
            output = translate( search_rand ,'ar')
            print(f"    اختارتلك نكت عن  {output}  ")
            speak_ar(f"    اختارتلك  نُكَتٌ عن  {output}  ")

        with open("C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt") as f:
            for line in f:
                line_num += 1
                if "<<  " + search_rand + "  >>\n" in line:
                    num_jokes = int( all_lines[line_num] )
                    return search_rand, num_jokes

    #************************ handling Data base if search in database *************#
    with open("C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt") as f:
        print("joke found in database")
        for line in f:
            line_num += 1
            if "<<  " + search + "  >>\n" in line:
                Found=True
                num_jokes = int( all_lines[line_num] ) #get from jokes list (num is written in data after each name )
                return search_rand, num_jokes



    #************************ handling Data base if search not in database *************#
    if(Found==False):
        print("joke not found in database")
        response = requests.get(f'https://www.ducksters.com/jokes/{search}.php')
        soup = BeautifulSoup(response.text, 'html.parser')
        Q = soup.findAll(text=re.compile('Q:'))
        A = soup.findAll(text=re.compile('A: '))

        #************************ handling user input  **********************#
        Q_List = [] ; A_List = [] ; Jokes = []

        for q in Q:
            Q_List.append(q)
        for a in A:
            A_List.append(a)
        if(len(Q_List) != len(A_List)):
            Q_List = Q_List[1:]

        for i in range(len(Q_List)):
            j = str(Q_List[i]) + "  " + str(A_List[i])
            Jokes.append(j)

        if( len(Jokes)==0 ):
            print("اسف لم اجدها اختر واحدة تاني")
            
        else:
            File_object = open(r"C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_list.txt",'a')
            File_object.write(search + "\n")
            File_object.close()

            File_object = open(r"C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt",'a')
            File_object.write("*********************************************************\n")
            File_object.write("<<  " + search + "  >>\n")
            File_object.write( str(len(Q_List)) )
            for i in range(len(Jokes)):
                File_object.writelines(Jokes[i])
            File_object.close()

        return "",len(Jokes)






