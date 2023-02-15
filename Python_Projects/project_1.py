# Function to convert decimal number to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Function to convert binary number to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Function to perform integer addition of two decimal numbers
def integer_addition(decimal1, decimal2):
    # Convert decimal inputs to binary
    binary1 = decimal_to_binary(decimal1)
    binary2 = decimal_to_binary(decimal2)
    
    # Determine the maximum length of binary strings
    max_len = max(len(binary1), len(binary2))
    
    # Add leading zeroes to binary strings to make them the same length
    binary1 = binary1.zfill(max_len)
    binary2 = binary2.zfill(max_len)
    
    # Initialize variables for binary addition
    result = ''
    carry = 0
    
    # Iterate through binary strings from right to left and perform binary addition
    for i in range(max_len-1, -1, -1):
        digit1 = int(binary1[i])
        digit2 = int(binary2[i])
        sum = digit1 + digit2 + carry
        
        if sum == 0:
            result = '0' + result
            carry = 0
        elif sum == 1:
            result = '1' + result
            carry = 0
        elif sum == 2:
            result = '0' + result
            carry = 1
        elif sum == 3:
            result = '1' + result
            carry = 1
            
    # If there is a final carry, add it to the left side of the result
    if carry == 1:
        result = '1' + result
        
    # Convert binary result to decimal and return
    return binary_to_decimal(result)

# Example usage of integer_addition function
result = integer_addition(10, 5)
print(result)  
