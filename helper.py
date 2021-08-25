def parse_bits(string):
    bits = []
    for char in string:
        if char == '1':
            bits.append(True)
        elif char == '0':
            bits.append(False)
    return bits

def binary_to_decimal(binary):
        decimal = 0 
        for digit in binary: 
            decimal = decimal*2 + int(digit) 
        return decimal 

def array_to_decimal(address):
        out = ""
        for i in address:
            if i:
                out += "1"
            else: out += "0"
        return binary_to_decimal(out)