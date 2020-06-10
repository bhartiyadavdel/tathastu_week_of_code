def replace(number):
    return int(str(number).replace('0','5'))
num = int(input("Enter the number : "))
print("The number after replacing all 0 with 5 will be",replace(num))
