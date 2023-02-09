
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
    n=int(input('what language_?')) 
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

#def transfer(e:list):
#    e=list(map(str, e)) 
#    word=str(e) 
#    n=e.count(word)
#    pos=0
#    for j in range(n): 
#        ind=e.index(word, pos) 
#        w=e[ind] 
#        print(f'{w}') 
#        pos=ind+1

def word_transfer(e:list,l:list): 
    n=input('Which laguage_? English>:1 Russian>:2')
    if int(n)==1: 
        e=list(map(str,e)) 
        pos=0 
        n=input('English:') 
        ind=e.index(n,pos) 
        n=print(l[ind]) 
        pos=ind+1 
       
        

    elif int(n)==2:  
        l=list(map(str, l)) 
        pos=0 
        n=input('Russian:') 
        ind=l.index(n, pos) 
        n=print(e[ind]) 
        pos=+1
    #elif int(n) not in e and int(n) not in l: 
    #    print('there is no such word in the dictionary ')




    






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
                        


    

   

