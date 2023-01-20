decimal = int(input("input decimal number: "))
result = ""
while decimal > 0:
    result = str(decimal%2)+result
    decimal = decimal //2

print(result)