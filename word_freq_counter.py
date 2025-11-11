
def word_freq_counter(text):
    freq_dict = {}

    # split sentence into a list of words 
    list_of_word = text.split(" ")

    # create an empty set to store unique words
    set_of_word = set()
    
    #store all word in a set to avoid repetition
    for word in list_of_word:
        set_of_word.add(word)

    for word in set_of_word:
        cpt = 0
        for word_ in list_of_word:
            if word == word_ :
                cpt += 1 
        
        freq_dict[word] = cpt    

    # the goal here is to get the most often word
    list_of_keys = list(freq_dict.keys())

    more_freq_name = ""
    more_freq_value = 0
    for key in list_of_keys:
        if freq_dict[key] > more_freq_value:
            more_freq_value = freq_dict[key]
            more_freq_name = key
    print("The most often is :",more_freq_name)
    print("with this value:",more_freq_value)


    return freq_dict


res = word_freq_counter("Bonjour Bonjour Bonjour je m'appele aicha je aicha")
print(res)

