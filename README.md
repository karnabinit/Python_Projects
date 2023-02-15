# Python_Projects
Academic Assignments


Project_1: Python program that performs integer addition of two decimal numbers and outputs the result in binary form.

In this program, the decimal_to_binary function converts a decimal number to a binary string, while the binary_to_decimal function converts a binary string to a decimal number. The integer_addition function takes two decimal numbers as inputs, converts them to binary strings, performs binary addition, and returns the result as a decimal number.

Note that this program assumes that the input numbers are non-negative integers. If you need to handle negative numbers or decimals, additional code would be required to handle these cases.


Project_2: A software application that affects the action of a digital circuit performing integer addition using Python, we need to use a library that can interact with the digital circuit. One such library is the pyFPGA library, which can be used to interact with Field Programmable Gate Arrays (FPGAs) to implement digital circuits.

In this program, we first instantiate an object of the Fpga class from the pyfpga library. We then connect to the FPGA using the connect() method. Next, we define the input values for the integer addition operation and send them to the FPGA using the write() method. We then read the output value from the FPGA using the read() method and print the result.

Finally, we disconnect from the FPGA using the disconnect() method.

Note that the exact implementation of the digital circuit performing integer addition on the FPGA will depend on the specific FPGA used, as well as the design of the circuit. This program assumes that the FPGA has already been programmed to perform integer addition, and provides a simple way to send input values to the circuit and retrieve the output value.
