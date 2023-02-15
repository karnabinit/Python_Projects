# importing modules named calculationfunction
import calculationfunction

# validating the sum of two inputs not to exceed 255
def NumberInput(re_enter):
    while(re_enter < 0 or re_enter > 255):
        print("Invalid ! Total characters should be in the range of 0 and 255")
        print("\n")
        re_enter = int(input("Please enter a number again!\n"))
    return re_enter    

# This function pulls remainder of the entered number and stores the value
def decimalToBinary(inputValue):
    bit = [0, 0, 0, 0, 0, 0, 0, 0]
    counter = 0
    while counter != 8:
        remainder = inputValue % 2
        bit[7-counter] = remainder
        inputValue = inputValue//2
        counter += 1
    return bit
    
# checking whether input values exceeds 8bit operation or not
def check(a, b):
    # Storing the values into list
    storeForFirst = []
    storeForSecond = []
    # calling decimalToBinary function
    storeForFirst = decimalToBinary(a)
    storeForSecond = decimalToBinary(b)
    # creating list to store the final output of the binary addition
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("\n")
    # calling calculationfunction modules with pre-defined function called calculateResult
    calculationfunction.calculateResult(storeForFirst, storeForSecond, result)
    # storing the value of final outcome in o after slicing the 0 which comes before 1
    o = calculationfunction.removeZero(result)
    # calling calculationfunction modules with display function
    calculationfunction.display(a, b, storeForFirst, storeForSecond, o)
