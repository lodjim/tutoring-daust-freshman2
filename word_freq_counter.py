from collections import Counter




def count_word_frequencies(text):
    words = text.split()
    return dict(Counter(words))



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

    return freq_dict




res = word_freq_counter("Bonjour Bonjour Bonjour je m'appele aicha je aicha")
print(res)


print("----------------------------------------------")


res = count_word_frequencies("Bonjour Bonjour Bonjour je m'appele aicha je aicha")
print(res)
