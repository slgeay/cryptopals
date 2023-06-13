def challenge03(s: str) -> str:
    decoded_string = bytes.fromhex(s)
    best_score = 0
    best_result = ""
    for k in range(256):
        result = b""
        for b in decoded_string:
            result += bytes([b ^ k])
        try:
            result = result.decode()
        except:
            continue

        freq = {}
        for c in result:
            freq[c] = freq.get(c, 0) + 1

        score = 0
        for c in freq:
            if c in "etaoinshrdlu ":
                score += freq[c]
        
        if score > best_score:
            best_score = score
            best_result = result

    return best_result


def challenge03_golf(s: str) -> str:
    return max([bytes([b^k for b in bytes.fromhex(s)]).decode("ascii",errors="ignore")for k in range(256)],key=lambda r:sum([r.count(c)for c in"etaoinshrdlu "]))
