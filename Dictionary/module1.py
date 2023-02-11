from random import*
import random 


def read_file(file:str)->list: 

    fail=open(file,'r', encoding='utf-8-sig') 
    mas=[] 
    for row in fail: 
        if row.isdigit(): 
            mas.append(row.strip()) 
        else:
            mas.append(row.strip()) 
    fail.close()
    return mas 

def save_to_file(mas:list,file:str): 

    f=open(file,'w', encoding='utf-8-sig') 
    for item in mas: 
        f.write(item+'\n') 
    f.close() 

def input_word(e:list,r:list): 
    n=int(input('what language_? 1 English, 2 Russian')) 
    if int(n)==1:
        english=input('English:') 
        e.append(english) 
        russian=input('Russian:') 
        r.append(russian) 
    else:
        russian=input('Russian:') 
        r.append(russian) 
        english=input('English:') 
        e.append(english) 

    return e,r 

def fix_e(name:str,e:list):
    v=e.count(name) 
    v=input('enter word has to be fixed:') 
    if v in name: 
        fix_word=input('correction:') 
        for n,i in enumerate(name): 
            if i==v: 
                name[n]=fix_word
                print('fixed:\n{0}'.format(name))

def fix_r(name:str,r:list): 
    v=r.count(name) 
    v=input('enter word has to be fixed:')
    if v in name: 
        fix_word=input('correction:')
        for f,j in enumerate(name): 
            if j==v: 
                name[f]=fix_word
                print('fixed:\n{0}'.format(name)) 

def control_word(e:list,r:list):
    eng=list(map(str,e)) 
    eng=random.choice(eng) 
    print(eng)  
    rus=list(map(str,r)) 
    while True: 
        answ=input('word:') 
        if answ in rus: 
            print('right') 
        else: 
            print('wrong') 
        return e,r




    






#def input_word(choice,amount,zipped:list): 
#    if choice==1: 
        
#        for i in zipped: 
#            if i[0]<amount: 
#                print('')
#                print(input('English:'))
#                zipped.append(english)
                
#            elif choice==2: 
#                print('')
#                for i in zipped: 
#                    if i[0]>amount: 
#                        russian=input('russian:') 
#                        zipped.append(russian) 
                        


    

   

