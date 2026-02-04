def printMessage():
    print("i don't return a value")


def printMessage2(value1, value2):
    ans = value1 + value2
    return ans


answer = printMessage2(4,2)#calling function with arguments
print(answer)
printMessage()
