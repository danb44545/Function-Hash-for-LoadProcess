import NuMpy, sys

def ror_str(byte, count):
    # Ror a byte by 'count' bits
    # padded 32 bit
    binb = numpy.base_repr(byte,2).zfill(32)
    while count > 0:
        # ROTATE BY 1 BYTE: example for 0x41
        # 0000000000000000000000001000001
        binb = binb[-1] + binb[0:-1]
        # 1000000000000000000000000100000
        count = count -1
    return (int(binb,2))

if __name__ == '__main__':
    esi = "ExitProcess"

    # Initialize variables
    edx = 0x00
    ror_count = 0
    for eax in esi:
        edx = edx + ord(eax)
        if ror_count < len(esi)-1:
            edx = ror_str(edx,0xd)
        ror_count = ror_count + 1
    print(hex(edx))
    # e.g. example if esi = "ExitProcess" answer will be 0x73e2d87e
