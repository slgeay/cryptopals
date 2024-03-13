from itertools import cycle

def challenge05(s: str) -> str:
    key = "ICE"
    result = b""
    for i, c in enumerate(s.encode()):
        result += bytes([c ^ ord(key[i % 3])])
    return result.hex()


def challenge05_golf(s: str) -> str:
    return bytes([b ^ k for b, k in zip(s.encode(), cycle(map(ord,"ICE")))]).hex()
