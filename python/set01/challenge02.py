def challenge02(s: str) -> str:
    lines = s.splitlines()
    string = lines[0]
    key = lines[1]
    decoded_string = bytes.fromhex(string)
    decoded_key = bytes.fromhex(key)
    
    result = b""
    for a, b in zip(decoded_string, decoded_key):
        result += bytes([a ^ b])

    return result.hex()


def challenge02_golf(s: str) -> str:
    return bytes((m:=tuple(map(bytes.fromhex,s.split("\n"))),[a^b for a,b in zip(m[0],m[1])])[1]).hex()
