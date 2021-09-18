def number_to_time(number):
    hours = int(number / 60)
    minutes = number % 60
    time = ( str(hours) + " hours "+ str(minutes) + " minutes")
    return time
output = number_to_time(71)
print(output)