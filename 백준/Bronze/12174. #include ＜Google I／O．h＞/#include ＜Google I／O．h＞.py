T = int(input())
for t in range(1, T+1):
    B = int(input())
    input_data = input().replace('I', '1').replace('O', '0')

    message = ""
    for i in range(B):
        byte = input_data[i*8:(i+1)*8]
        message += chr(int(byte, 2))

    print(f"Case #{t}: {message}")
