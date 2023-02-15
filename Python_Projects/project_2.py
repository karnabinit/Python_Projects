from pyfpga import Fpga

# Instantiate the FPGA object
fpga = Fpga()

# Connect to the FPGA
fpga.connect()

# Define the input values
a = 5
b = 3

# Send the input values to the FPGA
fpga.write(0, a)
fpga.write(1, b)

# Get the output value from the FPGA
result = fpga.read(2)

# Print the result
print(f"{a} + {b} = {result}")

# Disconnect from the FPGA
fpga.disconnect()
