def find_vowels(word):
    vowels = "AaEeIiOoUu"
    vowels_value = ""
    for i in word:
      if i in vowels:
           vowels_value += i
    return vowels_value
      
output = find_vowels("neurobiological")
print("vowels: "+", ".join(output))