def number_to_time(number):
    hours = int(number / 60)
    minutes = number % 60
    if hours > 1:
        time = ( str(hours) + " hours "+ str(minutes) + " minutes")
    else: 
        time = ( str(hours) + " hour "+ str(minutes) + " minutes")
    return time
print(number_to_time(71))