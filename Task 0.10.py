def common_character(first_string,second_string):
    common_letter = ''
    for word in first_string:
        if word in second_string:
            common_letter += word
    return common_letter
output =  common_character('house','computers')
print(output)