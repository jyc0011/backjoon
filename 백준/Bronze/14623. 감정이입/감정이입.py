dec_B1 = int(input().strip(), 2)
dec_B2 = int(input().strip(), 2)

result = dec_B1 * dec_B2
bin_result = bin(result).replace("0b", "")

print(bin_result)