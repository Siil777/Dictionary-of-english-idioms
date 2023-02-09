from module1 import* 


while True: 
    print('----------------------------------------')
    print('\n0 read file\n1 input words\n2 save words to dictionary\n3 translate word') 
    v=input('>>:')
    if v=='0': 
        english=[] 
        russian=[] 
        english=read_file('eng_file.txt') 
        russian=read_file('rus_file.txt') 
        zipped=list(zip(english,russian))
        print(english)  
        print(russian) 
    #elif v==1:
    #    choice=input('in what language do you want to add a word to the database_? English>1: Russian>2: ') 
    #    #amount,zipped=input('in what language do you want to add a word to the database_? English>1: Russian>2: ')
    #    input_word(english,russian,zipped)
     

    elif v=='1': 
        english,russian=input_word(english,russian) 
        print(english) 
        print(russian)
    elif v=='2':  
        save_to_file(english,'eng_file.txt') 
        save_to_file(russian,'rus_file.txt')
    elif v=='3': 
        word_transfer(english,russian)


