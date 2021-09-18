def find_vowels(word):
    vowels = "AaEeIiOoUu"
    vowels_value = []
    for i in word:
      if i in vowels:
           vowels_value.append(i)
    return vowels_value
      
output = find_vowels("Umuzi")
print(output)