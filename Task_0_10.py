def common_character(first_string,second_string):
    common_letter = ''
    for word in first_string.lower():
        if word in second_string.lower():
            common_letter += word
    return common_letter
output =  common_character('Dear','Ear')
print("Common letters: "+",".join(output))