import struct


def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xffffffff


def sha1(data: str):
    h0: int = 0x67452301
    h1: int = 0xEFCDAB89
    h2: int = 0x98BADCFE
    h3: int = 0x10325476
    h4: int = 0xC3D2E1F0

    ml: int = len(data) * 8
    data += b'\x80'
    data += b'\x00' * ((56 - (len(data) % 64)) % 64)
    data += struct.pack('>Q', ml)

    chunks: list = [data[i:i + 64] for i in range(0, len(data), 64)]

    for chunk in chunks:
        words = struct.unpack('>16I', chunk)
        w = list(words)
        for i in range(16, 80):
            w.append(left_rotate(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1))

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        for i in range(80):
            if i <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (left_rotate(a, 5) + f + e + k + w[i]) & 0xffffffff
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xffffffff
        h1 = (h1 + b) & 0xffffffff
        h2 = (h2 + c) & 0xffffffff
        h3 = (h3 + d) & 0xffffffff
        h4 = (h4 + e) & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)
