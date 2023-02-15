# calling the modules
import multiplefunction

# intiger initalizing to the data structure for storing the decimal numbers
userInputValueFirst = 0
userInputValueSecond = 0

def main():
    global userInputValueFirst, userInputValueSecond
    # asking for the values of two intigers a and b from the user and passing the value to the function
    continuation = True
    inputValue = False
    while continuation == True:
        while inputValue == False:
            # exceptional handling
            try:
                userInputValueFirst = int(input("Enter the first number:"))
                # calling multiplefunction module with defined function NumberInput
                userInputValueFirst = multiplefunction.NumberInput(userInputValueFirst)
                print("\n")
                inputValue = True
            # checking the validity of the data type of first number
            except ValueError:
                print("INVALID INPUT!!! Please, enter integer value.")
                print("\n")
                continue
            while inputValue == True:
                try:
                    userInputValueSecond = int(input("Enter the second number:"))
                    # calling multiplefunction module with defined function NumberInput
                    userInputValueSecond = multiplefunction.NumberInput(userInputValueSecond)
                    print("\n")
                    break
                # checking the validity of the data type of second number
                except ValueError:
                    print("INVALID INPUT!!! Please, enter integer value.")
                    print("\n")
            # calling multiplefunction module with check function
            
        multiplefunction.check(userInputValueFirst, userInputValueSecond)
        # asking whether user want to continue again or not
        exit_code = input("Do you wish to continue? Type 'No' to exit:").lower()
        if exit_code == "no":
            break
        else:
            inputValue = False
            print("\n")

print("\n")
# calling main function
main()
