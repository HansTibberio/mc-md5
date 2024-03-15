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
    0xd7, 0x6a, 0xa4, 0x78, 0xe8, 0xc7, 0xb7, 0x56, 0x24, 0x20, 0x70, 0xdb, 0xc1, 0xbd, 0xce, 0xee,
    0xf5, 0x7c, 0x0f, 0xaf, 0x47, 0x87, 0xc6, 0x2a, 0xa8, 0x30, 0x46, 0x13, 0xfd, 0x46, 0x95, 0x01,
    0x69, 0x80, 0x98, 0xd8, 0x8b, 0x44, 0xf7, 0xaf, 0xff, 0xff, 0x5b, 0xb1, 0x89, 0x5c, 0xd7, 0xbe,
    0x6b, 0x90, 0x11, 0x22, 0xfd, 0x98, 0x71, 0x93, 0xa6, 0x79, 0x43, 0x8e, 0x49, 0xb4, 0x08, 0x21
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