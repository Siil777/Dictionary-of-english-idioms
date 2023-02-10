from module1 import* 


while True: 
    print('----------------------------------------')
    print('\n0 read file\n1 input words\n2 save words to dictionary\n3 translate word/find word\n4 fix_word') 
    v=input('>>:')
    if v=='0': 
        english=[] 
        russian=[] 
        english=read_file('eng_file.txt') 
        russian=read_file('rus_file.txt') 
        zipped=list(zip(english,russian))
        for e,n in zip(english,russian): 
                print(f'{e} / {n}')
        
    elif v=='1': 
        english,russian=input_word(english,russian) 
        for t,v in zip(english,russian): 
                print(f'{t} / {v}')
    elif v=='2':
          
        save_to_file(english,'eng_file.txt') 
        save_to_file(russian,'rus_file.txt')
    elif v=='3':




        with open('eng_file.txt','r', encoding='utf-8-sig') as name_file, open('rus_file.txt', 'r', encoding='utf-8-sig') as salary_file:
            eng = map(str.rstrip, name_file)
            rus = map(str.rstrip, salary_file)
            

            data = dict(zip(eng, rus))
            
            n=input('what laguage? 1 Englis, 2 Russian')
            if int(n)==1: 
                word =input('English ')
                if word in data.keys():
                    print(f'word: {word} is found: {data[word]}')
                if word not in data.keys():
                    print('word is not found')
                if word not in data.keys(): 
                    print('would you like to input the word to the dictionary?:1 yes,2 no')
                    c=input('')
                    if c=='1':
                           english,russian=input_word(english,russian) 
                           for x,o in zip(english,russian):  
                               print(f'{x} / {o}')
                    elif c=='2':
                        break
            if int(n)==2:  
                with open('eng_file.txt','r', encoding='utf-8-sig') as name_file, open('rus_file.txt', 'r', encoding='utf-8-sig') as salary_file: 
                    eng = map(str.rstrip, name_file) 
                    rus = map(str.rstrip, salary_file) 
                    data = dict(zip(rus, eng))  
                    word =input('Russian') 
                    if word in data.keys():
                            print(f'word: {word} is found: {data[word]}') 
                    if word not in data.keys():
                            print('word is not found')
                    if word not in data.keys(): 
                            print('would you like to input the word to the dictionary?:1 yes,2 no')
                            c=input('')
                            if c=='1':
                                   english,russian=input_word(english,russian) 
                                   for z,l in zip(english,russian):   
                                       print(f'{z} / {l}')
                            elif c=='2':
                                break
    elif v=='4':
        c=input('in which language the word should be corrected? 1 English,2 Russian ') 
        if c=='1': 
            fix_e(english,russian) 
        elif c=='2': 
            fix_r(russian,english)

