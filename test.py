def toNumber(binary):
    num = 0
    count = 0

    binary = int(binary)

    while binary:
        num += (binary % 10)*(2**count)
        binary = binary // 10
        count+=1
    return num

print(toNumber('000011'))