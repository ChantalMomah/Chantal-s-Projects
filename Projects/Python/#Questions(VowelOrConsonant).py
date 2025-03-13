def vowel_or_consonant(letter):
    if(letter == 'a, e , i, o, u'):
        return f"{letter} is a vowel."
    else:
        return f"{letter} is a consonant."
    
    
letter = 'e'
print(vowel_or_consonant(letter))