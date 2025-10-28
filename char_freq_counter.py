

def charac_word (text):
    freq_dict={}
    set_char=set()
    for char in text:
        set_char.add(char)
    for char in set_char:
        compt=0
        for char_ in text:
            if char==char_:
                compt+=1
        freq_dict[char]=compt
    return freq_dict

res=charac_word("bonjour bonjour je suis rays")

print(res)