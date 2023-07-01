import random

def gameEnd():
    userPlay = input('Do you want to play again Enter Yes or No\n').lower()
    if userPlay == 'yes':
        start()
    elif userPlay == 'no':
         print('You are Exit now')
    else:
        print('please enter yes or no !!!!')

def start():
    stages =[
         '''
            +-------+
            |       |
                    |
           \o       | 
            |\      |
           / \    	|       
           ===========
        '''
        ,
        
         '''
            +-------+
            |       |
              	    |
            o       |
           /|\|     |
           / \    	|
           ===========
        '''
        
        ,
        
         '''
            +-------+
            |       |
              	    |
            o       |
           /|\      |
           / \ |==| |
           ===========
        '''
        ,
        
         '''
            +-------+
            |       |
              	    |
            o       |
           /|\      |
           / \      |
          |==|      |
           ===========
        '''      
        ,
         '''
            +-------+
            |       |
            | 	    |
            o       |
           /|\      |
           / \      |
          |==|      |
           ===========
        '''  
        
        ,
        
         '''
            +-------+
            |       |
            |  	    |
            o       |
            /|\     |
            / \    	|
            \==\    |
           ===========
        '''
        
    ]
    
    
    
    
    word_list = ["apple" ,"baboon" , "camel" ,"horse" ,"red"]
    choosen_word = random.choice(word_list)
    print(choosen_word)
    empty_list = []
    for num in range(0,len(choosen_word)):
        empty_list.append("_")
    count = len(choosen_word) + 1
    countstages = 0
    while count > 0:
        print(empty_list)
        user_input =input('gusse the word :\n').lower()
        for position in range(0,len(choosen_word)):
                if user_input == choosen_word[position]:
                    empty_list[position] = choosen_word[position]
                    print(stages[countstages])
                    countstages+=1
        if "_" not in empty_list:
            break        
        count -= 1
        
         
    user_words = ""
    for word in empty_list:
            user_words += word
    print(user_words == choosen_word)
    if user_words == choosen_word:
        print('You won this game') 
        print(
         '''
            +-------+
            |       | Thanks For Saving me !!!!
              	    |
            o       |
           /|\      |
           / \ |==| |
           ===========
        '''
        )
        gameEnd()
    else:
        print("Game over")
        gameEnd() 
        
def start_game():
    print("hey!!! wanna play Game let's start")
    start_or_not = input("Enter 'start' to play game\n").lower()
    if start_or_not == "start":
        start()
    else:
        print('please type start !!!!')

start_game()
