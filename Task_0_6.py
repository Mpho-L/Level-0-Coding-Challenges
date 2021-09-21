def maximum(num1,num2,num3):
    if (num1 > num2) and (num1 > num3):
        maximum_number = num1
    elif (num2 > num1) and (num2 > num3):
        maximum_number = num2
    else:
        maximum_number = num3
    return maximum_number
print(maximum(12,34,5))