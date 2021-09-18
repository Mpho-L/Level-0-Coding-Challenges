def celsius_to_fahrenheit(celsius):
  Fahrenheit = celsius * 9/5 + 32
  return Fahrenheit
output = celsius_to_fahrenheit(13)
print(str(output) + " F")

def fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * 5/9 
  return celsius
output = fahrenheit_to_celsius(13)
print(str(output) + " C")