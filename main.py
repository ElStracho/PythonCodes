
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ondřej Stach
email: stachondrej@post.cz
"""
TEXTS = [

    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

#Tvůj program bude obsahovat následující:
#Vyžádá si od uživatele přihlašovací jméno a heslo,
#zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
#pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
#pokud není registrovaný, upozorni jej a ukonči program.

reg_users = {
    "bob":"123",
    "ann":"pass123",
    "mike":"password123",
    "liz":"pass123"
    }

user_name = input("username:")
password = input("password:")

dash_line = "-"*40

if reg_users.get(user_name) == password: #vyhodnocení příhlašovacích údajů
    print(dash_line)
    print("Welcome to the app, ", user_name)
    print("We have ", len(TEXTS), " texts to be analyzed.")
    print(dash_line)
    
    selected_number = input("Enter a number btw. 1 and 3 to select: ")

    if not selected_number.isnumeric(): #vyhodnocení zadaného čísla textu k analýze
        print("nebylo zadané číslo nebo celé číslo")
    elif int(selected_number) not in range (1,4) :
        print("číslo je mimo rozsah")
    else:
        analyzed_text = TEXTS[int(selected_number)-1]
        print(dash_line)
    
        list_of_words  = [""] # seznam slov v textu
        word_counter = 0      

        for i in analyzed_text: #separace na jednotlivá slova do listu list_of_words
            if i == analyzed_text[len(analyzed_text)-1] and not i.isalnum(): #ošetření znaku na konci textu
                continue
            elif not i.isalnum() and not list_of_words[word_counter]=="": 
                word_counter = word_counter +1
                list_of_words.append("")
            elif i.isalnum():
                list_of_words[word_counter]= list_of_words[word_counter]+i

        titlecase_words = 0
        uppercase_words = 0
        lowercase_words = 0
        numeric_strings = 0
        sum_of_num_strings = 0
    
        for i in list_of_words:
            if i.istitle():
                titlecase_words = titlecase_words +1 
            elif i.isupper():
                uppercase_words = uppercase_words +1
            elif i.islower():
                lowercase_words = lowercase_words +1
            elif i.isnumeric():
                numeric_strings = numeric_strings +1
                sum_of_num_strings = sum_of_num_strings+int(i)
            else:
                continue

        print("There are ", len(list_of_words), " words in the selected text.")
        print("There are ", titlecase_words, " titlecase words.")
        print("There are ", uppercase_words, " uppercase words.")
        print("There are ", lowercase_words, " lowercase words.")
        print("There are ", numeric_strings, " numeric strings.")
        print("The sum of all the numbers ", sum_of_num_strings)
        #print(list_of_words)
        print(dash_line)
        print("LEN|  OCCURENCES", " "*9, "|NR.")
        print(dash_line)
    
        len_occurences_list = list() #vytvoření pomocného listu s délkami slov
        for word in list_of_words:
            len_occurences_list.append(len(word))
    
        maximal_length = max(len_occurences_list)

        for len in range(1, maximal_length + 1): # vytvoření grafu
            print(
                f"{len:>2} |", 
                "*"*len_occurences_list.count(len), 
                " "*(20-len_occurences_list.count(len)), 
                "|", 
                len_occurences_list.count(len)
                )
          
else:
    print("unregistered user, terminating the program..")
