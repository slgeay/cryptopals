def challenge04(s: str) -> str:
    lines = s.splitlines()
    best_score = 0
    best_result = ""
    for l in lines:
        decoded_string = bytes.fromhex(l)
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


def challenge04_golf(s: str) -> str:
    return max([bytes([b^k for b in bytes.fromhex(l)]).decode("ascii",errors="ignore")for k in range(256)for l in s.splitlines()],key=lambda r:sum([r.count(c)for c in"etaoinshrdlu "]))
