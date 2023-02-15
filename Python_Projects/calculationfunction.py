# and gate 
def andGate(A, B):
    return A & B
# or gate 
def orGate(A, B):
    return A | B
# compliement 
def compliment(bitDigit):
    return ~bitDigit
# xor gate 
def xorGate(A, B):
    return orGate(andGate(compliment(A), B), andGate(A, compliment(B)))
# nor gate
def norGate(A, B):
    return ~(orGate(A, B))
# nand gate
def nandGate(A,B):
    return compliment(andGate(A, B))


# calculation 
def calculateResult(a, b, c):
    carryIn = 0
    for i in range(7, -1, -1):
        X = a[i]
        Y = b[i]
        andGate_1 = andGate(X, Y)
        xorGate_1 = xorGate(X, Y)
        orGate_1 = orGate(xorGate_1, carryIn)
        nandGate_1 = nandGate(xorGate_1, carryIn)
        Sum = andGate(orGate_1, nandGate_1)
        andGate_2 = andGate(xorGate_1, carryIn)
        norGate_1 = norGate(andGate_1, andGate_2)
        carryOut = compliment(norGate_1)
        carryIn = carryOut
        c[i+1] = Sum
        if i == 0:
            c[i] = carryIn

# function which helps to remove 0 if the final output has 0 before 1 
def removeZero(Sum):
    for i in range(len(Sum)):
        if Sum[i] == 1:
            return (Sum[i:])
            break

# displaying the final outcome by converting list into string
def display(a, b, x, y, z):
    stringValue = ""
    StringValue1 = ""
    StringValue2 = ""
    for value in x:
        StringValue1 = StringValue1+str(value)
    for value in y:
        StringValue2 = StringValue2+str(value)
    print(f"Binary value of {a} is: ", StringValue1, "\n")
    print(f"Binary value of {b} is: ", StringValue2, "\n\n")
    print("\n")

# exceptional handling
    try:
        for i in range(len(z)):
            stringValue = stringValue+str(z[i])
            print(f"Binary addition of {StringValue1} and {StringValue2} is: ",stringValue,"\n\n")
            print("**  **  **  **  **  **")
    except TypeError:
        # print out 0 if the both inputs are 0
        print(f"Binary addition of {StringValue1} and {StringValue2} is: 0")
        print("**  **  **  **  **  **")
