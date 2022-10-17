# Converting binary into numbers
def bin_to_dec(binary_string):
    bin_list = list(str(binary_string))
    i = len(bin_list) - 1
    x = 0
    decimal = 0
    while i >= 0 and x < len(bin_list):
        if int(bin_list[i]) == 1:
            decimal += 2**x
        i -= 1
        x += 1
    return decimal


print(bin_to_dec('010001110'))
# result: 142
