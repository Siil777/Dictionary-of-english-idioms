


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
                        


    

   

