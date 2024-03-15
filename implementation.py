def rotateLeft(x, n):
    return int(f'{x:08b}'[n:] + f'{x:08b}'[:n], 2)

def hexDigest(byte):
    hexFormat = format(byte,'02x')
    return hexFormat

def pad(block):
    blockLength = len(block)
    block += '1'
    while len(block) % 128 != 112:
        block += '0'
    lastPart = format(blockLength,'016b')
    block += lastPart
    return block

def getBlock(block):
    currPos = 0
    while currPos < len(block):
        currPart = block[currPos:currPos+128]
        mySplits = []
        for i in range(16):
            mySplits.append(int(currPart[8*i:8*i+8],2))
        yield mySplits
        currPos += 128


def MCMD5(data):
    block = ''.join(f'{byte:08b}' for byte in data)
    block = pad(block)
    file = open('message.txt', 'w')
    file.write(block)
    file.close()

    Z = 2**8
  
    SIGMA = [
    1, 5, 2, 6, 1, 5, 2, 6, 1, 5, 2, 6, 1, 5, 2, 6, 
    2, 6, 3, 7, 2, 6, 3, 7, 2, 6, 3, 7, 2, 6, 3, 7,
    4, 1, 5, 2, 4, 1, 5, 2, 4, 1, 5, 2, 4, 1, 5, 2,
    3, 7, 4, 1, 3, 7, 4, 1, 3, 7, 4, 1, 3, 7, 4, 1
    ]

    KVALUES = [
    0xd7, 0xe8, 0x24, 0xc1, 0xf5, 0x47, 0xa8, 0xfd, 0x69, 0x8b, 0xff, 0x89, 0x6b, 0xfd, 0xa6, 0x49,
    0xf6, 0xc0, 0x26, 0xe9, 0xd6, 0x02, 0xd8, 0xe7, 0x21, 0xc3, 0xf4, 0x45, 0xa9, 0xfc, 0x67, 0x8d,
    0xff, 0x87, 0x6d, 0xfd, 0xa4, 0x4b, 0xf6, 0xbe, 0x28, 0xea, 0xd4, 0x04, 0xd9, 0xe6, 0x1f, 0xc4,
    0xf4, 0x43, 0xab, 0xfc, 0x65, 0x8f, 0xff, 0x85, 0x6f, 0xfe, 0xa3, 0x4e, 0xf7, 0xbd, 0x2a, 0xeb
    ]

    a0 = 0x89
    b0 = 0xab
    c0 = 0xcd
    d0 = 0xef

    for M in getBlock(block):

        A = a0
        B = b0
        C = c0
        D = d0

        for i in range(64):
            if i <= 15:
                F = (B & C) | ((~ B) & D)
                g=i

            elif i <= 31:
                F = (D & B) | ((~ D) & C)
                g=(5*i+1)%16

            elif i <= 47:
                F = B ^ C ^ D
                g=(3*i+5)%16

            elif i <= 64:
                F = C ^ (B | (~ D))
                g=(7*i)%16

            F = (F + A + KVALUES[i] + M[g])%Z
            A = D
            D = C
            C = B
            B = (B + rotateLeft(F, SIGMA[i]))%Z

        a0 = (a0 + A)%Z
        b0 = (b0 + B)%Z
        c0 = (c0 + C)%Z
        d0 = (d0 + D)%Z

    hexdigest = hexDigest(a0) + hexDigest(b0) + hexDigest(c0) + hexDigest(d0)
    return hexdigest