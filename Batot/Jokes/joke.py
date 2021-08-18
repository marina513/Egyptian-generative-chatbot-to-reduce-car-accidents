import requests
from bs4 import BeautifulSoup
import re

#************************ search for user input  **********************#
def joke_fn(search, num):
    print("search joke")
    num = int(num)
    #************************ handling Data base if search in database *************#
    line_num = 0
    file_variable = open('C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt')
    all_lines = file_variable.readlines()
    joke = []
    with open("C:/Users/AnyOneElse/GP_POP/Batot/Jokes/jokes_data.txt") as f:
        for line in f:
            line_num += 1
            if "<<  " + search + "  >>\n" in line:
                print("joke found")
                Q=[];A=[]
                num_jokes = int( all_lines[line_num] )
               
                for i in range( (num_jokes+1) * 2 + (num_jokes - 2) ): #Q&A - space
                    try:
                        if((len(all_lines[line_num  + i ]) > 3) and (i%2==0)):
                            Q.append(all_lines[line_num  + i ])
                        elif((len(all_lines[line_num  + i ]) > 3) and (i%2!=0)):
                            A.append(all_lines[line_num  + i ])
                    except:
                        e = 5;    

                if(num < len(A)):        
                    q = Q[num]
                    a = A[num]
                else:
                    q = Q[0]
                    a = A[0]
                joke.append(q)
                joke.append(a)
                print(joke)
                return joke
                







